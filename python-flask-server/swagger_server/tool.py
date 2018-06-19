import hashlib, base64, requests, json
from swagger_server.mysql_db import *
import time
import xlsxwriter
from swagger_server.export_report import *
from collections import Counter


# from db import *


# 加密方法
def encryption(data):
    encodestr = base64.b64encode(data.encode(encoding="utf-8"))
    mstr = encodestr.decode('UTF-8')[::-1].upper()
    return hashlib.md5(mstr.encode('UTF-8')).hexdigest().upper()


# 获取坐标
def getxy(address, area):
    if address != '1.0' and address != '---':
        if address.find('FTTH') != -1 and ('-') not in address:
            url1 = 'http://api.map.baidu.com/geocoder/v2/?address=' + address.replace('FTTH',
                                                                                      '') + '&output=json&ak=gRManfxm4xGfswhaIT4xGh78UpHV8kCV'
            r = requests.get(url1)
            print(address)
            result = json.loads(r.text)
            x = result['result']['location']['lng']
            print(x)
            y = result['result']['location']['lat']
            xy = [x, y]
        if address.find('-') != -1:
            url1 = 'http://api.map.baidu.com/geocoder/v2/?address=' + address.split('-')[
                0] + '&output=json&ak=gRManfxm4xGfswhaIT4xGh78UpHV8kCV'
            r = requests.get(url1)
            print(address)
            result = json.loads(r.text)
            x = result['result']['location']['lng']
            print(x)
            y = result['result']['location']['lat']
            xy = [x, y]
        else:
            url1 = 'http://api.map.baidu.com/geocoder/v2/?address=' + address + '&output=json&ak=gRManfxm4xGfswhaIT4xGh78UpHV8kCV'
            r = requests.get(url1)
            print(address)
            result = json.loads(r.text)
            x = result['result']['location']['lng']
            print(x)
            y = result['result']['location']['lat']
            xy = [x, y]

        return (xy)
    else:
        url1 = 'http://api.map.baidu.com/geocoder/v2/?address=宜昌' + area + '&output=json&ak=gRManfxm4xGfswhaIT4xGh78UpHV8kCV'
        r = requests.get(url1)
        result = json.loads(r.text)
        x = result['result']['location']['lng']
        y = result['result']['location']['lat']
        xy = [x, y]
        return (xy)


def getmanyi(msg):
    manyi = 21  # 人工满意 2？代表人工，1？代表ivr 后面的1代表满意，0代表不满意
    if msg.find('IVR') != -1 and msg.find('【满意】') != -1:
        manyi = 11
    if msg.find('IVR') != -1 and msg.find('【不满意】') != -1:
        manyi = 10
    if msg.find('IVR') == -1 and msg.find('【满意】') != -1:
        manyi = 21
    if msg.find('IVR') == -1 and msg.find('【不满意】'):
        manyi = 20
    return manyi

# 修正坐标


#获取小区名
def getxiaoqu(address):
    try:
        if address.find('小区')!=-1:
            xiaoqu=re.findall(r'.*?小区',address)[0]
            return xiaoqu
        if address.find('小区')==-1:
            xiaoqu='null'
            return xiaoqu
    except:
        pass
