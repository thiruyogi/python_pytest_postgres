import pytest
import psycopg2
import pdb

class DmlCommands():
    def __init__(self,cur,conn) -> None:
        self.cur = cur
        self.conn = conn
        
    def fetch_all_data_from_table(self, tableName : str, condition :dict = None):
        if condition:
            condition_string = ""
            for column, value in condition.items():
                if(isinstance(value,int)):
                    condition_string = condition_string + "{0} = {1}".format(column , value)
                else:
                    condition_string = condition_string + "{0} = '{1}'".format(column , value)
            condition_string = condition_string.replace('"', "")
            query = "SELECT * FROM {0} WHERE {1}".format(tableName,condition_string)
        else:
            query = "SELECT * FROM {0}".format(tableName)
        self.cur.execute(query)
        return self.cur.fetchall()
    
    def insert_data_into_table(self, tableName:str, column_names:tuple, data:tuple):
        no_of_columns = len(column_names)
        column_names = str(column_names).replace("'","")
        place_holders =()  
        for i in range (no_of_columns):
            place_holders = place_holders +('%s',)
        place_holders = str(place_holders).replace("'", "")
        insert_query = "INSERT INTO {0} {1} VALUES {2}".format(tableName,column_names,place_holders)
        insert_values = []
        if isinstance(data,list):
            insert_values = data
        elif isinstance(data,tuple):
            insert_values.append(data)
        for record in insert_values:
            self.cur.execute(insert_query,record)
            
    def update_data_in_table(self, tableName:str, update_values:dict, condition:dict= None):
        update_string = ""
        for column , value in update_values.items():
            if(isinstance(value,int)):
                update_string = update_string+'{0} = {1},'.format(column,value)
            else:
                update_string = update_string+"{0} = '{1}',".format(column,value)
        update_string = update_string.replace('"', "")
        update_string = update_string[:-1]
        update_query = "UPDATE {0} SET {1}".format(tableName,update_string)
        if condition:
            update_query = "UPDATE {0} SET {1} WHERE {2}".format(tableName,update_string,condition)
        self.cur.execute(update_query)
        
    def delete_data_from_table(self, tableName, condition):
        delete_query = "DELET FROM {0} WHERE {1}".format(tableName, condition)
          
        