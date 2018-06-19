import connexion
import six

from swagger_server.models.home_chart import HomeChart  # noqa: E501
from swagger_server.models.success import Success  # noqa: E501
from swagger_server import util
from swagger_server.mysql_db import *
from swagger_server.export_report import *
from swagger_server.models.notice_data import NoticeData  # noqa: E501
from swagger_server.models.notice_list import NoticeList  # noqa: E501
from swagger_server.models.notice_list2 import NoticeList2  # noqa: E501
from swagger_server.models.notice_lists2 import NoticeLists2  # noqa: E501
from swagger_server.controllers.complain_controller import *
from swagger_server.controllers.installed_controller import *
from swagger_server.tool import *
import datetime, xlwt


def get_yes_time():
    now_time = datetime.datetime.now()
    yes_time = now_time + datetime.timedelta(days=-1)
    yes_time_nyr = yes_time.strftime('%Y-%m-%d')  # //格式化输出
    return yes_time_nyr


def home_bartwo_get():  # noqa: E501
    """Index Bartwo Chart
    Index Bartwo Chart # noqa: E501
    :rtype: HomeChart
    """
    msg = {
        "code": 0,
        "msg": "返回成功",
        "result": [
            {
                "name": "网络连接",
                "value": "64"
            },
            {
                "name": "拨号认证",
                "value": "42"
            },
            {
                "name": "网速",
                "value": "12"
            },
            {
                "name": "互联网电视",
                "value": "10"
            },
            {
                "name": "其它",
                "value": "23"
            },

        ]
    }
    return msg


def index_barone_get():  # noqa: E501
    """Index Barone Chart
    Index Barone Chart # noqa: E501
    :rtype: HomeChart
    """
    msg = {
        "code": 0,
        "msg": "suucess",
        "result": [
            {
                "name": "<10M",
                "value": "0.18"
            },

            {
                "name": "10M",
                "value": "0.1"
            },
            {
                "name": "20M",
                "value": "0.13"
            },
            {
                "name": "50M",
                "value": "0.36"
            },
            {
                "name": "100M",
                "value": "0.12"
            },
            {
                "name": "其它",
                "value": "0.11"
            }
        ]
    }
    return msg


def index_lineone_get():  # noqa: E501
    """Index Lineone Chart
    Index Lineone Chart # noqa: E501
    :rtype: HomeChart
    """
    starttime = '2018-02-14 00:00:00'

    endtime = '2018-02-15 00:00:00'
    result = []
    area_list = ['秭归', '枝江', '长阳', '远安', '宜都', '夷陵', '兴山', '五峰', '开发区', '当阳', '城区']
    for area in area_list:
        like = '%' + area + '%'
        name = area
        value = YCcomplaints.select().where((YCcomplaints.area % like) & (
            YCcomplaints.starttime >= utc_str_to_timestamp(starttime)) & (
                                                YCcomplaints.starttime <= utc_str_to_timestamp(endtime))).count()
        result.append({"name": name, "value": value})
    msg = {"code": 0, "msg": "success", "result": result}
    return msg


def index_linetwo_get():  # noqa: E501
    """Index Linetwo Chart
    Index Linetwo Chart # noqa: E501
    :rtype: HomeChart
    """
    starttime = '2018-02-14 00:00:00'

    endtime = '2018-02-15 00:00:00'
    result = []
    area_list = ['秭归', '枝江', '长阳', '远安', '宜都', '夷陵', '兴山', '五峰', '开发区', '当阳', '城区']
    for area in area_list:
        like = '%' + area + '%'
        name = area
        value = YCcomplaints.select().where((YCcomplaints.area % like) & (YCcomplaints.type == '服务质量') & (
            YCcomplaints.starttime >= utc_str_to_timestamp(starttime)) & (
                                                YCcomplaints.starttime <= utc_str_to_timestamp(endtime))).count()
        result.append({"name": name, "value": value})
    msg = {"code": 0, "msg": "success", "result": result}
    return msg


def index_pan_get():  # noqa: E501
    """Index Pan Chart
    Index Pan Chart # noqa: E501
    :rtype: HomeChart
    """

    starttime = '2018-02-14 00:00:00'

    endtime = '2018-02-15 00:00:00'

    data = YCcomplaints.select().where((YCcomplaints.platform == 2) & (
        YCcomplaints.starttime >= utc_str_to_timestamp(starttime)) & (
                                           YCcomplaints.starttime <= utc_str_to_timestamp(endtime)))
    acceptance = YCcomplaints.select().where((YCcomplaints.platform == 2) & (
        YCcomplaints.starttime >= utc_str_to_timestamp(starttime)) & (
                                                 YCcomplaints.starttime <= utc_str_to_timestamp(
                                                     endtime))).count()
    avtime = 0
    for item in data:
        avtime = avtime + item.usetime
    print(avtime, acceptance)
    twentfour = data.where(YCcomplaints.usetime <= 24).count()

    try:
        av_time = avtime / acceptance
    except:
        av_time = 0
    result = [{"name": '及时率',
               "value": '%.2f' % (twentfour * 100 / acceptance),
               }, {"name": '平均处理时长',
                   "value": '%.2f' % (av_time),
                   }]

    msg = {"code": 0, "msg": "success", "result": result}
    return msg


