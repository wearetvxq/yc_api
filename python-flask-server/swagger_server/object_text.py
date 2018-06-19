from swagger_server.mysql_db import *

# def cunzaixiaoyan(object,dict):
#     for k,val in dict.items():
#         if object.select().where(object.k==val).count()==1:
#             return True
#     return False

# db_dict={
#     "YCuse":YCuse
#
# }

# class Cunzaixiaoyan(YCuse):
#
#     def __init__(self, dicts):  # 先继承，在重构
#         super(Cunzaixiaoyan, self).__init__(self)  #继承父类的构造方法，也可以写成：super(Chinese,self).__init__(name,age)
#         self.dicts = dicts    # 定义类的本身属性
#
#     def cunzaixiaoyan(self):
#         for k,val in self.dicts.items():
#             if YCuse.select().where(object.k==val).count()==1:
#                 return True
#         return False
from swagger_server.tool import *


# 单条 传date
# 单挑过滤赛选
from swagger_server.importsql import *


def one_filter(db, k, val):
    date = db.select()
    if val != None and val != '':
        if k == 'starttime':
            starttime = utc_str_to_timestamp(val)
            data = date.where(starttime <= db.posttime)
        if k == 'endtime':
            endtime = utc_str_to_timestamp(val)
            data = date.where(db.posttime <= endtime)
        if k == 'work':
            work = get_sort_or_name(YCwork, val)
            data = date.where(db.work == work)
        if k == 'type':
            type = get_sort_or_name(YCterminal_type, val)
            data = date.where(db.type == type)
        if k == 'model':
            model = get_sort_or_name(YCterminal_model, val)
            data = date.where(db.model == model)
        if k == 'order':
            data = date.where(db.order == val)
        if k == 'status':
            data = date.where(db.status == val)
        return data
    else:
        return date


def _filter(db, **kw):
    for k, val in kw.items():
        if val != None and val != '':
            date = one_filter(db, k, val)
            print(date.count())
    num = 0
    for val in kw.values():
        if val == None or val == '':
            num += 1
    if num == len(kw):
        date = db.select()
    return date


def if_exist_one(db, k, val):
    if k == 'order' and db.select().where(db.order == val).count() == 1:
        return True
    if k == 'code' and db.select().where(db.code == val).count() == 1:
        return True
    if k == 'ocode' and db.select().where(db.ocode == val).count() == 1:
        return True
    if k == 'orderid' and db.select().where(db.orderid == val).count() == 1:
        return True
    return False


def if_exist_all(db, **kw):
    num = 0
    for k, val in kw.items():
        if if_exist_one(db, k, val):
            num += 1
    if num == len(kw):
        print(len(kw))
        return True
    return False


def if_not_exist_one(db, k, val):
    if k == 'order' and db.select().where(db.order == val).count() != 1:
        return True
    if k == 'code' and db.select().where(db.code == val).count() != 1:
        return True
    if k == 'ocode' and db.select().where(db.ocode == val).count() != 1:
        return True
    if k == 'orderid' and db.select().where(db.orderid == val).count() != 1:
        return True
    return False


def if_not_exist_all(db, **kw):
    num = 0
    for k, val in kw.items():
        if if_not_exist_one(db, k, val):
            num += 1
    if num == len(kw):
        print(len(kw))
        return True
    return False


def get_sort_or_name(db, sn):
    if sn.isdigit():
        return db.select().where(db.sort == sn).get().name
    else:
        return db.select().where(db.name == sn).get().sort


import xlrd


def uploadmanyi():
    data = xlrd.open_workbook('/var/www/downfile/张萌_装机IVR满意度回访4月.xls')
    sheet1 = data.sheet_by_index(0)
    nrows = sheet1.nrows
    print(nrows)
    for i in range(4, nrows + 1):
        row_data = sheet1.row_values(i)
        code = row_data[3]
        code_sa = row_data[11]
        print(if_not_exist_one(YCinstalled, 'orderid', code))
        print(code)
        print(code_sa)
        data = YCinstalled.select().where(YCinstalled.orderid == code)  #27172018010359808319
        print(data.count())
        for i in data:
            print(i.satisfied)
        if if_not_exist_one(YCinstalled, 'orderid', code):
            continue
        if code_sa == '满意':
            YCinstalled.update(satisfied=1).where(YCinstalled.orderid == code).execute()
            print('manyi')
        if code_sa == '不满意':
            YCinstalled.update(satisfied=2).where(YCinstalled.orderid == code).execute()
            print('bumanyi')
        if code_sa == '未回复':
            YCinstalled.update(satisfied=0).where(YCinstalled.orderid == code).execute()
            print('weihuifu')


import xlwt


