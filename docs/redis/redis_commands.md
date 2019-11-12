`redis-cli`
=

to run type `redis-cli`

#### string

- `set name alex` - set key=name, value=alex
- `get name` - get value alex by key name
- `del name` - delete key and value
- `expires name 30` - set expire time
- `ttl name` - display countdown
- `setex name 30 alex` - set key-value and expire in one command
- `mset name alex job foo` - multiple key-value set
- `append name " shchegretsov"` - append data to value
- `rename name full_name` - rename key
- `flushall` - clear all redis data


#### redis list, common commands

- `lpush people brad tom scott` - create list "people" and insert into LIST-HEAD each name
- `lrange people 0 -1` - display whole list
- `rpush people alex` - add value to the end of the list
- `llen people` - list length
- `lpop people` - remove first list element
- `rpop people` - remove last list element
- `linsert people before tom jack` - insert value "jack" before first occurrence of value tom


#### redis set, common

set - unordered collection of strings.
It's possible to add, remove or test for existence of members in O(1)

- `sadd cars honda` - create set "cars" and add value "honda"
- `smembers cars` - return all values in set
- `ismember cars ford` - is "ford" a cars member?
- `scard cars` - return how many elements in a set
- `smove cars ford_cars ford` - move value "ford" from cars set to ford_cars set
- `srem cars honda` - remove value "honda" from cars set


#### sorted sets, common

The difference is that every member of a sorted set is 
associated with the score. Score can repeat, but keys are unique.
it looks like:
```
# sorted by score, where score is year

1) 1989 "mike"
2) 1975 "John"
3) 1967 "alex"
4) 1953 "alexey" 
and so on
```

- `zadd users 1989 "mike x"` - create a sorted set users and add value
- `zrange users 0 -1` - display all set members or range from x to y
- `zrank users "mike x"` - return set index of value "mike x"
- `zincrby users "mike x"` - increment score of key "mike x"


#### hashes

- `hset user:alex name "Alex X"` - add key name with value "Alex X" to user:alex
- `hset user:alex email "x@.com"` - add another field
- `hgetall user:alex` - get all fields
- `hget user:alex name` - returns value of name field
- `hmset user:alex first alex last shchegretsov birthyear 1989` - set multiple fields
- `hkeys user:alex` - returns all keys
- `hvals user:alex` - returns all values
- `hincrby user:alex birthyear 1` - increment integer field
- `hdel user:alex age` - delete key age with it's associated value
- `hlen user:alex` - number of key-value pairs

