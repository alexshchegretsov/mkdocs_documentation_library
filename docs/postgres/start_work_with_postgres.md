1. Create a new user in postgres
`CREATE USER sample_user WITH PASSWORD 'sample_password';`
2. Create a new database and give the new user access
`CREATE DATABASE sample_database WITH OWNER sample_user;`

In Postgres, the owner of the database has full control over it, 
to perform any operation on current or future tables. 



`psql -d data_base -h host -p port -U data_base_user` - вход

`\conninfo` - информация о соединении с конкретной БД, пользователе.

`\l` - список баз данных кластера

`\c database username host port` - ещё один вариант подключения

`\db` - список табличных пространств
