import connexion
from swagger_server.models.inline_response200 import InlineResponse200
from swagger_server.models.keyword import Keyword
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime
from swagger_server.db import YCdown_file,YChistorical



def down_file(sort):
    """
    down the file
    down the file
    :param sort: the msg of down_file
    :type sort: dict | bytes

    :rtype: InlineResponse200
    """
    if connexion.request.is_json:
        sort = Keyword.from_dict(connexion.request.get_json())
        try:
            id = sort.id
            result=YCdown_file.select().where(YCdown_file.pid == id)
            data1=YChistorical.select().where(YChistorical.id==id)
            YChistorical.update(down_num=int(data1[0].down_num)+1).where(YChistorical.id==data1[0].id).execute()
            msg = {"code": 0, "msg": result[0].down_path}
        except:
            msg ={"code" :-1, "msg": "system error"}

    return msg
