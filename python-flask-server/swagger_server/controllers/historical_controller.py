import connexion
from swagger_server.models.inline_response2001 import InlineResponse2001
from swagger_server.models.inline_response5001 import InlineResponse5001
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime
from swagger_server.db import YChistorical
from swagger_server.tool import paging,timestamp_to_utc_strtime,utc_strtime_to_timestamp,timestamp_to_str
import time


def historical(page=1,size=10,type=None,status=None,time=None):
    """
    historical_data
    get the data of historical_data
    :param pageindex: the num of data
    :type pageindex: int
    :param type: the file_type of user choose
    :type type: str
    :param status: the status of user choose
    :type status: str
    :param time: the time of user choose
    :type time: int

    :rtype: InlineResponse2001
    """
    try:
        if (type != None) or (status != None) or (time != None):
            data=YChistorical.select()
            if type!=None and type!='':
                data=YChistorical.select().where(YChistorical.type == type)
            if status!=None and status!='':
                data = YChistorical.select().where(YChistorical.status == status)
            if time!=None and time!='':
                time=utc_strtime_to_timestamp(time)
                data = YChistorical.select().where(int(YChistorical.time) < int(time))
            rowCount=data.count()
            data=data.paginate(int(page), int(size))
            # data=YChistorical.select().where((YChistorical.type==type) & (YChistorical.status==status) & (YChistorical.time < time)).paginate(int(page), int(size))
            # rowCount=YChistorical.select().where((YChistorical.type==type) & (YChistorical.status==status) & (YChistorical.time <time)).count()
        else:
            data=YChistorical.select().paginate(int(page), int(size))
            rowCount=YChistorical.select().count()
        result_list=[{'ID': item.id, 'type': item.type,'down_num':item.down_num,'status':item.status,'time':timestamp_to_str(int(item.time)/1000)} for item in data]
        msg = {"rowCount": rowCount,"msg": "success", "result":result_list}

    except:
        msg = {"code": -1, "msg": "system error"}
    return msg
