import connexion,os
import six

from swagger_server.models.keyword import Keyword  # noqa: E501
from swagger_server.models.success import Success  # noqa: E501
from swagger_server.models.upload import Upload  # noqa: E501
from swagger_server.models.upload_file import UploadFile  # noqa: E501
from swagger_server import util
from flask import request
from swagger_server.mysql_db import *
from swagger_server.importsql import *


def upload_delete(id):  # noqa: E501
    """User Upload

    User Upload # noqa: E501

    :param id: data
    :type id: int

    :rtype: Success
    """
    try:
        YCimport.delete().where(YCimport.id==int(id)).execute()
        msg={"code":0,"msg":"success"}
    except:
        msg={"code":-1,"msg":"Error"}
    return msg


def upload_file_post(files=None):  # noqa: E501
    """User Upload

    User Upload # noqa: E501

    :param files: file data
    :type files: werkzeug.datastructures.FileStorage

    :rtype: UploadFile
    """
    try:
        file = request.files['files']
        file.save(os.path.join('/var/www/downfile', file.filename))
        new_filepath = '/var/www/downfile/{}'.format(file.filename)
        msg = {'code': 0, 'msg': new_filepath}
    except:
        msg = {'code': -1, 'msg': 'Error'}
    return msg
#获取文件类型
def getfiletype(filetype):
    if filetype=='家宽投诉列表类':
        ft='1'
    if filetype=='家宽新装/移机列表类':
        ft='2'
    if filetype=='回访不满意工单类':
        ft='3'
    if filetype=='用户基础信息类':
        ft='4'
    return ft

def upload_filelist_get(starttime=None, endtime=None):  # noqa: E501
    """User Upload

    User Upload # noqa: E501

    :param starttime: starttime
    :type starttime: str
    :param endtime: endtime
    :type endtime: str

    :rtype: Keyword
    """
    data=YCimport.select()
    if starttime!='':
        data=data.where(YCimport.posttime>=utc_str_to_timestamp(starttime))
    if endtime!='':
        data=data.where(YCimport.posttime<=utc_str_to_timestamp(endtime))
    data=data.order_by(YCimport.posttime.desc())
    result=[{"id":item.id,"name":item.name,"time":utc_timestamp_to_str(item.posttime),"url":item.path.replace("/var/www/downfile","mail.itlaolang.com/downfile")} for item in data]
    msg={"code":0,"msg":"success","result":result}
    return msg


def upload_post(body):  # noqa: E501
    """User Upload

    User Upload # noqa: E501

    :param body: data
    :type body: dict | bytes

    :rtype: Success
    """
    if connexion.request.is_json:
        body = Upload.from_dict(connexion.request.get_json())  # noqa: E501
        try:
            msg = {'code': 0, 'msg': "success"}

            YCimport.insert(path='mail.itlaolang.com/downfile/{}'.format(body.name), type=body.type, name=body.name, posttime=int(time.time())).execute()

        except:
            msg={"code":-1,"msg":"Error"}
        total =YCimport.select().count()
        pid=YCimport.select()[total-1].id
        try:
            return msg
        finally:
            print ('------------','/var/www/downfile/{}'.format(body.name),getfiletype(body.type),pid)
            import_sql(file_path='/var/www/downfile/{}'.format(body.name),filetype=getfiletype(body.type),pid=pid)


