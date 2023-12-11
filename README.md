# python_pytest_postgres
This code operates on python and Pytest, to test DDL and DML commands in a postgresql DB.

Prerequesites:
1. Python version 3.x
2. Pogresql Local server or Remote server (Up and running)
3. Pip already installed

How to Run:
1. Clone the repo into a local repo
2. Navigate to the project directory in terminal
3. Execute 'pip3 install -r requiremnets.txt'. This will install all the dependencies.
4. Update the 'configs/default_config.ini' file with necessary details about the postgres server.
5. Execute 'pytest' for running all the test files.
6. Excute 'pytest <test file path> for running a specific file.
7. Test Execution HTML report will be genrated under reports folder.
