
import hashlib, base64, calendar, time
from datetime import datetime
from swagger_server.db import *



#加密方法
def encryption(data):
    encodestr = base64.b64encode(data.encode(encoding="utf-8"))
    mstr = encodestr.decode('UTF-8')[::-1].upper()
    return hashlib.md5(mstr.encode('UTF-8')).hexdigest().upper()