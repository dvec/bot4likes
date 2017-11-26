# Bot for likes
### Running
First, you're need to create security.properties in the root of the project. It must look like this:
```properties
[api]
group_token=[Your group token]
service_token=[Your service token]

[db]
database=[Your PostgreSQL database name]
user=[Your PostgreSQL database user]
password=[Your PostgreSQL database password]
host=[Your PostgreSQL database host]
```
Then just run **main.py**:
```
python [project path]/bot4likes/main.py
```