#获取高频小区list
def gethigh(area,starttime,endtime,type):
    if type=='EMOS':
        result_list = []
        high=[]
        like="%"+area+"%"
        data = YCcomplaints.select().where( (YCcomplaints.platform==2) &(YCcomplaints.starttime >= utc_str_to_timestamp(starttime)) & (
        YCcomplaints.endtime < utc_str_to_timestamp(endtime)) & (YCcomplaints.type=='服务质量') & (YCcomplaints.area % like))

        for item in data:
            try:
                if item.tsaddress != '---' and item.tsaddress != '1.0' and item.tsaddress != '' and item.tsaddress != 'A市B区':
                    xiaoqu_msg=re.findall(r'.*?[花园|小区|社区|片区|号|栋]',item.tsaddress)[0]
                    result_list.append(xiaoqu_msg)

            except:
                xiaoqu_msg=item.tsaddress
                result_list.append(xiaoqu_msg)
        msg_list = Counter(result_list).most_common(20)
        #选取大于次数3 的小区
        for xiaoqu in msg_list:
            if xiaoqu[1] >= 3:
                high.append([xiaoqu[0]])
        total=0
        for addrss in high:
            addlike='%' +addrss[0] +'%'
            total=total+data.where(YCcomplaints.tsaddress % addlike).count()
            addrss.append(total)
        return (high)
    if type == '微信一键报障':
        result_list = []
        high=[]
        like = "%" + area + "%"
        data = YCcomplaints.select().where(
            (YCcomplaints.platform == 1) & (YCcomplaints.starttime >= utc_str_to_timestamp(starttime)) & (
                YCcomplaints.endtime < utc_str_to_timestamp(endtime)) & (YCcomplaints.type == '服务质量') & (
            YCcomplaints.area % like))
        for item in data:
            result_list.append(item.tsaddress)
        msg_list = Counter(result_list).most_common(20)
        for xiaoqu  in msg_list:
            if xiaoqu[1]>=3:
                high.append([xiaoqu[0]])
        total = 0
        for addrss in high:
            addlike='%' +addrss[0] +'%'
            total=total+data.where(YCcomplaints.tsaddress % addlike).count()
            addrss.append(total)
        return (high,total)
# #获取高频小区infolist
def gethigh1(area,starttime,endtime,type):
    if type=='EMOS':
        result_list = []
        high=[]
        like="%"+area+"%"
        data = YCcomplaints.select().where( (YCcomplaints.platform==2) &(YCcomplaints.starttime >= utc_str_to_timestamp(starttime)) & (
        YCcomplaints.endtime < utc_str_to_timestamp(endtime)) & (YCcomplaints.type=='服务质量') & (YCcomplaints.area % like))

        for item in data:
            try:
                if item.tsaddress !='---' and item.tsaddress!='1.0' and item.tsaddress!='' and item.tsaddress!='A市B区':
                    xiaoqu_msg=re.findall(r'.*?[花园|小区|社区|片区|号|栋]',item.tsaddress)[0]
                    result_list.append(xiaoqu_msg)

            except:
                xiaoqu_msg=item.tsaddress
                result_list.append(xiaoqu_msg)
        msg_list = Counter(result_list).most_common(10)
        for xiaoqu in msg_list:
            if xiaoqu[1] >= 3:
                high.append([xiaoqu[0],xiaoqu[1]])
        total=0
        for addrss in high:
            addlike='%' +addrss[0] +'%'
            total=total+data.where(YCcomplaints.tsaddress % addlike).count()
        return (high,total)
    if type == '微信一键报障':
        result_list = []
        high=[]
        like = "%" + area + "%"
        data = YCcomplaints.select().where(
            (YCcomplaints.platform == 1) & (YCcomplaints.starttime >= utc_str_to_timestamp(starttime)) & (
                YCcomplaints.endtime < utc_str_to_timestamp(endtime)) & (YCcomplaints.type == '服务质量') & (
            YCcomplaints.area % like))
        for item in data:
            result_list.append(item.tsaddress)
        msg_list = Counter(result_list).most_common(10)
        for xiaoqu  in msg_list:
            if xiaoqu[1]>=3:
                high.append([xiaoqu[0],xiaoqu[1]])
        total = 0
        for addrss in high:
            addlike='%' +addrss[0] +'%'
            total=total+data.where(YCcomplaints.tsaddress % addlike).count()
        return (high,total)

def utc_str_to_timestamp(dt):
    timeArray = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
    # 转换成时间戳
    timestamp = time.mktime(timeArray)
    return (int(timestamp))


def utc_timestamp_to_str(dt):
    # 时间戳变成字符串
    timeArray = time.localtime(dt)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return otherStyleTime


def utc_timestamp_to_str3(dt):
    # 时间戳变成字符串
    timeArray = time.localtime(dt)
    otherStyleTime = time.strftime("%Y-%m-%d", timeArray)
    return otherStyleTime


