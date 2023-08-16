## Nosql Database, Redis

### 1. Redis Basic Commands

#### 1.1. Redis Basic Commands

- `SET key value` : Set the string value of a key
- `GET key` : Get the value of a key
- `DEL key` : Delete a key
- `EXISTS key` : Determine if a key exists
- `KEYS pattern` : Find all keys matching the given pattern
- `FLUSHALL` : Remove all keys from all databases
- `FLUSHDB` : Remove all keys from the current database
- `DBSIZE` : Return the number of keys in the current database
- `SAVE` : Synchronously save the dataset to disk
- `BGSAVE` : Asynchronously save the dataset to disk
- `LASTSAVE` : Get the UNIX time stamp of the last successful save to disk
- `INFO` : Get information and statistics about the server
- `MONITOR` : Listen for all requests received by the server in real time
- `SLAVEOF host port` : Make the server a slave of another instance, or promote it as master
- `CONFIG get parameter` : Get the value of a configuration parameter
- `CONFIG set parameter value` : Set a configuration parameter to the given value

#### 1.2. Redis String Commands

- `SET key value` : Set the string value of a key
- `GET key` : Get the value of a key
- `GETRANGE key start end` : Get a substring of the string stored at a key
- `GETSET key value` : Set the string value of a key and return its old value
- `GETBIT key offset` : Return the bit value at offset in the string value stored at a key
- `MGET key [key ...]` : Get the values of all the given keys
- `SETBIT key offset value` : Sets or clears the bit at offset in the string value stored at a key
- `SETEX key seconds value` : Set the value and expiration of a key
- `SETNX key value` : Set the value of a key, only if the key does not exist
- `SETRANGE key offset value` : Overwrite part of a string at key starting at the specified offset
- `STRLEN key` : Get the length of the value stored in a key
- `MSET key value [key value ...]` : Set multiple keys to multiple values

#### 1.3. Redis Hash Commands

- `HSET key field value` : Set the string value of a hash field
- `HGET key field` : Get the value of a hash field
- `HDEL key field [field ...]` : Delete one or more hash fields
- `HEXISTS key field` : Determine if a hash field exists

#### 1.4. Redis List Commands

- `LPUSH key value [value ...]` : Prepend one or multiple values to a list
- `RPUSH key value [value ...]` : Append one or multiple values to a list
- `LPOP key` : Remove and get the first element in a list
- `RPOP key` : Remove and get the last element in a list
- `LLEN key` : Get the length of a list
- `LRANGE key start stop` : Get a range of elements from a list
- `LINDEX key index` : Get an element from a list by its index
- `LSET key index value` : Set the value of an element in a list by its index
- `LTRIM key start stop` : Trim a list to the specified range
- `LREM key count value` : Remove elements from a list by value
- `RPOPLPUSH source destination` : Remove the last element in a list, prepend it to another list and return it

#### 1.5. Redis Set Commands

- `SADD key member [member ...]` : Add one or more members to a set
- `SREM key member [member ...]` : Remove one or more members from a set
- `SISMEMBER key member` : Determine if a given value is a member of a set
