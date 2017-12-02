# Bot for likes
### Configuring
First, you're need to create security.properties in the root of the project. It must look like this:
```properties
[api]
group_token=[Your group token]
user1.login=[Your first account login]
user1.password=[Your first account password]

# You can pass only one account, but it's better to pass more
user2.login=[Your second account login]
user2.password=[Your second account password]

[db]
database=[Your PostgreSQL database name]
user=[Your PostgreSQL database user]
password=[Your PostgreSQL database password]
host=[Your PostgreSQL database host]
```
### Running
It's very simple. Just run make:
```
make run
```