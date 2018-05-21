import peewee
from peewee import *

database = MySQLDatabase('ycyd', **{'host': '39.108.165.149', 'port': 3306, 'user': 'wy','password':'wy666666'})
#--------------test---------
#database = MySQLDatabase('ycyd', **{'host': 'localhost', 'port': 3306, 'user': 'root','password':'123456'})
class UnknownField(object):
    def __init__(self, *_, **__):
        pass

class BaseModel(Model):
    class Meta:
        database = database

class YClogin(BaseModel):
    username = CharField()
    passwd = CharField()
    posttime = IntegerField()

    class Meta:
        db_table = 'yd_login'