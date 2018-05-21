import connexion
import six

from swagger_server.models.body import Body  # noqa: E501
from swagger_server.models.success import Success  # noqa: E501
from swagger_server.tool import encryption
from swagger_server.mysql_db import *
from swagger_server import util


def login_post(body):  # noqa: E501
    """User Login

    System User Login # noqa: E501

    :param body: data
    :type body: dict | bytes

    :rtype: Success
    """
    if connexion.request.is_json:
        body = Body.from_dict(connexion.request.get_json())
        try:
            encrypStr = body.username + body.password
            passwd = encryption(encrypStr)
            data = YCadmin.select().where(YCadmin.username == body.username)
            if data[0].passwd == passwd:
                msg = {"code": 0, "msg": "success"}
            else:
                msg = {"code": -1, "msg": "wrong password"}
        except:
            msg = {"code": -2, "msg": "User does not exist"}

    return msg