def exprort(data, name, style, *args):
    workbook_m = xlwt.Workbook(encoding='utf-8')
    xlsheet = workbook_m.add_sheet(name, cell_overwrite_ok=True)
    # 格式1 （有自动换行）
    style1 = xlwt.easyxf('pattern: pattern solid, fore_colour white')
    style1.font.height = 200
    style1.font.name = u'文泉驿点阵正黑'
    style1.font.colour_index = 0
    style1.borders.left = xlwt.Borders.THIN
    style1.borders.right = xlwt.Borders.THIN
    style1.borders.top = xlwt.Borders.THIN
    style1.borders.bottom = xlwt.Borders.THIN
    # style1.font.bold = True
    style1.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
    style1.alignment.horz = xlwt.Alignment.HORZ_CENTER

    # 格式2  （没有自动换行）
    style2 = xlwt.easyxf('pattern: pattern solid, fore_colour white')
    style2.font.height = 200
    style2.font.name = u'文泉驿点阵正黑'
    style2.font.colour_index = 0
    style2.borders.left = xlwt.Borders.THIN
    style2.borders.right = xlwt.Borders.THIN
    style2.borders.top = xlwt.Borders.THIN
    style2.borders.bottom = xlwt.Borders.THIN
    # style2.font.bold = True
    # style2.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
    # style2.alignment.horz = xlwt.Alignment.HORZ_CENTER

    # 格式3 黄色背景色
    style3 = xlwt.easyxf('pattern: pattern solid, fore_colour yellow')
    style3.font.height = 200
    style3.font.name = u'文泉驿点阵正黑'
    style3.font.colour_index = 0
    # style3.borders.left = xlwt.Borders.THIN
    # style3.borders.right = xlwt.Borders.THIN
    # style3.borders.top = xlwt.Borders.THIN
    # style3.borders.bottom = xlwt.Borders.THIN

    # style4 格式4 0.00%
    style4 = xlwt.easyxf('pattern: pattern solid, fore_colour white')
    style4.font.height = 200
    style4.font.name = u'文泉驿点阵正黑'
    style4.font.colour_index = 0
    style4.borders.left = xlwt.Borders.THIN
    style4.borders.right = xlwt.Borders.THIN
    style4.borders.top = xlwt.Borders.THIN
    style4.borders.bottom = xlwt.Borders.THIN
    # style4.font.bold = True
    style4.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
    style4.alignment.horz = xlwt.Alignment.HORZ_CENTER
    style4.num_format_str = '0.00%'

    # style2.font.bold = True
    # style2.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
    # style2.alignment.horz = xlwt.Alignment.HORZ_CENTER
    # 写excel表头
    # 设置单元格
    style_dict = {
        'style1': style1,
        'style2': style2,
        'style3': style3,
        'style4': style4,
    }
    for i, val in enumerate(args):
        xlsheet.write(0, i, val, style_dict[style])

    number = 0
    for item in data:
        number += 1
        for j, val in enumerate(item):
            xlsheet.write(number, j, val)
            # for j in range(0,len(item)):
            #     xlsheet.write(number, j, item['j'])
    xlsname = name + str(int(time.time()))
    workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
    return xlsname


def sql():
    import time
    Post = YCinstalled  # fn.COUNT(Post.id).alias('num')
    # data = time.time() - 604800
    data=0
    # mydata_2 = Post.select(fn.COUNT(YCinstalled.satisfied).alias('satisfied_num')).where(YCinstalled.posttime>=data,YCinstalled.satisfied==2)
    mydata_2=Post.select().where(YCinstalled.satisfied==2).count()
    print(mydata_2)
    # for i in mydata_2:
    #     print(i.satisfied_num)

import datetime
def get_yes_time():
    now_time = datetime.datetime.now()
    yes_time = now_time + datetime.timedelta(days=-1)
    yes_time_nyr = yes_time.strftime('%Y-%m-%d') #//格式化输出

#获取上个月的时间
def get_f_l_day():
    #上一个月的第一天
    lst_fist = str(datetime.date(datetime.date.today().year,datetime.date.today().month-1,1))+' 00:00:00'
    #上一个月的最后一天
    lst_last = str(datetime.date(datetime.date.today().year,datetime.date.today().month,1)-datetime.timedelta(1))+' 23:59:59'
    return (lst_fist,lst_last)


def desc_all(self):
    data=YChome
    data=data.select().order_by(YChome.posttime.desc())
    # data=YChome.select().count()
    print(data)
    return data


def desc_one(self,id):
    data=YChome.select().where(YChome.id==id).get()
    return data

#如果要重写这个create 加上posttime等于datatime 的话 应该要改写 BaseModel这个类 改名 集成 加这个方法 同时这个方法super creat这个方法

# if __name__ == '__main__':
#     p=YChome()
#     p.create(content='sdasd',type=1,posttime=int(time.time()),title='titlehythty')
    # p.content='sdasd'
    # p.type='dsadad'
    # p.posttime=int(time.time())
    # p.title='titlehythty'
    # p.save()
    # print([{"id":item.id}for item in p.desc_all()])

    # uploadmanyi()
    # b=YCinstalled.select().where(YCinstalled.orderid=='27172018050720718443').count()
    # a=if_exist_one(YCinstalled,'orderid','27172018050720718443')
    # print(a)
    # print(b)
    # data=YCinstalled.select().where(YCinstalled.orderid=='27172018040186814671')
    # print(data.count())
    # for i in data:
    #     print(i.satisfied)
    # sql()
    # data = [['a', 'b', 'c', 'd'], ['a', 'b', 'c', 'd'], ['a', 'b', 'c', 'd'], ['a', 'b', 'c', 'd'],
    #         ['a', 'b', 'c', 'd']]
    #
    # exprort(data, 'text', 'style4', 'A', 'B', 'C', 'D')

    # date2= one_fileter(date,'work','宜昌城区')
    # print(date2.count())
    # date=_filter(YCuse,order=None,work=None)

    # date = _filter(YCoutbound, status=None,work='宜昌城区')
    # print(str(date.count())+'gl')

    # datetimenowTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # print(datetimenowTime)
    # time1=datetimenowTime[0:7]+'-01 00:00:00'
    # time1 = datetimenowTime[0:7] + '-01 00:00:00'
    # str='1234567'
    # if str.isdigit():
    #     print('ok')
    # print(YCuse)
    # a=Cunzaixiaoyan(YCuse)
    # b={
    #     "order":"3194109640",
    #     "people": "马宏宇",
    # }
    # for k,val in b.items():
    #     print(k)
