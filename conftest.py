import pytest
import psycopg2
import psycopg2.extras
import pdb
from pytest_testconfig import config
import configparser

@pytest.fixture(scope='class')
def setup(request):
    conn = None
    cur = None
    try:  
        conn = psycopg2.connect(
        host = config['POSTGRES']['HOSTNAME'],
        dbname = config['POSTGRES']['DATABASE'],
        user = config['POSTGRES']['USERNAME'],
        password = config['POSTGRES']['PWD'],
        port = config['POSTGRES']['PORT_NUM']
        )
        cur = conn.cursor()
        print("Connection Successfull")
        request.cls.cur = cur
        request.cls.conn = conn
        
        # create_script = ''' CREATE TABLE IF NOT EXISTS employee (
        #     id int PRIMARY KEY,
        #     name varchar(40) NOT NULL,
        #     salary int,
        #     dept_id varchar(30))
        # '''
        # cur.execute(create_script)
        # conn.commit()
    except Exception as error:
        print(error) 
    yield
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()