def out_make_report(starttime=None, endtime=None, work=None, type=None, model=None, keyword=None):
    if (starttime != None and starttime != '') or \
            (endtime != None and endtime != '') or \
            (work != None and work != '') or \
            (type != None and type != '') \
            or (model != None and model != '') \
            or (keyword != None and keyword != ''):
        data = YCoutbound.select()
        print (data.count())
        if keyword != None and keyword != '':
            #  厂家 条形码  入库人 均为字符串赛选
            print (keyword)
            like = '%' + keyword + '%'
            data = data.where((YCoutbound.factory % like) |
                              (YCoutbound.code % like) |
                              (YCoutbound.people % like))
        if starttime != None and starttime != '':
            starttime = utc_str_to_timestamp(starttime)
            data = data.where(starttime <= YCoutbound.posttime)
        if endtime != None and endtime != '':
            endtime = utc_str_to_timestamp(endtime)
            data = data.where(YCoutbound.posttime <= endtime)
        if work != None and work != '':
            work = get_work_sort(work)
            data = data.where(YCoutbound.work == work)
        if type != None and type != '':
            type = get_type_sort(type)
            data = data.where(YCoutbound.type == type)
        if model != None and model != '':
            model = get_model_sort(model)
            data = data.where(YCoutbound.model == model)
    else:
        data = YCoutbound.select()

    name = str(int(time.time()))

    name = utc_timestamp_to_str(name)
    name = name + '申领报表'

    workbook = xlsxwriter.Workbook('/var/www/downfile/{}.xlsx'.format(name))  # 建立文件

    worksheet = workbook.add_worksheet('sheet1')
    # worksheet = workbook.add_sheet('sheet1')
    bold = workbook.add_format({'bold': True})
    # worksheet.set_column('A:F', 15)
    # worksheet.set_column('G:G', 38)
    # worksheet.set_default_row(55)
    worksheet.write(0, 0, '工作站', bold)
    worksheet.write(0, 1, '装维人员', bold)
    worksheet.write(0, 2, '终端类型', bold)
    worksheet.write(0, 3, '厂家', bold)
    worksheet.write(0, 4, '型号', bold)
    worksheet.write(0, 5, '条形码', bold)
    worksheet.write(0, 6, '申领时间', bold)
    # worksheet.write(0, 7, '最新状态', bold)
    number = 0
    for item in data:
        number += 1
        # work =YCwork.select().where(YCwork.sort==item.work).get()
        # type =YCterminal_type.select().where(YCwork.sort==item.type).get()
        # model=YCterminal_model.select().where(YCwork.sort==item.model).get()
        # 直接改成映射函数
        work = get_work_name(item.work)
        type = get_type_name(item.type)
        model = get_model_name(item.model)
        worksheet.write(number, 0, work)
        worksheet.write(number, 1, item.people)
        worksheet.write(number, 2, model)
        worksheet.write(number, 3, item.factory)
        worksheet.write(number, 4, type)
        posttime = utc_timestamp_to_str(item.posttime)
        worksheet.write(number, 5, item.code)
        worksheet.write(number, 6, posttime)

    workbook.close()
    # result={}
    # result['name']='{}.xlsx'.format(name)
    # result['times']=times

    print (name)
    return '{}.xlsx'.format(name)
    # return result


    # work =YCwork.select().where(YCwork.sort==item.work).get()
    #     type =YCterminal_type.select().where(YCwork.sort==item.type).get()
    #     model=YCterminal_model.select().where(YCwork.sort==item.model).get()


