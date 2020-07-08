import os


class Config:
    MONGODB_HOST = os.environ.get("MONGODB_HOST", default="localhost")
    MONGODB_DATABSE = os.environ.get("MONGODB_DATABASE", default="gitbase")

