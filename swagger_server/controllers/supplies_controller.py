# coding=utf8
import connexion
import six
from operator import itemgetter, attrgetter

from swagger_server.models.export import Export  # noqa: E501
from swagger_server.models.maintain_list import MaintainList  # noqa: E501
from swagger_server.models.out_data import OutData  # noqa: E501
from swagger_server.models.out_list import OutList  # noqa: E501
from swagger_server.models.statistics_install_list import StatisticsInstallList  # noqa: E501
from swagger_server.models.statistics_work_list import StatisticsWorkList  # noqa: E501
from swagger_server.models.storage_data import StorageData  # noqa: E501
from swagger_server.models.storage_data_edit import StorageDataEdit  # noqa: E501
from swagger_server.models.storage_list import StorageList  # noqa: E501
from swagger_server.models.success import Success  # noqa: E501
from swagger_server.models.supplies_query import SuppliesQuery  # noqa: E501
from swagger_server.models.use_codes import UseCodes  # noqa: E501
from swagger_server.models.use_list import UseList  # noqa: E501
from swagger_server.models.waste_list import WasteList  # noqa: E501
from swagger_server import util
from swagger_server.export_report import *
from swagger_server.models.success import Success  # noqa: E501
from swagger_server import util
from swagger_server.mysql_db import *
from swagger_server.infoexport import *
from ..tool import *
from flask import request
from flask import request
import os
import sys,xlwt
import datetime as datime
from datetime import datetime
from xlrd import xldate_as_tuple
#获取上个月的时间
def get_f_l_day():
    #上一个月的第一天
    lst_fist = str(datime.date(datime.date.today().year,datime.date.today().month-1,1))+' 00:00:00'
    #上一个月的最后一天
    lst_last = str(datime.date(datime.date.today().year,datime.date.today().month,1)-datime.timedelta(1))+' 23:59:59'
    return (lst_fist,lst_last)
#获取当月的时间
def get_f_l_day_now():
    #本月的第一天
    lst_fist = str(datime.date(datime.date.today().year,datime.date.today().month,1))+' 00:00:00'
    #本月的最后一天
    lst_last = str(datime.date(datime.date.today().year,datime.date.today().month+1,1)-datime.timedelta(1))+' 23:59:59'
    return (lst_fist,lst_last)
#获取申领所有的人员
def get_workman(work_id):
    datawork=YCoutbound.select(YCoutbound.people).where(YCoutbound.work==work_id).group_by(YCoutbound.people)
    work_list=[]
    for item in datawork:
        work_list.append(item.people)
    return work_list

# 公司上维护报表模板得到
def supplies_maintain_export_get(starttime=None, endtime=None, work=None, type=None, keyword=None):  # noqa: E501
    """maintain list

    maintain list # noqa: E501

    :param starttime: the starttime for user choose
    :type starttime: strx
    :param endtime: the endtime for user choose
    :type endtime: str
    :param work: workstation
    :type work: str
    :param type: terminal type
    :type type: str
    :param keyword: keyword
    :type keyword: str

    :rtype: Export
    """
    try:
        name = maintain_make_report(starttime=starttime, endtime=endtime, work=work,
                                    type=type, keyword=keyword)
        print(name + 'star')
        msg = {
            "msg": "msg",
            "code": 0,
            "url": "down.flyminer.cn:89/{}".format(name),
        }
    except:
        msg = {

            "code": -1,
            "msg": "system error"

        }
    return msg


def supplies_maintain_get(page, size, starttime=None, endtime=None, work=None, type=None, keyword=None):  # noqa: E501
    """maintain list

    maintain list # noqa: E501

    :param page: page number
    :type page: str
    :param size: Per page display quantity
    :type size: str
    :param starttime: the starttime for user choose
    :type starttime: str
    :param endtime: the endtime for user choose
    :type endtime: str
    :param work: workstation
    :type work: str
    :param type: terminal type
    :type type: str
    :param keyword: keyword
    :type keyword: str

    :rtype: MaintainList
    """
    try:
        if (starttime != None and starttime != '') or \
                (endtime != None and endtime != '') or \
                (work != None and work != '') or \
                (type != None and type != '') \
                or (keyword != None and keyword != ''):
            data = YCmaintain.select()
            print(data.count())
            if keyword != None and keyword != '':
                #  厂家 条形码  入库人 均为字符串赛选
                # 条形码有多个
                print(keyword)
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
            total = data.count()
            data = data.paginate(int(page), int(size))

        else:
            data = YCmaintain.select().paginate(int(page), int(size))
            total = YCmaintain.select().count()

        result_list = [{
            'posttime': utc_timestamp_to_str(item.posttime),
            'code': item.code,

            'work': get_work_name(item.work),
            'ocode': item.ocode,
            'personnel': item.people,
            'type': get_type_name(item.type),

            'order': item.order,
            'id': item.id,
        } for item in data]
        msg = {"code": 0, "msg": "success", "total": total, "result": result_list}
    except:
        msg = {"code": -1, "msg": "Error"}
    return msg


def supplies_maintain_upload_post(files=None):  # noqa: E501
    """Install usage details import

    Install usage details import # noqa: E501

    :param files: file data
    :type files: werkzeug.datastructures.FileStorage

    :rtype: Success
    """
    # 加一个status的维护使用  加一个入库状态   判断？ 判断是否在库里
    try:
        file = request.files['files']
        file.save(os.path.join('/var/www/downfile', file.filename))
        # new_filepath = '/var/www/downfile/{}'.format(file.filename)

        # file = request.files['files']
        # file.save(os.path.join('../down', file.filename))

        data = xlrd.open_workbook('/var/www/downfile/{}'.format(file.filename))
        table = data.sheets()[0]  # 通过索引顺序获取
        # table = data.sheet_by_index(0) #通过索引顺序获取
        # table = data.sheet_by_name(u'Sheet1')#通过名称获取
        num = table.col_values(0)  # 获取整列的信息

        # # 获取单元格
        # table.cell(0,0).value
        # table.cell(2,3).value
        print(len(num))
        GLitem = []
        for i in range(1, len(num)):
            try:
                info = {}
                item = table.row_values(i)  # 获取整行的信息
                # companys = table.col_values(0)  #获取整列的信息
                # # 获取单元格
                # table.cell(0,0).value
                # table.cell(2,3).value
                print(len(item))

                work = item[0]
                order = str(item[1]).replace(".0", "")
                type = item[2]
                ocode = str(item[3]).replace(".0", "")
                code = str(item[4]).replace(".0", "")
                people = item[5]
                posttime = item[6]
                try:
                    posttime = str(datetime(*xldate_as_tuple(posttime, 0)))
                except:
                    posttime = item[6]
                if people == '' or posttime == '' or order == '':
                    msg = {'code': 10003, 'msg': i}
                    return msg
                if ocode == None or ocode == '' or code == None or code == '':
                    return {'code': 10003, 'msg': i}

                count = YCoutbound.select().where(YCoutbound.code == ocode).count()
                if count < 1:
                    msg = {'code': 10003, 'msg': i}
                    return msg
                count = YCoutbound.select().where(YCoutbound.code == code).count()
                if count < 1:
                    msg = {'code': 10003, 'msg': i}
                    return msg

                info['work'] = work
                info['order'] = order
                info['type'] = type
                info['ocode'] = ocode
                info['code'] = code
                info['people'] = people
                info['posttime'] = posttime
                GLitem.append(info)
            except:
                return {'code': 10003, 'msg': i}
        if len(GLitem) == 0:
            return {'code': -1, 'msg': 'Error'}

        for item in GLitem:
            YCmaintain.insert(work=get_work_sort(item['work']),
                              type=get_type_sort(item['type']),
                              order=item['order'],
                              code=item['code'],
                              ocode=item['ocode'],
                              people=item['people'],
                              posttime=utc_str_to_timestamp(item['posttime'])).execute()
            #  YCstorage.   新条码应该也是在库里的吧  处于没有 use 的状态
            # 把out 中 新code 改成2
            YCoutbound.update(status=2).where(YCoutbound.code == item['code']).execute()
            YCstatus.insert(use='维修使用',
                            work=get_work_sort(item['work']),
                            code=item['code'],
                            people=item['people'],
                            posttime=utc_str_to_timestamp(item['posttime'])).execute()

        msg = {"code": 0, "msg": "success"}
    except Exception as e:
        print(e)
        msg = {"code": -1, "msg": "Error"}
    return msg


def supplies_out_export_get(starttime=None, endtime=None, work=None, type=None, keyword=None, model=None):  # noqa: E501
    """Inventory list

    Inventory list # noqa: E501

    :param starttime: the starttime for user choose
    :type starttime: str
    :param endtime: the endtime for user choose
    :type endtime: str
    :param work: workstation
    :type work: str
    :param type: business type
    :type type: str
    :param keyword: keyword
    :type keyword: str

    :rtype: Export
    """

    try:
        name = out_make_report(starttime=starttime, endtime=endtime, work=work,
                               type=type, model=model, keyword=keyword)
        print(name + 'star')
        msg = {
            "msg": "msg",
            "code": 0,
            "url": "down.flyminer.cn:89/{}".format(name),
        }
    except:
        msg = {

            "code": -1,
            "msg": "system error"

        }

    return msg

