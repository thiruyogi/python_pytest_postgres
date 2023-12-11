from base.baseClass import BaseClass
from pages.ddl_commands import DdlCommands
from pages.dml_commands import DmlCommands
import pytest
import pdb
from expects import *
from ddt import ddt,data, unpack
from utils.read_data import getCSVData


class TestDmlCommands(BaseClass):
    
    @pytest.fixture(scope='class',autouse=True)
    def beforeAllSetup(self,setup):
        self.__class__.ddl_commands = DdlCommands(self.cur, self.conn)
        self.__class__.dml_commands = DmlCommands(self.cur, self.conn)
        self.__class__.columns = ('id', 'name', 'salary', 'dept_id')
        self.ddl_commands.drop_table('emplpoyee')
        self.ddl_commands.create_employee_table()
        yield
        self.ddl_commands.drop_table('emplpoyee')
    @ddt
    @data(*getCSVData("test_data/insert_data.csv"))  
    @unpack
    def test_insert_multiple_data_into_table(self,id,name,salary,dept_id):
        # columns = ('id', 'name', 'salary', 'dept_id')
        # values = [{'id':1,'name':'leo','salary':12000,'department':'D2'},
        #           {'id':2,'name':'dass','salary':120010,'department':'D1'},
        #           {'id':1,'name':'harold','salary':120020,'department':'D2'}]
        values= [(int(id),name,int(salary),dept_id)]
        print(values)
        #values = [(1, 'Leo', 120000, 'D2'),(2, 'Dass', 120000, 'D2'),(3, 'Harold', 130030, 'D2')]
        self.dml_commands.insert_data_into_table('employee',self.columns,values)
        table_data = self.dml_commands.fetch_all_data_from_table('employee')
        for record in values:
            expect(table_data).to(contain(record))
            
    def test_insert_single_data_into_table(self):
        values = (4, 'Sathya', 11000, 'D2')
        self.dml_commands.insert_data_into_table('employee',self.columns,values)
        table_data = self.dml_commands.fetch_all_data_from_table('employee')
        expect(table_data).to(contain(values))
        
    def test_update_values_in_table(self):
        values = (5, 'Sathya1', 11000, 'D2')
        updated_values = (5, 'Sathya1', 200, 'D3')
        self.dml_commands.insert_data_into_table('employee',self.columns,values)
        update_values = {"dept_id":"D3","salary":200}
        cond = {"id":5}
        self.dml_commands.update_data_in_table('employee',update_values,'id=5')
        table_data = self.dml_commands.fetch_all_data_from_table('employee',cond)
        expect(table_data).to(contain(updated_values))
        
        
    