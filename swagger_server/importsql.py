import peewee
#-*-coding:utf-8-*-
#cmx and cd

import xlwt,xlrd,re,time
from xlwt import *
from xlrd import *
from swagger_server.mysql_db import *
from swagger_server.tool import *
def utc_str_to_timestamp(dt):
    timeArray = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
    # 转换成时间戳
    timestamp = time.mktime(timeArray)
    return (int(timestamp))


def utc_timestamp_to_str(dt):
    # 时间戳变成字符串
    timeArray = time.localtime(dt)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return otherStyleTime




#----------------------装机日报的工具代码---------------------------
#地址的匹配(24小时报表)
def find_area(text, text1):
    area_list = ['当阳', '五峰', '兴山', '夷陵', '宜都', '远安', '长阳', '枝江', '秭归', '宜昌开发区', '宜昌城区', '西陵', '猇亭', '伍家岗']
    if text!='':
        area=text.replace("工作站",'')
    else:
        try:
            area = re.findall('宜昌.*?[市|县|区]', text1)[0][2:]
        except:
            area = '宜昌开发区'
    return (area)
#判断是否完成(24小时报表)
def get_status(st):
    if st!='':
        stat='完成'
    else:
        stat='未完成'
    return stat
#判断是否超时----------------------(24小时报表)
def get_timeout(stime,etime,area):
    wherelist=['新农村','乡镇','行政村','一般农村','自然村']
    if etime!='':
        try:
            timeout = '否'
            if area in wherelist:
                if int(utc_str_to_timestamp(etime) - utc_str_to_timestamp(stime)) > (36 * 60 * 60):
                    timeout = '是'
            else:
                if int(utc_str_to_timestamp(etime) - utc_str_to_timestamp(stime)) > (24 * 60 * 60):
                    timeout = '是'
        except:
            timeout = '否'
    else:
        timeout = '是'
    return timeout
#判断是否超时----------------------(8小时报表)
def get_timeout_8(stime,etime,area):
    wherelist=['新农村','乡镇','行政村','一般农村','自然村']
    try:
        timeout = '否'
        if area in wherelist:
                if int(utc_str_to_timestamp(etime) - utc_str_to_timestamp(stime)) > (36 * 60 * 60):
                    timeout = '是'
        else:
                if int(utc_str_to_timestamp(etime) - utc_str_to_timestamp(stime)) > (24 * 60 * 60):
                    timeout = '是'
    except:
        timeout='否'
    return timeout

#判断是否压单(24小时报表)
def downdan(stime):
    if int(stime[5:7])!=int(utc_timestamp_to_str(int(time.time()))[5:7]):
        dd=1
    else:
        dd=0
    return dd
#获取完成单的耗时(24小时报表)
def time_for_end(stime,etime):
    if etime=='':
        lt=0
    if etime!="":
        lt=((utc_str_to_timestamp(etime)-utc_str_to_timestamp(stime))/60)/60
    return lt
#返回平均装机时长(24小时报表)
def av_time(all_time,other):
    try:
        at=all_time/other
    except:
        at=0.00
    return at
#判断是否超时----------------------(农普)
def get_timeout_np(stime,etime):
    if etime!='':
        if int(utc_str_to_timestamp(etime) - utc_str_to_timestamp(stime)) > (24 * 60 * 60 * 7):
            timeout = '是'
        else:
            timeout = '否'
    else:
            timeout = '是'

    return timeout

def find_area1(text,text1):
    if text!='':
        try:
            text = text.replace("宜昌", '')
            if text.find('开发区') != -1:
                area = '开发区'
            else:
                area = text[0:2]
        except:
            area='开发区'
    else:
        try:
            area = re.findall('宜昌.*?[市|县|区]', text1)[0][3:-2]
        except:
            area='开发区'
    if area=='通城':
        area='宜都'
    return area

#地址的匹配（一键保障）
def find_area2(text):
    if text!='':
        try:
            text = text.replace("支撑服务中心", '')
            if text=='东山' or text=='伍家' :
                area = '开发区'
            else:
                area = text
        except:
            area='开发区'
    return area