def supplies_out_get(page, size, starttime=None, endtime=None, work=None, type=None, keyword=None,
                     model=None):  # noqa: E501
    """Inventory list

    Inventory list # noqa: E501

    :param page: page number
    :type page: str
    :param size: Per page display quantity
    :type size: str
    :param starttime: the starttime for user choose
    :type starttime: str
    :param endtime: the endtime for user choose
    :type endtime: str
    :param work: workstation
    :type work: str
    :param type: business type
    :type type: str
    :param keyword: keyword
    :type keyword: str

    :rtype: OutList
    """
    try:
        if (starttime != None and starttime != '') or \
                (endtime != None and endtime != '') or \
                (work != None and work != '') or \
                (type != None and type != '') \
                or (model != None and model != '') \
                or (keyword != None and keyword != ''):
            data = YCoutbound.select()
            print(data.count())
            if keyword != None and keyword != '':
                #  厂家 条形码  入库人 均为字符串赛选
                print(keyword)
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
                # if keyword != None and keyword != '':
                #     # 如果是工作站    厂家 条形码  入库人
                #     print (keyword)
                #
                #     data = data.where(YCstorage.factory ** '%' + keyword + '%')
                #     if data.count() == 0:
                #         data = data.where(YCstorage.code ** '%' + keyword + '%')
                #     if data.count() == 0:
                #         data = data.where(YCstorage.code ** '%' + keyword + '%')
                #     print (data.count())
                # if data.count()==0:
                #     try:          # % ‘%ba%’
                #         work_name = YCwork.select().where(YCwork.name ** '%' + keyword + '%').get()
                #         data=data.where(YCstorage.work==work_name)
                #     except:
                #         pass
            total = data.count()
            data = data.order_by(YCoutbound.posttime.desc()).paginate(int(page), int(size))

        else:
            data = YCoutbound.select().order_by(YCoutbound.posttime.desc()).paginate(int(page), int(size))
            total = YCoutbound.select().count()
        result_list = [{'principal': item.people,
                        'posttime': utc_timestamp_to_str(item.posttime),
                        'factory': item.factory,
                        'code': item.code,
                        'work': get_work_name(item.work),
                        'model': get_model_name(item.model),
                        'id': item.id,
                        'type': get_type_name(item.type)} for item in data]
        msg = {"code": 0, "msg": "success", "total": total, "result": result_list}

    except Exception as e:
        print(e)
        msg = {"code": -1, "msg": "system error"}
    return msg


def supplies_out_post(body):  # noqa: E501
    """Product warehousing

    Product warehousing # noqa: E501

    :param body: data
    :type body: dict | bytes

    :rtype: Success
    """
    if connexion.request.is_json:
        body = OutData.from_dict(connexion.request.get_json())  # noqa: E501

        try:
            if YCoutbound.select().where(YCoutbound.code == body.code).count() >= 1:
                msg = {"code": 10003, "msg": "code not exist"}
                return msg
        except Exception as e:
            print(e)
            msg = {"code": 10003, "msg": "code not exist"}

        try:
            work = get_work_sort(body.work)
            type = get_type_sort(body.type)
            model = get_model_sort(body.model)
            factory = YCstorage.select().where(YCstorage.code == body.code).get().factory

            YCoutbound.insert(work=work, type=type, factory=factory,
                              model=model, people=body.people, code=body.code,
                              posttime=int(time.time()),
                              status=0).execute()

            YCstatus.insert(work=work, use='装维申领', people=body.people, code=body.code,
                            posttime=int(time.time())).execute()
            YCstorage.update(status=1).where(YCstorage.code == body.code).execute()
            msg = {
                "msg": "success",
                "code": 0
            }
        except Exception as e:
            print(e)
            msg = {"code": -1, "msg": "Error"}
        return msg


def supplies_query_code_get(code):  # noqa: E501
    """According to the challenge, check the terminal status

    According to the challenge, check the terminal status # noqa: E501

    :param code: Terminal barcode
    :type code: str

    :rtype: SuppliesQuery
    """
    try:
        datas = YCstorage.select().where(YCstorage.code == code).get()

        print(code)
        data = YCstatus.select().where(YCstatus.code == code).order_by(YCstatus.posttime.desc())
        print(data.count())
        #
        # for i in data:
        #     print (i.people)
        #     print (utc_timestamp_to_str(i.posttime))

        result_list = []
        result = {}
        type = get_type_name(datas.type)
        model = get_model_name(datas.model)
        result['type'] = type
        result['model'] = model
        result['code'] = code

        info_list = [
            {'posttime': utc_timestamp_to_str(item.posttime), 'receive': item.people, 'work': get_work_name(item.work),
             'use': item.use, } for item in data]
        result['info'] = info_list
        result_list.append(result)

        msg = {"code": 0, "msg": "success", "result": result_list}
    except Exception as e:
        # print (e)
        msg = {"code": -1, "msg": "system error"}
    return msg


def supplies_statistics_install_export_get(page, size, type, starttime=None, endtime=None, work=None, model=None,
                                           people=None, keyword=None):  # noqa: E501
    """Personnel statistics

    Personnel statistics # noqa: E501

    :param page: page number
    :type page: str
    :param size: Per page display quantity
    :type size: str
    :param type: terminal type
    :type type: str
    :param starttime: the starttime for user choose
    :type starttime: str
    :param endtime: the endtime for user choose
    :type endtime: str
    :param work: workstation
    :type work: str
    :param model: model
    :type model: str
    :param people: Installation staff
    :type people: str
    :param keyword: keyword
    :type keyword: str

    :rtype: Export
    """
    # 默认类型为当月1号到月底
    if starttime == '':
        starttime = get_f_l_day_now()[0]
    if endtime == '':
        endtime = get_f_l_day_now()[1]

    # 默认终端类型为智能网关
    if type == '':
        type = '智能网关'

    # 默认厂家为杭研
    if model == '':
        modle = '杭研'
    if model != '':
        modle = model
    workpeople = people
    # 本期申领数量
    data = YCoutbound.select()
    msg_out_list = []
    # print(starttime,endtime)
    if starttime != '':
        data = data.where(YCoutbound.posttime >= utc_str_to_timestamp(starttime))
    if endtime != '':
        data = data.where(YCoutbound.posttime <= utc_str_to_timestamp(endtime))

    if type != '':
        data = data.where(YCoutbound.type == get_type_sort(type))
    if modle != '':
        data = data.where(YCoutbound.factory == modle)
    if work != '':
        if workpeople == '':
            data = data.where(YCoutbound.work == get_work_sort(work))
            workman_list = get_workman(get_work_sort(work))
            for workman in workman_list:
                data_i = data.where(YCoutbound.people == workman)
                msg_out_list.append([work, workman, data_i.count()])
        if workpeople != '':
            data_i = data.where(YCoutbound.people == workman)
            msg_out_list.append([work, workman, data_i.count()])

    if work == '':
        if workpeople == '':
            for i in range(2, 12):
                workman_list = get_workman(i)
                for workman in workman_list:
                    data_man = data.where(YCoutbound.people == workman)
                    msg_out_list.append([get_work_name(i), workman, data_man.count()])
        if workpeople != '':
            data_i = data.where(YCoutbound.people == workman)
            msg_out_list.append([get_work_name(data_i.get().work), workman, data_i.count()])

    print(msg_out_list)

    # 装机使用量
    data2 = YCuse.select()
    total_use_list = []

    if starttime != '':
        data2 = data2.where(YCuse.posttime >= utc_str_to_timestamp(starttime))
    if endtime != '':
        data2 = data2.where(YCuse.posttime <= utc_str_to_timestamp(endtime))
    if type != '':
        data2 = data2.where(YCuse.business == get_type_sort(type))
    if modle != '':
        data2 = data2.where(YCuse.produce == modle)
    if work == '':
        if workpeople == '':
            for i in range(2, 12):
                workman_list = get_workman(i)
                for workman in workman_list:
                    data2_i = data2.where(YCuse.people == workman)
                    total_use_list.append(data2_i.count())
        if workpeople != '':
            data2_i = data2.where(YCuse.people == workman)
            total_use_list.append(data2_i.count())

    if work != '':
        if workpeople == '':
            data2 = data2.where(YCuse.work == get_work_sort(work))
            workman_list = get_workman(get_work_sort(work))
            for workman in workman_list:
                data2_i = data2.where(YCuse.people == workman)
                total_use_list.append(data2_i.count())
        if workpeople != '':
            data2_i = data2.where(YCuse.people == workman)
            total_use_list.append(data2_i.count())

    # 计算本期报废数量
    data3 = YCwaste.select().where(YCwaste.status == 1)
    total_waste_list = []

    if starttime != '':
        data3 = data3.where(YCwaste.posttime >= utc_str_to_timestamp(starttime))
    if endtime != '':
        data3 = data3.where(YCwaste.posttime <= utc_str_to_timestamp(endtime))
    if type != '':
        data3 = data3.where(YCwaste.type == get_type_sort(type))
    if modle != '':
        data3 = data3.where(YCwaste.factory == modle)
    if work == '':
        if workpeople == '':
            for i in range(2, 12):
                workman_list = get_workman(i)
                for workman in workman_list:
                    # data3_i = data3.where(YCwaste.people == workman)
                    total_waste_list.append(0)
        if workpeople != '':
            total_waste_list.append(0)

    if work != '':
        if workpeople == '':
            data3 = data3.where(YCwaste.work == get_work_sort(work))
            workman_list = get_workman(get_work_sort(work))
            for workman in workman_list:
                # data3_i = data3.where(YCuse.people == workman)
                total_waste_list.append(0)
        if workpeople != '':
            total_waste_list.append(0)

    # 计算本期返修数量
    data4 = YCwaste.select().where(YCwaste.status == 2)
    total_waste1_list = []

    if starttime != '':
        data4 = data4.where(YCwaste.posttime >= utc_str_to_timestamp(starttime))
    if endtime != '':
        data4 = data4.where(YCwaste.posttime <= utc_str_to_timestamp(endtime))
    if type != '':
        data4 = data4.where(YCwaste.type == get_type_sort(type))
    if modle != '':
        data4 = data4.where(YCwaste.factory == modle)
    if work == '':
        if workpeople == '':
            for i in range(2, 12):
                workman_list = get_workman(i)
                for workman in workman_list:
                    # data4_i = data4.where(YCwaste.people == workman)
                    total_waste1_list.append(0)
        if workpeople != '':
            total_waste1_list.append(0)
    if work != '':
        if workpeople == '':
            data4 = data4.where(YCuse.work == get_work_sort(work))
            workman_list = get_workman(get_work_sort(work))
            for workman in workman_list:
                # data4_i = data4.where(YCuse.people == workman)
                total_waste1_list.append(0)
        if workpeople != '':
            total_waste1_list.append(0)

    # 计算维护使用数量
    data5 = YCmaintain.select()
    total_maintain_list = []
    if starttime != '':
        data5 = data5.where(YCmaintain.posttime >= utc_str_to_timestamp(starttime))
    if endtime != '':
        data5 = data5.where(YCmaintain.posttime <= utc_str_to_timestamp(endtime))
    if type != '':
        data5 = data5.where(YCmaintain.type == get_type_sort(type))
    if work == '':
        if workpeople == '':
            for i in range(2, 12):
                workman_list = get_workman(i)
                for workman in workman_list:
                    data5_i = data5.where(YCmaintain.people == workman)
                    total_maintain_list.append(data5_i.count())
        if workpeople != '':
            data5_i = data5.where(YCmaintain.people == workman)
            total_maintain_list.append(data5_i.count())
    if work != '':
        if workpeople == '':
            data5 = data5.where(YCmaintain.work == get_work_sort(work))
            workman_list = get_workman(get_work_sort(work))
            for workman in workman_list:
                data5_i = data5.where(YCmaintain.people == workman)
                total_maintain_list.append(data5_i.count())
        if workpeople != '':
            data5_i = data5.where(YCmaintain.people == workman)
            total_maintain_list.append(data5_i.count())
    result = [{"work": msg_out_list[item][0], "people": msg_out_list[item][1], "type": type, "produce": modle,
               "model": 'TL_EP110',
               "last": total_use_list[item] + total_maintain_list[item] + total_waste1_list[item] + total_waste_list[
                   item] - total_use_list[item], "now": msg_out_list[item][2], "use": total_use_list[item],
               "maintain": total_maintain_list[item], "good": total_waste1_list[item], "bad": total_waste_list[item]}
              for item in range(len(msg_out_list))]
    workbook_m = xlwt.Workbook(encoding='utf-8')
    xlsheet = workbook_m.add_sheet('装维人员终端统计')
    xlsheet.write(0, 0, '工作站')
    xlsheet.write(0, 1, '装维人员')
    xlsheet.write(0, 2, '终端类型')
    xlsheet.write(0, 3, '厂家')
    xlsheet.write(0, 4, '型号')
    xlsheet.write(0, 5, '上期结存')
    xlsheet.write(0, 6, '本期申领数量')
    xlsheet.write(0, 7, '装机使用数量')
    xlsheet.write(0, 8, '维护使用数量')
    xlsheet.write(0, 9, '结余好件数量')
    xlsheet.write(0, 10, '结余坏件数量')

    for i in range(len(result)):
        xlsheet.write(i + 1, 0, result[i]['work'])
        xlsheet.write(i + 1, 1, result[i]['people'])
        xlsheet.write(i + 1, 2, result[i]['type'])
        xlsheet.write(i + 1, 3, result[i]['produce'])
        xlsheet.write(i + 1, 4, result[i]['model'])
        xlsheet.write(i + 1, 5, result[i]['last'])
        xlsheet.write(i + 1, 6, result[i]['now'])
        xlsheet.write(i + 1, 7, result[i]['use'])
        xlsheet.write(i + 1, 8, result[i]['maintain'])
        xlsheet.write(i + 1, 9, result[i]['good'])
        xlsheet.write(i + 1, 10, result[i]['bad'])
    xlsname = utc_timestamp_to_str(int(time.time())) + '装维人员统计'
    workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
    return ({'code': 0, 'msg': 'success', 'url': 'down.flyminer.cn:89/{}.xls'.format(xlsname)})


