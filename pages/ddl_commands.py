import pytest
import psycopg2


class DdlCommands():
    def __init__(self,cur,conn) -> None:
        self.cur = cur
        self.conn = conn
        
    def create_employee_table(self):
        table_data = [['id','int', 'PRIMARY KEY'],['name','varchar(40)', 'NOT NULL'],['salary','int', ''],['dept_id','varchar(30)', '']]
        self.create_table('employee',table_data)
        
    def employee_table_actual_schema(self):
        schema = [('id', 'integer', 'NO'), ('salary', 'integer', 'YES'), ('name', 'character varying', 'NO'), ('dept_id', 'character varying', 'YES')]
        return schema  
          
    def create_table(self,tableName, table_details):
        query1 = ""
        for data in table_details:
            for column in data:
                query1 = query1+' ' +column
            query1 = query1+','
        query1 = query1[:-2]
        create_script = "CREATE TABLE IF NOT EXISTS {0} ({1}) ".format(tableName, query1)
        self.cur.execute(create_script)
        res = self.conn.commit()
    
    def read_table_schema(self, tableName):
        query = """                              
        SELECT column_name, data_type, is_nullable
        FROM information_schema.columns
        WHERE table_name = %s;
        """ 
        self.cur.execute(query, (tableName,))
        response = self.cur.fetchall()
        return response
    
    def drop_table(self, tableName):
        query = 'DROP TABLE IF EXISTS {0}'.format(tableName)
        self.cur.execute(query)
    