#运行中的工单是否超过24小时(EMOS)
def get_timeout1(status,stime,etime):
    if etime!='':
        stime = str(xlrd.xldate_as_datetime(stime, 0))
        etime = str(xlrd.xldate_as_datetime(etime, 0))
        if status == '运行中':
            if (utc_str_to_timestamp(etime) - utc_str_to_timestamp(stime)) > (24 * 60 * 60):
                tt = '是'
            else:
                tt = '否'
        if status == '归档':
            if (utc_str_to_timestamp(etime) - utc_str_to_timestamp(stime)) > (24 * 60 * 60):
                tt = '是'
            else:
                tt = '否'
    else:
        tt='是'
    return tt

#运行中的工单是否超过24小时(一键报障)
def get_timeout2(status,stime,etime):
    if etime!='':
        stime = str(stime)
        etime = str(etime)
        if status != '归档':
            if (utc_str_to_timestamp(etime) - utc_str_to_timestamp(stime)) > (24 * 60 * 60):
                tt = '是'
            else:
                tt = '否'
        if status == '归档':
            if (utc_str_to_timestamp(etime) - utc_str_to_timestamp(stime)) > (24 * 60 * 60):
                tt = '是'
            else:
                tt = '否'
    else:
        tt="是"
    return tt
#获取操作时长（EMOS）
def time_for_end1(stime,etime):
    stime = str(xlrd.xldate_as_datetime(stime, 0))
    etime = str(xlrd.xldate_as_datetime(etime, 0))
    tn=(utc_str_to_timestamp(etime)-utc_str_to_timestamp(stime))/(60*60)
    return tn

#获取操作时长（一键保障）
def time_for_end2(stime,etime):
    if etime=='':
        tn=0
    else:
        stime = str(stime)
        etime = str(etime)
        tn = (utc_str_to_timestamp(etime) - utc_str_to_timestamp(stime)) / (60 * 60)
    return tn
#装机报表的生成
def get_type(stat):
    if stat=='移机装':
        st=2
    if stat=='宽带装机':
        st=1
    if stat=='和TV单独安装':
       st=3
    if stat=='IMS单独安装':
        st=4
    return st