def supplies_statistics_install_get(page, size, type, starttime=None, endtime=None, work=None, model=None, people=None,
                                    keyword=None):  # noqa: E501
    """Personnel statistics

    Personnel statistics # noqa: E501

    :param page: page number
    :type page: str
    :param size: Per page display quantity
    :type size: str
    :param type: terminal type
    :type type: str
    :param starttime: the starttime for user choose
    :type starttime: str
    :param endtime: the endtime for user choose
    :type endtime: str
    :param work: workstation
    :type work: str
    :param model: model
    :type model: str
    :param people: Installation staff
    :type people: str
    :param keyword: keyword
    :type keyword: str

    :rtype: StatisticsInstallList
    """
    # 默认类型为当月1号到月底
    if starttime == '':
        starttime = get_f_l_day_now()[0]
    if endtime == '':
        endtime = get_f_l_day_now()[1]

    # 默认终端类型为智能网关
    if type == '':
        type = '智能网关'

    # 默认厂家为杭研
    if model == '' or model == None:
        modle = '杭研'

    workpeople = people
    # 本期申领数量
    data = YCoutbound.select()
    msg_out_list = []
    #print(starttime,endtime)
    if starttime != '':
        data = data.where(YCoutbound.posttime >= utc_str_to_timestamp(starttime))
    if endtime != '':
        data = data.where(YCoutbound.posttime <= utc_str_to_timestamp(endtime))

    if type != '':
        data = data.where(YCoutbound.type == get_type_sort(type))
    if modle != '':
        data = data.where(YCoutbound.factory == modle)
    if work != '' and work != None:
        if workpeople == '' or workpeople == None:
            data = data.where(YCoutbound.work == get_work_sort(work))
            workman_list = get_workman(get_work_sort(work))
            for workman in workman_list:
                data_i = data.where(YCoutbound.people == workman)
                msg_out_list.append([work, workman, data_i.count()])
        else:
            for workman in workpeople:
                data_i = data.where(YCoutbound.people == workman)
                msg_out_list.append([work, workman, data_i.count()])

    if work == '':
        if workpeople == '' or workpeople == None:
            for i in range(2, 12):
                workman_list = get_workman(i)
                for workman in workman_list:
                    data_man = data.where(YCoutbound.people == workman)
                    msg_out_list.append([get_work_name(i), workman, data_man.count()])
        else:
            #指定了people的判断
            data_i = data.where(YCoutbound.people == workman)
            msg_out_list.append([get_work_name(data_i.get().work), workman, data_i.count()])

    print(msg_out_list)

    # 装机使用量
    data2 = YCuse.select()
    total_use_list = []

    if starttime != '':
        data2 = data2.where(YCuse.posttime >= utc_str_to_timestamp(starttime))
    if endtime != '':
        data2 = data2.where(YCuse.posttime <= utc_str_to_timestamp(endtime))
    if type != '':
        data2 = data2.where(YCuse.business == get_type_sort(type))
    if modle != '':
        data2 = data2.where(YCuse.produce == modle)
    if work == '':
        if workpeople == ''or workpeople == None:
            for i in range(2, 12):
                workman_list = get_workman(i)
                for workman in workman_list:
                    data2_i = data2.where(YCuse.people == workman)
                    total_use_list.append(data2_i.count())
        else:
            data2_i = data2.where(YCuse.people == workman)
            total_use_list.append(data2_i.count())

    if work != '':
        if workpeople == ''or workpeople == None:
            data2 = data2.where(YCuse.work == get_work_sort(work))
            workman_list = get_workman(get_work_sort(work))
            for workman in workman_list:
                data2_i = data2.where(YCuse.people == workman)
                total_use_list.append(data2_i.count())
        else:
            data2_i = data2.where(YCuse.people == workman)
            total_use_list.append(data2_i.count())

    # 计算本期报废数量
    data3 = YCwaste.select().where(YCwaste.status == 1)
    total_waste_list = []

    if starttime != '':
        data3 = data3.where(YCwaste.posttime >= utc_str_to_timestamp(starttime))
    if endtime != '':
        data3 = data3.where(YCwaste.posttime <= utc_str_to_timestamp(endtime))
    if type != '':
        data3 = data3.where(YCwaste.type == get_type_sort(type))
    if modle != '':
        data3 = data3.where(YCwaste.factory == modle)
    if work == '':
        if workpeople == '' or workpeople == None:
            for i in range(2, 12):
                workman_list = get_workman(i)
                for workman in workman_list:
                    # data3_i = data3.where(YCwaste.people == workman)
                    total_waste_list.append(0)
        else:
            total_waste_list.append(0)

    if work != '':
        if workpeople == '' or workpeople == None:
            data3 = data3.where(YCwaste.work == get_work_sort(work))
            workman_list = get_workman(get_work_sort(work))
            for workman in workman_list:
                # data3_i = data3.where(YCuse.people == workman)
                total_waste_list.append(0)
        else:
            total_waste_list.append(0)

    # 计算本期返修数量
    data4 = YCwaste.select().where(YCwaste.status == 2)
    total_waste1_list = []

    if starttime != '':
        data4 = data4.where(YCwaste.posttime >= utc_str_to_timestamp(starttime))
    if endtime != '':
        data4 = data4.where(YCwaste.posttime <= utc_str_to_timestamp(endtime))
    if type != '':
        data4 = data4.where(YCwaste.type == get_type_sort(type))
    if modle != '':
        data4 = data4.where(YCwaste.factory == modle)
    if work == '':
        if workpeople == ''or workpeople == None:
            for i in range(2, 12):
                workman_list = get_workman(i)
                for workman in workman_list:
                    # data4_i = data4.where(YCwaste.people == workman)
                    total_waste1_list.append(0)
        else:
            total_waste1_list.append(0)
    if work != '':
        if workpeople == '' or workpeople == None:
            data4 = data4.where(YCuse.work == get_work_sort(work))
            workman_list = get_workman(get_work_sort(work))
            for workman in workman_list:
                # data4_i = data4.where(YCuse.people == workman)
                total_waste1_list.append(0)
        else:
            total_waste1_list.append(0)

    # 计算维护使用数量
    data5 = YCmaintain.select()
    total_maintain_list = []
    if starttime != '':
        data5 = data5.where(YCmaintain.posttime >= utc_str_to_timestamp(starttime))
    if endtime != '':
        data5 = data5.where(YCmaintain.posttime <= utc_str_to_timestamp(endtime))
    if type != '':
        data5 = data5.where(YCmaintain.type == get_type_sort(type))
    if work == '':
        if workpeople == ''or workpeople == None:
            for i in range(2, 12):
                workman_list = get_workman(i)
                for workman in workman_list:
                    data5_i = data5.where(YCmaintain.people == workman)
                    total_maintain_list.append(data5_i.count())
        else:
            data5_i = data5.where(YCmaintain.people == workman)
            total_maintain_list.append(data5_i.count())
    if work != '':
        if workpeople == '' or workpeople == None:
            data5 = data5.where(YCmaintain.work == get_work_sort(work))
            workman_list = get_workman(get_work_sort(work))
            for workman in workman_list:
                data5_i = data5.where(YCmaintain.people == workman)
                total_maintain_list.append(data5_i.count())
        else:
            data5_i = data5.where(YCmaintain.people == workman)
            total_maintain_list.append(data5_i.count())
    result = [{"work": msg_out_list[item][0], "people": msg_out_list[item][1], "type": type, "produce": modle,
               "model": 'TL_EP110',
               "last": total_use_list[item] + total_maintain_list[item] + total_waste1_list[item] + total_waste_list[
                   item] - total_use_list[item], "now": msg_out_list[item][2], "use": total_use_list[item],
               "maintain": total_maintain_list[item], "good": total_waste1_list[item], "bad": total_waste_list[item]}
              for item in range(len(msg_out_list))]
    msg = {"code": 0, "msg": 'success', "result": result}
    return msg



