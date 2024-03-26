import psycopg2
from psycopg2 import OperationalError

DB_HOST = "0.0.0.0"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASS = "postgres"
def check_conn():
    try:
        connection_string = f"host={DB_HOST} user={DB_USER} password={DB_PASS} dbname={DB_NAME}"
        conn = psycopg2.connect(connection_string)
        cur = conn.cursor()
        cur.execute("Select 1")
        # print("DB is good.")
        conn.close()
        return True, f"Database connection is good!"
        # if cur.fetch() == "10%":
        #     send_mail()
    except OperationalError as error:
        return False, f"Can't connect to database. Error: {error}"
        # send_email()

def send_mail():
    import smtplib
    with smtplib.SMTP('localhost', 1025) as server:
        server.sendmail(
            "python@tools.com", #from
            "sysadmin@abc.com", #to
            "Hello NA"
        )

if __name__ == '__main__':
    while True:
        is_good,message = check_conn()
        if is_good:
            print(message)
        else:
            send_mail()
        from time import sleep
        sleep(2)