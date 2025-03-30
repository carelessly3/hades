"""
This is the configuration file for database.
DEFAULT_SSL_MODE can be `None` or `require`
MAIN_DATABASE property contains the DB which will be used to fetch activity and attempt data.
Each database configuration (both shard & main) contains 1 write node & multiple read replicas.
"""

DEFAULT_SSL_MODE = None

MONGO_LOCAL = {
    "PROTOCOL": "mongodb",
    "HOST": "localhost",
    "PORT": "27103",
    "USER": "",
    "PASSWORD": "",
    "NAME": "hades",
}

MONGO_DATABASE = MONGO_LOCAL