def index_showall_get(starttime, endtime, type):  # noqa: E501
    """Index Showall

    Index Barone Chart # noqa: E501

    :param starttime: the starttime for user choose
    :type starttime: str
    :param endtime: the endtime for user choose
    :type endtime: str
    :param type: the user choose type
    :type type: str

    :rtype: HomeChart
    """
    if starttime == '':
        starttime = "2018-02-14 00:00:00"
    if endtime == '':
        endtime = "2018-02-15 00:00:00"
    # 投诉总表
    result_24 = complain_twenty_four_list_get(type='EMOS', starttime=starttime, endtime=endtime)
    result_8 = complain_eight_chart_get(type='投诉处理及时率', starttime=starttime, endtime=endtime)
    result_frist = complain_emos_first_chart_get(type='首次联系用户时长占比', starttime=starttime, endtime=endtime)

    # 装机总表
    starttime = "2018-02-14 00:00:00"
    endtime = "2018-02-15 00:00:00"
    result_install_24 = installed_twenty_four_list_get(type='宽带装机', starttime=starttime, endtime=endtime)
    result_install_8 = installed_eight_chart_get(type='880装机及时率', starttime=starttime, endtime=endtime)
    result_isntall_frist = installed_orders_chart_get(type='宽带装机_接单时长占比', starttime=starttime, endtime=endtime)

    all_results = {  # Result

        "area": "全市",
        "value_0": 0,
        "value_1": 0,
        "value_2": 0,
        "value_3": 0,
        "value_4": 0,
        "value_5": 0,
        "value_6": 0,
        "value_7": 0,
        "value_8": 0,
        "value_9": 0,
        "value_10": 0,
    }
    reslut = []
    for i in range(len(result_24['result'])):
        area = result_24['result'][i]['area']

        data_time = time.time() - 604800
        reslut_isntall_satisfied = YCinstalled.select().where(YCinstalled.area == area,
                                                              YCinstalled.posttime >= data_time,
                                                              YCinstalled.satisfied == 1).count()
        reslut_isntall_satisfied2 = YCinstalled.select().where(YCinstalled.area == area,
                                                               YCinstalled.posttime >= data_time,
                                                               YCinstalled.satisfied == 2).count()
        reslut_isntall_satisfied3 = YCinstalled.select().where(YCinstalled.area == area,
                                                               YCinstalled.posttime >= data_time,
                                                               YCinstalled.satisfied == 0).count()
        try:
            reslut_isntall_satisfied = '%.2f' % (reslut_isntall_satisfied * 100 / (
                reslut_isntall_satisfied + reslut_isntall_satisfied2 + reslut_isntall_satisfied3))
        except:
            reslut_isntall_satisfied = 0
        reslut_isntall_satisfied = reslut_isntall_satisfied
        msg_list = {"area": result_24['result'][i]['area'],  # 地点
                    "value_0": result_24['result'][i]['timely'].replace("%", ""),  # 24
                    "value_1": result_8['result'][i]['value'].replace("%", ""),  # 8
                    "value_2": result_frist['result'][i]['inside'],
                    # str(result_frist['result'][i]['inside']) + '%',  # 首次
                    "value_3": result_24['result'][i]['average'],  # 时长
                    "value_4": '100%'.replace("%", ""),  # 满意度
                    "value_5": result_24['result'][i]['investment'],  # 万投比
                    "value_6": result_install_24['result'][i]['rate'].replace("%", ""),  # 24
                    "value_7": result_install_8['result'][i]['value'],
                    # str(result_install_8['result'][i]['value']) + '%',  # 8
                    "value_8": result_isntall_frist['result'][i]['inside'],
                    # str(result_isntall_frist['result'][i]['inside']) + '%',  # 装机时长及时率
                    "value_9": result_install_24['result'][i]['ave'],  # 平均装机时长
                    "value_10": reslut_isntall_satisfied, }  # 满意度
        print(msg_list)
        reslut.append(msg_list)
        import copy
        msg_list2 = copy.copy(msg_list)
        # msg_list2=msg_list
        for k in all_results.keys():
            if k != 'area' and k != "value_4":
                print(msg_list2[k])
                try:
                    all_results[k] += int(msg_list2[k])
                except:
                    msg_list2[k] = msg_list2[k].split('.')[0]
                    all_results[k] += int(msg_list2[k])
    for k in all_results.keys():
        if k != 'area':
            all_results[k] = '%.2f' % (all_results[k] / 11)
    all_results = [all_results] + reslut

    print(all_results)
    for item in all_results:
        for k in item.keys():
            print(k)
            if k == "value_4":
                item[k] = '100%'
            if k != "area" and k != "value_3" and k != "value_4" and k != "value_9":
                item[k] = str(item[k]) + '%'
                # print(val)
                # print(item)
    print(all_results)
    msg = {"code": 0, "msg": 'success', "result": all_results}
    print(msg)
    return msg


