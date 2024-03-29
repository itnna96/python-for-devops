"""
Create a command line tool in python, having these features:
    a.Get the latest tag of given repository name.
    b.Create new tag, by increase the latest tag by 1.
        Example: latest tag: v2 -> new tag will be v3
    c.Make a new release from a tag.
        Use release name from user input.
        If not, auto generate release name by format "release/dd-mm-yy"


./week4.2_ex.py tag --lastet -> output lastet tag
./week4.2_ex.py tag --create

./week4.2_ex.py release --tag <tag-name> [--name <release-name>]
"""
import argparse,requests,os

API_KEY = os.environ.get('GITHUB_API_KEY')
HEADERS ={
    "Authorization": "Bearer " + API_KEY
}
BASE_URL = "https://api.github.com"

if not API_KEY:
    print("Please provide GITHUB_API_KEY")
    exit(1)


def get_latest_tag(repo_name):
    url = BASE_URL + f'/repos/{repo_name}/tags'
    reponse = requests.get(url,headers=HEADERS)
    if reponse.status_code !=200:
        print("Can't get tags.")
        return
    tags = reponse.json()
    #v2, v1.1, v1
    latest = 0
    # for tag in tags:
    #     name=tag['name'][1:]
    #     version = name.split('.')[0]
    #     if version > latest:
    #         latest = version
    versions = []
    for tag in tags:
        name = tag['name'][1:]
        version = name.split(',')[0]
        try:
            versions.append(int(version))
        except:
            print(f"Invalid tag name: {tag['name']}")
    #versions = [2,1,1]
    latest = max(versions)
    print(f"Latest version is v{latest}.")
    return latest

def get_sha_main(repo_name):
    url = BASE_URL + f'/repos/{repo_name}/branches/master'
    reponse = requests.get(url,headers=HEADERS)
    if reponse.status_code != 200:
        print('Cant get branch main. Error: {repose.text}')
    sha = reponse.json()['commit']['sha']
    # print(sha)
    return sha
def create_tag(repo_name):
    url = BASE_URL + f'/repos/{repo_name}/git/refs'
    latest_tag = get_latest_tag(repo_name)
    tag = f"refs/tags/v{latest_tag + 1}"
    sha = get_sha_main(repo_name)
    if not sha:
        print("Empty SHA. Cant create tag.")
        return False
    payload ={
        'ref': tag,
        'sha': sha,
    }
    
    reponse = requests.post(url,headers=HEADERS,json=payload)
    print(reponse.status_code)
    print(reponse.text)
    if reponse.status_code != 201:
        print('Error')
        return
    print(f"Tag {tag} created success!")
    return True

def create_release(repo_name,_tag,_name):
    url = BASE_URL + f'/repos/{repo_name}/releases'

    #format date time
    if not _name:
        "release/dd-mm-yy"
        from datetime import date
        _name = date.today().strftime("release/%d-%m-%y")

    payload = {
        "tag_name": _tag,
        "name": _name
    }

    reponse = requests.post(url,headers=HEADERS,json=payload)
    if reponse.status_code !=201:
        print('Error')
        print(reponse.txt)
        return
    
    print(f'New release create from tag {_tag}, with name: {_name}')
    return True

if __name__ == "__main__":

    paser = argparse.ArgumentParser(description="Github Tool")
    sub_paser=paser.add_subparsers(dest="command")
    paser.add_argument('REPO',help='Repository name.')
    ##Tag command
    tag_parser=sub_paser.add_parser('tag',help="Manage tag.")
    tag_parser.add_argument('--latest',action='store_true',help='Get latest tag.')
    tag_parser.add_argument('--create',action='store_true',help='Create new tag.')
    ## Release commnad
    release_paser = sub_paser.add_parser('release',help="Create release.")
    release_paser.add_argument('--tag','-t',help='Tag to make release',required=True)
    release_paser.add_argument('--name','-n',help='Name of release',required=False)    

    args = paser.parse_args()
    repo_name = args.REPO
    if args.command == 'tag':
        if args.latest == True:
            get_latest_tag(repo_name)
        if args.create == True:
            create_tag(repo_name)

    if args.command == 'release':
        create_release(repo_name,args.tag,args.name)