def supplies_statistics_work_export_get(page, size, type, starttime=None, endtime=None, work=None, model=None,
                                        keyword=None):  # noqa: E501
    """Workstation installation dimension statistics

    Workstation installation dimension statistics # noqa: E501

    :param page: page number
    :type page: str
    :param size: Per page display quantity
    :type size: str
    :param type: terminal type
    :type type: str
    :param starttime: the starttime for user choose
    :type starttime: str
    :param endtime: the endtime for user choose
    :type endtime: str
    :param work: workstation
    :type work: str
    :param model: model
    :type model: str
    :param keyword: keyword
    :type keyword: str

    :rtype: Export
    """
    if type == '':
        type = '智能网关'
    if model == '':
        modle_list = ['杭研','华为','贝尔','中兴']
    if model != '':
        modle_list = [model]
    # m没有的话从本月1号开始计算
    if starttime == '':
        starttime = get_f_l_day_now()[0]
    if endtime == '':
        endtime = get_f_l_day_now()[1]
    print(starttime, endtime)

    result=[]
    for modle in modle_list:
        total_last_list = []
        total_now_list = []
        total_use_list = []
        total_waste_list = []
        total_waste1_list = []
        # 计算上期结存
        data = YCstorage.select().where(YCstorage.status == 0)

        if work == '':
            if starttime != '':
                data = data.where(YCstorage.posttime >= utc_str_to_timestamp(get_f_l_day()[0]))
            if endtime != '':
                data = data.where(YCstorage.posttime <= utc_str_to_timestamp(get_f_l_day()[1]))
            if type != '':
                data = data.where(YCstorage.type == get_type_sort(type))
            if modle != '':
                data = data.where(YCstorage.factory == modle)
            if keyword != '':
                like = '%' + keyword + '%'
                data = data.where((YCstorage.people % like) | (YCstorage.factory % like))
            for i in range(2, 12):
                data_i = data.where(YCstorage.work == i)
                total_last = data_i.count()
                total_last_list.append([total_last,i])
        if work != '':
            if starttime != '':
                data = data.where(YCstorage.posttime >= utc_str_to_timestamp(get_f_l_day()[0]))
            if endtime != '':
                data = data.where(YCstorage.posttime <= utc_str_to_timestamp(get_f_l_day()[1]))
            if type != '':
                data = data.where(YCstorage.type == get_type_sort(type))
            if modle != '':
                data = data.where(YCstorage.factory == modle)
            if keyword != '':
                like = '%' + keyword + '%'
                data = data.where((YCstorage.people % like) | (YCstorage.factory % like))
            data = data.where(YCstorage.work == get_work_sort(work))
            total_last_list.append([data.count(),get_work_sort(work)])

        # 计算本期入库
        data1 = YCstorage.select().where(YCstorage.status == 0)

        if work == '':
            if starttime != '':
                data1 = data1.where(YCstorage.posttime >= utc_str_to_timestamp(starttime))
            if endtime != '':
                data1 = data1.where(YCstorage.posttime <= utc_str_to_timestamp(endtime))
            if type != '':
                data1 = data1.where(YCstorage.type == get_type_sort(type))
            if modle != '':
                data1 = data1.where(YCstorage.factory == modle)
            if keyword != '':
                like = '%' + keyword + '%'
                data1 = data1.where((YCstorage.people % like) | (YCstorage.factory % like))
            for i in range(2, 12):
                data1_i = data1.where(YCstorage.work == i)
                total_now = data1_i.count()
                total_now_list.append(total_now)
        if work != '':
            if starttime != '':
                data1 = data1.where(YCstorage.posttime >= utc_str_to_timestamp(starttime))
            if endtime != '':
                data1 = data1.where(YCstorage.posttime <= utc_str_to_timestamp(endtime))
            if type != '':
                data1 = data1.where(YCstorage.type == get_type_sort(type))
            if modle != '':
                data1 = data1.where(YCstorage.factory == modle)
            if keyword != '':
                like = '%' + keyword + '%'
                data1 = data1.where((YCstorage.people % like) | (YCstorage.factory % like))
            data1 = data1.where(YCstorage.work == get_work_sort(work))
            total_now_list.append(data1.count())

        # 计算出库数量
        data2 = YCuse.select()

        if work == '':
            if starttime != '':
                data2 = data2.where(YCuse.posttime >= utc_str_to_timestamp(starttime))
            if endtime != '':
                data2 = data2.where(YCuse.posttime <= utc_str_to_timestamp(endtime))
            if type != '':
                data2 = data2.where(YCuse.type == get_type_sort(type))
            if modle != '':
                data2 = data2.where(YCuse.produce == modle)
            if keyword != '':
                like = '%' + keyword + '%'
                data2 = data2.where(YCuse.people % like)
            for i in range(2, 12):
                data2_i = data2.where(YCuse.work == i)
                total_use = data2_i.count()
                total_use_list.append(total_use)
        if work != '':
            if starttime != '':
                data2 = data2.where(YCuse.posttime >= utc_str_to_timestamp(starttime))
            if endtime != '':
                data2 = data2.where(YCuse.posttime <= utc_str_to_timestamp(endtime))
            if type != '':
                data2 = data2.where(YCuse.type == get_type_sort(type))
            if modle != '':
                data2 = data2.where(YCuse.produce == modle)
            if keyword != '':
                like = '%' + keyword + '%'
                data2 = data2.where(YCuse.people % like)
            data2 = data2.where(YCuse.work == get_work_sort(work))
            total_use_list.append(data2.count())

        # 计算本期报废数量
        data3 = YCwaste.select().where(YCwaste.status == 1)

        if work == '':
            if starttime != '':
                data3 = data3.where(YCwaste.posttime >= utc_str_to_timestamp(starttime))
            if endtime != '':
                data3 = data3.where(YCwaste.posttime <= utc_str_to_timestamp(endtime))
            if type != '':
                data3 = data3.where(YCwaste.type == get_type_sort(type))
            if modle != '':
                data3 = data3.where(YCwaste.factory == modle)
            if keyword != '':
                like = '%' + keyword + '%'
                data3 = data3.where(YCwaste.factory % like)
            for i in range(2, 12):
                data3_i = data3.where(YCwaste.work == i)
                total_waste = data3_i.count()
                total_waste_list.append(total_waste)
        if work != '':
            if starttime != '':
                data3 = data3.where(YCwaste.posttime >= utc_str_to_timestamp(starttime))
            if endtime != '':
                data3 = data3.where(YCwaste.posttime <= utc_str_to_timestamp(endtime))
            if type != '':
                data3 = data3.where(YCwaste.type == get_type_sort(type))
            if modle != '':
                data3 = data3.where(YCwaste.factory == modle)
            if keyword != '':
                like = '%' + keyword + '%'
                data3 = data3.where(YCwaste.factory % like)
            data3 = data3.where(YCwaste.work == get_work_sort(work))
            total_waste_list.append(data3.count())
        # 计算本期返修数量
        data4 = YCwaste.select().where(YCwaste.status == 2)

        if work == '':
            if starttime != '':
                data4 = data4.where(YCwaste.posttime >= utc_str_to_timestamp(starttime))
            if endtime != '':
                data4 = data4.where(YCwaste.posttime <= utc_str_to_timestamp(endtime))
            if type != '':
                data4 = data4.where(YCwaste.type == get_type_sort(type))
            if modle != '':
                data4 = data4.where(YCwaste.factory == modle)
            if keyword != '':
                like = '%' + keyword + '%'
                data4 = data4.where(YCwaste.factory % like)
            for i in range(2, 12):
                data4_i = data4.where(YCwaste.work == i)
                total_waste1 = data4_i.count()
                total_waste1_list.append(total_waste1)
        if work != '':
            if starttime != '':
                data4 = data4.where(YCwaste.posttime >= utc_str_to_timestamp(starttime))
            if endtime != '':
                data4 = data4.where(YCwaste.posttime <= utc_str_to_timestamp(endtime))
            if type != '':
                data4 = data4.where(YCwaste.type == get_type_sort(type))
            if modle != '':
                data4 = data4.where(YCwaste.factory == modle)
            if keyword != '':
                like = '%' + keyword + '%'
                data4 = data4.where(YCwaste.factory % like)
                data4 = data4.where(YCwaste.work == get_work_sort(work))
            total_waste1_list.append(data4.count())
        print(len((total_waste_list)))
        for i in range(len(total_waste_list)):
            result.append({"work": get_work_name(total_last_list[i][1]), "type": type, "produce": modle, "modle": 'TL_EP110',
                            'last': total_last_list[i][0],
                            'now': total_now_list[i], "use": total_use_list[i], "waste": total_waste_list[i],
                            "w_return": total_waste1_list[i],
                            "result": total_last_list[i][0] + total_now_list[i] - total_use_list[i] - total_waste_list[i] -
                                      total_waste1_list[i]} )
    result=sorted(result, key=lambda i: i['work'])
    for item_i in result:
        if item_i['result'] < 0:
            item_i['result'] = 0
    workbook_m = xlwt.Workbook(encoding='utf-8')
    xlsheet = workbook_m.add_sheet('工作站终端统计')
    xlsheet.write(0, 0, '工作站')
    xlsheet.write(0, 1, '终端类型')
    xlsheet.write(0, 2, '厂家')
    xlsheet.write(0, 3, '型号')
    xlsheet.write(0, 4, '上期结存')
    xlsheet.write(0, 5, '本期入库数量')
    xlsheet.write(0, 6, '本期出库数量')
    xlsheet.write(0, 7, '本期报废数量')
    xlsheet.write(0, 8, '本期返修数量')
    xlsheet.write(0, 9, '库存结余数量')

    for i in range(len(result)):
        xlsheet.write(i + 1, 0, result[i]['work'])
        xlsheet.write(i + 1, 1, result[i]['type'])
        xlsheet.write(i + 1, 2, result[i]['produce'])
        xlsheet.write(i + 1, 3, result[i]['modle'])
        xlsheet.write(i + 1, 4, result[i]['last'])
        xlsheet.write(i + 1, 5, result[i]['now'])
        xlsheet.write(i + 1, 6, result[i]['use'])
        xlsheet.write(i + 1, 7, result[i]['waste'])
        xlsheet.write(i + 1, 8, result[i]['w_return'])
        xlsheet.write(i + 1, 9, result[i]['result'])
    xlsname = utc_timestamp_to_str(int(time.time())) + '工作站统计'
    workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
    return ({'code': 0, 'msg': 'success', 'url': 'down.flyminer.cn:89/{}.xls'.format(xlsname)})