def index_showall_export_get(starttime, endtime, type):  # noqa: E501
    """Index Showall

    Index Barone Chart # noqa: E501

    :param starttime: the starttime for user choose
    :type starttime: str
    :param endtime: the endtime for user choose
    :type endtime: str
    :param type: the user choose type
    :type type: str

    :rtype: HomeChart
    """

    if starttime == '':
        starttime = "2018-02-14 00:00:00"
    if endtime == '':
        endtime = "2018-02-15 00:00:00"
    # 投诉总表
    result_24 = complain_twenty_four_list_get(type='EMOS', starttime=starttime, endtime=endtime)
    result_8 = complain_eight_chart_get(type='投诉处理及时率', starttime=starttime, endtime=endtime)
    result_frist = complain_emos_first_chart_get(type='首次联系用户时长占比', starttime=starttime, endtime=endtime)

    # 装机总表
    starttime = "2018-02-14 00:00:00"
    endtime = "2018-02-15 00:00:00"
    result_install_24 = installed_twenty_four_list_get(type='宽带装机', starttime=starttime, endtime=endtime)
    result_install_8 = installed_eight_chart_get(type='880装机及时率', starttime=starttime, endtime=endtime)
    result_isntall_frist = installed_orders_chart_get(type='宽带装机_接单时长占比', starttime=starttime, endtime=endtime)
    reslut = []

    workbook_m = xlwt.Workbook(encoding='utf-8')
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
    # style1.font.bold = True
    style4.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
    style4.alignment.horz = xlwt.Alignment.HORZ_CENTER
    style4.num_format_str = '0.00%'

    # style2.font.bold = True
    # style2.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
    # style2.alignment.horz = xlwt.Alignment.HORZ_CENTER
    # 写excel表头
    # 设置单元格
    workbook_m = xlwt.Workbook(encoding='utf-8')
    xlsheet = workbook_m.add_sheet('高频小区', cell_overwrite_ok=True)
    xlsheet.write(0, 0, '起始时间:')
    xlsheet.write(0, 1, starttime)
    xlsheet.write(0, 2, '结束时间:')
    xlsheet.write(0, 3, endtime)
    xlsheet.write(1, 0, '所属区')
    xlsheet.write(1, 1, '投诉24小时及时率')
    xlsheet.write(1, 2, '投诉8小时及时率')
    xlsheet.write(1, 3, '首次联系用户及时率')
    xlsheet.write(1, 4, '平均处理时长')
    xlsheet.write(1, 5, '投诉回访满意度')
    xlsheet.write(1, 6, '万投比')
    xlsheet.write(1, 7, '24小时装机及时率')
    xlsheet.write(1, 8, '8小时装机及时率')
    xlsheet.write(1, 9, '首次联系用户及时率')
    xlsheet.write(1, 10, '平均联系用户时长')
    xlsheet.write(1, 11, '装机回访满意度')

    item = 2
    for i in range(len(result_24['result'])):
        if type == '':
            xlsheet.write(item, 0, result_24['result'][i]['area'])
            xlsheet.write(item, 1, result_24['result'][i]['timely'])
            xlsheet.write(item, 2, result_8['result'][i]['value'])

            xlsheet.write(item, 3, str(result_frist['result'][i]['inside']) + '%')
            xlsheet.write(item, 4, result_24['result'][i]['average'])
            xlsheet.write(item, 5, '100%')
            xlsheet.write(item, 6, result_24['result'][i]['investment'])
            xlsheet.write(item, 7, result_install_24['result'][i]['rate'])
            xlsheet.write(item, 8, str(result_install_8['result'][i]['value']) + '%')
            xlsheet.write(item, 9, str(result_isntall_frist['result'][i]['inside']) + '%')
            xlsheet.write(item, 10, result_install_24['result'][i]['ave'])
            xlsheet.write(item, 11, '100%')
            item = item + 1
        if type == result_24['result'][i]['area']:
            xlsheet.write(item, 0, result_24['result'][i]['area'])
            xlsheet.write(item, 1, result_24['result'][i]['timely'])
            xlsheet.write(item, 2, result_8['result'][i]['value'])

            xlsheet.write(item, 3, str(result_frist['result'][i]['inside']) + '%')
            xlsheet.write(item, 4, result_24['result'][i]['average'])
            xlsheet.write(item, 5, '100%')
            xlsheet.write(item, 6, result_24['result'][i]['investment'])
            xlsheet.write(item, 7, result_install_24['result'][i]['rate'])
            xlsheet.write(item, 8, str(result_install_8['result'][i]['value']) + '%')
            xlsheet.write(item, 9, str(result_isntall_frist['result'][i]['inside']) + '%')
            xlsheet.write(item, 10, result_install_24['result'][i]['ave'])
            xlsheet.write(item, 11, '100%')
    xlsname = '{}'.format(type) + '汇总表' + str(int(time.time()))
    workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
    url = 'down.caicool.cc:89/{}.xls'.format(xlsname)
    msg = {'code': 0, "msg": 'success', "url": url}
    print(msg)

    return msg


