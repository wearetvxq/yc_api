import connexion
from swagger_server.models.inline_response200 import InlineResponse200
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime
from flask import request
import os

def import_data(files):
    """
    import_data
    import_data
    :param files: the file of name
    :type files: werkzeug.datastructures.FileStorage

    :rtype: InlineResponse200
    """
    try:
        file = request.files['files']
        file.save(os.path.join('/var/www/downfile', file.filename))
        new_filepath = '/var/www/downfile/{}'.format(file.filename)
        msg = {'code': 0, 'msg': new_filepath}
    except:
        msg = {'code': -1, 'msg': 'Error'}
    return msg