def supplies_statistics_work_get(page, size, type=None, starttime=None, endtime=None, work=None, model=None,
                                 keyword=None):  # noqa: E501
    """Workstation installation dimension statistics

    Workstation installation dimension statistics # noqa: E501

    :param page: page number
    :type page: str
    :param size: Per page display quantity
    :type size: str
    :param type: terminal type
    :type type: str
    :param starttime: the starttime for user choose
    :type starttime: str
    :param endtime: the endtime for user choose
    :type endtime: str
    :param work: workstation
    :type work: str
    :param model: model
    :type model: str
    :param keyword: keyword
    :type keyword: str

    :rtype: StatisticsWorkList
    """
    # 默认类型为智能网关
    if type == '':
        type = '智能网关'
    if model == '':
        modle_list = ['杭研','华为','贝尔','中兴']
    if model != '':
        modle_list = [model]
    # m没有的话从本月1号开始计算
    if starttime == '':
        starttime = get_f_l_day_now()[0]
    if endtime == '':
        endtime = get_f_l_day_now()[1]
    print(starttime, endtime)

    result=[]
    for modle in modle_list:
        total_last_list = []
        total_now_list = []
        total_use_list = []
        total_waste_list = []
        total_waste1_list = []
        # 计算上期结存
        data = YCstorage.select().where(YCstorage.status == 0)

        if work == '':
            if starttime != '':
                data = data.where(YCstorage.posttime >= utc_str_to_timestamp(get_f_l_day()[0]))
            if endtime != '':
                data = data.where(YCstorage.posttime <= utc_str_to_timestamp(get_f_l_day()[1]))
            if type != '':
                data = data.where(YCstorage.type == get_type_sort(type))
            if modle != '':
                data = data.where(YCstorage.factory == modle)
            if keyword != '':
                like = '%' + keyword + '%'
                data = data.where((YCstorage.people % like) | (YCstorage.factory % like))
            for i in range(2, 12):
                data_i = data.where(YCstorage.work == i)
                total_last = data_i.count()
                total_last_list.append([total_last,i])
        if work != '':
            if starttime != '':
                data = data.where(YCstorage.posttime >= utc_str_to_timestamp(get_f_l_day()[0]))
            if endtime != '':
                data = data.where(YCstorage.posttime <= utc_str_to_timestamp(get_f_l_day()[1]))
            if type != '':
                data = data.where(YCstorage.type == get_type_sort(type))
            if modle != '':
                data = data.where(YCstorage.factory == modle)
            if keyword != '':
                like = '%' + keyword + '%'
                data = data.where((YCstorage.people % like) | (YCstorage.factory % like))
            data = data.where(YCstorage.work == get_work_sort(work))
            total_last_list.append([data.count(),get_work_sort(work)])

        # 计算本期入库
        data1 = YCstorage.select().where(YCstorage.status == 0)

        if work == '':
            if starttime != '':
                data1 = data1.where(YCstorage.posttime >= utc_str_to_timestamp(starttime))
            if endtime != '':
                data1 = data1.where(YCstorage.posttime <= utc_str_to_timestamp(endtime))
            if type != '':
                data1 = data1.where(YCstorage.type == get_type_sort(type))
            if modle != '':
                data1 = data1.where(YCstorage.factory == modle)
            if keyword != '':
                like = '%' + keyword + '%'
                data1 = data1.where((YCstorage.people % like) | (YCstorage.factory % like))
            for i in range(2, 12):
                data1_i = data1.where(YCstorage.work == i)
                total_now = data1_i.count()
                total_now_list.append(total_now)
        if work != '':
            if starttime != '':
                data1 = data1.where(YCstorage.posttime >= utc_str_to_timestamp(starttime))
            if endtime != '':
                data1 = data1.where(YCstorage.posttime <= utc_str_to_timestamp(endtime))
            if type != '':
                data1 = data1.where(YCstorage.type == get_type_sort(type))
            if modle != '':
                data1 = data1.where(YCstorage.factory == modle)
            if keyword != '':
                like = '%' + keyword + '%'
                data1 = data1.where((YCstorage.people % like) | (YCstorage.factory % like))
            data1 = data1.where(YCstorage.work == get_work_sort(work))
            total_now_list.append(data1.count())

        # 计算出库数量
        data2 = YCuse.select()

        if work == '':
            if starttime != '':
                data2 = data2.where(YCuse.posttime >= utc_str_to_timestamp(starttime))
            if endtime != '':
                data2 = data2.where(YCuse.posttime <= utc_str_to_timestamp(endtime))
            if type != '':
                data2 = data2.where(YCuse.type == get_type_sort(type))
            if modle != '':
                data2 = data2.where(YCuse.produce == modle)
            if keyword != '':
                like = '%' + keyword + '%'
                data2 = data2.where(YCuse.people % like)
            for i in range(2, 12):
                data2_i = data2.where(YCuse.work == i)
                total_use = data2_i.count()
                total_use_list.append(total_use)
        if work != '':
            if starttime != '':
                data2 = data2.where(YCuse.posttime >= utc_str_to_timestamp(starttime))
            if endtime != '':
                data2 = data2.where(YCuse.posttime <= utc_str_to_timestamp(endtime))
            if type != '':
                data2 = data2.where(YCuse.type == get_type_sort(type))
            if modle != '':
                data2 = data2.where(YCuse.produce == modle)
            if keyword != '':
                like = '%' + keyword + '%'
                data2 = data2.where(YCuse.people % like)
            data2 = data2.where(YCuse.work == get_work_sort(work))
            total_use_list.append(data2.count())

        # 计算本期报废数量
        data3 = YCwaste.select().where(YCwaste.status == 1)

        if work == '':
            if starttime != '':
                data3 = data3.where(YCwaste.posttime >= utc_str_to_timestamp(starttime))
            if endtime != '':
                data3 = data3.where(YCwaste.posttime <= utc_str_to_timestamp(endtime))
            if type != '':
                data3 = data3.where(YCwaste.type == get_type_sort(type))
            if modle != '':
                data3 = data3.where(YCwaste.factory == modle)
            if keyword != '':
                like = '%' + keyword + '%'
                data3 = data3.where(YCwaste.factory % like)
            for i in range(2, 12):
                data3_i = data3.where(YCwaste.work == i)
                total_waste = data3_i.count()
                total_waste_list.append(total_waste)
        if work != '':
            if starttime != '':
                data3 = data3.where(YCwaste.posttime >= utc_str_to_timestamp(starttime))
            if endtime != '':
                data3 = data3.where(YCwaste.posttime <= utc_str_to_timestamp(endtime))
            if type != '':
                data3 = data3.where(YCwaste.type == get_type_sort(type))
            if modle != '':
                data3 = data3.where(YCwaste.factory == modle)
            if keyword != '':
                like = '%' + keyword + '%'
                data3 = data3.where(YCwaste.factory % like)
            data3 = data3.where(YCwaste.work == get_work_sort(work))
            total_waste_list.append(data3.count())
        # 计算本期返修数量
        data4 = YCwaste.select().where(YCwaste.status == 2)

        if work == '':
            if starttime != '':
                data4 = data4.where(YCwaste.posttime >= utc_str_to_timestamp(starttime))
            if endtime != '':
                data4 = data4.where(YCwaste.posttime <= utc_str_to_timestamp(endtime))
            if type != '':
                data4 = data4.where(YCwaste.type == get_type_sort(type))
            if modle != '':
                data4 = data4.where(YCwaste.factory == modle)
            if keyword != '':
                like = '%' + keyword + '%'
                data4 = data4.where(YCwaste.factory % like)
            for i in range(2, 12):
                data4_i = data4.where(YCwaste.work == i)
                total_waste1 = data4_i.count()
                total_waste1_list.append(total_waste1)
        if work != '':
            if starttime != '':
                data4 = data4.where(YCwaste.posttime >= utc_str_to_timestamp(starttime))
            if endtime != '':
                data4 = data4.where(YCwaste.posttime <= utc_str_to_timestamp(endtime))
            if type != '':
                data4 = data4.where(YCwaste.type == get_type_sort(type))
            if modle != '':
                data4 = data4.where(YCwaste.factory == modle)
            if keyword != '':
                like = '%' + keyword + '%'
                data4 = data4.where(YCwaste.factory % like)
                data4 = data4.where(YCwaste.work == get_work_sort(work))
            total_waste1_list.append(data4.count())
        print(len((total_waste_list)))
        for i in range(len(total_waste_list)):
            result.append({"work": get_work_name(total_last_list[i][1]), "type": type, "produce": modle, "modle": 'TL_EP110',
                            'last': total_last_list[i][0],
                            'now': total_now_list[i], "use": total_use_list[i], "waste": total_waste_list[i],
                            "w_return": total_waste1_list[i],
                            "result": total_last_list[i][0] + total_now_list[i] - total_use_list[i] - total_waste_list[i] -
                                      total_waste1_list[i]} )
    result=sorted(result, key=lambda i: i['work'])
    print (result)
    for item_i in result:
        if item_i['result'] < 0:
            item_i['result'] = 0
    msg = {"code": 0, "msg": "success",'total':len(result), "result": result}

    return msg