def maintain_make_report(starttime=None, endtime=None, work=None, type=None, keyword=None):
    if (starttime != None and starttime != '') or \
            (endtime != None and endtime != '') or \
            (work != None and work != '') or \
            (type != None and type != '') \
            or (keyword != None and keyword != ''):
        data = YCmaintain.select()
        print (data.count())
        if keyword != None and keyword != '':
            #  厂家 条形码  入库人 均为字符串赛选
            # 条形码有多个
            print (keyword)
            like = '%' + keyword + '%'
            data = data.where((YCmaintain.order % like) |
                              (YCmaintain.code % like) |
                              (YCmaintain.ocode % like) |
                              (YCmaintain.people % like))
        if starttime != None and starttime != '':
            starttime = utc_str_to_timestamp(starttime)
            data = data.where(starttime <= YCmaintain.posttime)
        if endtime != None and endtime != '':
            endtime = utc_str_to_timestamp(endtime)
            data = data.where(YCmaintain.posttime <= endtime)
        if work != None and work != '':
            work = get_work_sort(work)
            data = data.where(YCmaintain.work == work)
        if type != None and type != '':
            type = get_type_sort(type)
            data = data.where(YCmaintain.type == type)

    else:
        data = YCmaintain.select()

    name = str(int(time.time()))

    name = utc_timestamp_to_str(name)
    name = name + '维护报表'
    workbook = xlsxwriter.Workbook('/var/www/downfile/{}.xlsx'.format(name))  # 建立文件

    worksheet = workbook.add_worksheet('sheet1')
    # worksheet = workbook.add_sheet('sheet1')
    bold = workbook.add_format({'bold': True})
    # worksheet.set_column('A:F', 15)
    # worksheet.set_column('G:G', 38)
    # worksheet.set_default_row(55)
    worksheet.write(0, 0, '工作站', bold)
    worksheet.write(0, 1, '投诉工单工单号', bold)
    worksheet.write(0, 2, '更换终端类型', bold)
    worksheet.write(0, 3, '原条码', bold)
    worksheet.write(0, 4, '新条码', bold)
    worksheet.write(0, 5, '装维人员', bold)
    worksheet.write(0, 6, '维护使用时间', bold)

    number = 0
    for item in data:
        number += 1
        # work =YCwork.select().where(YCwork.sort==item.work).get()
        # type =YCterminal_type.select().where(YCwork.sort==item.type).get()
        # model=YCterminal_model.select().where(YCwork.sort==item.model).get()
        # 直接改成映射函数
        work = get_work_name(item.work)
        type = get_type_name(item.type)
        worksheet.write(number, 0, work)
        worksheet.write(number, 1, item.order)
        worksheet.write(number, 2, type)
        worksheet.write(number, 3, item.ocode)
        worksheet.write(number, 4, item.code)
        worksheet.write(number, 5, item.people)
        posttime = utc_timestamp_to_str(item.posttime)
        worksheet.write(number, 6, posttime)

    workbook.close()
    # result={}
    # result['name']='{}.xlsx'.format(name)
    # result['times']=times

    print (name)
    return '{}.xlsx'.format(name)
    # return result


    # work =YCwork.select().where(YCwork.sort==item.work).get()
    #     type =YCterminal_type.select().where(YCwork.sort==item.type).get()
    #     model=YCterminal_model.select().where(YCwork.sort==item.model).get()


