# Python - Object-relational Mapping (ORM)

## Before

- **MySQL server is in 8.0** -> [How to install MySQL 8.0 in Ubuntu 20.04](https://dev.mysql.com/doc/mysql-installation-excerpt/8.0/en/)

## Background Context

This project introduces Object-Relational Mapping (ORM) using SQLAlchemy in Python, allowing interaction with relational databases in an object-oriented way. Instead of writing raw SQL queries, we work with Python objects, making it easier to integrate database operations directly into Python code.

### Part 1

You'll use the module `MySQLdb` to connect to a MySQL database and execute your SQL queries.

### Part 2

You'll use the module `SQLAlchemy`, an Object Relational Mapper (ORM).

### Install MySQLdb module version 2.0.x:

```bash
$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo apt-get install pkg-config
$ sudo pip3 install mysqlclient
$ python3
>>> import MySQLdb
>>> MySQLdb.version_info
(2, 1, 1, 'final', 0)

```

### Install SQLAlchemy module version 2.0.x:

```bash
$ sudo pip3 install SQLAlchemy
$ python3
>>> import sqlalchemy
>>> sqlalchemy.__version__
'2.0.36'
```

## Example Tasks

- **Define a Model**: Create a class representing a table (e.g., `State` for a `states` table with columns `id` and `name`).
- **Manipulate Data**: Use sessions to retrieve, insert, update, or delete records in the database.
- **Advanced Queries**: Use filters, sorting, and joins to query the database efficiently.

## Example Commands

- **List objects in a table**: `session.query(State).order_by(State.id).all()`
- **Add an object**: `session.add(new_state); session.commit()`
- **Update an object**: `state.name = "New Name"; session.commit()`
- **Delete an object**: `session.delete(state); session.commit()`

## Author

- [Morgan Bouaziz](https://github.com/Morg92b)