def import_sql(file_path,filetype,pid):
    if filetype=='2':
        workbook_r = xlrd.open_workbook(file_path)
        msg_list = []
        msg_list1 = []
        for name in workbook_r.sheet_names():
            sheet = workbook_r.sheet_by_name(name)
            for x in range(1, sheet.nrows):

                    try:
                        msg = sheet.row_values(x)
                        # 这是时间段之内受理工单数据
                        if msg[9] != 'order_status_6':
                            result = [find_area(msg[1], msg[11]), get_status(msg[15]),
                                      get_timeout(msg[12], msg[15], msg[19]), downdan(msg[12]),
                                      time_for_end(msg[12], msg[15])]

                            if msg[15] == '':
                                endtime = 0
                            else:
                                endtime = utc_str_to_timestamp(msg[15])
                            YCinstalled.insert(type=get_type(msg[3]), area=result[0], status='order_status_5', timeout=result[2],
                                               account=msg[5], grid=msg[2], orderid=msg[4], service=msg[6],
                                               phone=msg[7], attach=msg[8], transfer=msg[10], pboos=msg[11],
                                               accept=utc_str_to_timestamp(msg[12]),
                                               orders=utc_str_to_timestamp(msg[13]), receipt=msg[14], confirm=endtime,
                                               pid=pid, areaType=msg[-1], posttime=int(time.time())).execute()
                            print('-----------order_status_5',x)
                        if msg[9] == 'order_status_6':
                            result = [find_area(msg[1], msg[11]), get_status(msg[15]),
                                      get_timeout(msg[12], msg[15], msg[19]), downdan(msg[12]),
                                      time_for_end(msg[12], msg[15])]

                            if msg[15] == '':
                                endtime = 0
                            else:
                                endtime = utc_str_to_timestamp(msg[15])
                            if msg[13] == '':
                                orders = 0
                            else:
                                orders = utc_str_to_timestamp(msg[13])
                            YCinstalled.insert(type=get_type(msg[3]), area=result[0], status=msg[9], timeout=result[2],
                                               account=msg[5], grid=msg[2], orderid=msg[4], service=msg[6],
                                               phone=msg[7], attach=msg[8], transfer=msg[10], pboos=msg[11],
                                               accept=utc_str_to_timestamp(msg[12]),
                                               orders=orders, receipt=msg[14], confirm=endtime,
                                               pid=pid, areaType=msg[-1], posttime=int(time.time())).execute()
                            print('-----------order_status_6',x)
                    except:
                        print(x)
    if filetype=='1':
        workbook_r = xlrd.open_workbook(file_path)
        msg_list = []
        for name in workbook_r.sheet_names():
            if name=='EMOS':
                sheet = workbook_r.sheet_by_name('EMOS')
                for x in range(1, sheet.nrows):
                    msg = sheet.row_values(x)
                    #这是接受的工单量
                    if msg[8] != '待回访' and msg[18]!='' :
                        result = [find_area1(msg[-1], msg[2]), msg[8], get_timeout1(msg[8], msg[16], msg[18]),
                                  time_for_end1(msg[16], msg[18]), msg[2]]#地区，状态，超时（包括运行中，归档），投诉时长,投诉地址
                        YCcomplaints.insert(area=result[0],platform=2,status=result[1],timeout=result[2],starttime=str(utc_str_to_timestamp(str(xlrd.xldate_as_datetime(msg[16],0)))),endtime=str(utc_str_to_timestamp(str(xlrd.xldate_as_datetime(msg[18],0)))),pid=pid,usetime='%.2f' % result[-2],contacts=msg[4],phone=msg[12],fristtime=str(utc_str_to_timestamp(str(xlrd.xldate_as_datetime(msg[66],0)))),serial=msg[1],t2endtime=str(utc_str_to_timestamp(str(xlrd.xldate_as_datetime(msg[19],0)))),manyi=getmanyi(msg[15]),tsaddress=result[-1],posttime=int(time.time())).execute()

        for name in workbook_r.sheet_names():
            if name=='一键报障':
                sheet = workbook_r.sheet_by_name('一键报障')
                for x in range(1, sheet.nrows):

                    msg = sheet.row_values(x)
                    #这是接受的工单量
                    result = [find_area2(msg[8]), msg[11], get_timeout2(msg[11], msg[22], msg[25]),
                              time_for_end2(msg[22], msg[25]), msg[10]]
                    #地区，状态，超时（包括运行中，归档），投诉时长,投诉地址
                    print(msg[0],msg[25],msg[22])
                    if msg[25]=='':
                        msg[25]=0
                    else:
                        msg[25]=utc_str_to_timestamp(str(msg[25]))

                    if msg[24]=='':
                        msg[24]=0
                    else:
                        msg[24]=utc_str_to_timestamp(str(msg[24]))

                    YCcomplaints.insert(area=result[0],platform=1,status=result[1],timeout=result[2],starttime=utc_str_to_timestamp(str(msg[22])),endtime=msg[25],pid=pid,posttime=int(time.time()),usetime=result[-2],contacts=msg[26],phone=msg[15],fristtime=msg[24],serial=msg[1],manyi=2,tsaddress=result[-1]).execute()
        for name in workbook_r.sheet_names():
            if name=='CRM':
                sheet = workbook_r.sheet_by_name('CRM')
                for x in range(1, sheet.nrows):

                    msg = sheet.row_values(x)

                    #这是接受的工单量
                    result = [msg[0], msg[7], msg[8], 0.00, msg[3]]  #地区，状态，超时（包括运行中，归档），投诉时长,投诉地址
                    starttime = int(utc_str_to_timestamp(str(xlrd.xldate_as_datetime(msg[1], 0))))
                    if msg[6]!='':
                        endtime = int(
                            utc_str_to_timestamp(str(xlrd.xldate_as_datetime(msg[6], 0))))
                    else:
                        endtime=starttime
                    print(starttime,endtime,x)
                    YCcomplaints.insert(area=result[0],platform=3,status=result[1],timeout=result[2],starttime=starttime,endtime=endtime,pid=pid,manyi=2,posttime=int(time.time()),usetime=result[-2],tsaddress=result[-1]).execute()
#import_sql('/root/桌面/4月份工单EMOS.xlsx','1',10)
#import_sql('/root/桌面/装机.xlsx','2',1)
