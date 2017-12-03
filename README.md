# Bot for likes
### Configuring
First, you're need to create `security.properties` in the root of the project. It must look like this:
```properties
[api]
group_token=[Your group token]
user_login=[Your user login]
user_password=[Your user password]
[db]
database=[Your PostgreSQL database name]
user=[Your PostgreSQL database user]
password=[Your PostgreSQL database password]
host=[Your PostgreSQL database host]
```

### Running
Just run **make**:
```
make
```