def supplies_storage_delete(id):  # noqa: E501
    """Delete inventory

    Delete inventory # noqa: E501

    :param id: data
    :type id: int

    :rtype: Success
    """
    try:
        if YCstorage.delete().where(YCstorage.id == id).execute():
            msg = {"code": 0, "msg": "success"}
        else:
            msg = {"code": 10003, "msg": "Record does not exist"}
    except:
        msg = {"code": -1, "msg": "system error"}
    return msg


def supplies_storage_export_get(starttime=None, endtime=None, work=None, type=None, model=None,
                                keyword=None):  # noqa: E501
    """Inventory list

    Inventory list # noqa: E501

    :param starttime: the starttime for user choose
    :type starttime: str
    :param endtime: the endtime for user choose
    :type endtime: str
    :param work: workstation
    :type work: str
    :param type: terminal type
    :type type: str
    :param model: Terminal model
    :type model: str
    :param keyword: keyword
    :type keyword: str

    :rtype: Export
    """
    try:
        name = storage_make_report(starttime=starttime, endtime=endtime, work=work,
                                   type=type, model=model, keyword=keyword)
        print(name + 'star')
        msg = {
            "msg": "msg",
            "code": 0,
            "url": "down.flyminer.cn:89/{}".format(name),
        }
    except:
        msg = {

            "code": -1,
            "msg": "system error"

        }

    return msg


# 入库明细
def supplies_storage_get(page, size, starttime=None, endtime=None, work=None, type=None, model=None,
                         keyword=None):  # noqa: E501
    """Inventory list

    Inventory list # noqa: E501

    :param page: page number
    :type page: str
    :param size: Per page display quantity
    :type size: str
    :param starttime: the starttime for user choose
    :type starttime: str
    :param endtime: the endtime for user choose
    :type endtime: str
    :param work: workstation
    :type work: str
    :param type: terminal type
    :type type: str
    :param model: Terminal model
    :type model: str
    :param keyword: keyword
    :type keyword: str

    :rtype: StorageList
    """

    try:

        if (starttime != None and starttime != '') or \
                (endtime != None and endtime != '') or \
                (work != None and work != '') or \
                (type != None and type != '') \
                or (model != None and model != '') \
                or (keyword != None and keyword != ''):
            data = YCstorage.select()
            print(data.count())
            if keyword != None and keyword != '':
                #  厂家 条形码  入库人 均为字符串赛选
                print(keyword)
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
                # if keyword != None and keyword != '':
                #     # 如果是工作站    厂家 条形码  入库人
                #     print (keyword)
                #
                #     data = data.where(YCstorage.factory ** '%' + keyword + '%')
                #     if data.count() == 0:
                #         data = data.where(YCstorage.code ** '%' + keyword + '%')
                #     if data.count() == 0:
                #         data = data.where(YCstorage.code ** '%' + keyword + '%')
                #     print (data.count())
                # if data.count()==0:
                #     try:          # % ‘%ba%’
                #         work_name = YCwork.select().where(YCwork.name ** '%' + keyword + '%').get()
                #         data=data.where(YCstorage.work==work_name)
                #     except:
                #         pass
            total = data.count()
            data = data.order_by(YCstorage.posttime.desc()).paginate(int(page), int(size))
        else:
            data = YCstorage.select().order_by(YCstorage.posttime.desc()).paginate(int(page), int(size))
            total = YCstorage.select().count()
        result_list = [{'principal': item.people,
                        'posttime': utc_timestamp_to_str(item.posttime),
                        'factory': item.factory,
                        'code': item.code,
                        'work': get_work_name(item.work),
                        'model': get_model_name(item.model),
                        'id': item.id,
                        'type': get_type_name(item.type)} for item in data]
        msg = {"code": 0, "msg": "success", "total": total, "result": result_list}

    except Exception as e:
        print(e)
        msg = {"code": -1, "msg": "system error"}
    return msg


def supplies_storage_query_code_get(code):  # noqa: E501
    """Inventory list

    Inventory list # noqa: E501

    :param code: the starttime for user choose
    :type code: str

    :rtype: StorageQuery
    """
    try:
        data = YCstorage.select().where(YCstorage.code == code)

        result_list = [{'principal': item.people,
                        'posttime': utc_timestamp_to_str(item.posttime),
                        'factory': item.factory,
                        'code': item.code,
                        'work': get_work_name(item.work),
                        'model': get_model_name(item.model),
                        'id': item.id,
                        'type': get_type_name(item.type)} for item in data]
        msg = {"code": 0, "msg": "success", "result": result_list}
    except Exception as e:
        print(e)
        msg = {"code": -1, "msg": "system error"}
    return msg


# 目前不是这个增加  所以不需要增加一个 入库的status
def supplies_storage_post(body):  # noqa: E501
    """Product warehousing

    Product warehousing # noqa: E501

    :param body: data
    :type body: dict | bytes

    :rtype: Success
    """
    if connexion.request.is_json:
        body = StorageData.from_dict(connexion.request.get_json())  # noqa: E501

        try:
            if YCstorage.select().where(YCstorage.code == body.code).count() >= 1:
                msg = {"code": 10003, "msg": "code has exist"}
                return msg
        except:
            pass

        try:
            work = get_work_sort(body.work)
            type = get_type_sort(body.type)
            model = get_model_sort(body.model)
            YCstorage.insert(work=work, type=type, factory=body.factory,
                             model=model, people=body.principal, code=body.code,
                             status=0, posttime=int(time.time())).execute()
            YCstatus.insert(work=work, use='扫码入库', people=body.principal, code=body.code,
                            posttime=int(time.time())).execute()
            msg = {
                "msg": "success",
                "code": 0
            }
        except Exception as e:
            print(e)
            msg = {"code": -1, "msg": "Error"}
        return msg


def supplies_storage_put(body):  # noqa: E501
    """Edit inventory

    Edit inventory # noqa: E501

    :param body: data
    :type body: dict | bytes

    :rtype: Success
    """
    if connexion.request.is_json:
        body = StorageDataEdit.from_dict(connexion.request.get_json())  # noqa: E501

        try:
            if YCstorage.select().where(YCstorage.id == body.id).count() < 1:
                msg = {"code": 10003, "msg": "code not exist"}
                return msg
        except:
            pass
        try:
            work = get_work_sort(body.work)
            type = get_type_sort(body.type)
            model = get_model_sort(body.model)
            YCstorage.update(work=work, type=type, factory=body.factory,
                             model=model, people=body.principal, code=body.code,
                             posttime=int(time.time())).where(YCstorage.id == body.id).execute()
            msg = {
                "msg": "success",
                "code": 0
            }
        except Exception as e:
            print(e)
            msg = {"code": -1, "msg": "Error"}
        return msg


