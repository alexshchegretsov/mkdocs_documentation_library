`data manipulation language` 
=

DML is short name of Data Manipulation Language which deals with data manipulation and includes most common SQL statements 
such SELECT, INSERT, UPDATE, DELETE, etc., and it is used to store, modify, retrieve, delete and update data in a database. 

- `INSERT` - `mysql> insert into to_do (task_title, description) values ("SOme title", "Some description");`
- `SELECT`
```
mysql> select * from to_do;

mysql> select task_title from to_do where task_id<4;
```
- UPDATE
```
mysql> update to_do 
    -> set task_title="foo", description="bar"
    -> where task_id < 3;

```

- DELETE - `mysql> delete from to_do where task_title="foo";`



