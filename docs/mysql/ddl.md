`data definition language` - язык описания данных
=

Язык DDL служит для создания и модификации структуры БД, 
т.е. для создания/изменения/удаления таблиц и связей.

- CREATE - to create a database and its objects like (table, index, views, store procedure, function, and triggers)
=
```
mysql> create database x character set utf8 collate utf8_unicode_ci;


mysql> create table if not exists tasks (
    -> task_id int auto_increment primary key,
    -> title varchar(255) not null,
    -> description text,
    -> created_at timestamp default current_timestamp
    -> );
```
- ALTER - alters the structure of the existing database 
=
```
# add 1 column
mysql> alter table tasks
    -> add
    -> author varchar(50)
    -> after description
    -> ;

# add multiple columns
alter table tasks add
author varchar(30) after description,
worker varchar(30);

# alter columns
mysql> alter table tasks modify description text not null, modify worker varchar(100);

# altre change column(name or parameters)
mysql> alter table tasks change column title task_title varchar(100) not null;

# alter drop column
mysql> alter table tasks drop column author;

# alter rename
mysql> alter table tasks rename to to_do;

```
- DROP - delete objects from the database
=

```
# drop db
drop database db;

# drop table
drop table table;

# drop column
alter table drop column author;
```

- TRUNCATE - remove all records from a table, including all spaces allocated for the records are removed
=
```
# delete all data in a table
mysql> truncate table to_do;
```

