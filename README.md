# python_pytest_postgres
This code operates on Python and Pytest, to test DDL and DML commands in a Postgresql DB.

Prerequisites:
1. Python version 3.x
2. Pogresql Local server or Remote server (Up and running)
3. Pip already installed

How to Run:
1. Clone the repo into a local repo
2. Navigate to the project directory in terminal
3. Execute 'pip3 install -r requiremnets.txt'. This will install all the dependencies.
4. Update the 'configs/default_config.ini' file with necessary details about the Postgres server.
5. Execute 'pytest' for running all the test files.
6. Excute 'pytest <test_file_path>' for running a specific file.
7. In case a new config file has to be used, please make sure all the necessary details of the DB are captured in the file and use 'pytest --tc-file=<config_file_path>'
8. Test Execution HTML report will be generated under the reports folder. 
