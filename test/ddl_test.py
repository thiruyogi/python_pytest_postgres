from base.baseClass import BaseClass
from pages.ddl_commands import DdlCommands
from pages.dml_commands import DmlCommands
import pytest
import pdb
from expects import *
from ddt import ddt,data, unpack

class TestDdlCommands(BaseClass):
    
    @pytest.fixture(scope='class',autouse=True)
    def beforeAllSetup(self,setup):
        self.__class__.ddl_commands = DdlCommands(self.cur, self.conn)
        self.__class__.dml_commands = DmlCommands(self.cur, self.conn)
        self.ddl_commands.drop_table('emplpoyee')
        self.ddl_commands.create_employee_table()
        yield
        self.ddl_commands.drop_table('emplpoyee')
        
    def test_verify_table_schema(self):
        response = self.ddl_commands.read_table_schema('employee')
        expected_schema = self.ddl_commands.employee_table_actual_schema()
        for record in response:
            expect(expected_schema).to(contain(record))
    