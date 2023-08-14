## NOSQL Mongodb Practice

### 1. Install mongodb

#### 1.1 Install mongodb on Mac

```bash
brew install mongodb
```

#### 1.2 Install mongodb on Ubuntu

```bash
sudo apt-get install mongodb
```

### 2. Start mongodb

```bash
mongod
```

### 3. Connect to mongodb

```bash
mongo
```

### 4. Create database

```bash
use test
```

### 5. Create collection

```bash
db.createCollection("user")
```

### 6. Insert document

```bash
db.user.insert({"name":"xiaoming","age":18})
db.user.insert({"name":"xiaohong","age":20})
```

### 7. Query document

```bash
db.user.find()
db.user.find({"name":"xiaoming"})
db.user.find({"age":{$gt:18}})

db.user.find().sort({"age":1})
db.user.find().sort({"age":-1})

```
