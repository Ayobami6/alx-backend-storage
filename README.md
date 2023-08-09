## Backend Storage With Database

### 1. Introduction

In this section, we will introduce how to use database as backend storage. We will use MySQL as an example.

### 2. Prerequisites

- MySQL 5.7 or higher
- Python 3.6 or higher
- Python MySQL Connector

### 3. Database Configuration

#### 3.1 Create Database

First, we need to create a database for our project. We can use MySQL command line tool to create a database named `mydb`:

```sql
CREATE DATABASE mydb;
```

#### 3.2 Create Table

Then, we need to create a table named `mytable` in the database. We can use MySQL command line tool to create a table named `mytable`:

```sql
CREATE TABLE mytable (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    PRIMARY KEY (id)
);
```

#### 3.3 Create User

Next, we need to create a user for our project. We can use MySQL command line tool to create a user named `myuser`:

```sql
CREATE USER 'myuser'@'localhost' IDENTIFIED BY 'mypassword';
```

#### 3.4 Grant Privileges

Finally, we need to grant privileges to the user. We can use MySQL command line tool to grant privileges to the user:
