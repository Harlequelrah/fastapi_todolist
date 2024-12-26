from harlequelrah_fastapi.authentication.authenticate import Authentication


database_username = "Harlequin"
database_password = "Quinlehar0179"
connector = "mysql+mysqlconnector"
database_name = "fastapi_todolist"
server = "pv2qj5pz-3306.usw3.devtunnels.ms:3306"
authentication = Authentication(
    database_username=database_username,
    database_password=database_password,
    connector=connector,
    database_name=database_name,
    server=server,
)
