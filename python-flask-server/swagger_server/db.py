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
        db_table = 'YClogin'

class YCformlist(BaseModel):
    id= IntegerField()
    pingtai= CharField()
    area= CharField()
    status= CharField()
    complaint= CharField()
    Timeout= CharField()
    start_time=CharField()
    end_time=CharField()
    time_24_8=IntegerField()
    manyi=IntegerField()

    class Meta:
        db_table = 'YCformlist'


class YChistorical(BaseModel):
    id = IntegerField()
    type = CharField()
    down_num = IntegerField()
    filepath=CharField()
    status =CharField()
    time =CharField()

    class Meta:
        db_table = 'YChistorical'

class YCdown_file(BaseModel):
    pid = IntegerField()
    filetype = CharField()
    down_path = CharField()
    down_time =IntegerField()
    id=IntegerField()

    class Meta:
        db_table = 'YCdown_file'

class YCimport_file(BaseModel):
    pid = IntegerField()
    file_path = CharField()
    filetype=CharField()
    import_time =IntegerField()
    status=IntegerField()
    id=IntegerField()

    class Meta:
        db_table = 'YCimport_file'

