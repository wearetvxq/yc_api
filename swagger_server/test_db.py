from swagger_server.mysql_db import *

# data = YCadmin.get(YCadmin.id == 1)


data_one = YCinstalled.select(YCinstalled.accept)

for i in data_one:
    print(i.accept)