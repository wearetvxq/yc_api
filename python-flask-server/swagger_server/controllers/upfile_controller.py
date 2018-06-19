import connexion
from swagger_server.models.inline_response200 import InlineResponse200
from swagger_server.models.keyword1 import Keyword1
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime
from swagger_server.db import YChistorical,YCformlist,YCdown_file
from swagger_server.tool import read_file,makefile
import time
def up_data(keyword):
    """
    up_data
    up_data
    :param keyword: the msg of down_file
    :type keyword: dict | bytes

    :rtype: InlineResponse200
    """
    if connexion.request.is_json:
        keyword = Keyword1.from_dict(connexion.request.get_json())
        try:
            filetype = keyword.filetype
            filepath = keyword.filepath
            try:
                data = YChistorical.select().count()
                test_data = YChistorical.select()
                #print(int(test_data[-1].id) + 1)
                insert_id = int(test_data[data-1].id) + 1
            except:
                insert_id=1
            try:
                YChistorical.insert(id=insert_id, type=filetype, down_num=0, status='读取中', time=str(int(time.time()))+'000',filepath=filepath).execute()
            except:
                msg = {'code': -1, "msg": "Error"}
#------------------------------------数据库写入
            data1 = YChistorical.select().where(YChistorical.id == insert_id)
            if data1[0].status!='已生成':
                #--------------------往数据库读数据
                #print('hahahahahahhaa')
                list=read_file(file_path=data1[0].filepath)
                for msg1 in list:
                    YCformlist.insert(id=insert_id,pingtai=msg1[0],area=msg1[1],status=msg1[3],complaint=msg1[2],Timeout=msg1[4],start_time=str(msg1[5]),end_time=str(msg1[6]),time_24_8=int(msg1[7]),manyi=msg1[8]).execute()
                YChistorical.update(status='已生成').where(YChistorical.id == data1[0].id).execute()
                #print('----------haha')
            file_data=YChistorical.select().where(id==insert_id)
            new_path=makefile(filetype=filetype,id=insert_id)

            try:
                data_1=YCdown_file.select().where(YCdown_file.pid==insert_id)
                print(data_1[0].pid)
            except:
                YCdown_file.insert(down_path=new_path, filetype=filetype, down_time=int(time.time())*1000, id=1,pid=insert_id).execute()
                #print('-------------')
            msg = {'code': 0, "msg": new_path}
        except:
            YChistorical.delete().where(YChistorical.id==insert_id)
            msg = {'code': -1, "msg": "Error"}
    return msg