def supplies_use_code_id_get(id):  # noqa: E501
    """Query a few devices and barcodes in the current work order

    Query a few devices and barcodes in the current work order # noqa: E501

    :param id: ID
    :type id: str

    :rtype: UseCodes
    """

    result = []
    try:
        data = YCuse.select().where(YCuse.id == id).get()
        print(data.modem)
        if (data.modem != None and data.modem != '' and data.modem != '0'):
            results = {}
            info = YCstorage.select().where(YCstorage.code == data.modem).get()
            print(info.code)
            results['code'] = info.code
            results['model'] = get_model_name(info.model)
            results['type'] = get_type_name(info.type)
            result.append(results)
        if (data.gateway != None and data.gateway != '' and data.gateway != '0'):
            results = {}
            info = YCstorage.select().where(YCstorage.code == data.gateway).get()
            print(info.code)
            results['code'] = info.code
            results['model'] = get_model_name(info.model)
            results['type'] = get_type_name(info.type)
            result.append(results)
        if (data.box != None and data.box != '' and data.box != '0'):
            results = {}
            info = YCstorage.select().where(YCstorage.code == data.box).get()
            results['code'] = info.code
            results['model'] = get_model_name(info.model)
            results['type'] = get_type_name(info.type)
            result.append(results)
        if (data.hemu != None and data.hemu != '' and data.hemu != '0'):
            results = {}
            info = YCstorage.select().where(YCstorage.code == data.hemu).get()
            results['code'] = info.code
            results['model'] = get_model_name(info.model)
            results['type'] = get_type_name(info.type)
            result.append(results)
        if (data.phone != None and data.phone != '' and data.phone != '0'):
            results = {}
            info = YCstorage.select().where(YCstorage.code == data.phone).get()
            results['code'] = info.code
            results['model'] = get_model_name(info.model)
            results['type'] = get_type_name(info.type)
            result.append(results)

        msg = {"code": 0, "msg": "success", "result": result}

    except Exception as e:
        print(e)
        msg = {"code": -1, "msg": "system error"}
    return msg


def supplies_use_export_get(starttime=None, endtime=None, work=None, type=None, keyword=None):  # noqa: E501
    """Inventory list

    Inventory list # noqa: E501

    :param starttime: the starttime for user choose
    :type starttime: str
    :param endtime: the endtime for user choose
    :type endtime: str
    :param work: workstation
    :type work: str
    :param type: business type
    :type type: str
    :param keyword: keyword
    :type keyword: str

    :rtype: Export
    """
    try:
        name = use_make_report(starttime=starttime, endtime=endtime, work=work,
                               type=type, keyword=keyword)
        print(name + 'star')
        msg = {
            "msg": "msg",
            "code": 0,
            "url": "down.flyminer.cn:89/{}".format(name),
        }
    except:
        msg = {

            "code": -1,
            "msg": "system error"

        }

    return msg


def supplies_use_get(page, size, starttime=None, endtime=None, work=None, type=None, keyword=None):  # noqa: E501
    """Inventory list

    Inventory list # noqa: E501

    :param page: page number
    :type page: str
    :param size: Per page display quantity
    :type size: str
    :param starttime: the starttime for user choose
    :type starttime: str
    :param endtime: the endtime for user choose
    :type endtime: str
    :param work: workstation
    :type work: str
    :param type: business type
    :type type: str
    :param keyword: keyword
    :type keyword: str

    :rtype: UseList
    """
    try:
        if (starttime != None and starttime != '') or \
                (endtime != None and endtime != '') or \
                (work != None and work != '') or \
                (type != None and type != '') \
                or (keyword != None and keyword != ''):
            data = YCuse.select()
            print(data.count())
            if keyword != None and keyword != '':
                #  厂家 条形码  入库人 均为字符串赛选
                # 条形码有多个
                print(keyword)
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
            total = data.count()
            data = data.order_by(YCuse.posttime.desc()).paginate(int(page), int(size))
        else:
            data = YCuse.select().order_by(YCuse.posttime.desc()).paginate(int(page), int(size))
            total = YCuse.select().count()
#lambda x:"yes" if x==1 else "no"

        b = lambda x: x if x != ''else'暂无数据'


        result_list = [{
            'posttime': utc_timestamp_to_str(item.posttime),
            'business': get_business_name(item.business),
            'hemu': b(item.hemu) ,
            'phone': b(item.phone),
            'modem': b(item.modem),
            'box': b(item.box),
            'gateway': b(item.gateway),
            'principal': item.people,
            'work': get_work_name(item.work),
            'order': item.order,
            'id': item.id,
        } for item in data]
        msg = {"code": 0, "msg": "success", "total": total, "result": result_list}
    except:
        msg = {"code": -1, "msg": "Error"}
    return msg


def supplies_use_upload_post(files=None):  # noqa: E501
    """Install usage details import

    Install usage details import # noqa: E501

    :param files: file data
    :type files: werkzeug.datastructures.FileStorage

    :rtype: Success
    """
    # try:
    #     file = request.files['files']
    #     print(file.filename)
    #     file.save(os.path.join('/var/www/downfile', file.filename))
    #     new_filepath = '/var/www/downfile/{}'.format(file.filename)
    #     msg = {'code': 0, 'msg': new_filepath}
    # except Exception as e:
    #     print (e)
    #     msg = {'code': -1, 'msg': 'Error'}
    # return msg
    try:
        now_type = 0
        file = request.files["files"]
        file.save(os.path.join('/var/www/downfile', file.filename))
        print('ssss')

        # data = xlrd.open_workbook('/var/www/downfile/update.xlsx')
        data = xlrd.open_workbook('/var/www/downfile/{}'.format(file.filename))
        table = data.sheets()[0]  # 通过索引顺序获取
        # table = data.sheet_by_index(0) #通过索引顺序获取
        # table = data.sheet_by_name(u'Sheet1')#通过名称获取
        num = table.col_values(0)  # 获取整列的信息

        # # 获取单元格
        # table.cell(0,0).value
        # table.cell(2,3).value
        print(len(num))
        GLitem = []
        for i in range(1, len(num)):
            try:
                info = {}
                item = table.row_values(i)  # 获取整行的信息
                # companys = table.col_values(0)  #获取整列的信息
                # # 获取单元格
                # table.cell(0,0).value
                # table.cell(2,3).value
                print(len(item))
                work = item[0]
                type = item[1]
                order = str(item[2]).replace(".0", "")
                modem = str(item[3]).replace(".0", "")
                gateway = str(item[4]).replace(".0", "")
                box = str(item[5]).replace(".0", "")
                hemu = str(item[6]).replace(".0", "")
                phone = str(item[7]).replace(".0", "")
                people = item[8]
                posttime = item[9]
                try:
                    posttime = str(datetime(*xldate_as_tuple(posttime, 0)))
                except:
                    posttime = item[9]
                if people == '' or posttime == '' or order == '':
                    msg = {'code': 10003, 'msg': i}
                    return msg
                print(gateway)
                if (modem != None and modem != ''):
                    now_type = 1
                    count = YCstorage.select().where(YCstorage.code == modem).count()
                    if count < 1:
                        msg = {'code': 10003, 'msg': i}
                        return msg
                if (gateway != None and gateway != ''):
                    now_type = 1
                    count = YCstorage.select().where(YCstorage.code == gateway).count()
                    if count < 1:
                        msg = {'code': 10003, 'msg': i}
                        return msg
                if (box != None and box != ''):
                    count = YCstorage.select().where(YCstorage.code == box).count()
                    if count < 1:
                        msg = {'code': 10003, 'msg': i}
                        return msg
                if (hemu != None and hemu != ''):
                    count = YCstorage.select().where(YCstorage.code == hemu).count()
                    if count < 1:
                        msg = {'code': 10003, 'msg': i}
                        return msg
                if (phone != None and phone != ''):
                    count = YCstorage.select().where(YCstorage.code == phone).count()
                    if count < 1:
                        msg = {'code': 10003, 'msg': i}
                        return msg
                info['work'] = work
                info['type'] = type
                info['order'] = order
                info['modem'] = modem
                info['gateway'] = gateway
                info['box'] = box
                info['hemu'] = hemu
                info['phone'] = phone
                info['people'] = people
                info['posttime'] = posttime
                GLitem.append(info)
            except Exception as e:
                print(e)
                return {'code': 10003, 'msg': i}
        if len(GLitem) == 0:
            return {'code': -1, 'msg': 'Error'}

        for item in GLitem:
            factory = ''
            if (item['modem'] != None and item['modem'] != ''):
                YCstatus.insert(use='装机使用',
                                work=get_work_sort(item['work']),
                                code=item['modem'],
                                people=item['people'],
                                posttime=utc_str_to_timestamp(item['posttime'])).execute()
                YCoutbound.update(status=1).where(YCoutbound.code == item['modem']).execute()
                factory = YCstorage.select().where(YCstorage.code == item['modem']).get().factory
            if (item['gateway'] != None and item['gateway'] != ''):
                YCstatus.insert(use='装机使用',
                                work=get_work_sort(item['work']),
                                code=item['gateway'],
                                people=item['people'],
                                posttime=utc_str_to_timestamp(item['posttime'])).execute()
                YCoutbound.update(status=1).where(YCoutbound.code == item['gateway']).execute()
                factory = YCstorage.select().where(YCstorage.code == item['gateway']).get().factory
            if (item['box'] != None and item['box'] != ''):
                YCstatus.insert(use='装机使用',
                                work=get_work_sort(item['work']),
                                code=item['box'],
                                people=item['people'],
                                posttime=utc_str_to_timestamp(item['posttime'])).execute()
                YCoutbound.update(status=1).where(YCoutbound.code == item['box']).execute()
                factory = YCstorage.select().where(YCstorage.code == item['box']).get().factory
            if (item['hemu'] != None and item['hemu'] != ''):
                YCstatus.insert(use='装机使用',
                                work=get_work_sort(item['work']),
                                code=item['hemu'],
                                people=item['people'],
                                posttime=utc_str_to_timestamp(item['posttime'])).execute()
                YCoutbound.update(status=1).where(YCoutbound.code == item['hemu']).execute()
                factory = YCstorage.select().where(YCstorage.code == item['hemu']).get().factory
            if (item['phone'] != None and item['phone'] != ''):
                YCstatus.insert(use='装机使用',
                                work=get_work_sort(item['work']),
                                code=item['phone'],
                                people=item['people'],
                                posttime=utc_str_to_timestamp(item['posttime'])).execute()
                YCoutbound.update(status=1).where(YCoutbound.code == item['phone']).execute()
                factory = YCstorage.select().where(YCstorage.code == item['phone']).get().factory
            YCuse.insert(
                produce=factory,
                work=get_work_sort(item['work']),
                business=get_business_sort(item['type']),
                order=item['order'],
                modem=item['modem'],
                gateway=item['gateway'],
                box=item['box'],
                hemu=item['hemu'],
                phone=item['phone'],
                people=item['people'],
                type=now_type,
                posttime=utc_str_to_timestamp(item['posttime'])).execute()
        msg = {"code": 0, "msg": "success"}
    except Exception as e:
        print(e)
        msg = {"code": -1, "msg": "Error"}
    return msg


