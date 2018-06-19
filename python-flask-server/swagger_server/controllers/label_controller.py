import connexion
import six

from swagger_server.models.dict_list import DictList  # noqa: E501
from swagger_server.models.success import Success  # noqa: E501
from swagger_server import util
from swagger_server.mysql_db import *
from swagger_server.infoexport import *
from ..tool import *
from flask import request
from flask import request


def label_business_get():  # noqa: E501
    """business type

    business type # noqa: E501


    :rtype: DictList
    """
    try:
        data = YCbusiness.select()
        result_list = [{'id': item.sort,
                        'name': item.name,
                        } for item in data]
        msg = {"code": 0, "msg": "success", "result": result_list}
    except:
        msg = {"code": -1, "msg": "error"}
    return msg


def label_people_get(id=None):  # noqa: E501
    """Installed Dimensions Staff Dictionary Table

    Installed Dimensions Staff Dictionary Table # noqa: E501

    :param id: Workstation ID, if it is empty means to get all the dimensioning staff
    :type id: str

    :rtype: DictList
    """
    try:
        if id != None and id != '':

            data = YCpeople.select().where(YCpeople.pid == id)
        else:
            data = YCpeople.select()
        result_list = [{'id': item.sort,
                        'name': item.name,
                        } for item in data]
        msg = {"code": 0, "msg": "success", "result": result_list}

    except:
        msg = {"code": -1, "msg": "error"}
    return msg


def label_terminal_model_get(id=None):  # noqa: E501
    """terminal model

    terminal model # noqa: E501

    :param id: terminal type ID, if it is empty means to get all the dimensioning staff
    :type id: str

    :rtype: DictList
    """
    try:
        if id != None and id != '':
            data = YCterminal_model.select().where(YCterminal_model.pid == id)
        else:
            data = YCterminal_model.select()
        result_list = [{'id': item.sort,
                        'name': item.name,
                        } for item in data]
        msg = {"code": 0, "msg": "success", "result": result_list}

    except Exception as e:
        print (e)
        msg = {"code": -1, "msg": "error"}
    return msg


def label_terminal_type_get():  # noqa: E501
    """terminal type

    terminal type # noqa: E501


    :rtype: DictList
    """
    try:
        data = YCterminal_type.select()
        result_list = [{'id': item.sort,
                        'name': item.name,
                        } for item in data]
        msg = {"code": 0, "msg": "success", "result": result_list}
    except:
        msg = {"code": -1, "msg": "error"}
    return msg


def label_work_get():  # noqa: E501
    """Workstation dictionary interface

    Workstation dictionary interface # noqa: E501


    :rtype: DictList
    """
    try:
        data = YCwork.select()[1:]
        result_list = [{'id': item.sort,
                        'name': item.name,
                        } for item in data]
        msg = {"code": 0, "msg": "success", "result": result_list}
    except:
        msg = {"code": -1, "msg": "error"}
    return msg
