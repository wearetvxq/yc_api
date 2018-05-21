import connexion
import six

from swagger_server.models.home_chart import HomeChart  # noqa: E501
from swagger_server.models.success import Success  # noqa: E501
from swagger_server import util
from swagger_server.mysql_db import *
from swagger_server.export_report import *


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


def home_barone_get():  # noqa: E501
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


def home_lineone_get():  # noqa: E501
    """Index Lineone Chart
    Index Lineone Chart # noqa: E501
    :rtype: HomeChart
    """
    starttime = '2018-02-14 00:00:00'

    endtime = '2018-02-15 00:00:00'
    result=[]
    area_list = ['秭归', '枝江', '长阳', '远安', '宜都', '夷陵', '兴山', '五峰', '开发区', '当阳', '城区']
    for area in area_list:
        like='%'+area+'%'
        name=area
        value=YCcomplaints.select().where( (YCcomplaints.area % like) & (
            YCcomplaints.starttime >= utc_str_to_timestamp(starttime)) & (
                                        YCcomplaints.starttime <= utc_str_to_timestamp(endtime))).count()
        result.append({"name":name,"value":value})
    msg={"code":0,"msg":"success","result":result}
    return msg



def home_linetwo_get():  # noqa: E501
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
        value = YCcomplaints.select().where((YCcomplaints.area % like) & (YCcomplaints.type=='服务质量') &(
            YCcomplaints.starttime >= utc_str_to_timestamp(starttime)) & (
                                                YCcomplaints.starttime <= utc_str_to_timestamp(endtime))).count()
        result.append({"name": name, "value": value})
    msg = {"code": 0, "msg": "success", "result": result}
    return msg


def home_pan_get():  # noqa: E501
    """Index Pan Chart
    Index Pan Chart # noqa: E501
    :rtype: HomeChart
    """

    starttime='2018-02-14 00:00:00'

    endtime='2018-02-15 00:00:00'

    data = YCcomplaints.select().where((YCcomplaints.platform == 2)  & (
        YCcomplaints.starttime >= utc_str_to_timestamp(starttime)) & (
                                           YCcomplaints.starttime <= utc_str_to_timestamp(endtime)))
    acceptance = YCcomplaints.select().where((YCcomplaints.platform == 2) &  (
        YCcomplaints.starttime >= utc_str_to_timestamp(starttime)) & (
                                                 YCcomplaints.starttime <= utc_str_to_timestamp(
                                                     endtime))).count()
    avtime = 0
    for item in data:
        avtime = avtime + item.usetime
    print(avtime,acceptance)
    twentfour = data.where(YCcomplaints.usetime<= 24).count()




    try:
        av_time = avtime / acceptance
    except:
        av_time = 0
    result =[ {"name": '及时率',
            "value":'%.2f' %(twentfour* 100 / acceptance) ,
            },{"name": '平均处理时长',
            "value":'%.2f' % (av_time) ,
            }]

    msg = {"code": 0, "msg": "success", "result": result}
    return msg