def supplies_waste_export_get(type, starttime=None, endtime=None, work=None, keyword=None):  # noqa: E501
    """maintain list

    maintain list # noqa: E501

    :param page: page number
    :type page: str
    :param size: Per page display quantity
    :type size: str
    :param type: 1 means scrap, 2 means return
    :type type: str
    :param starttime: the starttime for user choose
    :type starttime: str
    :param endtime: the endtime for user choose
    :type endtime: str
    :param work: workstation
    :type work: str
    :param keyword: keyword
    :type keyword: str

    :rtype: Export
    """
    try:
        print(type)
        name = waste_make_report(type=type, starttime=starttime, endtime=endtime, work=work,
                                 keyword=keyword)
        print(name + 'star')
        msg = {
            "msg": "msg",
            "code": 0,
            "url": "down.flyminer.cn:89/{}".format(name),
        }
    except:
        msg = {

            "code": -1,
            "msg": "system error"

        }

    return msg


def supplies_waste_get(page, size, type, starttime=None, endtime=None, work=None, keyword=None):  # noqa: E501
    """maintain list

    maintain list # noqa: E501

    :param page: page number
    :type page: str
    :param size: Per page display quantity
    :type size: str
    :param type: 1 means scrap, 2 means return
    :type type: str
    :param starttime: the starttime for user choose
    :type starttime: str
    :param endtime: the endtime for user choose
    :type endtime: str
    :param work: workstation
    :type work: str
    :param keyword: keyword
    :type keyword: str

    :rtype: WasteList
    """
    try:
        if type == '1':
            if (starttime != None and starttime != '') or \
                    (endtime != None and endtime != '') or \
                    (work != None and work != '') \
                    or (keyword != None and keyword != ''):
                data = YCwaste.select().where(YCwaste.status == 1)
                print(data.count())
                if keyword != None and keyword != '':
                    #  厂家 条形码  入库人 均为字符串赛选
                    # 条形码有多个
                    print(keyword)
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
                total = data.where(YCwaste.status == 1).count()
                data = data.order_by(YCwaste.posttime.desc()).paginate(int(page), int(size))
            else:
                data = YCwaste.select().where(YCwaste.status == 1).order_by(YCwaste.posttime.desc()).paginate(int(page), int(size))
                total = YCwaste.select().where(YCwaste.status == 1).count()
            result_list = [{
                'posttime': utc_timestamp_to_str(item.posttime),
                'code': item.code,
                'work': get_work_name(item.work),
                'model': get_model_name(item.model),
                'factory': item.factory,
                'type': get_type_name(item.type),
                'id': item.id,
            } for item in data]
            msg = {"code": 0, "msg": "success", "total": total, "result": result_list}
        else:
            if (starttime != None and starttime != '') or \
                    (endtime != None and endtime != '') or \
                    (work != None and work != '') \
                    or (keyword != None and keyword != ''):
                data = YCwaste.select().where(YCwaste.status == 2)
                print(data.count())
                if keyword != None and keyword != '':
                    #  厂家 条形码  入库人 均为字符串赛选
                    # 条形码有多个
                    print(keyword)
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
                total = data.where(YCwaste.status == 2).count()
                data = data.order_by(YCwaste.posttime.desc()).paginate(int(page), int(size))
            else:
                total = YCwaste.select().where(YCwaste.status == 2).count()
                data = YCwaste.select().order_by(YCwaste.posttime.desc()).where(YCwaste.status == 2).paginate(int(page), int(size))
            result_list = [{
                'posttime': utc_timestamp_to_str(item.posttime),
                'code': item.code,
                'work': get_work_name(item.work),
                'model': get_model_name(item.model),
                'factory': item.factory,
                'type': get_type_name(item.type),
                'id': item.id,
            } for item in data]
            msg = {"code": 0, "msg": "success", "total": total, "result": result_list}
    except Exception as e:
        print(e)
        msg = {"code": -1, "msg": "Error"}
    return msg


def supplies_waste_upload_post(type, files=None):  # noqa: E501
    """Install usage details import

    Install usage details import # noqa: E501

    :param type: 1 means scrap, 2 means return
    :type type: werkzeug.datastructures.FileStorage
    :param files: file data
    :type files: werkzeug.datastructures.FileStorage

    :rtype: Success
    """
    #   type  区分！   也可以从报表里面的字段来区分
    try:
        excle_status = type
        file = request.files['files']
        file.save(os.path.join('/var/www/downfile', file.filename))
        # new_filepath = '/var/www/downfile/{}'.format(file.filename)

        # file = request.files['files']
        # file.save(os.path.join('../down', file.filename))

        data = xlrd.open_workbook('/var/www/downfile/{}'.format(file.filename))
        table = data.sheets()[0]  # 通过索引顺序获取
        # table = data.sheet_by_index(0) #通过索引顺序获取
        # table = data.sheet_by_name(u'Sheet1')#通过名称获取
        num = table.col_values(0)  # 获取整列的信息

        # # 获取单元格
        # table.cell(0,0).value
        # status_word = table.cell(0, 2).value
        # if '报废' in status_word:
        #     excle_status = 1
        # elif "返修" in status_word:
        #     excle_status = 2
        # else:
        #     msg = {'code': 10003, 'msg': 'Error'}
        #     return msg

        print(len(num))
        GLitem = []
        for i in range(1, len(num)):
            try:
                info = {}
                item = table.row_values(i)  # 获取整行的信息
                # companys = table.col_values(0)  #获取整列的信息
                # # 获取单元格
                # table.cell(0,0).value
                # table.cell(2,3).value
                print(len(item))

                work = item[0]
                type = item[1]
                code = str(item[2]).replace(".0", "")
                factory = item[3]
                model = item[4]
                posttime = item[5]
                try:
                    posttime = str(datetime(*xldate_as_tuple(posttime, 0)))
                except:
                    posttime = item[5]
                if factory == '' or posttime == '' or type == '' or code == '':
                    print('空')
                    msg = {'code': 10003, 'msg': i}
                    return msg

                count = YCoutbound.select().where(YCoutbound.code == code).count()
                if count < 1:
                    msg = {'code': 10003, 'msg': i}
                    return msg

                info['work'] = work
                info['type'] = type
                info['code'] = code
                info['factory'] = factory
                info['model'] = model
                info['posttime'] = posttime
                GLitem.append(info)
            except:
                msg = {'code': 10003, 'msg': 'Error'}
                return msg
        if len(GLitem) == 0:
            return {'code': 10003, 'msg': 'Error'}

        for item in GLitem:
            YCwaste.insert(status=excle_status,
                           work=get_work_sort(item['work']),
                           type=get_type_sort(item['type']),

                           code=item['code'],
                           factory=item['factory'],
                           model=get_model_sort(item['model']),
                           posttime=utc_str_to_timestamp(item['posttime'])).execute()
            # 报废没有people 所以不加状态
            # if excle_status == '1':
            #     YCstatus.insert(use='设备报废',
            #                     work=get_work_sort(item['work']),
            #                     code=item['code'],
            #                     people=item['people'],
            #                     posttime=utc_str_to_timestamp(item['posttime'])).execute()
            # else:
            #     YCstatus.insert(use='设备返修',
            #                     work=get_work_sort(item['work']),
            #                     code=item['code'],
            #                     people=item['people'],
            #                     posttime=utc_str_to_timestamp(item['posttime'])).execute()

        msg = {"code": 0, "msg": "success"}
    except Exception as e:
        print(e)
        msg = {"code": -1, "msg": "Error"}
    return msg