def waste_make_report(starttime=None, endtime=None, work=None, type=None, keyword=None):
    print (type)
    print ('?????')
    if type == '1':
        name = str(int(time.time()))

        name = utc_timestamp_to_str(name)
        name = name + '报废报表'
        print ('1111111')
        if (starttime != None and starttime != '') or \
                (endtime != None and endtime != '') or \
                (work != None and work != '') \
                or (keyword != None and keyword != ''):
            data = YCwaste.select().where(YCwaste.status == 1)
            print (data.count())
            if keyword != None and keyword != '':
                #  厂家 条形码  入库人 均为字符串赛选
                # 条形码有多个
                print (keyword)
                like = '%' + keyword + '%'
                data = data.where((YCwaste.factory % like) |
                                  (YCwaste.code % like))
            if starttime != None and starttime != '':
                starttime = utc_str_to_timestamp(starttime)
                data = data.where(starttime <= YCwaste.posttime)
            if endtime != None and endtime != '':
                endtime = utc_str_to_timestamp(endtime)
                data = data.where(YCwaste.posttime <= endtime)
            if work != None and work != '':
                work = get_work_sort(work)
                data = data.where(YCwaste.work == work)
        else:
            data = YCwaste.select().where(YCwaste.status == 1)
    else:
        name = str(int(time.time()))

        name = utc_timestamp_to_str(name)
        name = name + '返修报表'
        if (starttime != None and starttime != '') or \
                (endtime != None and endtime != '') or \
                (work != None and work != '') \
                or (keyword != None and keyword != ''):
            data = YCwaste.select().where(YCwaste.status == 2)
            print (data.count())
            if keyword != None and keyword != '':
                #  厂家 条形码  入库人 均为字符串赛选
                # 条形码有多个
                print (keyword)
                like = '%' + keyword + '%'
                data = data.where((YCwaste.factory % like) |
                                  (YCwaste.code % like))
            if starttime != None and starttime != '':
                starttime = utc_str_to_timestamp(starttime)
                data = data.where(starttime <= YCwaste.posttime)
            if endtime != None and endtime != '':
                endtime = utc_str_to_timestamp(endtime)
                data = data.where(YCwaste.posttime <= endtime)
            if work != None and work != '':
                work = get_work_sort(work)
                data = data.where(YCwaste.work == work)
        else:
            data = YCwaste.select().where(YCwaste.status == 2)

    workbook = xlsxwriter.Workbook('/var/www/downfile/{}.xlsx'.format(name))  # 建立文件

    worksheet = workbook.add_worksheet('sheet1')
    # worksheet = workbook.add_sheet('sheet1')
    bold = workbook.add_format({'bold': True})
    # worksheet.set_column('A:F', 15)
    # worksheet.set_column('G:G', 38)
    # worksheet.set_default_row(55)
    if type == '1':
        worksheet.write(0, 2, '报废条形码', bold)
        worksheet.write(0, 5, '报废时间', bold)
    else:
        worksheet.write(0, 2, '返修条形码', bold)
        worksheet.write(0, 5, '返修时间', bold)

    worksheet.write(0, 0, '工作站', bold)
    worksheet.write(0, 1, '终端类型', bold)

    worksheet.write(0, 3, '厂家', bold)
    worksheet.write(0, 4, '型号', bold)

    number = 0
    for item in data:
        number += 1
        # work =YCwork.select().where(YCwork.sort==item.work).get()
        # type =YCterminal_type.select().where(YCwork.sort==item.type).get()
        # model=YCterminal_model.select().where(YCwork.sort==item.model).get()
        # 直接改成映射函数
        work = get_work_name(item.work)
        type = get_type_name(item.type)
        worksheet.write(number, 0, work)
        worksheet.write(number, 1, type)
        worksheet.write(number, 2, item.code)
        worksheet.write(number, 3, item.factory)
        worksheet.write(number, 4, get_model_name(item.model))
        posttime = utc_timestamp_to_str(item.posttime)
        worksheet.write(number, 5, posttime)

    workbook.close()
    # result={}
    # result['name']='{}.xlsx'.format(name)
    # result['times']=times

    print (name)
    return '{}.xlsx'.format(name)
    # return result


    # work =YCwork.select().where(YCwork.sort==item.work).get()
    #     type =YCterminal_type.select().where(YCwork.sort==item.type).get()
    #     model=YCterminal_model.select().where(YCwork.sort==item.model).get()


