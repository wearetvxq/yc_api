import connexion,time
from swagger_server.models.inline_response200 import InlineResponse200
from swagger_server.models.keyword import Keyword
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime
from swagger_server.tool import makefile
from swagger_server.db import YCimport_file,YCdown_file,YChistorical,YCformlist
from swagger_server.tool import read_file


def make_file(keyword):
    """
    make the file
    make the file
    :param keyword: the key of file
    :type keyword: dict | bytes

    :rtype: InlineResponse200
    """
    if connexion.request.is_json:
        keyword = Keyword.from_dict(connexion.request.get_json())
        try:
            id=keyword.id
            filetype = keyword.filetype
            #---------------------------------判断是否生成
            data1=YChistorical.select().where(YChistorical.id==id)
            try:
                data_id=YCformlist.select()
                insert_id=data_id[-1].id+1
            except:
                insert_id=1
            #-------------另启程序启动---------------
            # if data1[0].status!='已生成':
            #     #--------------------往数据库读数据
            #     list=read_file(file_path=data1[0].filepath)
            #     for msg in list:
            #         print(msg)
            #         YCformlist.insert(id=insert_id,pingtai=msg[0],area=msg[1],status=msg[3],complaint=msg[2],Timeout=msg[4],start_time=int(str(int(msg[5]))[0:10]),end_time=int(str(int(msg[6]))[0:10]),time_24_8=int(msg[7]),manyi=msg[8]).execute()
            #     YChistorical.update(status='已生成').where(YChistorical.id == data1[0].id).execute()
            #     print('----------haha')
    #------------------------------------------------------
            #print(data1[0].type,data1[0].id)
            YChistorical.update(status='已生成').where(YChistorical.id == data1[0].id).execute()
            new_path=makefile(filetype=data1[0].type,id=data1[0].id)
            #print(new_path)
            try:
                data_1=YCdown_file.select().where(YCdown_file.pid==data1[0].id)
                #print(data_1[0].pid)
            except:
                YCdown_file.insert(down_path=new_path, filetype=filetype, down_time=int(time.time())*1000, id=1,pid=data1[0].id).execute()
                #print('-------------')

            msg = {"code": 0, "msg": "success"}
            #print(msg)
        except:
            msg = {"code": -1, "msg": 'Error,try again'}
    return msg
