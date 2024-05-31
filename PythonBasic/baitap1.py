class Video:
    def __init__(self, title, link):
        self.title = title
        self.link = link

def read_videos():
    videos = []

    valid = False
    while not valid:
        total_video = input("Enter how many videos : ")
        try:
            total_video = int(total_video)
            if total_video < 0 :
                print("Invalid ! Please enter a positive number ")
            else:
                valid = True
        except ValueError:
            print("Invalid input ! Please enter a number")

    for i in range(total_video):
        print(f"Video so {i+1}")
        title = input(f"Enter video title {i+1}: ")
        link = input(f"Enter video link {i+1}: ")
        videos.append(Video(title,link))
    return videos

def get_inf_video():
    videos = read_videos()
    print ("\n--- The video information includes the title ,link. ---")
    for i,video in enumerate(videos, start=1):
        print(f"# Video number {i}")
        print(f"Title: {video.title}")
        print(f"Link: {video.link}")
        print("-" * 20)
    return videos

def write_to_file(videos):
    total_video = len(videos)
    with open("baitap1.txt","w") as file:
        file.write(f"Total Video : {total_video}\n")
        for i, video in enumerate(videos, start=1):
            file.write(f"# Video number {i}\n")
            file.write(f"Title: {video.title}\n")
            file.write(f"Link: {video.link}\n")
            file.write("-" * 20 + "\n")

def main():
    videos = get_inf_video()
    write_to_file(videos)

main()