def use_make_report(starttime=None, endtime=None, work=None, type=None, keyword=None):
    if (starttime != None and starttime != '') or \
            (endtime != None and endtime != '') or \
            (work != None and work != '') or \
            (type != None and type != '') \
            or (keyword != None and keyword != ''):

        data = YCuse.select()
        print (data.count())
        if keyword != None and keyword != '':
            #  厂家 条形码  入库人 均为字符串赛选
            # 条形码有多个
            print (keyword)
            like = '%' + keyword + '%'
            data = data.where((YCuse.modem % like) |
                              (YCuse.gateway % like) |
                              (YCuse.box % like) |
                              (YCuse.hemu % like) |
                              (YCuse.phone % like) |
                              (YCuse.people % like))
        if starttime != None and starttime != '':
            starttime = utc_str_to_timestamp(starttime)
            data = data.where(starttime <= YCuse.posttime)
        if endtime != None and endtime != '':
            endtime = utc_str_to_timestamp(endtime)
            data = data.where(YCuse.posttime <= endtime)
        if work != None and work != '':
            work = get_work_sort(work)
            data = data.where(YCuse.work == work)
        if type != None and type != '':
            type = get_business_sort(type)
            data = data.where(YCuse.business == type)

    else:
        data = YCuse.select()
    name = str(int(time.time()))

    name = utc_timestamp_to_str(name)
    name = name + '装机报表'

    workbook = xlsxwriter.Workbook('/var/www/downfile/{}.xlsx'.format(name))  # 建立文件

    worksheet = workbook.add_worksheet('sheet1')
    # worksheet = workbook.add_sheet('sheet1')
    bold = workbook.add_format({'bold': True})
    # worksheet.set_column('A:F', 15)
    # worksheet.set_column('G:G', 38)
    # worksheet.set_default_row(55)
    worksheet.write(0, 0, '工作站', bold)
    worksheet.write(0, 1, '业务类型', bold)
    worksheet.write(0, 2, '装机工单业务账户', bold)
    worksheet.write(0, 3, '光猫条码', bold)
    worksheet.write(0, 4, '智能网关条码', bold)
    worksheet.write(0, 5, '机顶盒条码', bold)
    worksheet.write(0, 6, '和目条码', bold)
    worksheet.write(0, 7, '固话（移动）条码', bold)
    worksheet.write(0, 8, '装维人员', bold)
    worksheet.write(0, 9, '装机使用时间', bold)

    # worksheet.write(0, 7, '最新状态', bold)
    number = 0
    for item in data:
        number += 1
        # work =YCwork.select().where(YCwork.sort==item.work).get()
        # type =YCterminal_type.select().where(YCwork.sort==item.type).get()
        # model=YCterminal_model.select().where(YCwork.sort==item.model).get()
        # 直接改成映射函数
        work = get_work_name(item.work)
        type = get_business_name(item.business)
        worksheet.write(number, 0, work)
        worksheet.write(number, 1, type)
        worksheet.write(number, 2, item.order)
        worksheet.write(number, 3, item.modem)
        worksheet.write(number, 4, item.gateway)
        worksheet.write(number, 5, item.box)
        posttime = utc_timestamp_to_str(item.posttime)
        worksheet.write(number, 6, item.hemu)
        worksheet.write(number, 7, item.phone)
        worksheet.write(number, 8, item.people)
        worksheet.write(number, 9, posttime)

    workbook.close()
    # result={}
    # result['name']='{}.xlsx'.format(name)
    # result['times']=times

    print (name)
    return '{}.xlsx'.format(name)
    # return result


    # work =YCwork.select().where(YCwork.sort==item.work).get()
    #     type =YCterminal_type.select().where(YCwork.sort==item.type).get()
    #     model=YCterminal_model.select().where(YCwork.sort==item.model).get()


