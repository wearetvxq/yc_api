#!/bin/bash
str=$"/n"
if [ ! -f "/home/pyweb/yc_api/python-flask-server/logfile.txt" ];then
    cd /home/pyweb/yc_api/python-flask-server 
    nohup python3 -m swagger_server > logfile.txt & echo $! > pidfile.txt & 
    echo -e "\n"
else
    cd /home/pyweb/yc_api/python-flask-server
    kill -9 `cat ./pidfile.txt`    #根据文件中记录的pid杀死进程  
    rm -rf logfile.txt    #删除运行日志
    rm -rf pidfile.txt    #删除pid记录文件，重启后重新生成
    nohup python3 -m swagger_server > logfile.txt & echo $! > pidfile.txt & 
fi
sstr=$(echo -e $str)
echo "$sstr"
