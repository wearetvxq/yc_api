# coding=utf8
import peewee
from peewee import *

database = MySQLDatabase('ycyd', **{'host': '39.108.165.149', 'port': 3306, 'user': 'root', 'password': 'lcj123456'})


# --------------test---------
# database = MySQLDatabase('ycyd', **{'host': 'localhost', 'port': 3306, 'user': 'root','password':'123456'})
class UnknownField(object):
    def __init__(self, *_, **__):
        pass


class BaseModel(Model):
    class Meta:
        database = database


class YCadmin(BaseModel):
    id = IntegerField()
    username = CharField()
    passwd = CharField()
    posttime = IntegerField()

    class Meta:
        db_table = 'yc_admin'


class YCcomplaints(BaseModel):
    id = IntegerField()
    platform = IntegerField()
    area = CharField()
    status = CharField()
    type = CharField()
    timeout = CharField()
    starttime = IntegerField()
    endtime = IntegerField()
    rate = CharField()
    pid = IntegerField()
    posttime = IntegerField()
    usetime = FloatField()
    tsaddress = CharField()
    contacts = CharField()
    phone = CharField()
    fristtime = IntegerField()
    serial = CharField()
    t2endtime = IntegerField()
    manyi = IntegerField()
    network = CharField()

    class Meta:
        db_table = 'yc_complaints'


class YCimport(BaseModel):
    id = IntegerField()
    name = CharField()
    path = CharField()
    type = IntegerField()
    posttime = IntegerField()

    class Meta:
        db_table = 'yc_import'


class YCinstalled(BaseModel):
    id = IntegerField()
    type = IntegerField()
    area = CharField()
    status = CharField()
    timeout = CharField()
    account = CharField()
    grid = CharField()
    orderid = CharField()
    service = CharField()
    phone = CharField()
    attach = CharField()
    transfer = CharField()
    pboos = CharField()
    accept = IntegerField()
    orders = IntegerField()
    receipt = CharField()
    confirm = IntegerField()
    links = CharField()
    recent = CharField()
    areaType = CharField()
    pid = IntegerField()
    posttime = IntegerField()
    satisfied = IntegerField()

    class Meta:
        db_table = 'yc_installed'


# 维护使用明细表
# 工作站ID
# 投诉工单工单号
# 更换终端类型ID
# 原条形码
# 新条形码
# 装维人员
# 维护使用时间
class YCmaintain(BaseModel):
    work = IntegerField()
    order = CharField()
    type = IntegerField()
    ocode = CharField()
    code = CharField()
    people = CharField()
    posttime = IntegerField()

    class Meta:
        db_table = 'yc_maintain'


# '业务字典表'
# 工作站名称
# 排序

class YCbusiness(BaseModel):
    name = CharField()
    sort = IntegerField()

    class Meta:
        db_table = 'yc_business'


# 入库明细表（库存）  出口？
# 工作站ID
# 终端类型ID
# 厂家名称
# 型号ID
# 条形码
# 装维人员
# 申领时间

class YCoutbound(BaseModel):
    work = IntegerField()
    type = IntegerField()
    factory = CharField()
    model = IntegerField()
    code = CharField()
    people = CharField()
    posttime = IntegerField()
    status = IntegerField()

    class Meta:
        db_table = 'yc_outbound'


# 装维人员字典表
# 工作站名称
# 排序
# 工作站ID
class YCpeople(BaseModel):
    name = CharField()
    sort = IntegerField()
    pid = IntegerField()
    phone = IntegerField()
    class Meta:
        db_table = 'yc_people'


# '终端设备状态记录表'
# 工作站ID
# 用途
# 申领人
# 条形码
# 时间
class YCstatus(BaseModel):
    work = IntegerField()
    use = CharField()
    people = CharField()
    code = CharField()
    posttime = IntegerField()

    class Meta:
        db_table = 'yc_status'


# 入库明细表（库存）
# 工作站ID
# 终端类型ID
# 厂家名称
# 型号ID
# 条形码
# 入库人
# 入库时间
# 库存状态，用户区分设备是否被领取，默认为0，1表示被领取
class YCstorage(BaseModel):
    work = IntegerField()
    type = IntegerField()
    factory = CharField()
    model = IntegerField()
    code = CharField()
    people = CharField()
    posttime = IntegerField()
    status = IntegerField()

    class Meta:
        db_table = 'yc_storage'


# 终端型号字典表'
# 工作站名称
# 排序
# 工作站ID

class YCterminal_model(BaseModel):
    name = CharField()
    sort = IntegerField()
    pid = IntegerField()

    class Meta:
        db_table = 'yc_terminal_model'


# '终端类型字典表'
# 工作站名称
# 排序
class YCterminal_type(BaseModel):
    name = CharField()
    sort = IntegerField()

    class Meta:
        db_table = 'yc_terminal_type'


# ='装机使用明细'
# 工作站ID
# 业务类型ID
# 装机工单业务账号
# 光猫条形码
# 智能网关条形码
# 机顶盒条形码
# 和目条形码
# 固话（移动产权）条形码
# 装维人员
# 使用时间
class YCuse(BaseModel):
    work = IntegerField()
    business = IntegerField()
    order = CharField()
    modem = CharField()
    gateway = CharField()
    box = CharField()
    hemu = CharField()
    phone = CharField()
    people = CharField()
    posttime = IntegerField()
    type = IntegerField()
    produce = CharField()

    class Meta:
        db_table = 'yc_use'


# '返厂及报废设备明细表'
# 工作站ID
# 终端类型
# 报废条形码
# 生产厂家
# 设备型号ID
# 报废时间
# 1:表示报废设备；2:表示返厂设备


class YCwaste(BaseModel):
    work = IntegerField()
    type = IntegerField()
    code = CharField()
    factory = CharField()
    model = IntegerField()
    posttime = IntegerField()
    status = IntegerField()

    class Meta:
        db_table = 'yc_waste'


# ='工作站字典表'

class YCwork(BaseModel):
    name = CharField()
    sort = IntegerField()

    class Meta:
        db_table = 'yc_work'


class YChome(BaseModel):
    content = TextField()
    posttime = IntegerField()
    title = CharField()
    type = IntegerField()

    class Meta:
        db_table = 'yc_home'

    #
    # def __init__(self,id):
    #     self.id=id

    @property
    def desc_1_five(self):
        data = YChome
        data = data.select().where(YChome.type == 1).order_by(YChome.posttime.desc()).limit(5)
        # data=YChome.select().count()
        print(data)
        return data

    @property
    def desc_2_five(self):
        data = YChome
        data = data.select().where(YChome.type == 2).order_by(YChome.posttime.desc()).limit(5)
        # data=YChome.select().count()
        print(data)
        return data

    def desc_one(self, id):
        data = YChome.select().where(YChome.id == id).get()
        return data
        # print(p.desc_one(id=1).posttime)


if __name__ == '__main__':
    ychome = YChome
    ychome.create(
        content='6在11月的装机劳模评选中，装机人员李四成绩突出，表现优异，创造了单月装机120单的佳绩。该员工充分发挥了宜昌移动员工不怕苦......',
        posttime=1527647795,
        title='【通知通报】6对11月份装机劳模李四的表彰通知',
        type=1,

    )

# import random, time

#
# def get_num():
#     num = ''.join(str(random.choice(range(10))) for _ in range(10))
#     return num
#
#
# def get_id():
#     num = random.choice(range(1, 5))
#     return num
