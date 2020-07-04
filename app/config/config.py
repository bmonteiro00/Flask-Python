from os import getenv


class Config:
    MONGODB_HOST = getenv('MONGODB_HOST')
    MONGODB_DATABSE = getenv('MONGODB_DATABASE')

