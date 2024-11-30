from harlequelrah_fastapi.authentication.authenticate import Authentication
database_username="Harlequin"
database_password="Quinlehar0179"
connector = "mysql+mysqlconnector"
database_name = "fastapi_todolist"
server = "localhost:3306"
authentication=Authentication(database_username,database_password,connector,database_name,server)
