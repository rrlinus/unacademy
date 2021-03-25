import os
DEBUG = os.getenv("ENVIRONEMENT") == "DEV"
HOST = os.getenv("APPLICATION_HOST", "localhost")
PORT = int(os.getenv("APPLICATION_PORT", "5000"))


DB_CONTAINER = os.getenv("APPLICATION_DB_CONTAINER", "localhost")


POSTGRES = {
    "user": os.getenv("DB_USER", "root"),
    "pw": os.getenv("DB_PW", ""),
    "host": os.getenv("DB_HOST", DB_CONTAINER),
    "port": os.getenv("DB_PORT", 3306),
    "db": os.getenv("DB", "unacademy"),
}
