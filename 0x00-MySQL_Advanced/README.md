## Mysql Advance

### Learning Objectives
- [x] How to create tables with constraints
- [x] How to optimize queries by adding indexes
- [x] What is and how to implement stored procedures and functions in MySQL
- [x] What is and how to implement views in MySQL
- [x] What is and how to implement triggers in MySQL


### Tasks
#### 0. We are all unique!
Write a SQL script that creates a table users following these requirements:
- With these attributes:
  - id, integer, never null, auto increment and primary key
  - email, string (255 characters), never null and unique
  - name, string (255 characters)

#### 1. In and not out
Write a SQL script that creates a table users following these requirements:
- With these attributes:
  - id, integer, never null, auto increment and primary key
  - email, string (255 characters), never null and unique
  - name, string (255) characters
  - country, enumeration of countries: US, CO and TN, never null (= default will be the first element of the enumeration)
  - created_at, datetime, never null and default value will be the current datetime
  - updated_at, datetime, never null and default value will be the current datetime

#### 2. Best band ever!
Write a SQL script that ranks country origins of bands, ordered by the number of (non-unique) fans
- Database: `database_optimization`
- Table: `bands`
- Column: `origin`
- Number of records: 150,000 (feel free to generate different values if you want)
- Import: [bands.sql](
https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/2-ranking_bands.sql)

#### 3. Old school band
Write a SQL script that ranks country origins of bands, ordered by the number of (non-unique) fans
- Database: `database_optimization`
- Table: `bands`
- Column: `origin`
- Number of records: 150,000 (feel free to generate different values if you want)
- Import: [bands.sql](
https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/3-ranking_bands.sql)

