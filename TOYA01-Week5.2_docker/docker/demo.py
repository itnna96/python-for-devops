#!/usr/bin/env python
import psycopg2
from psycopg2 import OperationalError
from time import sleep
from prometheus_client import start_http_server,Gauge
nowtime = 5

DB_HOST = "0.0.0.0"
DB_NAME = "postgres"
DB_USERNAME = "postgres"
DB_PASS = "postgres"

DB_STATUS = Gauge(
    'database_status',
    'Database connection status. 1 is ok . 0 is failded',
    ['DB_HOST','DB_USERNAME','DB_NAME']
)

DB_SIZE = Gauge(
    'database_size',
    'DB Size in Bytes',
    ['DB_HOST','DB_NAME']
)

def check_conn():
    db_check_metric = DB_STATUS.labels(DB_HOST,DB_USERNAME,DB_NAME)
    try:
        connection_string = f"host={DB_HOST} user={DB_USERNAME} password={DB_PASS} dbname={DB_NAME}"
        conn = psycopg2.connect(connection_string)
        cur = conn.cursor()
        cur.execute("Select 1")
        conn.close()
        db_check_metric.set(1)
        # return True, f"Database connection is good!"
    except OperationalError as error:
        db_check_metric.set(0)
        # return False, f"Can't connect to database. Error: {error}"

def check_db_size():
    try:
        connection_string = f"host={DB_HOST} user={DB_USERNAME} password={DB_PASS} dbname={DB_NAME}"
        conn = psycopg2.connect(connection_string)
        cur = conn.cursor()
        cur.execute("SELECT pg_database.datname as database_name, pg_database_size(pg_database.datname) AS size_bytes FROM pg_database")
        rows = cur.fetchall()
        for db_name,db_size in rows:
            DB_SIZE.labels(DB_HOST,db_name).set(db_size)
            # print(db_name,db_size)
        conn.close()
        
        # DB_SIZE.labels(DB_HOST,'postgres').set(8168303)
        # DB_SIZE.labels(DB_HOST,'template1').set(8020483)
        # DB_SIZE.labels(DB_HOST,'template0').set(8020483)
    except OperationalError as error:
        DB_SIZE.clear()
        print('Cant get db size')



if __name__ == '__main__':
    start_http_server(8080)
    while True:
        # from time import sleep
        check_conn()
        check_db_size()
        sleep(nowtime)