def home_notice_all_list_get():  # noqa: E501
    """Index Notice list

    index notice list # noqa: E501


    :rtype: NoticeList
    """
    try:
        yc_home = YChome()
        data1 = yc_home.desc_1_five
        data2 = yc_home.desc_2_five
        result1 = [{
            "id": item.id,
            "type": '通知通报' if item.type== 1 else '恶性事件',
            "title": item.title,
            "posttime": utc_timestamp_to_str(item.posttime)
        } for item in data1]
        result2 = [{
            "id": item.id,
            "type": '通知通报' if item.type== 1 else '恶性事件',
            "title": item.title,
            "posttime": utc_timestamp_to_str(item.posttime)
        } for item in data2]
        result = result1 + result2
        return {"code": 0, "msg": 'success', "result": result}
    except:
        return {"code": "-1", "msg": "error"}


def home_notice_get(id):  # noqa: E501
    """Notice desc

    notice list # noqa: E501

    :param id: community id
    :type id: str

    :rtype: NoticeLists2
    """
    try:
        yc_home = YChome()
        item = yc_home.desc_one(id)
        result = {
            "id": item.id,
            "desc": item.content,
            "title": item.title,
            "posttime": utc_timestamp_to_str(item.posttime)
        }
        return {"code": 0, "msg": 'success', "result": result}
    except Exception as e:
        print(e)
        return {"code": "-1", "msg": "error"}


def home_notice_list_get(page, size):  # noqa: E501
    """Notice list

    notice list # noqa: E501

    :param page: page number
    :type page: str
    :param size: Per page display quantity
    :type size: str

    :rtype: NoticeList2
    """
    # page = page if page != '' else '1'
    # size = size if size != '' else '10'
    size = '1' if size == '' else size
    page = '10' if page == '' else page
    try:
        data1 = YChome.select().where(YChome.type == 1)
        totle1=data1.count()
        data1=data1.paginate(int(page), int(size))
        data2 = YChome.select().where(YChome.type == 2)
        totle2=data2.count()
        data2=data2.paginate(int(page), int(size))
        totle = totle1 if totle1 > totle2 else totle2
        result1 = [{
            "id": item.id,
            "title": item.title,
            "posttime": utc_timestamp_to_str(item.posttime),
            "desc": item.content
        } for item in data1]
        result2 = [{
            "id": item.id,
            "title": item.title,
            "posttime": utc_timestamp_to_str(item.posttime),
            "desc": item.content
        } for item in data2]

        return {"code": 0, "msg": 'success',"totle":totle, "result": result1,"result2": result2}
    except Exception as e:
        print(e)
        return {"code": "-1", "msg": "error"}


def home_notice_post(body):  # noqa: E501
    """Notice desc

    notice list # noqa: E501

    :param body: data
    :type body: dict | bytes

    :rtype: Success
    """
    if connexion.request.is_json:
        body = NoticeData.from_dict(connexion.request.get_json())  # noqa: E501
    try:
        yc_home=YChome()
        yc_home.create(content=body.desc,
                       type=int(body.type),
                       posttime=int(time.time()),
                       title=body.title)
        return {"code": 0, "msg": 'success'}
    except Exception as e:
        print(e)
        return {"code": "-1", "msg": "error"}
