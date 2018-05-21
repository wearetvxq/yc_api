import connexion,json
from swagger_server.models.inline_response2002 import InlineResponse2002
from swagger_server.models.inline_response5001 import InlineResponse5001
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime
from swagger_server.db import YCformlist,database
from swagger_server.tool import paging,transpositionTime,timestamp_to_utc_strtime,utc_strtime_to_timestamp
import time


def formlist(page=1,size=10, area=None, pingtai=None, status=None, complaint=None, Timeout=None, start_time=None, end_time=None):
    """
    get the data of form_list
    get the data of form_list
    :param pageindex: the num of data
    :type pageindex: int
    :param area: the area of user choose
    :type area: str
    :param pingtai: the pingtai of user choose
    :type pingtai: str
    :param status: the status of user choose
    :type status: str
    :param complaint: the complaint_type of user choose
    :type complaint: str
    :param Timeout: the Timeout of user choose
    :type Timeout: str
    :param start_time: the start_time of user choose
    :type start_time: int
    :param end_time: the end_time of user choose
    :type end_time: int

    :rtype: InlineResponse2002
    """

    try:
        if (area != None) or (pingtai != None) or (status != None) or (complaint != None) or (Timeout != None) or (start_time != None) or (end_time != None):
            print('-------------', area, pingtai, status, complaint, Timeout, start_time, end_time)
            area_like = '%' + area + '%'

            data=YCformlist.select()
            if area!=None and area!='':
                data=data.where(YCformlist.area % area_like)
            if pingtai!=None and pingtai!='':
                data = data.where(YCformlist.pingtai == pingtai)
            if status!=None and status!='':
                data = data.where(YCformlist.status == status)
            if complaint!=None and complaint!='':
                data = data.where(YCformlist.complaint == complaint)
            if Timeout!=None and Timeout!='':
                data = data.where(YCformlist.Timeout == Timeout)
            if start_time!=None and start_time!='':
                start_time=utc_strtime_to_timestamp(start_time)
                data = data.where(int(YCformlist.start_time) > int(start_time))
            if end_time!=None and end_time!='':
                data = data.where(int(YCformlist.end_time)< int(end_time))
            rowCount = data.count()
            data=data.paginate(int(page), int(size))
            # data = YCformlist.select().where(
            #     (YCformlist.area % area_like) & (YCformlist.pingtai == pingtai) & (YCformlist.status == status) & (
            #     YCformlist.complaint == complaint) & (YCformlist.Timeout == Timeout) & (
            #     YCformlist.start_time > start_time) & (YCformlist.end_time < end_time)).paginate(int(page), int(size))
            # print(data)
            # rowCount = YCformlist.select().where(
            #     (YCformlist.area % area_like) & (YCformlist.pingtai == pingtai) & (YCformlist.status == status) & (
            #     YCformlist.complaint == complaint) & (YCformlist.Timeout == Timeout) & (
            #         YCformlist.start_time > start_time) & (YCformlist.start_time < start_time) & (
            #         YCformlist.end_time > end_time) & (YCformlist.end_time < end_time)).count()
        else:
            data = YCformlist.select().paginate(int(page), int(size))
            rowCount = YCformlist.select().count()
        result_list = [{'area': item.area, 'pingtai': item.pingtai, 'status': item.status, 'complaint': item.complaint,
                        'Timeout': item.Timeout, 'start_time': timestamp_to_utc_strtime(int(item.start_time)), 'end_time': timestamp_to_utc_strtime(int(item.end_time))} for item in
                       data]
        print(result_list)
        msg = {"rowCount": rowCount, "msg": "success", "result": result_list}

    except:
        msg={'code':-1,"msg":"Error"}



    return msg

