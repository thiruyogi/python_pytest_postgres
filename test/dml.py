import psycopg2
import psycopg2.extras
import pdb

hostname = 'localhost'
database = 'postgres'
username = 'revathiru'
pwd = 'ps1234'
port_num = 5432
conn = None
cur = None

try:  
    conn = psycopg2.connect(
    host = hostname,
    dbname = database,
    user = username,
    password = pwd,
    port = port_num
    )
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    print("Connection Successfull")
    
    cur.execute('DROP TABLE IF EXISTS employee')
    
    query1 = ""
    
    table_data = [['id','int', 'PRIMARY KEY'],['name','varchar(40)', 'NOT NULL'],['salary','int', ''],['dept_id','varchar(30)', '']]
    for data in table_data:
        for column in data:
            query1 = query1+' ' +column
        query1 = query1+','
    query1 = query1[:-2]
    create_script = " CREATE TABLE IF NOT EXISTS employee ({0})".format(query1)
    cur.execute(create_script, query1)
    res = conn.commit()
    print(res)
    tup = ('id', 'name', 'salary', 'dept_id')
    new_tup = (str(tup)).replace("'", "")
    pdb.set_trace()
    insert_query = "INSERT INTO employee {0} VALUES (1, 'Leo', 120000, 'D2')".format(new_tup)
    insert_values = [(1, 'Leo', 120000, 'D2'),(2, 'Dass', 120000, 'D2')]
    for records in insert_values:
        cur.execute(insert_query,records)
    try:
        cur.execute(insert_query)
    except Exception as error:
        pdb.set_trace()
        print(error)
    qury = """                              
        SELECT column_name, data_type, is_nullable
        FROM information_schema.columns
        WHERE table_name = %s;
        """ 
    cur.execute(qury, ('employee',))
    output = cur.fetchall()
    print(output)
    q1 = '''SELECT * 
        FROM INFORMATION_SCHEMA.CONSTRAINT_COLUMN_USAGE
        WHERE table_name = 'employee'
        AND constraint_name LIKE '%pkey' '''
    cur.execute(q1)
    output = cur.fetchall()
except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
print("Connection closed")