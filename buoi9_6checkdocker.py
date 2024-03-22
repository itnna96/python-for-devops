#docker-compose 
#you can connection : psql postgres://postgres:postgres@0.0.0.0:5432
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
        print("DB is good.")
        conn.close()
        # if cur.fetch() == "10%":
        #     send_mail()
    except OperationalError as error:
        print("Can't connect to database. Error: ", error)
        # send_email()
if __name__ == '__main__':
    while True:
        check_conn()
        from time import sleep
        sleep(2)