def storage_make_report(starttime=None, endtime=None, work=None, type=None, model=None, keyword=None):
    if (starttime != None and starttime != '') or \
            (endtime != None and endtime != '') or \
            (work != None and work != '') or \
            (type != None and type != '') \
            or (model != None and model != '') \
            or (keyword != None and keyword != ''):
        data = YCstorage.select()
        print (data.count())
        if keyword != None and keyword != '':
            #  厂家 条形码  入库人 均为字符串赛选
            print (keyword)
            like = '%' + keyword + '%'
            data = data.where((YCstorage.factory % like) |
                              (YCstorage.code % like) |
                              (YCstorage.people % like))
        if starttime != None and starttime != '':
            starttime = utc_str_to_timestamp(starttime)
            data = data.where(starttime <= YCstorage.posttime)
        if endtime != None and endtime != '':
            endtime = utc_str_to_timestamp(endtime)
            data = data.where(YCstorage.posttime <= endtime)
        if work != None and work != '':
            work = get_work_sort(work)
            data = data.where(YCstorage.work == work)
        if type != None and type != '':
            type = get_type_sort(type)
            data = data.where(YCstorage.type == type)
        if model != None and model != '':
            model = get_model_sort(model)
            data = data.where(YCstorage.model == model)
    else:
        data = YCstorage.select()

    name = str(int(time.time()))
    name = str(int(time.time()))

    name = utc_timestamp_to_str(name)
    name = name + '出库报表'

    workbook = xlsxwriter.Workbook('/var/www/downfile/{}.xlsx'.format(name))  # 建立文件

    worksheet = workbook.add_worksheet('sheet1')
    # worksheet = workbook.add_sheet('sheet1')
    bold = workbook.add_format({'bold': True})
    # worksheet.set_column('A:F', 15)
    # worksheet.set_column('G:G', 38)
    # worksheet.set_default_row(55)
    worksheet.write(0, 0, '工作站', bold)
    worksheet.write(0, 1, '终端类型', bold)
    worksheet.write(0, 2, '厂家', bold)
    worksheet.write(0, 3, '型号', bold)
    worksheet.write(0, 4, '条形码', bold)
    worksheet.write(0, 5, '入库时间', bold)
    worksheet.write(0, 6, '入库人', bold)
    # worksheet.write(0, 7, '最新状态', bold)
    number = 0
    for item in data:
        number += 1
        # work =YCwork.select().where(YCwork.sort==item.work).get()
        # type =YCterminal_type.select().where(YCwork.sort==item.type).get()
        # model=YCterminal_model.select().where(YCwork.sort==item.model).get()
        # 直接改成映射函数
        work = get_work_name(item.work)
        type = get_type_name(item.type)
        model = get_model_name(item.model)
        worksheet.write(number, 0, work)
        worksheet.write(number, 1, type)
        worksheet.write(number, 2, item.factory)
        worksheet.write(number, 3, model)
        worksheet.write(number, 4, item.code)
        posttime = utc_timestamp_to_str(item.posttime)
        worksheet.write(number, 5, posttime)
        worksheet.write(number, 6, item.people)

    workbook.close()
    # result={}
    # result['name']='{}.xlsx'.format(name)
    # result['times']=times

    print (name)
    return '{}.xlsx'.format(name)
    # return result


    # work =YCwork.select().where(YCwork.sort==item.work).get()
    #     type =YCterminal_type.select().where(YCwork.sort==item.type).get()
    #     model=YCterminal_model.select().where(YCwork.sort==item.model).get()


def get_work_name(work):
    return YCwork.select().where(YCwork.sort == work).get().name


def get_type_name(type):
    return YCterminal_type.select().where(YCterminal_type.sort == type).get().name


def get_model_name(model):
    return YCterminal_model.select().where(YCterminal_model.id == model).get().name


def get_people_name(people):
    return YCpeople.select().where(YCpeople.sort == people).get().name


def get_business_name(business):
    return YCbusiness.select().where(YCbusiness.sort == business).get().name


def get_work_sort(work):
    return YCwork.select().where(YCwork.name == work).get().sort


def get_type_sort(type):
    return YCterminal_type.select().where(YCterminal_type.name == type).get().sort


def get_model_sort(model):
    return YCterminal_model.select().where(YCterminal_model.name == model).get().id


def get_people_sort(people):
    return YCpeople.select().where(YCpeople.name == people).get().sort


def get_business_sort(business):
    return YCbusiness.select().where(YCbusiness.name == business).get().sort


def if_exist_one(db,k,val):
    if k == 'order' and db.select().where(db.order == val).count() == 1:
        return True
    if k == 'code' and db.select().where(db.code == val).count() == 1:
        return True
    if k == 'ocode' and db.select().where(db.ocode == val).count() == 1:
        return True
    return False


def if_exist_all(db,**kw):
    num=0
    for k,val in kw.items():
        if if_exist_one(db,k,val):
            num += 1
    if num == len(kw):
        print(len(kw))
        return True
    return False

def if_not_exist_one(db,k,val):
    if k == 'order' and db.select().where(db.order == val).count() != 1:
        return True
    if k == 'code' and db.select().where(db.code == val).count() != 1:
        return True
    if k == 'ocode' and db.select().where(db.ocode == val).count() != 1:
        return True
    return False


def if_not_exist_all(db,**kw):
    num=0
    for k,val in kw.items():
        if if_not_exist_one(db,k,val):
            num += 1
    if num == len(kw):
        print(len(kw))
        return True
    return False

def get_sort_or_name(db,sn):
    if sn.isdigit():
        return db.select().where(db.sort == sn).get().name
    else:
        return db.select().where(db.name == sn).get().sort


# if __name__ == '__main__':
#     a= get_work_name(1)
#     print(a)

