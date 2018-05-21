#-*-coding:utf-8-*-
#cmx and cd

import xlwt,xlrd,re,time
from xlwt import *
from xlrd import *
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

#获取装机类型
def getinstalledtype(id):
    if id ==1:
        it='宽带装机'
    if id ==3:
        it='和TV'
    if id ==2:
        it='移装机'
    if id ==4:
        it='IMS装机'
    return it


#----------------------装机日报的工具代码---------------------------
#地址的匹配(24小时报表)
def find_area(text, text1):
    area_list = ['当阳', '五峰', '兴山', '夷陵', '宜都', '远安', '长阳', '枝江', '秭归', '宜昌开发区', '宜昌城区', '西陵', '猇亭', '伍家岗']
    try:
        try:
            if text.find('工作站') != -1:
                area = text.replace('工作站', '')
        except:
            try:
                area = re.findall('宜昌.*?[市|县|区]', text1)[0][2:]
            except:
                area = '宜昌开发区'
    except:
        area = '宜昌开发区'
    return (area)
#判断是否完成(24小时报表)
def get_status(st,starttime,endtime):
    if st!='':
        stat='完成'
    else:
        stat='未完成'
    return stat
#判断是否超时----------------------(24小时报表)
def get_timeout(stime,etime,area):
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



#---------------------------------投诉日报的工具代码------------------------------

#地址的匹配（EMOS）
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
def get_timeout1_8(status,stime,etime):
    if etime!='':
        stime = str(xlrd.xldate_as_datetime(stime, 0))
        etime = str(xlrd.xldate_as_datetime(etime, 0))
        if status == '运行中':
            if (utc_str_to_timestamp(etime) - utc_str_to_timestamp(stime)) > (20 * 60 * 60):
                tt = '是'
            else:
                tt = '否'
        if status == '归档':
            if (utc_str_to_timestamp(etime) - utc_str_to_timestamp(stime)) > (20 * 60 * 60):
                tt = '是'
            else:
                tt = '否'
    else:
        tt='是'
    return tt

#运行中的工单是否超过24小时(一键报障)
def get_timeout2(status,stime,etime):
    stime = str(stime)
    etime = str(etime)
    if status!='归档':
        if (utc_str_to_timestamp(etime)-utc_str_to_timestamp(stime))>(24*60*60):
            tt='是'
        else:
            tt='否'
    if status=='归档':
        if (utc_str_to_timestamp(etime)-utc_str_to_timestamp(stime))>(24*60*60):
            tt='是'
        else:
            tt='否'
    return tt
def get_timeout2_8(status,stime,etime):
    stime = str(stime)
    etime = str(etime)
    if status!='归档':
        if (utc_str_to_timestamp(etime)-utc_str_to_timestamp(stime))>(20*60*60):
            tt='是'
        else:
            tt='否'
    if status=='归档':
        if (utc_str_to_timestamp(etime)-utc_str_to_timestamp(stime))>(20*60*60):
            tt='是'
        else:
            tt='否'
    return tt
#获取操作时长（EMOS）
def time_for_end1(stime,etime):
    stime = str(xlrd.xldate_as_datetime(stime, 0))
    etime = str(xlrd.xldate_as_datetime(etime, 0))
    tn=(utc_str_to_timestamp(etime)-utc_str_to_timestamp(stime))/(60*60)
    return tn

#获取操作时长（一键保障）
def time_for_end2(stime,etime):
    stime = str(stime)
    etime = str(etime)
    tn=(utc_str_to_timestamp(etime)-utc_str_to_timestamp(stime))/(60*60)
    return tn

#装机报表的生成
def make_file(file_path,type,starttime,endtime,choose_type):
    area_list = ['当阳市', '五峰市', '兴山县', '夷陵区', '宜都市', '远安县', '长阳市', '枝江市', '秭归市', '宜昌开发区', '宜昌城区', '西陵区', '猇亭区', '伍家岗区']
    workbook_r = xlrd.open_workbook(file_path)
    msg_list=[]
    msg_list1=[]
    for name in workbook_r.sheet_names():
        sheet = workbook_r.sheet_by_name(name)
        if type=='装机24小时报表':

            if choose_type == '全量工单':
                for x in range(1, sheet.nrows):
                    try:
                        msg = sheet.row_values(x)
                        #这是之间段之内完成的工单数据
                        if msg[9] != 'order_status_6' and utc_str_to_timestamp(msg[15]) >= utc_str_to_timestamp(
                                starttime) and utc_str_to_timestamp(msg[15]) <= utc_str_to_timestamp(endtime) \
                                and msg[19] != '普服小区' and msg[19] != '普遍服务':
                            finshed=[find_area(msg[1], msg[11])]
                            msg_list1.append(finshed)
                        #这是时间段之内受理工单数据
                        if msg[9] != 'order_status_6' and utc_str_to_timestamp(msg[12]) >= utc_str_to_timestamp(
                                starttime) and utc_str_to_timestamp(msg[12]) <= utc_str_to_timestamp(endtime) \
                                and msg[19] != '普服小区' and msg[19] != '普遍服务':
                            result = [find_area(msg[1], msg[11]), get_status(msg[15],starttime,endtime),
                                      get_timeout(msg[12], msg[15], msg[19]), downdan(msg[12]),
                                      time_for_end(msg[12], msg[15])]
                            # print(result)
                            msg_list.append(result)

                    except:
                        pass
                # print(len([x for x in msg_list if x[0] == '枝江']))
                # print(len([x for x in msg_list if x[0] == '枝江' and x[1]=='完成']))
                # print(len([x for x in msg_list if x[0] == '枝江' and x[1]=='完成' and x[2]=='是']))
                # print(len([x for x in msg_list if x[0] == '枝江' and x[1]=='未完成' and x[2]=='是']))
                # print(len([x for x in msg_list if x[0] == '枝江' and x[1]=='未完成' and x[3]==1]))
                all_time = 0
                print(len([x for x in msg_list if x[0] == '夷陵' and x[1] == '完成']))
                for i in [x for x in msg_list if x[0] == '夷陵' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                # print(all_time)
                # print(av_time(all_time,len([x for x in msg_list if x[0] == '夷陵' and x[1] == '完成'])))
                print('%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '完成']))))

                workbook_m = xlwt.Workbook(encoding='utf-8')
                xlsheet = workbook_m.add_sheet('24小时装机日报（不含农普）', cell_overwrite_ok=True)
                # 格式1 （有自动换行）
                style1 = xlwt.easyxf('pattern: pattern solid, fore_colour white')
                style1.font.height = 200
                style1.font.name = u'文泉驿点阵正黑'
                style1.font.colour_index = 0
                style1.borders.left = xlwt.Borders.THIN
                style1.borders.right = xlwt.Borders.THIN
                style1.borders.top = xlwt.Borders.THIN
                style1.borders.bottom = xlwt.Borders.THIN
                # style1.font.bold = True
                style1.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
                style1.alignment.horz = xlwt.Alignment.HORZ_CENTER

                # 格式2  （没有自动换行）
                style2 = xlwt.easyxf('pattern: pattern solid, fore_colour white')
                style2.font.height = 200
                style2.font.name = u'文泉驿点阵正黑'
                style2.font.colour_index = 0
                style2.borders.left = xlwt.Borders.THIN
                style2.borders.right = xlwt.Borders.THIN
                style2.borders.top = xlwt.Borders.THIN
                style2.borders.bottom = xlwt.Borders.THIN

                # style2.font.bold = True
                # style2.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
                # style2.alignment.horz = xlwt.Alignment.HORZ_CENTER

                # 格式3 黄色背景色

                style3 = xlwt.easyxf('pattern: pattern solid, fore_colour yellow')
                style3.font.height = 200
                style3.font.name = u'文泉驿点阵正黑'
                style3.font.colour_index = 0
                # style3.borders.left = xlwt.Borders.THIN
                # style3.borders.right = xlwt.Borders.THIN
                # style3.borders.top = xlwt.Borders.THIN
                # style3.borders.bottom = xlwt.Borders.THIN

                # style4 格式4 0.00%

                style4 = xlwt.easyxf('pattern: pattern solid, fore_colour white')
                style4.font.height = 200
                style4.font.name = u'文泉驿点阵正黑'
                style4.font.colour_index = 0
                style4.borders.left = xlwt.Borders.THIN
                style4.borders.right = xlwt.Borders.THIN
                style4.borders.top = xlwt.Borders.THIN
                style4.borders.bottom = xlwt.Borders.THIN
                # style1.font.bold = True
                style4.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
                style4.alignment.horz = xlwt.Alignment.HORZ_CENTER
                style4.num_format_str = '0.00%'

                # style2.font.bold = True
                # style2.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
                # style2.alignment.horz = xlwt.Alignment.HORZ_CENTER
                # 写excel表头
                # 设置单元格
                xlsheet.write(0, 0, '起始时间：', style3)
                xlsheet.write(0, 1, starttime, style1)
                xlsheet.write(0, 3, '截止时间：', style3)
                xlsheet.write(0, 4, endtime, style1)
                xlsheet.write(0, 6, '工单类型：', style3)
                xlsheet.write(0, 7, choose_type, style3)
                xlsheet.write(1, 0, '区县（区域属性）', style1)
                xlsheet.write(1, 1, '当日受理工单量', style1)
                xlsheet.write(1, 2, '当日装机完成量', style1)
                xlsheet.write(1, 3, '已装超时量', style1)
                xlsheet.write(1, 4, '未装超时量', style1)
                xlsheet.write(1, 5, '压单量', style1)
                xlsheet.write(1, 6, '装机及时率', style1)
                xlsheet.write(1, 7, '平均装机时长（小时）', style1)
                xlsheet.write(2, 0, '备注', style1)
                xlsheet.write(2, 1, '本月受理的所有单子', style1)
                xlsheet.write(2, 2, '本月完成的所有单子', style1)
                xlsheet.write(2, 3, '已完成的超时工单（城区24小时、乡镇36小时）', style1)
                xlsheet.write(2, 4, '未完成的超时工单', style1)
                xlsheet.write(2, 5, '本月之前受理，且还没完成', style1)
                xlsheet.write(2, 6, '(受理工单量-已装超时量-未装超时量-本月以前压单量)/受理工单量', style1)
                xlsheet.write(2, 7, '已完成单子共花费时间/完成单子数', style1)
                xlsheet.write(3, 0, '城区', style1)
                xlsheet.write(3, 1, len([x for x in msg_list if x[0] == '宜昌城区']), style1)
                xlsheet.write(3, 2, len([x for x in msg_list1 if x[0] == '宜昌城区']), style1)
                xlsheet.write(3, 3, len([x for x in msg_list if x[0] == '宜昌城区' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(3, 4, len([x for x in msg_list if x[0] == '宜昌城区' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(3, 5, len([x for x in msg_list if x[0] == '宜昌城区' and x[1] == '未完成' and x[3] == 1]),
                              style1)
                xlsheet.write(3, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(4, 4, 4, 4, 4)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '宜昌城区' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(3, 7, '%.2f' % (
                    av_time(all_time, len([x for x in msg_list if x[0] == '宜昌城区' and x[1] == '完成']))), style1)

                xlsheet.write(4, 0, '当阳', style1)
                xlsheet.write(4, 1, len([x for x in msg_list if x[0] == '当阳']), style1)
                xlsheet.write(4, 2, len([x for x in msg_list1 if x[0] == '当阳' ]), style1)
                xlsheet.write(4, 3, len([x for x in msg_list if x[0] == '当阳' and x[1] == '完成' and x[2] == '是']), style1)
                xlsheet.write(4, 4, len([x for x in msg_list if x[0] == '当阳' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(4, 5, len([x for x in msg_list if x[0] == '当阳' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(4, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(5, 5, 5, 5, 5)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '当阳' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(4, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '当阳' and x[1] == '完成']))),
                              style1)
                xlsheet.write(5, 0, '开发区', style1)
                xlsheet.write(5, 1, len([x for x in msg_list if x[0] == '宜昌开发区']), style1)
                xlsheet.write(5, 2, len([x for x in msg_list1 if x[0] == '宜昌开发区']), style1)
                xlsheet.write(5, 3, len([x for x in msg_list if x[0] == '宜昌开发区' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(5, 4, len([x for x in msg_list if x[0] == '宜昌开发区' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(5, 5, len([x for x in msg_list if x[0] == '宜昌开发区' and x[1] == '未完成' and x[3] == 1]),
                              style1)
                xlsheet.write(5, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(6, 6, 6, 6, 6)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '宜昌开发区' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(5, 7, '%.2f' % (
                    av_time(all_time, len([x for x in msg_list if x[0] == '宜昌开发区' and x[1] == '完成']))),
                              style1)
                xlsheet.write(6, 0, '五峰', style1)
                xlsheet.write(6, 1, len([x for x in msg_list if x[0] == '五峰']), style1)
                xlsheet.write(6, 2, len([x for x in msg_list1 if x[0] == '五峰' ]), style1)
                xlsheet.write(6, 3, len([x for x in msg_list if x[0] == '五峰' and x[1] == '完成' and x[2] == '是']), style1)
                xlsheet.write(6, 4, len([x for x in msg_list if x[0] == '五峰' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(6, 5, len([x for x in msg_list if x[0] == '五峰' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(6, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(7, 7, 7, 7, 7)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '五峰' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(6, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '五峰' and x[1] == '完成']))),
                              style1)
                xlsheet.write(7, 0, '兴山', style1)
                xlsheet.write(7, 1, len([x for x in msg_list if x[0] == '兴山']), style1)
                xlsheet.write(7, 2, len([x for x in msg_list1 if x[0] == '兴山' ]), style1)
                xlsheet.write(7, 3, len([x for x in msg_list if x[0] == '兴山' and x[1] == '完成' and x[2] == '是']), style1)
                xlsheet.write(7, 4, len([x for x in msg_list if x[0] == '兴山' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(7, 5, len([x for x in msg_list if x[0] == '兴山' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(7, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(8, 8, 8, 8, 8)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '兴山' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(7, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '兴山' and x[1] == '完成']))),
                              style1)
                xlsheet.write(8, 0, '夷陵', style1)
                xlsheet.write(8, 1, len([x for x in msg_list if x[0] == '夷陵']), style1)
                xlsheet.write(8, 2, len([x for x in msg_list1 if x[0] == '夷陵' ]), style1)
                xlsheet.write(8, 3, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '完成' and x[2] == '是']), style1)
                xlsheet.write(8, 4, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(8, 5, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(8, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(9, 9, 9, 9, 9)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '夷陵' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(8, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '完成']))),
                              style1)
                xlsheet.write(9, 0, '宜都', style1)
                xlsheet.write(9, 1, len([x for x in msg_list if x[0] == '宜都']), style1)
                xlsheet.write(9, 2, len([x for x in msg_list1 if x[0] == '宜都' ]), style1)
                xlsheet.write(9, 3, len([x for x in msg_list if x[0] == '宜都' and x[1] == '完成' and x[2] == '是']), style1)
                xlsheet.write(9, 4, len([x for x in msg_list if x[0] == '宜都' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(9, 5, len([x for x in msg_list if x[0] == '宜都' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(9, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(10, 10, 10, 10, 10)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '宜都' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(9, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '宜都' and x[1] == '完成']))),
                              style1)
                xlsheet.write(10, 0, '远安', style1)
                xlsheet.write(10, 1, len([x for x in msg_list if x[0] == '远安']), style1)
                xlsheet.write(10, 2, len([x for x in msg_list1 if x[0] == '远安' ]), style1)
                xlsheet.write(10, 3, len([x for x in msg_list if x[0] == '远安' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(10, 4, len([x for x in msg_list if x[0] == '远安' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(10, 5, len([x for x in msg_list if x[0] == '远安' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(10, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(11, 11, 11, 11, 11)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '远安' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(10, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '远安' and x[1] == '完成']))),
                              style1)

                xlsheet.write(11, 0, '长阳', style1)
                xlsheet.write(11, 1, len([x for x in msg_list if x[0] == '长阳']), style1)
                xlsheet.write(11, 2, len([x for x in msg_list1 if x[0] == '长阳' ]), style1)
                xlsheet.write(11, 3, len([x for x in msg_list if x[0] == '长阳' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(11, 4, len([x for x in msg_list if x[0] == '长阳' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(11, 5, len([x for x in msg_list if x[0] == '长阳' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(11, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(12, 12, 12, 12, 12)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '长阳' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(11, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '长阳' and x[1] == '完成']))),
                              style1)

                xlsheet.write(12, 0, '枝江', style1)
                xlsheet.write(12, 1, len([x for x in msg_list if x[0] == '枝江']), style1)
                xlsheet.write(12, 2, len([x for x in msg_list1 if x[0] == '枝江' ]), style1)
                xlsheet.write(12, 3, len([x for x in msg_list if x[0] == '枝江' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(12, 4, len([x for x in msg_list if x[0] == '枝江' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(12, 5, len([x for x in msg_list if x[0] == '枝江' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(12, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(13, 13, 13, 13, 13)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '枝江' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(12, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '枝江' and x[1] == '完成']))),
                              style1)

                xlsheet.write(13, 0, '秭归', style1)
                xlsheet.write(13, 1, len([x for x in msg_list if x[0] == '秭归']), style1)
                xlsheet.write(13, 2, len([x for x in msg_list1 if x[0] == '秭归']), style1)
                xlsheet.write(13, 3, len([x for x in msg_list if x[0] == '秭归' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(13, 4, len([x for x in msg_list if x[0] == '秭归' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(13, 5, len([x for x in msg_list if x[0] == '秭归' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(13, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(14, 14, 14, 14, 14)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '秭归' and x[1] == '完成']:
                    all_time = all_time + i[-1]

                xlsheet.write(13, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '秭归' and x[1] == '完成']))),
                              style1)

                xlsheet.write(14, 0, '全市', style1)
                xlsheet.write(14, 1, xlwt.Formula("(B4+B5+B6+B7+B8+B9+B10+B11+B12+B13+B14)"), style1)
                xlsheet.write(14, 2, xlwt.Formula("(C4+C5+C6+C7+C8+C9+C10+C11+C12+C13+C14)"), style1)
                xlsheet.write(14, 3, xlwt.Formula("(D4+D5+D6+D7+D8+D9+D10+D11+D12+D13+D14)"), style1)
                xlsheet.write(14, 4, xlwt.Formula("(E4+E5+E6+E7+E8+E9+E10+E11+E12+E13+E14)"), style1)
                xlsheet.write(14, 5, xlwt.Formula("(F4+F5+F6+F7+F8+F9+F10+F11+F12+F13+F14)"), style1)
                xlsheet.write(14, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(15, 15, 15, 15, 15)), style4)
                xlsheet.write(14, 7, xlwt.Formula("(H4+H5+H6+H7+H8+H9+H10+H11+H12+H13+H14)/11"), style1)
                xlsname=choose_type + str(int(time.time()))
                workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
                return ('mail.itlaolang.com/downfile/{}.xls'.format(xlsname))

            if choose_type == '移机装':
                for x in range(1, sheet.nrows):
                    try:
                        msg = sheet.row_values(x)
                        #这是之间段之内完成的工单数据
                        if msg[9] != 'order_status_6' and msg[3] == '移机装' and utc_str_to_timestamp(msg[15]) >= utc_str_to_timestamp(
                                starttime) and utc_str_to_timestamp(msg[15]) <= utc_str_to_timestamp(endtime) \
                                and msg[19] != '普服小区' and msg[19] != '普遍服务':
                            finshed=[find_area(msg[1], msg[11])]
                            msg_list1.append(finshed)
                        #这是时间段之内受理工单数据
                        if msg[9] != 'order_status_6' and msg[3] == '移机装' and utc_str_to_timestamp(msg[12]) >= utc_str_to_timestamp(
                                starttime) and utc_str_to_timestamp(msg[12]) <= utc_str_to_timestamp(endtime) \
                                and msg[19] != '普服小区' and msg[19] != '普遍服务':
                            result = [find_area(msg[1], msg[11]), get_status(msg[15],starttime,endtime),
                                      get_timeout(msg[12], msg[15], msg[19]), downdan(msg[12]),
                                      time_for_end(msg[12], msg[15])]
                            # print(result)
                            msg_list.append(result)

                    except:
                        pass
                # print(len([x for x in msg_list if x[0] == '枝江']))
                # print(len([x for x in msg_list if x[0] == '枝江' and x[1]=='完成']))
                # print(len([x for x in msg_list if x[0] == '枝江' and x[1]=='完成' and x[2]=='是']))
                # print(len([x for x in msg_list if x[0] == '枝江' and x[1]=='未完成' and x[2]=='是']))
                # print(len([x for x in msg_list if x[0] == '枝江' and x[1]=='未完成' and x[3]==1]))
                all_time = 0
                print(len([x for x in msg_list if x[0] == '夷陵' and x[1] == '完成']))
                for i in [x for x in msg_list if x[0] == '夷陵' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                # print(all_time)
                # print(av_time(all_time,len([x for x in msg_list if x[0] == '夷陵' and x[1] == '完成'])))
                print('%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '完成']))))

                workbook_m = xlwt.Workbook(encoding='utf-8')
                xlsheet = workbook_m.add_sheet('24小时装机日报（不含农普）', cell_overwrite_ok=True)
                # 格式1 （有自动换行）
                style1 = xlwt.easyxf('pattern: pattern solid, fore_colour white')
                style1.font.height = 200
                style1.font.name = u'文泉驿点阵正黑'
                style1.font.colour_index = 0
                style1.borders.left = xlwt.Borders.THIN
                style1.borders.right = xlwt.Borders.THIN
                style1.borders.top = xlwt.Borders.THIN
                style1.borders.bottom = xlwt.Borders.THIN
                # style1.font.bold = True
                style1.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
                style1.alignment.horz = xlwt.Alignment.HORZ_CENTER

                # 格式2  （没有自动换行）
                style2 = xlwt.easyxf('pattern: pattern solid, fore_colour white')
                style2.font.height = 200
                style2.font.name = u'文泉驿点阵正黑'
                style2.font.colour_index = 0
                style2.borders.left = xlwt.Borders.THIN
                style2.borders.right = xlwt.Borders.THIN
                style2.borders.top = xlwt.Borders.THIN
                style2.borders.bottom = xlwt.Borders.THIN

                # style2.font.bold = True
                # style2.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
                # style2.alignment.horz = xlwt.Alignment.HORZ_CENTER

                # 格式3 黄色背景色

                style3 = xlwt.easyxf('pattern: pattern solid, fore_colour yellow')
                style3.font.height = 200
                style3.font.name = u'文泉驿点阵正黑'
                style3.font.colour_index = 0
                # style3.borders.left = xlwt.Borders.THIN
                # style3.borders.right = xlwt.Borders.THIN
                # style3.borders.top = xlwt.Borders.THIN
                # style3.borders.bottom = xlwt.Borders.THIN

                # style4 格式4 0.00%

                style4 = xlwt.easyxf('pattern: pattern solid, fore_colour white')
                style4.font.height = 200
                style4.font.name = u'文泉驿点阵正黑'
                style4.font.colour_index = 0
                style4.borders.left = xlwt.Borders.THIN
                style4.borders.right = xlwt.Borders.THIN
                style4.borders.top = xlwt.Borders.THIN
                style4.borders.bottom = xlwt.Borders.THIN
                # style1.font.bold = True
                style4.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
                style4.alignment.horz = xlwt.Alignment.HORZ_CENTER
                style4.num_format_str = '0.00%'

                # style2.font.bold = True
                # style2.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
                # style2.alignment.horz = xlwt.Alignment.HORZ_CENTER
                # 写excel表头
                # 设置单元格
                xlsheet.write(0, 0, '起始时间：', style3)
                xlsheet.write(0, 1, starttime, style1)
                xlsheet.write(0, 3, '截止时间：', style3)
                xlsheet.write(0, 4, endtime, style1)
                xlsheet.write(0, 6, '工单类型：', style3)
                xlsheet.write(0, 7, choose_type, style3)
                xlsheet.write(1, 0, '区县（区域属性）', style1)
                xlsheet.write(1, 1, '当日受理工单量', style1)
                xlsheet.write(1, 2, '当日装机完成量', style1)
                xlsheet.write(1, 3, '已装超时量', style1)
                xlsheet.write(1, 4, '未装超时量', style1)
                xlsheet.write(1, 5, '压单量', style1)
                xlsheet.write(1, 6, '装机及时率', style1)
                xlsheet.write(1, 7, '平均装机时长（小时）', style1)
                xlsheet.write(2, 0, '备注', style1)
                xlsheet.write(2, 1, '本月受理的所有单子', style1)
                xlsheet.write(2, 2, '本月完成的所有单子', style1)
                xlsheet.write(2, 3, '已完成的超时工单（城区24小时、乡镇36小时）', style1)
                xlsheet.write(2, 4, '未完成的超时工单', style1)
                xlsheet.write(2, 5, '本月之前受理，且还没完成', style1)
                xlsheet.write(2, 6, '(受理工单量-已装超时量-未装超时量-本月以前压单量)/受理工单量', style1)
                xlsheet.write(2, 7, '已完成单子共花费时间/完成单子数', style1)
                xlsheet.write(3, 0, '城区', style1)
                xlsheet.write(3, 1, len([x for x in msg_list if x[0] == '宜昌城区']), style1)
                xlsheet.write(3, 2, len([x for x in msg_list1 if x[0] == '宜昌城区']), style1)
                xlsheet.write(3, 3, len([x for x in msg_list if x[0] == '宜昌城区' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(3, 4, len([x for x in msg_list if x[0] == '宜昌城区' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(3, 5, len([x for x in msg_list if x[0] == '宜昌城区' and x[1] == '未完成' and x[3] == 1]),
                              style1)
                xlsheet.write(3, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(4, 4, 4, 4, 4)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '宜昌城区' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(3, 7, '%.2f' % (
                    av_time(all_time, len([x for x in msg_list if x[0] == '宜昌城区' and x[1] == '完成']))), style1)

                xlsheet.write(4, 0, '当阳', style1)
                xlsheet.write(4, 1, len([x for x in msg_list if x[0] == '当阳']), style1)
                xlsheet.write(4, 2, len([x for x in msg_list1 if x[0] == '当阳' ]), style1)
                xlsheet.write(4, 3, len([x for x in msg_list if x[0] == '当阳' and x[1] == '完成' and x[2] == '是']), style1)
                xlsheet.write(4, 4, len([x for x in msg_list if x[0] == '当阳' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(4, 5, len([x for x in msg_list if x[0] == '当阳' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(4, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(5, 5, 5, 5, 5)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '当阳' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(4, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '当阳' and x[1] == '完成']))),
                              style1)
                xlsheet.write(5, 0, '开发区', style1)
                xlsheet.write(5, 1, len([x for x in msg_list if x[0] == '宜昌开发区']), style1)
                xlsheet.write(5, 2, len([x for x in msg_list1 if x[0] == '宜昌开发区']), style1)
                xlsheet.write(5, 3, len([x for x in msg_list if x[0] == '宜昌开发区' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(5, 4, len([x for x in msg_list if x[0] == '宜昌开发区' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(5, 5, len([x for x in msg_list if x[0] == '宜昌开发区' and x[1] == '未完成' and x[3] == 1]),
                              style1)
                xlsheet.write(5, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(6, 6, 6, 6, 6)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '宜昌开发区' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(5, 7, '%.2f' % (
                    av_time(all_time, len([x for x in msg_list if x[0] == '宜昌开发区' and x[1] == '完成']))),
                              style1)
                xlsheet.write(6, 0, '五峰', style1)
                xlsheet.write(6, 1, len([x for x in msg_list if x[0] == '五峰']), style1)
                xlsheet.write(6, 2, len([x for x in msg_list1 if x[0] == '五峰' ]), style1)
                xlsheet.write(6, 3, len([x for x in msg_list if x[0] == '五峰' and x[1] == '完成' and x[2] == '是']), style1)
                xlsheet.write(6, 4, len([x for x in msg_list if x[0] == '五峰' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(6, 5, len([x for x in msg_list if x[0] == '五峰' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(6, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(7, 7, 7, 7, 7)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '五峰' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(6, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '五峰' and x[1] == '完成']))),
                              style1)
                xlsheet.write(7, 0, '兴山', style1)
                xlsheet.write(7, 1, len([x for x in msg_list if x[0] == '兴山']), style1)
                xlsheet.write(7, 2, len([x for x in msg_list1 if x[0] == '兴山' ]), style1)
                xlsheet.write(7, 3, len([x for x in msg_list if x[0] == '兴山' and x[1] == '完成' and x[2] == '是']), style1)
                xlsheet.write(7, 4, len([x for x in msg_list if x[0] == '兴山' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(7, 5, len([x for x in msg_list if x[0] == '兴山' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(7, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(8, 8, 8, 8, 8)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '兴山' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(7, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '兴山' and x[1] == '完成']))),
                              style1)
                xlsheet.write(8, 0, '夷陵', style1)
                xlsheet.write(8, 1, len([x for x in msg_list if x[0] == '夷陵']), style1)
                xlsheet.write(8, 2, len([x for x in msg_list1 if x[0] == '夷陵' ]), style1)
                xlsheet.write(8, 3, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '完成' and x[2] == '是']), style1)
                xlsheet.write(8, 4, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(8, 5, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(8, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(9, 9, 9, 9, 9)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '夷陵' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(8, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '完成']))),
                              style1)
                xlsheet.write(9, 0, '宜都', style1)
                xlsheet.write(9, 1, len([x for x in msg_list if x[0] == '宜都']), style1)
                xlsheet.write(9, 2, len([x for x in msg_list1 if x[0] == '宜都' ]), style1)
                xlsheet.write(9, 3, len([x for x in msg_list if x[0] == '宜都' and x[1] == '完成' and x[2] == '是']), style1)
                xlsheet.write(9, 4, len([x for x in msg_list if x[0] == '宜都' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(9, 5, len([x for x in msg_list if x[0] == '宜都' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(9, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(10, 10, 10, 10, 10)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '宜都' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(9, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '宜都' and x[1] == '完成']))),
                              style1)
                xlsheet.write(10, 0, '远安', style1)
                xlsheet.write(10, 1, len([x for x in msg_list if x[0] == '远安']), style1)
                xlsheet.write(10, 2, len([x for x in msg_list1 if x[0] == '远安' ]), style1)
                xlsheet.write(10, 3, len([x for x in msg_list if x[0] == '远安' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(10, 4, len([x for x in msg_list if x[0] == '远安' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(10, 5, len([x for x in msg_list if x[0] == '远安' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(10, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(11, 11, 11, 11, 11)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '远安' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(10, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '远安' and x[1] == '完成']))),
                              style1)

                xlsheet.write(11, 0, '长阳', style1)
                xlsheet.write(11, 1, len([x for x in msg_list if x[0] == '长阳']), style1)
                xlsheet.write(11, 2, len([x for x in msg_list1 if x[0] == '长阳' ]), style1)
                xlsheet.write(11, 3, len([x for x in msg_list if x[0] == '长阳' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(11, 4, len([x for x in msg_list if x[0] == '长阳' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(11, 5, len([x for x in msg_list if x[0] == '长阳' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(11, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(12, 12, 12, 12, 12)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '长阳' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(11, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '长阳' and x[1] == '完成']))),
                              style1)

                xlsheet.write(12, 0, '枝江', style1)
                xlsheet.write(12, 1, len([x for x in msg_list if x[0] == '枝江']), style1)
                xlsheet.write(12, 2, len([x for x in msg_list1 if x[0] == '枝江' ]), style1)
                xlsheet.write(12, 3, len([x for x in msg_list if x[0] == '枝江' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(12, 4, len([x for x in msg_list if x[0] == '枝江' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(12, 5, len([x for x in msg_list if x[0] == '枝江' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(12, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(13, 13, 13, 13, 13)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '枝江' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(12, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '枝江' and x[1] == '完成']))),
                              style1)

                xlsheet.write(13, 0, '秭归', style1)
                xlsheet.write(13, 1, len([x for x in msg_list if x[0] == '秭归']), style1)
                xlsheet.write(13, 2, len([x for x in msg_list1 if x[0] == '秭归']), style1)
                xlsheet.write(13, 3, len([x for x in msg_list if x[0] == '秭归' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(13, 4, len([x for x in msg_list if x[0] == '秭归' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(13, 5, len([x for x in msg_list if x[0] == '秭归' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(13, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(14, 14, 14, 14, 14)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '秭归' and x[1] == '完成']:
                    all_time = all_time + i[-1]

                xlsheet.write(13, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '秭归' and x[1] == '完成']))),
                              style1)

                xlsheet.write(14, 0, '全市', style1)
                xlsheet.write(14, 1, xlwt.Formula("(B4+B5+B6+B7+B8+B9+B10+B11+B12+B13+B14)"), style1)
                xlsheet.write(14, 2, xlwt.Formula("(C4+C5+C6+C7+C8+C9+C10+C11+C12+C13+C14)"), style1)
                xlsheet.write(14, 3, xlwt.Formula("(D4+D5+D6+D7+D8+D9+D10+D11+D12+D13+D14)"), style1)
                xlsheet.write(14, 4, xlwt.Formula("(E4+E5+E6+E7+E8+E9+E10+E11+E12+E13+E14)"), style1)
                xlsheet.write(14, 5, xlwt.Formula("(F4+F5+F6+F7+F8+F9+F10+F11+F12+F13+F14)"), style1)
                xlsheet.write(14, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(15, 15, 15, 15, 15)), style4)
                xlsheet.write(14, 7, xlwt.Formula("(H4+H5+H6+H7+H8+H9+H10+H11+H12+H13+H14)/11"), style1)
                xlsname=choose_type + str(int(time.time()))
                workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
                return ('mail.itlaolang.com/downfile/{}.xls'.format(xlsname))

            if choose_type == 'IMS单独安装':
                for x in range(1, sheet.nrows):
                    try:
                        msg = sheet.row_values(x)
                        #这是之间段之内完成的工单数据
                        if msg[9] != 'order_status_6' and msg[3] == 'IMS单独安装' and utc_str_to_timestamp(msg[15]) >= utc_str_to_timestamp(
                                starttime) and utc_str_to_timestamp(msg[15]) <= utc_str_to_timestamp(endtime) \
                                and msg[19] != '普服小区' and msg[19] != '普遍服务':
                            finshed=[find_area(msg[1], msg[11])]
                            msg_list1.append(finshed)
                        #这是时间段之内受理工单数据
                        if msg[9] != 'order_status_6' and msg[3] == 'IMS单独安装' and utc_str_to_timestamp(msg[12]) >= utc_str_to_timestamp(
                                starttime) and utc_str_to_timestamp(msg[12]) <= utc_str_to_timestamp(endtime) \
                                and msg[19] != '普服小区' and msg[19] != '普遍服务':
                            result = [find_area(msg[1], msg[11]), get_status(msg[15],starttime,endtime),
                                      get_timeout(msg[12], msg[15], msg[19]), downdan(msg[12]),
                                      time_for_end(msg[12], msg[15])]
                            # print(result)
                            msg_list.append(result)

                    except:
                        pass
                # print(len([x for x in msg_list if x[0] == '枝江']))
                # print(len([x for x in msg_list if x[0] == '枝江' and x[1]=='完成']))
                # print(len([x for x in msg_list if x[0] == '枝江' and x[1]=='完成' and x[2]=='是']))
                # print(len([x for x in msg_list if x[0] == '枝江' and x[1]=='未完成' and x[2]=='是']))
                # print(len([x for x in msg_list if x[0] == '枝江' and x[1]=='未完成' and x[3]==1]))
                all_time = 0
                print(len([x for x in msg_list if x[0] == '夷陵' and x[1] == '完成']))
                for i in [x for x in msg_list if x[0] == '夷陵' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                # print(all_time)
                # print(av_time(all_time,len([x for x in msg_list if x[0] == '夷陵' and x[1] == '完成'])))
                print('%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '完成']))))

                workbook_m = xlwt.Workbook(encoding='utf-8')
                xlsheet = workbook_m.add_sheet('24小时装机日报（不含农普）', cell_overwrite_ok=True)
                # 格式1 （有自动换行）
                style1 = xlwt.easyxf('pattern: pattern solid, fore_colour white')
                style1.font.height = 200
                style1.font.name = u'文泉驿点阵正黑'
                style1.font.colour_index = 0
                style1.borders.left = xlwt.Borders.THIN
                style1.borders.right = xlwt.Borders.THIN
                style1.borders.top = xlwt.Borders.THIN
                style1.borders.bottom = xlwt.Borders.THIN
                # style1.font.bold = True
                style1.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
                style1.alignment.horz = xlwt.Alignment.HORZ_CENTER

                # 格式2  （没有自动换行）
                style2 = xlwt.easyxf('pattern: pattern solid, fore_colour white')
                style2.font.height = 200
                style2.font.name = u'文泉驿点阵正黑'
                style2.font.colour_index = 0
                style2.borders.left = xlwt.Borders.THIN
                style2.borders.right = xlwt.Borders.THIN
                style2.borders.top = xlwt.Borders.THIN
                style2.borders.bottom = xlwt.Borders.THIN

                # style2.font.bold = True
                # style2.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
                # style2.alignment.horz = xlwt.Alignment.HORZ_CENTER

                # 格式3 黄色背景色

                style3 = xlwt.easyxf('pattern: pattern solid, fore_colour yellow')
                style3.font.height = 200
                style3.font.name = u'文泉驿点阵正黑'
                style3.font.colour_index = 0
                # style3.borders.left = xlwt.Borders.THIN
                # style3.borders.right = xlwt.Borders.THIN
                # style3.borders.top = xlwt.Borders.THIN
                # style3.borders.bottom = xlwt.Borders.THIN

                # style4 格式4 0.00%

                style4 = xlwt.easyxf('pattern: pattern solid, fore_colour white')
                style4.font.height = 200
                style4.font.name = u'文泉驿点阵正黑'
                style4.font.colour_index = 0
                style4.borders.left = xlwt.Borders.THIN
                style4.borders.right = xlwt.Borders.THIN
                style4.borders.top = xlwt.Borders.THIN
                style4.borders.bottom = xlwt.Borders.THIN
                # style1.font.bold = True
                style4.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
                style4.alignment.horz = xlwt.Alignment.HORZ_CENTER
                style4.num_format_str = '0.00%'

                # style2.font.bold = True
                # style2.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
                # style2.alignment.horz = xlwt.Alignment.HORZ_CENTER
                # 写excel表头
                # 设置单元格
                xlsheet.write(0, 0, '起始时间：', style3)
                xlsheet.write(0, 1, starttime, style1)
                xlsheet.write(0, 3, '截止时间：', style3)
                xlsheet.write(0, 4, endtime, style1)
                xlsheet.write(0, 6, '工单类型：', style3)
                xlsheet.write(0, 7, choose_type, style3)
                xlsheet.write(1, 0, '区县（区域属性）', style1)
                xlsheet.write(1, 1, '当日受理工单量', style1)
                xlsheet.write(1, 2, '当日装机完成量', style1)
                xlsheet.write(1, 3, '已装超时量', style1)
                xlsheet.write(1, 4, '未装超时量', style1)
                xlsheet.write(1, 5, '压单量', style1)
                xlsheet.write(1, 6, '装机及时率', style1)
                xlsheet.write(1, 7, '平均装机时长（小时）', style1)
                xlsheet.write(2, 0, '备注', style1)
                xlsheet.write(2, 1, '本月受理的所有单子', style1)
                xlsheet.write(2, 2, '本月完成的所有单子', style1)
                xlsheet.write(2, 3, '已完成的超时工单（城区24小时、乡镇36小时）', style1)
                xlsheet.write(2, 4, '未完成的超时工单', style1)
                xlsheet.write(2, 5, '本月之前受理，且还没完成', style1)
                xlsheet.write(2, 6, '(受理工单量-已装超时量-未装超时量-本月以前压单量)/受理工单量', style1)
                xlsheet.write(2, 7, '已完成单子共花费时间/完成单子数', style1)
                xlsheet.write(3, 0, '城区', style1)
                xlsheet.write(3, 1, len([x for x in msg_list if x[0] == '宜昌城区']), style1)
                xlsheet.write(3, 2, len([x for x in msg_list1 if x[0] == '宜昌城区']), style1)
                xlsheet.write(3, 3, len([x for x in msg_list if x[0] == '宜昌城区' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(3, 4, len([x for x in msg_list if x[0] == '宜昌城区' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(3, 5, len([x for x in msg_list if x[0] == '宜昌城区' and x[1] == '未完成' and x[3] == 1]),
                              style1)
                xlsheet.write(3, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(4, 4, 4, 4, 4)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '宜昌城区' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(3, 7, '%.2f' % (
                    av_time(all_time, len([x for x in msg_list if x[0] == '宜昌城区' and x[1] == '完成']))), style1)

                xlsheet.write(4, 0, '当阳', style1)
                xlsheet.write(4, 1, len([x for x in msg_list if x[0] == '当阳']), style1)
                xlsheet.write(4, 2, len([x for x in msg_list1 if x[0] == '当阳' ]), style1)
                xlsheet.write(4, 3, len([x for x in msg_list if x[0] == '当阳' and x[1] == '完成' and x[2] == '是']), style1)
                xlsheet.write(4, 4, len([x for x in msg_list if x[0] == '当阳' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(4, 5, len([x for x in msg_list if x[0] == '当阳' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(4, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(5, 5, 5, 5, 5)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '当阳' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(4, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '当阳' and x[1] == '完成']))),
                              style1)
                xlsheet.write(5, 0, '开发区', style1)
                xlsheet.write(5, 1, len([x for x in msg_list if x[0] == '宜昌开发区']), style1)
                xlsheet.write(5, 2, len([x for x in msg_list1 if x[0] == '宜昌开发区']), style1)
                xlsheet.write(5, 3, len([x for x in msg_list if x[0] == '宜昌开发区' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(5, 4, len([x for x in msg_list if x[0] == '宜昌开发区' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(5, 5, len([x for x in msg_list if x[0] == '宜昌开发区' and x[1] == '未完成' and x[3] == 1]),
                              style1)
                xlsheet.write(5, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(6, 6, 6, 6, 6)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '宜昌开发区' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(5, 7, '%.2f' % (
                    av_time(all_time, len([x for x in msg_list if x[0] == '宜昌开发区' and x[1] == '完成']))),
                              style1)
                xlsheet.write(6, 0, '五峰', style1)
                xlsheet.write(6, 1, len([x for x in msg_list if x[0] == '五峰']), style1)
                xlsheet.write(6, 2, len([x for x in msg_list1 if x[0] == '五峰' ]), style1)
                xlsheet.write(6, 3, len([x for x in msg_list if x[0] == '五峰' and x[1] == '完成' and x[2] == '是']), style1)
                xlsheet.write(6, 4, len([x for x in msg_list if x[0] == '五峰' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(6, 5, len([x for x in msg_list if x[0] == '五峰' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(6, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(7, 7, 7, 7, 7)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '五峰' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(6, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '五峰' and x[1] == '完成']))),
                              style1)
                xlsheet.write(7, 0, '兴山', style1)
                xlsheet.write(7, 1, len([x for x in msg_list if x[0] == '兴山']), style1)
                xlsheet.write(7, 2, len([x for x in msg_list1 if x[0] == '兴山' ]), style1)
                xlsheet.write(7, 3, len([x for x in msg_list if x[0] == '兴山' and x[1] == '完成' and x[2] == '是']), style1)
                xlsheet.write(7, 4, len([x for x in msg_list if x[0] == '兴山' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(7, 5, len([x for x in msg_list if x[0] == '兴山' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(7, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(8, 8, 8, 8, 8)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '兴山' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(7, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '兴山' and x[1] == '完成']))),
                              style1)
                xlsheet.write(8, 0, '夷陵', style1)
                xlsheet.write(8, 1, len([x for x in msg_list if x[0] == '夷陵']), style1)
                xlsheet.write(8, 2, len([x for x in msg_list1 if x[0] == '夷陵' ]), style1)
                xlsheet.write(8, 3, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '完成' and x[2] == '是']), style1)
                xlsheet.write(8, 4, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(8, 5, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(8, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(9, 9, 9, 9, 9)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '夷陵' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(8, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '完成']))),
                              style1)
                xlsheet.write(9, 0, '宜都', style1)
                xlsheet.write(9, 1, len([x for x in msg_list if x[0] == '宜都']), style1)
                xlsheet.write(9, 2, len([x for x in msg_list1 if x[0] == '宜都' ]), style1)
                xlsheet.write(9, 3, len([x for x in msg_list if x[0] == '宜都' and x[1] == '完成' and x[2] == '是']), style1)
                xlsheet.write(9, 4, len([x for x in msg_list if x[0] == '宜都' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(9, 5, len([x for x in msg_list if x[0] == '宜都' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(9, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(10, 10, 10, 10, 10)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '宜都' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(9, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '宜都' and x[1] == '完成']))),
                              style1)
                xlsheet.write(10, 0, '远安', style1)
                xlsheet.write(10, 1, len([x for x in msg_list if x[0] == '远安']), style1)
                xlsheet.write(10, 2, len([x for x in msg_list1 if x[0] == '远安' ]), style1)
                xlsheet.write(10, 3, len([x for x in msg_list if x[0] == '远安' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(10, 4, len([x for x in msg_list if x[0] == '远安' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(10, 5, len([x for x in msg_list if x[0] == '远安' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(10, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(11, 11, 11, 11, 11)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '远安' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(10, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '远安' and x[1] == '完成']))),
                              style1)

                xlsheet.write(11, 0, '长阳', style1)
                xlsheet.write(11, 1, len([x for x in msg_list if x[0] == '长阳']), style1)
                xlsheet.write(11, 2, len([x for x in msg_list1 if x[0] == '长阳' ]), style1)
                xlsheet.write(11, 3, len([x for x in msg_list if x[0] == '长阳' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(11, 4, len([x for x in msg_list if x[0] == '长阳' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(11, 5, len([x for x in msg_list if x[0] == '长阳' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(11, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(12, 12, 12, 12, 12)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '长阳' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(11, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '长阳' and x[1] == '完成']))),
                              style1)

                xlsheet.write(12, 0, '枝江', style1)
                xlsheet.write(12, 1, len([x for x in msg_list if x[0] == '枝江']), style1)
                xlsheet.write(12, 2, len([x for x in msg_list1 if x[0] == '枝江' ]), style1)
                xlsheet.write(12, 3, len([x for x in msg_list if x[0] == '枝江' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(12, 4, len([x for x in msg_list if x[0] == '枝江' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(12, 5, len([x for x in msg_list if x[0] == '枝江' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(12, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(13, 13, 13, 13, 13)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '枝江' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(12, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '枝江' and x[1] == '完成']))),
                              style1)

                xlsheet.write(13, 0, '秭归', style1)
                xlsheet.write(13, 1, len([x for x in msg_list if x[0] == '秭归']), style1)
                xlsheet.write(13, 2, len([x for x in msg_list1 if x[0] == '秭归']), style1)
                xlsheet.write(13, 3, len([x for x in msg_list if x[0] == '秭归' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(13, 4, len([x for x in msg_list if x[0] == '秭归' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(13, 5, len([x for x in msg_list if x[0] == '秭归' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(13, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(14, 14, 14, 14, 14)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '秭归' and x[1] == '完成']:
                    all_time = all_time + i[-1]

                xlsheet.write(13, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '秭归' and x[1] == '完成']))),
                              style1)

                xlsheet.write(14, 0, '全市', style1)
                xlsheet.write(14, 1, xlwt.Formula("(B4+B5+B6+B7+B8+B9+B10+B11+B12+B13+B14)"), style1)
                xlsheet.write(14, 2, xlwt.Formula("(C4+C5+C6+C7+C8+C9+C10+C11+C12+C13+C14)"), style1)
                xlsheet.write(14, 3, xlwt.Formula("(D4+D5+D6+D7+D8+D9+D10+D11+D12+D13+D14)"), style1)
                xlsheet.write(14, 4, xlwt.Formula("(E4+E5+E6+E7+E8+E9+E10+E11+E12+E13+E14)"), style1)
                xlsheet.write(14, 5, xlwt.Formula("(F4+F5+F6+F7+F8+F9+F10+F11+F12+F13+F14)"), style1)
                xlsheet.write(14, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(15, 15, 15, 15, 15)), style4)
                xlsheet.write(14, 7, xlwt.Formula("(H4+H5+H6+H7+H8+H9+H10+H11+H12+H13+H14)/11"), style1)
                xlsname=choose_type + str(int(time.time()))

                workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
                return ('mail.itlaolang.com/downfile/{}.xls'.format(xlsname))

            if choose_type == 'TV单独安装':
                for x in range(1, sheet.nrows):
                    try:
                        msg = sheet.row_values(x)
                        #这是之间段之内完成的工单数据
                        if msg[9] != 'order_status_6' and msg[3] == '和TV单独安装' and utc_str_to_timestamp(msg[15]) >= utc_str_to_timestamp(
                                starttime) and utc_str_to_timestamp(msg[15]) <= utc_str_to_timestamp(endtime) \
                                and msg[19] != '普服小区' and msg[19] != '普遍服务':
                            finshed=[find_area(msg[1], msg[11])]
                            msg_list1.append(finshed)
                        #这是时间段之内受理工单数据
                        if msg[9] != 'order_status_6' and msg[3] == '和TV单独安装' and utc_str_to_timestamp(msg[12]) >= utc_str_to_timestamp(
                                starttime) and utc_str_to_timestamp(msg[12]) <= utc_str_to_timestamp(endtime) \
                                and msg[19] != '普服小区' and msg[19] != '普遍服务':
                            result = [find_area(msg[1], msg[11]), get_status(msg[15],starttime,endtime),
                                      get_timeout(msg[12], msg[15], msg[19]), downdan(msg[12]),
                                      time_for_end(msg[12], msg[15])]
                            # print(result)
                            msg_list.append(result)

                    except:
                        pass
                # print(len([x for x in msg_list if x[0] == '枝江']))
                # print(len([x for x in msg_list if x[0] == '枝江' and x[1]=='完成']))
                # print(len([x for x in msg_list if x[0] == '枝江' and x[1]=='完成' and x[2]=='是']))
                # print(len([x for x in msg_list if x[0] == '枝江' and x[1]=='未完成' and x[2]=='是']))
                # print(len([x for x in msg_list if x[0] == '枝江' and x[1]=='未完成' and x[3]==1]))
                all_time = 0
                print(len([x for x in msg_list if x[0] == '夷陵' and x[1] == '完成']))
                for i in [x for x in msg_list if x[0] == '夷陵' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                # print(all_time)
                # print(av_time(all_time,len([x for x in msg_list if x[0] == '夷陵' and x[1] == '完成'])))
                print('%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '完成']))))

                workbook_m = xlwt.Workbook(encoding='utf-8')
                xlsheet = workbook_m.add_sheet('24小时装机日报（不含农普）', cell_overwrite_ok=True)
                # 格式1 （有自动换行）
                style1 = xlwt.easyxf('pattern: pattern solid, fore_colour white')
                style1.font.height = 200
                style1.font.name = u'文泉驿点阵正黑'
                style1.font.colour_index = 0
                style1.borders.left = xlwt.Borders.THIN
                style1.borders.right = xlwt.Borders.THIN
                style1.borders.top = xlwt.Borders.THIN
                style1.borders.bottom = xlwt.Borders.THIN
                # style1.font.bold = True
                style1.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
                style1.alignment.horz = xlwt.Alignment.HORZ_CENTER

                # 格式2  （没有自动换行）
                style2 = xlwt.easyxf('pattern: pattern solid, fore_colour white')
                style2.font.height = 200
                style2.font.name = u'文泉驿点阵正黑'
                style2.font.colour_index = 0
                style2.borders.left = xlwt.Borders.THIN
                style2.borders.right = xlwt.Borders.THIN
                style2.borders.top = xlwt.Borders.THIN
                style2.borders.bottom = xlwt.Borders.THIN

                # style2.font.bold = True
                # style2.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
                # style2.alignment.horz = xlwt.Alignment.HORZ_CENTER

                # 格式3 黄色背景色

                style3 = xlwt.easyxf('pattern: pattern solid, fore_colour yellow')
                style3.font.height = 200
                style3.font.name = u'文泉驿点阵正黑'
                style3.font.colour_index = 0
                # style3.borders.left = xlwt.Borders.THIN
                # style3.borders.right = xlwt.Borders.THIN
                # style3.borders.top = xlwt.Borders.THIN
                # style3.borders.bottom = xlwt.Borders.THIN

                # style4 格式4 0.00%

                style4 = xlwt.easyxf('pattern: pattern solid, fore_colour white')
                style4.font.height = 200
                style4.font.name = u'文泉驿点阵正黑'
                style4.font.colour_index = 0
                style4.borders.left = xlwt.Borders.THIN
                style4.borders.right = xlwt.Borders.THIN
                style4.borders.top = xlwt.Borders.THIN
                style4.borders.bottom = xlwt.Borders.THIN
                # style1.font.bold = True
                style4.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
                style4.alignment.horz = xlwt.Alignment.HORZ_CENTER
                style4.num_format_str = '0.00%'

                # style2.font.bold = True
                # style2.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
                # style2.alignment.horz = xlwt.Alignment.HORZ_CENTER
                # 写excel表头
                # 设置单元格
                xlsheet.write(0, 0, '起始时间：', style3)
                xlsheet.write(0, 1, starttime, style1)
                xlsheet.write(0, 3, '截止时间：', style3)
                xlsheet.write(0, 4, endtime, style1)
                xlsheet.write(0, 6, '工单类型：', style3)
                xlsheet.write(0, 7, choose_type, style3)
                xlsheet.write(1, 0, '区县（区域属性）', style1)
                xlsheet.write(1, 1, '当日受理工单量', style1)
                xlsheet.write(1, 2, '当日装机完成量', style1)
                xlsheet.write(1, 3, '已装超时量', style1)
                xlsheet.write(1, 4, '未装超时量', style1)
                xlsheet.write(1, 5, '压单量', style1)
                xlsheet.write(1, 6, '装机及时率', style1)
                xlsheet.write(1, 7, '平均装机时长（小时）', style1)
                xlsheet.write(2, 0, '备注', style1)
                xlsheet.write(2, 1, '本月受理的所有单子', style1)
                xlsheet.write(2, 2, '本月完成的所有单子', style1)
                xlsheet.write(2, 3, '已完成的超时工单（城区24小时、乡镇36小时）', style1)
                xlsheet.write(2, 4, '未完成的超时工单', style1)
                xlsheet.write(2, 5, '本月之前受理，且还没完成', style1)
                xlsheet.write(2, 6, '(受理工单量-已装超时量-未装超时量-本月以前压单量)/受理工单量', style1)
                xlsheet.write(2, 7, '已完成单子共花费时间/完成单子数', style1)
                xlsheet.write(3, 0, '城区', style1)
                xlsheet.write(3, 1, len([x for x in msg_list if x[0] == '宜昌城区']), style1)
                xlsheet.write(3, 2, len([x for x in msg_list1 if x[0] == '宜昌城区']), style1)
                xlsheet.write(3, 3, len([x for x in msg_list if x[0] == '宜昌城区' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(3, 4, len([x for x in msg_list if x[0] == '宜昌城区' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(3, 5, len([x for x in msg_list if x[0] == '宜昌城区' and x[1] == '未完成' and x[3] == 1]),
                              style1)
                xlsheet.write(3, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(4, 4, 4, 4, 4)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '宜昌城区' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(3, 7, '%.2f' % (
                    av_time(all_time, len([x for x in msg_list if x[0] == '宜昌城区' and x[1] == '完成']))), style1)

                xlsheet.write(4, 0, '当阳', style1)
                xlsheet.write(4, 1, len([x for x in msg_list if x[0] == '当阳']), style1)
                xlsheet.write(4, 2, len([x for x in msg_list1 if x[0] == '当阳' ]), style1)
                xlsheet.write(4, 3, len([x for x in msg_list if x[0] == '当阳' and x[1] == '完成' and x[2] == '是']), style1)
                xlsheet.write(4, 4, len([x for x in msg_list if x[0] == '当阳' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(4, 5, len([x for x in msg_list if x[0] == '当阳' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(4, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(5, 5, 5, 5, 5)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '当阳' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(4, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '当阳' and x[1] == '完成']))),
                              style1)
                xlsheet.write(5, 0, '开发区', style1)
                xlsheet.write(5, 1, len([x for x in msg_list if x[0] == '宜昌开发区']), style1)
                xlsheet.write(5, 2, len([x for x in msg_list1 if x[0] == '宜昌开发区']), style1)
                xlsheet.write(5, 3, len([x for x in msg_list if x[0] == '宜昌开发区' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(5, 4, len([x for x in msg_list if x[0] == '宜昌开发区' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(5, 5, len([x for x in msg_list if x[0] == '宜昌开发区' and x[1] == '未完成' and x[3] == 1]),
                              style1)
                xlsheet.write(5, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(6, 6, 6, 6, 6)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '宜昌开发区' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(5, 7, '%.2f' % (
                    av_time(all_time, len([x for x in msg_list if x[0] == '宜昌开发区' and x[1] == '完成']))),
                              style1)
                xlsheet.write(6, 0, '五峰', style1)
                xlsheet.write(6, 1, len([x for x in msg_list if x[0] == '五峰']), style1)
                xlsheet.write(6, 2, len([x for x in msg_list1 if x[0] == '五峰' ]), style1)
                xlsheet.write(6, 3, len([x for x in msg_list if x[0] == '五峰' and x[1] == '完成' and x[2] == '是']), style1)
                xlsheet.write(6, 4, len([x for x in msg_list if x[0] == '五峰' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(6, 5, len([x for x in msg_list if x[0] == '五峰' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(6, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(7, 7, 7, 7, 7)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '五峰' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(6, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '五峰' and x[1] == '完成']))),
                              style1)
                xlsheet.write(7, 0, '兴山', style1)
                xlsheet.write(7, 1, len([x for x in msg_list if x[0] == '兴山']), style1)
                xlsheet.write(7, 2, len([x for x in msg_list1 if x[0] == '兴山' ]), style1)
                xlsheet.write(7, 3, len([x for x in msg_list if x[0] == '兴山' and x[1] == '完成' and x[2] == '是']), style1)
                xlsheet.write(7, 4, len([x for x in msg_list if x[0] == '兴山' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(7, 5, len([x for x in msg_list if x[0] == '兴山' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(7, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(8, 8, 8, 8, 8)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '兴山' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(7, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '兴山' and x[1] == '完成']))),
                              style1)
                xlsheet.write(8, 0, '夷陵', style1)
                xlsheet.write(8, 1, len([x for x in msg_list if x[0] == '夷陵']), style1)
                xlsheet.write(8, 2, len([x for x in msg_list1 if x[0] == '夷陵' ]), style1)
                xlsheet.write(8, 3, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '完成' and x[2] == '是']), style1)
                xlsheet.write(8, 4, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(8, 5, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(8, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(9, 9, 9, 9, 9)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '夷陵' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(8, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '完成']))),
                              style1)
                xlsheet.write(9, 0, '宜都', style1)
                xlsheet.write(9, 1, len([x for x in msg_list if x[0] == '宜都']), style1)
                xlsheet.write(9, 2, len([x for x in msg_list1 if x[0] == '宜都' ]), style1)
                xlsheet.write(9, 3, len([x for x in msg_list if x[0] == '宜都' and x[1] == '完成' and x[2] == '是']), style1)
                xlsheet.write(9, 4, len([x for x in msg_list if x[0] == '宜都' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(9, 5, len([x for x in msg_list if x[0] == '宜都' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(9, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(10, 10, 10, 10, 10)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '宜都' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(9, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '宜都' and x[1] == '完成']))),
                              style1)
                xlsheet.write(10, 0, '远安', style1)
                xlsheet.write(10, 1, len([x for x in msg_list if x[0] == '远安']), style1)
                xlsheet.write(10, 2, len([x for x in msg_list1 if x[0] == '远安' ]), style1)
                xlsheet.write(10, 3, len([x for x in msg_list if x[0] == '远安' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(10, 4, len([x for x in msg_list if x[0] == '远安' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(10, 5, len([x for x in msg_list if x[0] == '远安' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(10, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(11, 11, 11, 11, 11)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '远安' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(10, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '远安' and x[1] == '完成']))),
                              style1)

                xlsheet.write(11, 0, '长阳', style1)
                xlsheet.write(11, 1, len([x for x in msg_list if x[0] == '长阳']), style1)
                xlsheet.write(11, 2, len([x for x in msg_list1 if x[0] == '长阳' ]), style1)
                xlsheet.write(11, 3, len([x for x in msg_list if x[0] == '长阳' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(11, 4, len([x for x in msg_list if x[0] == '长阳' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(11, 5, len([x for x in msg_list if x[0] == '长阳' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(11, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(12, 12, 12, 12, 12)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '长阳' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(11, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '长阳' and x[1] == '完成']))),
                              style1)

                xlsheet.write(12, 0, '枝江', style1)
                xlsheet.write(12, 1, len([x for x in msg_list if x[0] == '枝江']), style1)
                xlsheet.write(12, 2, len([x for x in msg_list1 if x[0] == '枝江' ]), style1)
                xlsheet.write(12, 3, len([x for x in msg_list if x[0] == '枝江' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(12, 4, len([x for x in msg_list if x[0] == '枝江' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(12, 5, len([x for x in msg_list if x[0] == '枝江' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(12, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(13, 13, 13, 13, 13)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '枝江' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(12, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '枝江' and x[1] == '完成']))),
                              style1)

                xlsheet.write(13, 0, '秭归', style1)
                xlsheet.write(13, 1, len([x for x in msg_list if x[0] == '秭归']), style1)
                xlsheet.write(13, 2, len([x for x in msg_list1 if x[0] == '秭归']), style1)
                xlsheet.write(13, 3, len([x for x in msg_list if x[0] == '秭归' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(13, 4, len([x for x in msg_list if x[0] == '秭归' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(13, 5, len([x for x in msg_list if x[0] == '秭归' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(13, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(14, 14, 14, 14, 14)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '秭归' and x[1] == '完成']:
                    all_time = all_time + i[-1]

                xlsheet.write(13, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '秭归' and x[1] == '完成']))),
                              style1)

                xlsheet.write(14, 0, '全市', style1)
                xlsheet.write(14, 1, xlwt.Formula("(B4+B5+B6+B7+B8+B9+B10+B11+B12+B13+B14)"), style1)
                xlsheet.write(14, 2, xlwt.Formula("(C4+C5+C6+C7+C8+C9+C10+C11+C12+C13+C14)"), style1)
                xlsheet.write(14, 3, xlwt.Formula("(D4+D5+D6+D7+D8+D9+D10+D11+D12+D13+D14)"), style1)
                xlsheet.write(14, 4, xlwt.Formula("(E4+E5+E6+E7+E8+E9+E10+E11+E12+E13+E14)"), style1)
                xlsheet.write(14, 5, xlwt.Formula("(F4+F5+F6+F7+F8+F9+F10+F11+F12+F13+F14)"), style1)
                xlsheet.write(14, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(15, 15, 15, 15, 15)), style4)
                xlsheet.write(14, 7, xlwt.Formula("(H4+H5+H6+H7+H8+H9+H10+H11+H12+H13+H14)/11"), style1)
                xlsname=choose_type + str(int(time.time()))

                workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
                return ('mail.itlaolang.com/downfile/{}.xls'.format(xlsname))

            if choose_type == '宽带装机':
                for x in range(1, sheet.nrows):
                    try:
                        msg = sheet.row_values(x)
                        #这是之间段之内完成的工单数据
                        if msg[9] != 'order_status_6' and msg[3] == '宽带装机' and utc_str_to_timestamp(msg[15]) >= utc_str_to_timestamp(
                                starttime) and utc_str_to_timestamp(msg[15]) <= utc_str_to_timestamp(endtime) \
                                and msg[19] != '普服小区' and msg[19] != '普遍服务':
                            finshed=[find_area(msg[1], msg[11])]
                            msg_list1.append(finshed)
                        #这是时间段之内受理工单数据
                        if msg[9] != 'order_status_6' and msg[3] == '宽带装机' and utc_str_to_timestamp(msg[12]) >= utc_str_to_timestamp(
                                starttime) and utc_str_to_timestamp(msg[12]) <= utc_str_to_timestamp(endtime) \
                                and msg[19] != '普服小区' and msg[19] != '普遍服务':
                            result = [find_area(msg[1], msg[11]), get_status(msg[15],starttime,endtime),
                                      get_timeout(msg[12], msg[15], msg[19]), downdan(msg[12]),
                                      time_for_end(msg[12], msg[15])]
                            # print(result)
                            msg_list.append(result)

                    except:
                        pass
                # print(len([x for x in msg_list if x[0] == '枝江']))
                # print(len([x for x in msg_list if x[0] == '枝江' and x[1]=='完成']))
                # print(len([x for x in msg_list if x[0] == '枝江' and x[1]=='完成' and x[2]=='是']))
                # print(len([x for x in msg_list if x[0] == '枝江' and x[1]=='未完成' and x[2]=='是']))
                # print(len([x for x in msg_list if x[0] == '枝江' and x[1]=='未完成' and x[3]==1]))
                all_time = 0
                print(len([x for x in msg_list if x[0] == '夷陵' and x[1] == '完成']))
                for i in [x for x in msg_list if x[0] == '夷陵' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                # print(all_time)
                # print(av_time(all_time,len([x for x in msg_list if x[0] == '夷陵' and x[1] == '完成'])))
                print('%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '完成']))))

                workbook_m = xlwt.Workbook(encoding='utf-8')
                xlsheet = workbook_m.add_sheet('24小时装机日报（不含农普）', cell_overwrite_ok=True)
                # 格式1 （有自动换行）
                style1 = xlwt.easyxf('pattern: pattern solid, fore_colour white')
                style1.font.height = 200
                style1.font.name = u'文泉驿点阵正黑'
                style1.font.colour_index = 0
                style1.borders.left = xlwt.Borders.THIN
                style1.borders.right = xlwt.Borders.THIN
                style1.borders.top = xlwt.Borders.THIN
                style1.borders.bottom = xlwt.Borders.THIN
                # style1.font.bold = True
                style1.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
                style1.alignment.horz = xlwt.Alignment.HORZ_CENTER

                # 格式2  （没有自动换行）
                style2 = xlwt.easyxf('pattern: pattern solid, fore_colour white')
                style2.font.height = 200
                style2.font.name = u'文泉驿点阵正黑'
                style2.font.colour_index = 0
                style2.borders.left = xlwt.Borders.THIN
                style2.borders.right = xlwt.Borders.THIN
                style2.borders.top = xlwt.Borders.THIN
                style2.borders.bottom = xlwt.Borders.THIN

                # style2.font.bold = True
                # style2.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
                # style2.alignment.horz = xlwt.Alignment.HORZ_CENTER

                # 格式3 黄色背景色

                style3 = xlwt.easyxf('pattern: pattern solid, fore_colour yellow')
                style3.font.height = 200
                style3.font.name = u'文泉驿点阵正黑'
                style3.font.colour_index = 0
                # style3.borders.left = xlwt.Borders.THIN
                # style3.borders.right = xlwt.Borders.THIN
                # style3.borders.top = xlwt.Borders.THIN
                # style3.borders.bottom = xlwt.Borders.THIN

                # style4 格式4 0.00%

                style4 = xlwt.easyxf('pattern: pattern solid, fore_colour white')
                style4.font.height = 200
                style4.font.name = u'文泉驿点阵正黑'
                style4.font.colour_index = 0
                style4.borders.left = xlwt.Borders.THIN
                style4.borders.right = xlwt.Borders.THIN
                style4.borders.top = xlwt.Borders.THIN
                style4.borders.bottom = xlwt.Borders.THIN
                # style1.font.bold = True
                style4.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
                style4.alignment.horz = xlwt.Alignment.HORZ_CENTER
                style4.num_format_str = '0.00%'

                # style2.font.bold = True
                # style2.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
                # style2.alignment.horz = xlwt.Alignment.HORZ_CENTER
                # 写excel表头
                # 设置单元格
                xlsheet.write(0, 0, '起始时间：', style3)
                xlsheet.write(0, 1, starttime, style1)
                xlsheet.write(0, 3, '截止时间：', style3)
                xlsheet.write(0, 4, endtime, style1)
                xlsheet.write(0, 6, '工单类型：', style3)
                xlsheet.write(0, 7, choose_type, style3)
                xlsheet.write(1, 0, '区县（区域属性）', style1)
                xlsheet.write(1, 1, '当日受理工单量', style1)
                xlsheet.write(1, 2, '当日装机完成量', style1)
                xlsheet.write(1, 3, '已装超时量', style1)
                xlsheet.write(1, 4, '未装超时量', style1)
                xlsheet.write(1, 5, '压单量', style1)
                xlsheet.write(1, 6, '装机及时率', style1)
                xlsheet.write(1, 7, '平均装机时长（小时）', style1)
                xlsheet.write(2, 0, '备注', style1)
                xlsheet.write(2, 1, '本月受理的所有单子', style1)
                xlsheet.write(2, 2, '本月完成的所有单子', style1)
                xlsheet.write(2, 3, '已完成的超时工单（城区24小时、乡镇36小时）', style1)
                xlsheet.write(2, 4, '未完成的超时工单', style1)
                xlsheet.write(2, 5, '本月之前受理，且还没完成', style1)
                xlsheet.write(2, 6, '(受理工单量-已装超时量-未装超时量-本月以前压单量)/受理工单量', style1)
                xlsheet.write(2, 7, '已完成单子共花费时间/完成单子数', style1)
                xlsheet.write(3, 0, '城区', style1)
                xlsheet.write(3, 1, len([x for x in msg_list if x[0] == '宜昌城区']), style1)
                xlsheet.write(3, 2, len([x for x in msg_list1 if x[0] == '宜昌城区']), style1)
                xlsheet.write(3, 3, len([x for x in msg_list if x[0] == '宜昌城区' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(3, 4, len([x for x in msg_list if x[0] == '宜昌城区' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(3, 5, len([x for x in msg_list if x[0] == '宜昌城区' and x[1] == '未完成' and x[3] == 1]),
                              style1)
                xlsheet.write(3, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(4, 4, 4, 4, 4)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '宜昌城区' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(3, 7, '%.2f' % (
                    av_time(all_time, len([x for x in msg_list if x[0] == '宜昌城区' and x[1] == '完成']))), style1)

                xlsheet.write(4, 0, '当阳', style1)
                xlsheet.write(4, 1, len([x for x in msg_list if x[0] == '当阳']), style1)
                xlsheet.write(4, 2, len([x for x in msg_list1 if x[0] == '当阳' ]), style1)
                xlsheet.write(4, 3, len([x for x in msg_list if x[0] == '当阳' and x[1] == '完成' and x[2] == '是']), style1)
                xlsheet.write(4, 4, len([x for x in msg_list if x[0] == '当阳' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(4, 5, len([x for x in msg_list if x[0] == '当阳' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(4, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(5, 5, 5, 5, 5)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '当阳' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(4, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '当阳' and x[1] == '完成']))),
                              style1)
                xlsheet.write(5, 0, '开发区', style1)
                xlsheet.write(5, 1, len([x for x in msg_list if x[0] == '宜昌开发区']), style1)
                xlsheet.write(5, 2, len([x for x in msg_list1 if x[0] == '宜昌开发区']), style1)
                xlsheet.write(5, 3, len([x for x in msg_list if x[0] == '宜昌开发区' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(5, 4, len([x for x in msg_list if x[0] == '宜昌开发区' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(5, 5, len([x for x in msg_list if x[0] == '宜昌开发区' and x[1] == '未完成' and x[3] == 1]),
                              style1)
                xlsheet.write(5, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(6, 6, 6, 6, 6)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '宜昌开发区' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(5, 7, '%.2f' % (
                    av_time(all_time, len([x for x in msg_list if x[0] == '宜昌开发区' and x[1] == '完成']))),
                              style1)
                xlsheet.write(6, 0, '五峰', style1)
                xlsheet.write(6, 1, len([x for x in msg_list if x[0] == '五峰']), style1)
                xlsheet.write(6, 2, len([x for x in msg_list1 if x[0] == '五峰' ]), style1)
                xlsheet.write(6, 3, len([x for x in msg_list if x[0] == '五峰' and x[1] == '完成' and x[2] == '是']), style1)
                xlsheet.write(6, 4, len([x for x in msg_list if x[0] == '五峰' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(6, 5, len([x for x in msg_list if x[0] == '五峰' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(6, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(7, 7, 7, 7, 7)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '五峰' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(6, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '五峰' and x[1] == '完成']))),
                              style1)
                xlsheet.write(7, 0, '兴山', style1)
                xlsheet.write(7, 1, len([x for x in msg_list if x[0] == '兴山']), style1)
                xlsheet.write(7, 2, len([x for x in msg_list1 if x[0] == '兴山' ]), style1)
                xlsheet.write(7, 3, len([x for x in msg_list if x[0] == '兴山' and x[1] == '完成' and x[2] == '是']), style1)
                xlsheet.write(7, 4, len([x for x in msg_list if x[0] == '兴山' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(7, 5, len([x for x in msg_list if x[0] == '兴山' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(7, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(8, 8, 8, 8, 8)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '兴山' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(7, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '兴山' and x[1] == '完成']))),
                              style1)
                xlsheet.write(8, 0, '夷陵', style1)
                xlsheet.write(8, 1, len([x for x in msg_list if x[0] == '夷陵']), style1)
                xlsheet.write(8, 2, len([x for x in msg_list1 if x[0] == '夷陵' ]), style1)
                xlsheet.write(8, 3, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '完成' and x[2] == '是']), style1)
                xlsheet.write(8, 4, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(8, 5, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(8, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(9, 9, 9, 9, 9)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '夷陵' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(8, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '完成']))),
                              style1)
                xlsheet.write(9, 0, '宜都', style1)
                xlsheet.write(9, 1, len([x for x in msg_list if x[0] == '宜都']), style1)
                xlsheet.write(9, 2, len([x for x in msg_list1 if x[0] == '宜都' ]), style1)
                xlsheet.write(9, 3, len([x for x in msg_list if x[0] == '宜都' and x[1] == '完成' and x[2] == '是']), style1)
                xlsheet.write(9, 4, len([x for x in msg_list if x[0] == '宜都' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(9, 5, len([x for x in msg_list if x[0] == '宜都' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(9, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(10, 10, 10, 10, 10)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '宜都' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(9, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '宜都' and x[1] == '完成']))),
                              style1)
                xlsheet.write(10, 0, '远安', style1)
                xlsheet.write(10, 1, len([x for x in msg_list if x[0] == '远安']), style1)
                xlsheet.write(10, 2, len([x for x in msg_list1 if x[0] == '远安' ]), style1)
                xlsheet.write(10, 3, len([x for x in msg_list if x[0] == '远安' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(10, 4, len([x for x in msg_list if x[0] == '远安' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(10, 5, len([x for x in msg_list if x[0] == '远安' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(10, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(11, 11, 11, 11, 11)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '远安' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(10, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '远安' and x[1] == '完成']))),
                              style1)

                xlsheet.write(11, 0, '长阳', style1)
                xlsheet.write(11, 1, len([x for x in msg_list if x[0] == '长阳']), style1)
                xlsheet.write(11, 2, len([x for x in msg_list1 if x[0] == '长阳' ]), style1)
                xlsheet.write(11, 3, len([x for x in msg_list if x[0] == '长阳' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(11, 4, len([x for x in msg_list if x[0] == '长阳' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(11, 5, len([x for x in msg_list if x[0] == '长阳' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(11, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(12, 12, 12, 12, 12)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '长阳' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(11, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '长阳' and x[1] == '完成']))),
                              style1)

                xlsheet.write(12, 0, '枝江', style1)
                xlsheet.write(12, 1, len([x for x in msg_list if x[0] == '枝江']), style1)
                xlsheet.write(12, 2, len([x for x in msg_list1 if x[0] == '枝江' ]), style1)
                xlsheet.write(12, 3, len([x for x in msg_list if x[0] == '枝江' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(12, 4, len([x for x in msg_list if x[0] == '枝江' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(12, 5, len([x for x in msg_list if x[0] == '枝江' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(12, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(13, 13, 13, 13, 13)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '枝江' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(12, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '枝江' and x[1] == '完成']))),
                              style1)

                xlsheet.write(13, 0, '秭归', style1)
                xlsheet.write(13, 1, len([x for x in msg_list if x[0] == '秭归']), style1)
                xlsheet.write(13, 2, len([x for x in msg_list1 if x[0] == '秭归']), style1)
                xlsheet.write(13, 3, len([x for x in msg_list if x[0] == '秭归' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(13, 4, len([x for x in msg_list if x[0] == '秭归' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(13, 5, len([x for x in msg_list if x[0] == '秭归' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(13, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(14, 14, 14, 14, 14)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '秭归' and x[1] == '完成']:
                    all_time = all_time + i[-1]

                xlsheet.write(13, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '秭归' and x[1] == '完成']))),
                              style1)

                xlsheet.write(14, 0, '全市', style1)
                xlsheet.write(14, 1, xlwt.Formula("(B4+B5+B6+B7+B8+B9+B10+B11+B12+B13+B14)"), style1)
                xlsheet.write(14, 2, xlwt.Formula("(C4+C5+C6+C7+C8+C9+C10+C11+C12+C13+C14)"), style1)
                xlsheet.write(14, 3, xlwt.Formula("(D4+D5+D6+D7+D8+D9+D10+D11+D12+D13+D14)"), style1)
                xlsheet.write(14, 4, xlwt.Formula("(E4+E5+E6+E7+E8+E9+E10+E11+E12+E13+E14)"), style1)
                xlsheet.write(14, 5, xlwt.Formula("(F4+F5+F6+F7+F8+F9+F10+F11+F12+F13+F14)"), style1)
                xlsheet.write(14, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(15, 15, 15, 15, 15)), style4)
                xlsheet.write(14, 7, xlwt.Formula("(H4+H5+H6+H7+H8+H9+H10+H11+H12+H13+H14)/11"), style1)
                xlsname=choose_type + str(int(time.time()))

                workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
                return ('mail.itlaolang.com/downfile/{}.xls'.format(xlsname))
        if type=='装机8小时报表':

            if choose_type == '全量工单':
                for x in range(1, sheet.nrows):
                    try:
                        msg = sheet.row_values(x)
                        #这是之间段之内完成的工单数据
                        if msg[9] != 'order_status_6' and utc_str_to_timestamp(msg[15]) >= utc_str_to_timestamp(
                                starttime) and utc_str_to_timestamp(msg[15]) <= utc_str_to_timestamp(endtime) \
                                and msg[19] != '普服小区' and msg[19] != '普遍服务':
                            finshed=[find_area(msg[1], msg[11])]
                            msg_list1.append(finshed)
                        #这是时间段之内受理工单数据
                        if msg[9] != 'order_status_6' and utc_str_to_timestamp(msg[12]) >= utc_str_to_timestamp(
                                starttime) and utc_str_to_timestamp(msg[12]) <= utc_str_to_timestamp(endtime) \
                                and msg[19] != '普服小区' and msg[19] != '普遍服务':
                            result = [find_area(msg[1], msg[11]), get_status(msg[15],starttime,endtime),
                                      get_timeout_8(msg[12], msg[15], msg[19]), downdan(msg[12]),
                                      time_for_end(msg[12], msg[15])]
                            # print(result)
                            msg_list.append(result)

                    except:
                        pass
                # print(len([x for x in msg_list if x[0] == '枝江']))
                # print(len([x for x in msg_list if x[0] == '枝江' and x[1]=='完成']))
                # print(len([x for x in msg_list if x[0] == '枝江' and x[1]=='完成' and x[2]=='是']))
                # print(len([x for x in msg_list if x[0] == '枝江' and x[1]=='未完成' and x[2]=='是']))
                # print(len([x for x in msg_list if x[0] == '枝江' and x[1]=='未完成' and x[3]==1]))
                all_time = 0
                print(len([x for x in msg_list if x[0] == '夷陵' and x[1] == '完成']))
                for i in [x for x in msg_list if x[0] == '夷陵' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                # print(all_time)
                # print(av_time(all_time,len([x for x in msg_list if x[0] == '夷陵' and x[1] == '完成'])))
                print('%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '完成']))))

                workbook_m = xlwt.Workbook(encoding='utf-8')
                xlsheet = workbook_m.add_sheet('装机8小时日报', cell_overwrite_ok=True)
                # 格式1 （有自动换行）
                style1 = xlwt.easyxf('pattern: pattern solid, fore_colour white')
                style1.font.height = 200
                style1.font.name = u'文泉驿点阵正黑'
                style1.font.colour_index = 0
                style1.borders.left = xlwt.Borders.THIN
                style1.borders.right = xlwt.Borders.THIN
                style1.borders.top = xlwt.Borders.THIN
                style1.borders.bottom = xlwt.Borders.THIN
                # style1.font.bold = True
                style1.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
                style1.alignment.horz = xlwt.Alignment.HORZ_CENTER

                # 格式2  （没有自动换行）
                style2 = xlwt.easyxf('pattern: pattern solid, fore_colour white')
                style2.font.height = 200
                style2.font.name = u'文泉驿点阵正黑'
                style2.font.colour_index = 0
                style2.borders.left = xlwt.Borders.THIN
                style2.borders.right = xlwt.Borders.THIN
                style2.borders.top = xlwt.Borders.THIN
                style2.borders.bottom = xlwt.Borders.THIN

                # style2.font.bold = True
                # style2.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
                # style2.alignment.horz = xlwt.Alignment.HORZ_CENTER

                # 格式3 黄色背景色

                style3 = xlwt.easyxf('pattern: pattern solid, fore_colour yellow')
                style3.font.height = 200
                style3.font.name = u'文泉驿点阵正黑'
                style3.font.colour_index = 0
                # style3.borders.left = xlwt.Borders.THIN
                # style3.borders.right = xlwt.Borders.THIN
                # style3.borders.top = xlwt.Borders.THIN
                # style3.borders.bottom = xlwt.Borders.THIN

                # style4 格式4 0.00%

                style4 = xlwt.easyxf('pattern: pattern solid, fore_colour white')
                style4.font.height = 200
                style4.font.name = u'文泉驿点阵正黑'
                style4.font.colour_index = 0
                style4.borders.left = xlwt.Borders.THIN
                style4.borders.right = xlwt.Borders.THIN
                style4.borders.top = xlwt.Borders.THIN
                style4.borders.bottom = xlwt.Borders.THIN
                # style1.font.bold = True
                style4.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
                style4.alignment.horz = xlwt.Alignment.HORZ_CENTER
                style4.num_format_str = '0.00%'

                # style2.font.bold = True
                # style2.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
                # style2.alignment.horz = xlwt.Alignment.HORZ_CENTER
                # 写excel表头
                # 设置单元格
                xlsheet.write(0, 0, '起始时间：', style3)
                xlsheet.write(0, 1, starttime, style1)
                xlsheet.write(0, 3, '截止时间：', style3)
                xlsheet.write(0, 4, endtime, style1)
                xlsheet.write(0, 6, '工单类型：', style3)
                xlsheet.write(0, 7, choose_type, style3)
                xlsheet.write(1, 0, '区县（区域属性）', style1)
                xlsheet.write(1, 1, '当日受理工单量', style1)
                xlsheet.write(1, 2, '当日装机完成量', style1)
                xlsheet.write(1, 3, '已装超时量', style1)
                xlsheet.write(1, 4, '未装超时量', style1)
                xlsheet.write(1, 5, '压单量', style1)
                xlsheet.write(1, 6, '装机及时率', style1)
                xlsheet.write(1, 7, '平均装机时长（小时）', style1)
                xlsheet.write(2, 0, '备注', style1)
                xlsheet.write(2, 1, '本月受理的所有单子', style1)
                xlsheet.write(2, 2, '本月完成的所有单子', style1)
                xlsheet.write(2, 3, '已完成的超时工单（城区24小时、乡镇36小时）', style1)
                xlsheet.write(2, 4, '未完成的超时工单', style1)
                xlsheet.write(2, 5, '本月之前受理，且还没完成', style1)
                xlsheet.write(2, 6, '(受理工单量-已装超时量-未装超时量-本月以前压单量)/受理工单量', style1)
                xlsheet.write(2, 7, '已完成单子共花费时间/完成单子数', style1)
                xlsheet.write(3, 0, '城区', style1)
                xlsheet.write(3, 1, len([x for x in msg_list if x[0] == '宜昌城区']), style1)
                xlsheet.write(3, 2, len([x for x in msg_list1 if x[0] == '宜昌城区']), style1)
                xlsheet.write(3, 3, len([x for x in msg_list if x[0] == '宜昌城区' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(3, 4, len([x for x in msg_list if x[0] == '宜昌城区' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(3, 5, len([x for x in msg_list if x[0] == '宜昌城区' and x[1] == '未完成' and x[3] == 1]),
                              style1)
                xlsheet.write(3, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(4, 4, 4, 4, 4)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '宜昌城区' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(3, 7, '%.2f' % (
                    av_time(all_time, len([x for x in msg_list if x[0] == '宜昌城区' and x[1] == '完成']))), style1)

                xlsheet.write(4, 0, '当阳', style1)
                xlsheet.write(4, 1, len([x for x in msg_list if x[0] == '当阳']), style1)
                xlsheet.write(4, 2, len([x for x in msg_list1 if x[0] == '当阳' ]), style1)
                xlsheet.write(4, 3, len([x for x in msg_list if x[0] == '当阳' and x[1] == '完成' and x[2] == '是']), style1)
                xlsheet.write(4, 4, len([x for x in msg_list if x[0] == '当阳' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(4, 5, len([x for x in msg_list if x[0] == '当阳' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(4, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(5, 5, 5, 5, 5)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '当阳' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(4, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '当阳' and x[1] == '完成']))),
                              style1)
                xlsheet.write(5, 0, '开发区', style1)
                xlsheet.write(5, 1, len([x for x in msg_list if x[0] == '宜昌开发区']), style1)
                xlsheet.write(5, 2, len([x for x in msg_list1 if x[0] == '宜昌开发区']), style1)
                xlsheet.write(5, 3, len([x for x in msg_list if x[0] == '宜昌开发区' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(5, 4, len([x for x in msg_list if x[0] == '宜昌开发区' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(5, 5, len([x for x in msg_list if x[0] == '宜昌开发区' and x[1] == '未完成' and x[3] == 1]),
                              style1)
                xlsheet.write(5, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(6, 6, 6, 6, 6)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '宜昌开发区' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(5, 7, '%.2f' % (
                    av_time(all_time, len([x for x in msg_list if x[0] == '宜昌开发区' and x[1] == '完成']))),
                              style1)
                xlsheet.write(6, 0, '五峰', style1)
                xlsheet.write(6, 1, len([x for x in msg_list if x[0] == '五峰']), style1)
                xlsheet.write(6, 2, len([x for x in msg_list1 if x[0] == '五峰' ]), style1)
                xlsheet.write(6, 3, len([x for x in msg_list if x[0] == '五峰' and x[1] == '完成' and x[2] == '是']), style1)
                xlsheet.write(6, 4, len([x for x in msg_list if x[0] == '五峰' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(6, 5, len([x for x in msg_list if x[0] == '五峰' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(6, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(7, 7, 7, 7, 7)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '五峰' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(6, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '五峰' and x[1] == '完成']))),
                              style1)
                xlsheet.write(7, 0, '兴山', style1)
                xlsheet.write(7, 1, len([x for x in msg_list if x[0] == '兴山']), style1)
                xlsheet.write(7, 2, len([x for x in msg_list1 if x[0] == '兴山' ]), style1)
                xlsheet.write(7, 3, len([x for x in msg_list if x[0] == '兴山' and x[1] == '完成' and x[2] == '是']), style1)
                xlsheet.write(7, 4, len([x for x in msg_list if x[0] == '兴山' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(7, 5, len([x for x in msg_list if x[0] == '兴山' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(7, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(8, 8, 8, 8, 8)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '兴山' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(7, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '兴山' and x[1] == '完成']))),
                              style1)
                xlsheet.write(8, 0, '夷陵', style1)
                xlsheet.write(8, 1, len([x for x in msg_list if x[0] == '夷陵']), style1)
                xlsheet.write(8, 2, len([x for x in msg_list1 if x[0] == '夷陵' ]), style1)
                xlsheet.write(8, 3, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '完成' and x[2] == '是']), style1)
                xlsheet.write(8, 4, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(8, 5, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(8, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(9, 9, 9, 9, 9)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '夷陵' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(8, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '完成']))),
                              style1)
                xlsheet.write(9, 0, '宜都', style1)
                xlsheet.write(9, 1, len([x for x in msg_list if x[0] == '宜都']), style1)
                xlsheet.write(9, 2, len([x for x in msg_list1 if x[0] == '宜都' ]), style1)
                xlsheet.write(9, 3, len([x for x in msg_list if x[0] == '宜都' and x[1] == '完成' and x[2] == '是']), style1)
                xlsheet.write(9, 4, len([x for x in msg_list if x[0] == '宜都' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(9, 5, len([x for x in msg_list if x[0] == '宜都' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(9, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(10, 10, 10, 10, 10)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '宜都' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(9, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '宜都' and x[1] == '完成']))),
                              style1)
                xlsheet.write(10, 0, '远安', style1)
                xlsheet.write(10, 1, len([x for x in msg_list if x[0] == '远安']), style1)
                xlsheet.write(10, 2, len([x for x in msg_list1 if x[0] == '远安' ]), style1)
                xlsheet.write(10, 3, len([x for x in msg_list if x[0] == '远安' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(10, 4, len([x for x in msg_list if x[0] == '远安' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(10, 5, len([x for x in msg_list if x[0] == '远安' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(10, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(11, 11, 11, 11, 11)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '远安' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(10, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '远安' and x[1] == '完成']))),
                              style1)

                xlsheet.write(11, 0, '长阳', style1)
                xlsheet.write(11, 1, len([x for x in msg_list if x[0] == '长阳']), style1)
                xlsheet.write(11, 2, len([x for x in msg_list1 if x[0] == '长阳' ]), style1)
                xlsheet.write(11, 3, len([x for x in msg_list if x[0] == '长阳' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(11, 4, len([x for x in msg_list if x[0] == '长阳' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(11, 5, len([x for x in msg_list if x[0] == '长阳' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(11, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(12, 12, 12, 12, 12)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '长阳' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(11, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '长阳' and x[1] == '完成']))),
                              style1)

                xlsheet.write(12, 0, '枝江', style1)
                xlsheet.write(12, 1, len([x for x in msg_list if x[0] == '枝江']), style1)
                xlsheet.write(12, 2, len([x for x in msg_list1 if x[0] == '枝江' ]), style1)
                xlsheet.write(12, 3, len([x for x in msg_list if x[0] == '枝江' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(12, 4, len([x for x in msg_list if x[0] == '枝江' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(12, 5, len([x for x in msg_list if x[0] == '枝江' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(12, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(13, 13, 13, 13, 13)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '枝江' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(12, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '枝江' and x[1] == '完成']))),
                              style1)

                xlsheet.write(13, 0, '秭归', style1)
                xlsheet.write(13, 1, len([x for x in msg_list if x[0] == '秭归']), style1)
                xlsheet.write(13, 2, len([x for x in msg_list1 if x[0] == '秭归']), style1)
                xlsheet.write(13, 3, len([x for x in msg_list if x[0] == '秭归' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(13, 4, len([x for x in msg_list if x[0] == '秭归' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(13, 5, len([x for x in msg_list if x[0] == '秭归' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(13, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(14, 14, 14, 14, 14)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '秭归' and x[1] == '完成']:
                    all_time = all_time + i[-1]

                xlsheet.write(13, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '秭归' and x[1] == '完成']))),
                              style1)

                xlsheet.write(14, 0, '全市', style1)
                xlsheet.write(14, 1, xlwt.Formula("(B4+B5+B6+B7+B8+B9+B10+B11+B12+B13+B14)"), style1)
                xlsheet.write(14, 2, xlwt.Formula("(C4+C5+C6+C7+C8+C9+C10+C11+C12+C13+C14)"), style1)
                xlsheet.write(14, 3, xlwt.Formula("(D4+D5+D6+D7+D8+D9+D10+D11+D12+D13+D14)"), style1)
                xlsheet.write(14, 4, xlwt.Formula("(E4+E5+E6+E7+E8+E9+E10+E11+E12+E13+E14)"), style1)
                xlsheet.write(14, 5, xlwt.Formula("(F4+F5+F6+F7+F8+F9+F10+F11+F12+F13+F14)"), style1)
                xlsheet.write(14, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(15, 15, 15, 15, 15)), style4)
                xlsheet.write(14, 7, xlwt.Formula("(H4+H5+H6+H7+H8+H9+H10+H11+H12+H13+H14)/11"), style1)
                xlsname=choose_type + str(int(time.time()))

                workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
                return ('mail.itlaolang.com/downfile/{}.xls'.format(xlsname))

            if choose_type == '移机装':
                for x in range(1, sheet.nrows):
                    try:
                        msg = sheet.row_values(x)
                        #这是之间段之内完成的工单数据
                        if msg[9] != 'order_status_6' and msg[3] == '移机装' and utc_str_to_timestamp(msg[15]) >= utc_str_to_timestamp(
                                starttime) and utc_str_to_timestamp(msg[15]) <= utc_str_to_timestamp(endtime) \
                                and msg[19] != '普服小区' and msg[19] != '普遍服务':
                            finshed=[find_area(msg[1], msg[11])]
                            msg_list1.append(finshed)
                        #这是时间段之内受理工单数据
                        if msg[9] != 'order_status_6' and msg[3] == '移机装' and utc_str_to_timestamp(msg[12]) >= utc_str_to_timestamp(
                                starttime) and utc_str_to_timestamp(msg[12]) <= utc_str_to_timestamp(endtime) \
                                and msg[19] != '普服小区' and msg[19] != '普遍服务':
                            result = [find_area(msg[1], msg[11]), get_status(msg[15],starttime,endtime),
                                      get_timeout_8(msg[12], msg[15], msg[19]), downdan(msg[12]),
                                      time_for_end(msg[12], msg[15])]
                            # print(result)
                            msg_list.append(result)

                    except:
                        pass
                # print(len([x for x in msg_list if x[0] == '枝江']))
                # print(len([x for x in msg_list if x[0] == '枝江' and x[1]=='完成']))
                # print(len([x for x in msg_list if x[0] == '枝江' and x[1]=='完成' and x[2]=='是']))
                # print(len([x for x in msg_list if x[0] == '枝江' and x[1]=='未完成' and x[2]=='是']))
                # print(len([x for x in msg_list if x[0] == '枝江' and x[1]=='未完成' and x[3]==1]))
                all_time = 0
                print(len([x for x in msg_list if x[0] == '夷陵' and x[1] == '完成']))
                for i in [x for x in msg_list if x[0] == '夷陵' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                # print(all_time)
                # print(av_time(all_time,len([x for x in msg_list if x[0] == '夷陵' and x[1] == '完成'])))
                print('%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '完成']))))

                workbook_m = xlwt.Workbook(encoding='utf-8')
                xlsheet = workbook_m.add_sheet('装机8小时日报', cell_overwrite_ok=True)
                # 格式1 （有自动换行）
                style1 = xlwt.easyxf('pattern: pattern solid, fore_colour white')
                style1.font.height = 200
                style1.font.name = u'文泉驿点阵正黑'
                style1.font.colour_index = 0
                style1.borders.left = xlwt.Borders.THIN
                style1.borders.right = xlwt.Borders.THIN
                style1.borders.top = xlwt.Borders.THIN
                style1.borders.bottom = xlwt.Borders.THIN
                # style1.font.bold = True
                style1.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
                style1.alignment.horz = xlwt.Alignment.HORZ_CENTER

                # 格式2  （没有自动换行）
                style2 = xlwt.easyxf('pattern: pattern solid, fore_colour white')
                style2.font.height = 200
                style2.font.name = u'文泉驿点阵正黑'
                style2.font.colour_index = 0
                style2.borders.left = xlwt.Borders.THIN
                style2.borders.right = xlwt.Borders.THIN
                style2.borders.top = xlwt.Borders.THIN
                style2.borders.bottom = xlwt.Borders.THIN

                # style2.font.bold = True
                # style2.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
                # style2.alignment.horz = xlwt.Alignment.HORZ_CENTER

                # 格式3 黄色背景色

                style3 = xlwt.easyxf('pattern: pattern solid, fore_colour yellow')
                style3.font.height = 200
                style3.font.name = u'文泉驿点阵正黑'
                style3.font.colour_index = 0
                # style3.borders.left = xlwt.Borders.THIN
                # style3.borders.right = xlwt.Borders.THIN
                # style3.borders.top = xlwt.Borders.THIN
                # style3.borders.bottom = xlwt.Borders.THIN

                # style4 格式4 0.00%

                style4 = xlwt.easyxf('pattern: pattern solid, fore_colour white')
                style4.font.height = 200
                style4.font.name = u'文泉驿点阵正黑'
                style4.font.colour_index = 0
                style4.borders.left = xlwt.Borders.THIN
                style4.borders.right = xlwt.Borders.THIN
                style4.borders.top = xlwt.Borders.THIN
                style4.borders.bottom = xlwt.Borders.THIN
                # style1.font.bold = True
                style4.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
                style4.alignment.horz = xlwt.Alignment.HORZ_CENTER
                style4.num_format_str = '0.00%'

                # style2.font.bold = True
                # style2.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
                # style2.alignment.horz = xlwt.Alignment.HORZ_CENTER
                # 写excel表头
                # 设置单元格
                xlsheet.write(0, 0, '起始时间：', style3)
                xlsheet.write(0, 1, starttime, style1)
                xlsheet.write(0, 3, '截止时间：', style3)
                xlsheet.write(0, 4, endtime, style1)
                xlsheet.write(0, 6, '工单类型：', style3)
                xlsheet.write(0, 7, choose_type, style3)
                xlsheet.write(1, 0, '区县（区域属性）', style1)
                xlsheet.write(1, 1, '当日受理工单量', style1)
                xlsheet.write(1, 2, '当日装机完成量', style1)
                xlsheet.write(1, 3, '已装超时量', style1)
                xlsheet.write(1, 4, '未装超时量', style1)
                xlsheet.write(1, 5, '压单量', style1)
                xlsheet.write(1, 6, '装机及时率', style1)
                xlsheet.write(1, 7, '平均装机时长（小时）', style1)
                xlsheet.write(2, 0, '备注', style1)
                xlsheet.write(2, 1, '本月受理的所有单子', style1)
                xlsheet.write(2, 2, '本月完成的所有单子', style1)
                xlsheet.write(2, 3, '已完成的超时工单（城区24小时、乡镇36小时）', style1)
                xlsheet.write(2, 4, '未完成的超时工单', style1)
                xlsheet.write(2, 5, '本月之前受理，且还没完成', style1)
                xlsheet.write(2, 6, '(受理工单量-已装超时量-未装超时量-本月以前压单量)/受理工单量', style1)
                xlsheet.write(2, 7, '已完成单子共花费时间/完成单子数', style1)
                xlsheet.write(3, 0, '城区', style1)
                xlsheet.write(3, 1, len([x for x in msg_list if x[0] == '宜昌城区']), style1)
                xlsheet.write(3, 2, len([x for x in msg_list1 if x[0] == '宜昌城区']), style1)
                xlsheet.write(3, 3, len([x for x in msg_list if x[0] == '宜昌城区' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(3, 4, len([x for x in msg_list if x[0] == '宜昌城区' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(3, 5, len([x for x in msg_list if x[0] == '宜昌城区' and x[1] == '未完成' and x[3] == 1]),
                              style1)
                xlsheet.write(3, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(4, 4, 4, 4, 4)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '宜昌城区' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(3, 7, '%.2f' % (
                    av_time(all_time, len([x for x in msg_list if x[0] == '宜昌城区' and x[1] == '完成']))), style1)

                xlsheet.write(4, 0, '当阳', style1)
                xlsheet.write(4, 1, len([x for x in msg_list if x[0] == '当阳']), style1)
                xlsheet.write(4, 2, len([x for x in msg_list1 if x[0] == '当阳' ]), style1)
                xlsheet.write(4, 3, len([x for x in msg_list if x[0] == '当阳' and x[1] == '完成' and x[2] == '是']), style1)
                xlsheet.write(4, 4, len([x for x in msg_list if x[0] == '当阳' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(4, 5, len([x for x in msg_list if x[0] == '当阳' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(4, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(5, 5, 5, 5, 5)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '当阳' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(4, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '当阳' and x[1] == '完成']))),
                              style1)
                xlsheet.write(5, 0, '开发区', style1)
                xlsheet.write(5, 1, len([x for x in msg_list if x[0] == '宜昌开发区']), style1)
                xlsheet.write(5, 2, len([x for x in msg_list1 if x[0] == '宜昌开发区']), style1)
                xlsheet.write(5, 3, len([x for x in msg_list if x[0] == '宜昌开发区' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(5, 4, len([x for x in msg_list if x[0] == '宜昌开发区' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(5, 5, len([x for x in msg_list if x[0] == '宜昌开发区' and x[1] == '未完成' and x[3] == 1]),
                              style1)
                xlsheet.write(5, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(6, 6, 6, 6, 6)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '宜昌开发区' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(5, 7, '%.2f' % (
                    av_time(all_time, len([x for x in msg_list if x[0] == '宜昌开发区' and x[1] == '完成']))),
                              style1)
                xlsheet.write(6, 0, '五峰', style1)
                xlsheet.write(6, 1, len([x for x in msg_list if x[0] == '五峰']), style1)
                xlsheet.write(6, 2, len([x for x in msg_list1 if x[0] == '五峰' ]), style1)
                xlsheet.write(6, 3, len([x for x in msg_list if x[0] == '五峰' and x[1] == '完成' and x[2] == '是']), style1)
                xlsheet.write(6, 4, len([x for x in msg_list if x[0] == '五峰' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(6, 5, len([x for x in msg_list if x[0] == '五峰' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(6, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(7, 7, 7, 7, 7)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '五峰' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(6, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '五峰' and x[1] == '完成']))),
                              style1)
                xlsheet.write(7, 0, '兴山', style1)
                xlsheet.write(7, 1, len([x for x in msg_list if x[0] == '兴山']), style1)
                xlsheet.write(7, 2, len([x for x in msg_list1 if x[0] == '兴山' ]), style1)
                xlsheet.write(7, 3, len([x for x in msg_list if x[0] == '兴山' and x[1] == '完成' and x[2] == '是']), style1)
                xlsheet.write(7, 4, len([x for x in msg_list if x[0] == '兴山' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(7, 5, len([x for x in msg_list if x[0] == '兴山' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(7, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(8, 8, 8, 8, 8)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '兴山' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(7, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '兴山' and x[1] == '完成']))),
                              style1)
                xlsheet.write(8, 0, '夷陵', style1)
                xlsheet.write(8, 1, len([x for x in msg_list if x[0] == '夷陵']), style1)
                xlsheet.write(8, 2, len([x for x in msg_list1 if x[0] == '夷陵' ]), style1)
                xlsheet.write(8, 3, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '完成' and x[2] == '是']), style1)
                xlsheet.write(8, 4, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(8, 5, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(8, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(9, 9, 9, 9, 9)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '夷陵' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(8, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '完成']))),
                              style1)
                xlsheet.write(9, 0, '宜都', style1)
                xlsheet.write(9, 1, len([x for x in msg_list if x[0] == '宜都']), style1)
                xlsheet.write(9, 2, len([x for x in msg_list1 if x[0] == '宜都' ]), style1)
                xlsheet.write(9, 3, len([x for x in msg_list if x[0] == '宜都' and x[1] == '完成' and x[2] == '是']), style1)
                xlsheet.write(9, 4, len([x for x in msg_list if x[0] == '宜都' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(9, 5, len([x for x in msg_list if x[0] == '宜都' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(9, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(10, 10, 10, 10, 10)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '宜都' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(9, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '宜都' and x[1] == '完成']))),
                              style1)
                xlsheet.write(10, 0, '远安', style1)
                xlsheet.write(10, 1, len([x for x in msg_list if x[0] == '远安']), style1)
                xlsheet.write(10, 2, len([x for x in msg_list1 if x[0] == '远安' ]), style1)
                xlsheet.write(10, 3, len([x for x in msg_list if x[0] == '远安' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(10, 4, len([x for x in msg_list if x[0] == '远安' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(10, 5, len([x for x in msg_list if x[0] == '远安' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(10, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(11, 11, 11, 11, 11)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '远安' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(10, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '远安' and x[1] == '完成']))),
                              style1)

                xlsheet.write(11, 0, '长阳', style1)
                xlsheet.write(11, 1, len([x for x in msg_list if x[0] == '长阳']), style1)
                xlsheet.write(11, 2, len([x for x in msg_list1 if x[0] == '长阳' ]), style1)
                xlsheet.write(11, 3, len([x for x in msg_list if x[0] == '长阳' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(11, 4, len([x for x in msg_list if x[0] == '长阳' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(11, 5, len([x for x in msg_list if x[0] == '长阳' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(11, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(12, 12, 12, 12, 12)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '长阳' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(11, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '长阳' and x[1] == '完成']))),
                              style1)

                xlsheet.write(12, 0, '枝江', style1)
                xlsheet.write(12, 1, len([x for x in msg_list if x[0] == '枝江']), style1)
                xlsheet.write(12, 2, len([x for x in msg_list1 if x[0] == '枝江' ]), style1)
                xlsheet.write(12, 3, len([x for x in msg_list if x[0] == '枝江' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(12, 4, len([x for x in msg_list if x[0] == '枝江' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(12, 5, len([x for x in msg_list if x[0] == '枝江' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(12, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(13, 13, 13, 13, 13)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '枝江' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(12, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '枝江' and x[1] == '完成']))),
                              style1)

                xlsheet.write(13, 0, '秭归', style1)
                xlsheet.write(13, 1, len([x for x in msg_list if x[0] == '秭归']), style1)
                xlsheet.write(13, 2, len([x for x in msg_list1 if x[0] == '秭归']), style1)
                xlsheet.write(13, 3, len([x for x in msg_list if x[0] == '秭归' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(13, 4, len([x for x in msg_list if x[0] == '秭归' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(13, 5, len([x for x in msg_list if x[0] == '秭归' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(13, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(14, 14, 14, 14, 14)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '秭归' and x[1] == '完成']:
                    all_time = all_time + i[-1]

                xlsheet.write(13, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '秭归' and x[1] == '完成']))),
                              style1)

                xlsheet.write(14, 0, '全市', style1)
                xlsheet.write(14, 1, xlwt.Formula("(B4+B5+B6+B7+B8+B9+B10+B11+B12+B13+B14)"), style1)
                xlsheet.write(14, 2, xlwt.Formula("(C4+C5+C6+C7+C8+C9+C10+C11+C12+C13+C14)"), style1)
                xlsheet.write(14, 3, xlwt.Formula("(D4+D5+D6+D7+D8+D9+D10+D11+D12+D13+D14)"), style1)
                xlsheet.write(14, 4, xlwt.Formula("(E4+E5+E6+E7+E8+E9+E10+E11+E12+E13+E14)"), style1)
                xlsheet.write(14, 5, xlwt.Formula("(F4+F5+F6+F7+F8+F9+F10+F11+F12+F13+F14)"), style1)
                xlsheet.write(14, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(15, 15, 15, 15, 15)), style4)
                xlsheet.write(14, 7, xlwt.Formula("(H4+H5+H6+H7+H8+H9+H10+H11+H12+H13+H14)/11"), style1)
                xlsname=choose_type + str(int(time.time()))
                workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
                return ('mail.itlaolang.com/downfile/{}.xls'.format(xlsname))

            if choose_type == 'IMS单独安装':
                for x in range(1, sheet.nrows):
                    try:
                        msg = sheet.row_values(x)
                        #这是之间段之内完成的工单数据
                        if msg[9] != 'order_status_6' and msg[3] == 'IMS单独安装' and utc_str_to_timestamp(msg[15]) >= utc_str_to_timestamp(
                                starttime) and utc_str_to_timestamp(msg[15]) <= utc_str_to_timestamp(endtime) \
                                and msg[19] != '普服小区' and msg[19] != '普遍服务':
                            finshed=[find_area(msg[1], msg[11])]
                            msg_list1.append(finshed)
                        #这是时间段之内受理工单数据
                        if msg[9] != 'order_status_6' and msg[3] == 'IMS单独安装' and utc_str_to_timestamp(msg[12]) >= utc_str_to_timestamp(
                                starttime) and utc_str_to_timestamp(msg[12]) <= utc_str_to_timestamp(endtime) \
                                and msg[19] != '普服小区' and msg[19] != '普遍服务':
                            result = [find_area(msg[1], msg[11]), get_status(msg[15],starttime,endtime),
                                      get_timeout_8(msg[12], msg[15], msg[19]), downdan(msg[12]),
                                      time_for_end(msg[12], msg[15])]
                            # print(result)
                            msg_list.append(result)

                    except:
                        pass
                # print(len([x for x in msg_list if x[0] == '枝江']))
                # print(len([x for x in msg_list if x[0] == '枝江' and x[1]=='完成']))
                # print(len([x for x in msg_list if x[0] == '枝江' and x[1]=='完成' and x[2]=='是']))
                # print(len([x for x in msg_list if x[0] == '枝江' and x[1]=='未完成' and x[2]=='是']))
                # print(len([x for x in msg_list if x[0] == '枝江' and x[1]=='未完成' and x[3]==1]))
                all_time = 0
                print(len([x for x in msg_list if x[0] == '夷陵' and x[1] == '完成']))
                for i in [x for x in msg_list if x[0] == '夷陵' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                # print(all_time)
                # print(av_time(all_time,len([x for x in msg_list if x[0] == '夷陵' and x[1] == '完成'])))
                print('%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '完成']))))

                workbook_m = xlwt.Workbook(encoding='utf-8')
                xlsheet = workbook_m.add_sheet('装机8小时日报', cell_overwrite_ok=True)
                # 格式1 （有自动换行）
                style1 = xlwt.easyxf('pattern: pattern solid, fore_colour white')
                style1.font.height = 200
                style1.font.name = u'文泉驿点阵正黑'
                style1.font.colour_index = 0
                style1.borders.left = xlwt.Borders.THIN
                style1.borders.right = xlwt.Borders.THIN
                style1.borders.top = xlwt.Borders.THIN
                style1.borders.bottom = xlwt.Borders.THIN
                # style1.font.bold = True
                style1.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
                style1.alignment.horz = xlwt.Alignment.HORZ_CENTER

                # 格式2  （没有自动换行）
                style2 = xlwt.easyxf('pattern: pattern solid, fore_colour white')
                style2.font.height = 200
                style2.font.name = u'文泉驿点阵正黑'
                style2.font.colour_index = 0
                style2.borders.left = xlwt.Borders.THIN
                style2.borders.right = xlwt.Borders.THIN
                style2.borders.top = xlwt.Borders.THIN
                style2.borders.bottom = xlwt.Borders.THIN

                # style2.font.bold = True
                # style2.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
                # style2.alignment.horz = xlwt.Alignment.HORZ_CENTER

                # 格式3 黄色背景色

                style3 = xlwt.easyxf('pattern: pattern solid, fore_colour yellow')
                style3.font.height = 200
                style3.font.name = u'文泉驿点阵正黑'
                style3.font.colour_index = 0
                # style3.borders.left = xlwt.Borders.THIN
                # style3.borders.right = xlwt.Borders.THIN
                # style3.borders.top = xlwt.Borders.THIN
                # style3.borders.bottom = xlwt.Borders.THIN

                # style4 格式4 0.00%

                style4 = xlwt.easyxf('pattern: pattern solid, fore_colour white')
                style4.font.height = 200
                style4.font.name = u'文泉驿点阵正黑'
                style4.font.colour_index = 0
                style4.borders.left = xlwt.Borders.THIN
                style4.borders.right = xlwt.Borders.THIN
                style4.borders.top = xlwt.Borders.THIN
                style4.borders.bottom = xlwt.Borders.THIN
                # style1.font.bold = True
                style4.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
                style4.alignment.horz = xlwt.Alignment.HORZ_CENTER
                style4.num_format_str = '0.00%'

                # style2.font.bold = True
                # style2.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
                # style2.alignment.horz = xlwt.Alignment.HORZ_CENTER
                # 写excel表头
                # 设置单元格
                xlsheet.write(0, 0, '起始时间：', style3)
                xlsheet.write(0, 1, starttime, style1)
                xlsheet.write(0, 3, '截止时间：', style3)
                xlsheet.write(0, 4, endtime, style1)
                xlsheet.write(0, 6, '工单类型：', style3)
                xlsheet.write(0, 7, choose_type, style3)
                xlsheet.write(1, 0, '区县（区域属性）', style1)
                xlsheet.write(1, 1, '当日受理工单量', style1)
                xlsheet.write(1, 2, '当日装机完成量', style1)
                xlsheet.write(1, 3, '已装超时量', style1)
                xlsheet.write(1, 4, '未装超时量', style1)
                xlsheet.write(1, 5, '压单量', style1)
                xlsheet.write(1, 6, '装机及时率', style1)
                xlsheet.write(1, 7, '平均装机时长（小时）', style1)
                xlsheet.write(2, 0, '备注', style1)
                xlsheet.write(2, 1, '本月受理的所有单子', style1)
                xlsheet.write(2, 2, '本月完成的所有单子', style1)
                xlsheet.write(2, 3, '已完成的超时工单（城区24小时、乡镇36小时）', style1)
                xlsheet.write(2, 4, '未完成的超时工单', style1)
                xlsheet.write(2, 5, '本月之前受理，且还没完成', style1)
                xlsheet.write(2, 6, '(受理工单量-已装超时量-未装超时量-本月以前压单量)/受理工单量', style1)
                xlsheet.write(2, 7, '已完成单子共花费时间/完成单子数', style1)
                xlsheet.write(3, 0, '城区', style1)
                xlsheet.write(3, 1, len([x for x in msg_list if x[0] == '宜昌城区']), style1)
                xlsheet.write(3, 2, len([x for x in msg_list1 if x[0] == '宜昌城区']), style1)
                xlsheet.write(3, 3, len([x for x in msg_list if x[0] == '宜昌城区' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(3, 4, len([x for x in msg_list if x[0] == '宜昌城区' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(3, 5, len([x for x in msg_list if x[0] == '宜昌城区' and x[1] == '未完成' and x[3] == 1]),
                              style1)
                xlsheet.write(3, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(4, 4, 4, 4, 4)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '宜昌城区' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(3, 7, '%.2f' % (
                    av_time(all_time, len([x for x in msg_list if x[0] == '宜昌城区' and x[1] == '完成']))), style1)

                xlsheet.write(4, 0, '当阳', style1)
                xlsheet.write(4, 1, len([x for x in msg_list if x[0] == '当阳']), style1)
                xlsheet.write(4, 2, len([x for x in msg_list1 if x[0] == '当阳' ]), style1)
                xlsheet.write(4, 3, len([x for x in msg_list if x[0] == '当阳' and x[1] == '完成' and x[2] == '是']), style1)
                xlsheet.write(4, 4, len([x for x in msg_list if x[0] == '当阳' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(4, 5, len([x for x in msg_list if x[0] == '当阳' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(4, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(5, 5, 5, 5, 5)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '当阳' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(4, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '当阳' and x[1] == '完成']))),
                              style1)
                xlsheet.write(5, 0, '开发区', style1)
                xlsheet.write(5, 1, len([x for x in msg_list if x[0] == '宜昌开发区']), style1)
                xlsheet.write(5, 2, len([x for x in msg_list1 if x[0] == '宜昌开发区']), style1)
                xlsheet.write(5, 3, len([x for x in msg_list if x[0] == '宜昌开发区' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(5, 4, len([x for x in msg_list if x[0] == '宜昌开发区' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(5, 5, len([x for x in msg_list if x[0] == '宜昌开发区' and x[1] == '未完成' and x[3] == 1]),
                              style1)
                xlsheet.write(5, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(6, 6, 6, 6, 6)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '宜昌开发区' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(5, 7, '%.2f' % (
                    av_time(all_time, len([x for x in msg_list if x[0] == '宜昌开发区' and x[1] == '完成']))),
                              style1)
                xlsheet.write(6, 0, '五峰', style1)
                xlsheet.write(6, 1, len([x for x in msg_list if x[0] == '五峰']), style1)
                xlsheet.write(6, 2, len([x for x in msg_list1 if x[0] == '五峰' ]), style1)
                xlsheet.write(6, 3, len([x for x in msg_list if x[0] == '五峰' and x[1] == '完成' and x[2] == '是']), style1)
                xlsheet.write(6, 4, len([x for x in msg_list if x[0] == '五峰' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(6, 5, len([x for x in msg_list if x[0] == '五峰' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(6, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(7, 7, 7, 7, 7)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '五峰' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(6, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '五峰' and x[1] == '完成']))),
                              style1)
                xlsheet.write(7, 0, '兴山', style1)
                xlsheet.write(7, 1, len([x for x in msg_list if x[0] == '兴山']), style1)
                xlsheet.write(7, 2, len([x for x in msg_list1 if x[0] == '兴山' ]), style1)
                xlsheet.write(7, 3, len([x for x in msg_list if x[0] == '兴山' and x[1] == '完成' and x[2] == '是']), style1)
                xlsheet.write(7, 4, len([x for x in msg_list if x[0] == '兴山' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(7, 5, len([x for x in msg_list if x[0] == '兴山' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(7, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(8, 8, 8, 8, 8)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '兴山' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(7, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '兴山' and x[1] == '完成']))),
                              style1)
                xlsheet.write(8, 0, '夷陵', style1)
                xlsheet.write(8, 1, len([x for x in msg_list if x[0] == '夷陵']), style1)
                xlsheet.write(8, 2, len([x for x in msg_list1 if x[0] == '夷陵' ]), style1)
                xlsheet.write(8, 3, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '完成' and x[2] == '是']), style1)
                xlsheet.write(8, 4, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(8, 5, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(8, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(9, 9, 9, 9, 9)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '夷陵' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(8, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '完成']))),
                              style1)
                xlsheet.write(9, 0, '宜都', style1)
                xlsheet.write(9, 1, len([x for x in msg_list if x[0] == '宜都']), style1)
                xlsheet.write(9, 2, len([x for x in msg_list1 if x[0] == '宜都' ]), style1)
                xlsheet.write(9, 3, len([x for x in msg_list if x[0] == '宜都' and x[1] == '完成' and x[2] == '是']), style1)
                xlsheet.write(9, 4, len([x for x in msg_list if x[0] == '宜都' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(9, 5, len([x for x in msg_list if x[0] == '宜都' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(9, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(10, 10, 10, 10, 10)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '宜都' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(9, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '宜都' and x[1] == '完成']))),
                              style1)
                xlsheet.write(10, 0, '远安', style1)
                xlsheet.write(10, 1, len([x for x in msg_list if x[0] == '远安']), style1)
                xlsheet.write(10, 2, len([x for x in msg_list1 if x[0] == '远安' ]), style1)
                xlsheet.write(10, 3, len([x for x in msg_list if x[0] == '远安' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(10, 4, len([x for x in msg_list if x[0] == '远安' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(10, 5, len([x for x in msg_list if x[0] == '远安' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(10, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(11, 11, 11, 11, 11)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '远安' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(10, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '远安' and x[1] == '完成']))),
                              style1)

                xlsheet.write(11, 0, '长阳', style1)
                xlsheet.write(11, 1, len([x for x in msg_list if x[0] == '长阳']), style1)
                xlsheet.write(11, 2, len([x for x in msg_list1 if x[0] == '长阳' ]), style1)
                xlsheet.write(11, 3, len([x for x in msg_list if x[0] == '长阳' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(11, 4, len([x for x in msg_list if x[0] == '长阳' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(11, 5, len([x for x in msg_list if x[0] == '长阳' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(11, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(12, 12, 12, 12, 12)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '长阳' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(11, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '长阳' and x[1] == '完成']))),
                              style1)

                xlsheet.write(12, 0, '枝江', style1)
                xlsheet.write(12, 1, len([x for x in msg_list if x[0] == '枝江']), style1)
                xlsheet.write(12, 2, len([x for x in msg_list1 if x[0] == '枝江' ]), style1)
                xlsheet.write(12, 3, len([x for x in msg_list if x[0] == '枝江' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(12, 4, len([x for x in msg_list if x[0] == '枝江' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(12, 5, len([x for x in msg_list if x[0] == '枝江' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(12, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(13, 13, 13, 13, 13)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '枝江' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(12, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '枝江' and x[1] == '完成']))),
                              style1)

                xlsheet.write(13, 0, '秭归', style1)
                xlsheet.write(13, 1, len([x for x in msg_list if x[0] == '秭归']), style1)
                xlsheet.write(13, 2, len([x for x in msg_list1 if x[0] == '秭归']), style1)
                xlsheet.write(13, 3, len([x for x in msg_list if x[0] == '秭归' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(13, 4, len([x for x in msg_list if x[0] == '秭归' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(13, 5, len([x for x in msg_list if x[0] == '秭归' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(13, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(14, 14, 14, 14, 14)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '秭归' and x[1] == '完成']:
                    all_time = all_time + i[-1]

                xlsheet.write(13, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '秭归' and x[1] == '完成']))),
                              style1)

                xlsheet.write(14, 0, '全市', style1)
                xlsheet.write(14, 1, xlwt.Formula("(B4+B5+B6+B7+B8+B9+B10+B11+B12+B13+B14)"), style1)
                xlsheet.write(14, 2, xlwt.Formula("(C4+C5+C6+C7+C8+C9+C10+C11+C12+C13+C14)"), style1)
                xlsheet.write(14, 3, xlwt.Formula("(D4+D5+D6+D7+D8+D9+D10+D11+D12+D13+D14)"), style1)
                xlsheet.write(14, 4, xlwt.Formula("(E4+E5+E6+E7+E8+E9+E10+E11+E12+E13+E14)"), style1)
                xlsheet.write(14, 5, xlwt.Formula("(F4+F5+F6+F7+F8+F9+F10+F11+F12+F13+F14)"), style1)
                xlsheet.write(14, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(15, 15, 15, 15, 15)), style4)
                xlsheet.write(14, 7, xlwt.Formula("(H4+H5+H6+H7+H8+H9+H10+H11+H12+H13+H14)/11"), style1)
                xlsname=choose_type + str(int(time.time()))
                workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
                return ('mail.itlaolang.com/downfile/{}.xls'.format(xlsname))

            if choose_type == 'TV单独安装':
                for x in range(1, sheet.nrows):
                    try:
                        msg = sheet.row_values(x)
                        #这是之间段之内完成的工单数据
                        if msg[9] != 'order_status_6' and msg[3] == '和TV单独安装' and utc_str_to_timestamp(msg[15]) >= utc_str_to_timestamp(
                                starttime) and utc_str_to_timestamp(msg[15]) <= utc_str_to_timestamp(endtime) \
                                and msg[19] != '普服小区' and msg[19] != '普遍服务':
                            finshed=[find_area(msg[1], msg[11])]
                            msg_list1.append(finshed)
                        #这是时间段之内受理工单数据
                        if msg[9] != 'order_status_6' and msg[3] == '和TV单独安装' and utc_str_to_timestamp(msg[12]) >= utc_str_to_timestamp(
                                starttime) and utc_str_to_timestamp(msg[12]) <= utc_str_to_timestamp(endtime) \
                                and msg[19] != '普服小区' and msg[19] != '普遍服务':
                            result = [find_area(msg[1], msg[11]), get_status(msg[15],starttime,endtime),
                                      get_timeout_8(msg[12], msg[15], msg[19]), downdan(msg[12]),
                                      time_for_end(msg[12], msg[15])]
                            # print(result)
                            msg_list.append(result)

                    except:
                        pass
                # print(len([x for x in msg_list if x[0] == '枝江']))
                # print(len([x for x in msg_list if x[0] == '枝江' and x[1]=='完成']))
                # print(len([x for x in msg_list if x[0] == '枝江' and x[1]=='完成' and x[2]=='是']))
                # print(len([x for x in msg_list if x[0] == '枝江' and x[1]=='未完成' and x[2]=='是']))
                # print(len([x for x in msg_list if x[0] == '枝江' and x[1]=='未完成' and x[3]==1]))
                all_time = 0
                print(len([x for x in msg_list if x[0] == '夷陵' and x[1] == '完成']))
                for i in [x for x in msg_list if x[0] == '夷陵' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                # print(all_time)
                # print(av_time(all_time,len([x for x in msg_list if x[0] == '夷陵' and x[1] == '完成'])))
                print('%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '完成']))))

                workbook_m = xlwt.Workbook(encoding='utf-8')
                xlsheet = workbook_m.add_sheet('装机8小时日报', cell_overwrite_ok=True)
                # 格式1 （有自动换行）
                style1 = xlwt.easyxf('pattern: pattern solid, fore_colour white')
                style1.font.height = 200
                style1.font.name = u'文泉驿点阵正黑'
                style1.font.colour_index = 0
                style1.borders.left = xlwt.Borders.THIN
                style1.borders.right = xlwt.Borders.THIN
                style1.borders.top = xlwt.Borders.THIN
                style1.borders.bottom = xlwt.Borders.THIN
                # style1.font.bold = True
                style1.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
                style1.alignment.horz = xlwt.Alignment.HORZ_CENTER

                # 格式2  （没有自动换行）
                style2 = xlwt.easyxf('pattern: pattern solid, fore_colour white')
                style2.font.height = 200
                style2.font.name = u'文泉驿点阵正黑'
                style2.font.colour_index = 0
                style2.borders.left = xlwt.Borders.THIN
                style2.borders.right = xlwt.Borders.THIN
                style2.borders.top = xlwt.Borders.THIN
                style2.borders.bottom = xlwt.Borders.THIN

                # style2.font.bold = True
                # style2.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
                # style2.alignment.horz = xlwt.Alignment.HORZ_CENTER

                # 格式3 黄色背景色

                style3 = xlwt.easyxf('pattern: pattern solid, fore_colour yellow')
                style3.font.height = 200
                style3.font.name = u'文泉驿点阵正黑'
                style3.font.colour_index = 0
                # style3.borders.left = xlwt.Borders.THIN
                # style3.borders.right = xlwt.Borders.THIN
                # style3.borders.top = xlwt.Borders.THIN
                # style3.borders.bottom = xlwt.Borders.THIN

                # style4 格式4 0.00%

                style4 = xlwt.easyxf('pattern: pattern solid, fore_colour white')
                style4.font.height = 200
                style4.font.name = u'文泉驿点阵正黑'
                style4.font.colour_index = 0
                style4.borders.left = xlwt.Borders.THIN
                style4.borders.right = xlwt.Borders.THIN
                style4.borders.top = xlwt.Borders.THIN
                style4.borders.bottom = xlwt.Borders.THIN
                # style1.font.bold = True
                style4.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
                style4.alignment.horz = xlwt.Alignment.HORZ_CENTER
                style4.num_format_str = '0.00%'

                # style2.font.bold = True
                # style2.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
                # style2.alignment.horz = xlwt.Alignment.HORZ_CENTER
                # 写excel表头
                # 设置单元格
                xlsheet.write(0, 0, '起始时间：', style3)
                xlsheet.write(0, 1, starttime, style1)
                xlsheet.write(0, 3, '截止时间：', style3)
                xlsheet.write(0, 4, endtime, style1)
                xlsheet.write(0, 6, '工单类型：', style3)
                xlsheet.write(0, 7, choose_type, style3)
                xlsheet.write(1, 0, '区县（区域属性）', style1)
                xlsheet.write(1, 1, '当日受理工单量', style1)
                xlsheet.write(1, 2, '当日装机完成量', style1)
                xlsheet.write(1, 3, '已装超时量', style1)
                xlsheet.write(1, 4, '未装超时量', style1)
                xlsheet.write(1, 5, '压单量', style1)
                xlsheet.write(1, 6, '装机及时率', style1)
                xlsheet.write(1, 7, '平均装机时长（小时）', style1)
                xlsheet.write(2, 0, '备注', style1)
                xlsheet.write(2, 1, '本月受理的所有单子', style1)
                xlsheet.write(2, 2, '本月完成的所有单子', style1)
                xlsheet.write(2, 3, '已完成的超时工单（城区24小时、乡镇36小时）', style1)
                xlsheet.write(2, 4, '未完成的超时工单', style1)
                xlsheet.write(2, 5, '本月之前受理，且还没完成', style1)
                xlsheet.write(2, 6, '(受理工单量-已装超时量-未装超时量-本月以前压单量)/受理工单量', style1)
                xlsheet.write(2, 7, '已完成单子共花费时间/完成单子数', style1)
                xlsheet.write(3, 0, '城区', style1)
                xlsheet.write(3, 1, len([x for x in msg_list if x[0] == '宜昌城区']), style1)
                xlsheet.write(3, 2, len([x for x in msg_list1 if x[0] == '宜昌城区']), style1)
                xlsheet.write(3, 3, len([x for x in msg_list if x[0] == '宜昌城区' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(3, 4, len([x for x in msg_list if x[0] == '宜昌城区' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(3, 5, len([x for x in msg_list if x[0] == '宜昌城区' and x[1] == '未完成' and x[3] == 1]),
                              style1)
                xlsheet.write(3, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(4, 4, 4, 4, 4)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '宜昌城区' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(3, 7, '%.2f' % (
                    av_time(all_time, len([x for x in msg_list if x[0] == '宜昌城区' and x[1] == '完成']))), style1)

                xlsheet.write(4, 0, '当阳', style1)
                xlsheet.write(4, 1, len([x for x in msg_list if x[0] == '当阳']), style1)
                xlsheet.write(4, 2, len([x for x in msg_list1 if x[0] == '当阳' ]), style1)
                xlsheet.write(4, 3, len([x for x in msg_list if x[0] == '当阳' and x[1] == '完成' and x[2] == '是']), style1)
                xlsheet.write(4, 4, len([x for x in msg_list if x[0] == '当阳' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(4, 5, len([x for x in msg_list if x[0] == '当阳' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(4, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(5, 5, 5, 5, 5)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '当阳' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(4, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '当阳' and x[1] == '完成']))),
                              style1)
                xlsheet.write(5, 0, '开发区', style1)
                xlsheet.write(5, 1, len([x for x in msg_list if x[0] == '宜昌开发区']), style1)
                xlsheet.write(5, 2, len([x for x in msg_list1 if x[0] == '宜昌开发区']), style1)
                xlsheet.write(5, 3, len([x for x in msg_list if x[0] == '宜昌开发区' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(5, 4, len([x for x in msg_list if x[0] == '宜昌开发区' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(5, 5, len([x for x in msg_list if x[0] == '宜昌开发区' and x[1] == '未完成' and x[3] == 1]),
                              style1)
                xlsheet.write(5, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(6, 6, 6, 6, 6)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '宜昌开发区' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(5, 7, '%.2f' % (
                    av_time(all_time, len([x for x in msg_list if x[0] == '宜昌开发区' and x[1] == '完成']))),
                              style1)
                xlsheet.write(6, 0, '五峰', style1)
                xlsheet.write(6, 1, len([x for x in msg_list if x[0] == '五峰']), style1)
                xlsheet.write(6, 2, len([x for x in msg_list1 if x[0] == '五峰' ]), style1)
                xlsheet.write(6, 3, len([x for x in msg_list if x[0] == '五峰' and x[1] == '完成' and x[2] == '是']), style1)
                xlsheet.write(6, 4, len([x for x in msg_list if x[0] == '五峰' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(6, 5, len([x for x in msg_list if x[0] == '五峰' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(6, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(7, 7, 7, 7, 7)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '五峰' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(6, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '五峰' and x[1] == '完成']))),
                              style1)
                xlsheet.write(7, 0, '兴山', style1)
                xlsheet.write(7, 1, len([x for x in msg_list if x[0] == '兴山']), style1)
                xlsheet.write(7, 2, len([x for x in msg_list1 if x[0] == '兴山' ]), style1)
                xlsheet.write(7, 3, len([x for x in msg_list if x[0] == '兴山' and x[1] == '完成' and x[2] == '是']), style1)
                xlsheet.write(7, 4, len([x for x in msg_list if x[0] == '兴山' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(7, 5, len([x for x in msg_list if x[0] == '兴山' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(7, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(8, 8, 8, 8, 8)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '兴山' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(7, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '兴山' and x[1] == '完成']))),
                              style1)
                xlsheet.write(8, 0, '夷陵', style1)
                xlsheet.write(8, 1, len([x for x in msg_list if x[0] == '夷陵']), style1)
                xlsheet.write(8, 2, len([x for x in msg_list1 if x[0] == '夷陵' ]), style1)
                xlsheet.write(8, 3, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '完成' and x[2] == '是']), style1)
                xlsheet.write(8, 4, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(8, 5, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(8, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(9, 9, 9, 9, 9)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '夷陵' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(8, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '完成']))),
                              style1)
                xlsheet.write(9, 0, '宜都', style1)
                xlsheet.write(9, 1, len([x for x in msg_list if x[0] == '宜都']), style1)
                xlsheet.write(9, 2, len([x for x in msg_list1 if x[0] == '宜都' ]), style1)
                xlsheet.write(9, 3, len([x for x in msg_list if x[0] == '宜都' and x[1] == '完成' and x[2] == '是']), style1)
                xlsheet.write(9, 4, len([x for x in msg_list if x[0] == '宜都' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(9, 5, len([x for x in msg_list if x[0] == '宜都' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(9, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(10, 10, 10, 10, 10)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '宜都' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(9, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '宜都' and x[1] == '完成']))),
                              style1)
                xlsheet.write(10, 0, '远安', style1)
                xlsheet.write(10, 1, len([x for x in msg_list if x[0] == '远安']), style1)
                xlsheet.write(10, 2, len([x for x in msg_list1 if x[0] == '远安' ]), style1)
                xlsheet.write(10, 3, len([x for x in msg_list if x[0] == '远安' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(10, 4, len([x for x in msg_list if x[0] == '远安' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(10, 5, len([x for x in msg_list if x[0] == '远安' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(10, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(11, 11, 11, 11, 11)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '远安' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(10, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '远安' and x[1] == '完成']))),
                              style1)

                xlsheet.write(11, 0, '长阳', style1)
                xlsheet.write(11, 1, len([x for x in msg_list if x[0] == '长阳']), style1)
                xlsheet.write(11, 2, len([x for x in msg_list1 if x[0] == '长阳' ]), style1)
                xlsheet.write(11, 3, len([x for x in msg_list if x[0] == '长阳' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(11, 4, len([x for x in msg_list if x[0] == '长阳' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(11, 5, len([x for x in msg_list if x[0] == '长阳' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(11, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(12, 12, 12, 12, 12)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '长阳' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(11, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '长阳' and x[1] == '完成']))),
                              style1)

                xlsheet.write(12, 0, '枝江', style1)
                xlsheet.write(12, 1, len([x for x in msg_list if x[0] == '枝江']), style1)
                xlsheet.write(12, 2, len([x for x in msg_list1 if x[0] == '枝江' ]), style1)
                xlsheet.write(12, 3, len([x for x in msg_list if x[0] == '枝江' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(12, 4, len([x for x in msg_list if x[0] == '枝江' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(12, 5, len([x for x in msg_list if x[0] == '枝江' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(12, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(13, 13, 13, 13, 13)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '枝江' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(12, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '枝江' and x[1] == '完成']))),
                              style1)

                xlsheet.write(13, 0, '秭归', style1)
                xlsheet.write(13, 1, len([x for x in msg_list if x[0] == '秭归']), style1)
                xlsheet.write(13, 2, len([x for x in msg_list1 if x[0] == '秭归']), style1)
                xlsheet.write(13, 3, len([x for x in msg_list if x[0] == '秭归' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(13, 4, len([x for x in msg_list if x[0] == '秭归' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(13, 5, len([x for x in msg_list if x[0] == '秭归' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(13, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(14, 14, 14, 14, 14)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '秭归' and x[1] == '完成']:
                    all_time = all_time + i[-1]

                xlsheet.write(13, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '秭归' and x[1] == '完成']))),
                              style1)

                xlsheet.write(14, 0, '全市', style1)
                xlsheet.write(14, 1, xlwt.Formula("(B4+B5+B6+B7+B8+B9+B10+B11+B12+B13+B14)"), style1)
                xlsheet.write(14, 2, xlwt.Formula("(C4+C5+C6+C7+C8+C9+C10+C11+C12+C13+C14)"), style1)
                xlsheet.write(14, 3, xlwt.Formula("(D4+D5+D6+D7+D8+D9+D10+D11+D12+D13+D14)"), style1)
                xlsheet.write(14, 4, xlwt.Formula("(E4+E5+E6+E7+E8+E9+E10+E11+E12+E13+E14)"), style1)
                xlsheet.write(14, 5, xlwt.Formula("(F4+F5+F6+F7+F8+F9+F10+F11+F12+F13+F14)"), style1)
                xlsheet.write(14, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(15, 15, 15, 15, 15)), style4)
                xlsheet.write(14, 7, xlwt.Formula("(H4+H5+H6+H7+H8+H9+H10+H11+H12+H13+H14)/11"), style1)
                xlsname=choose_type + str(int(time.time()))
                workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
                return ('mail.itlaolang.com/downfile/{}.xls'.format(xlsname))

            if choose_type == '宽带装机':
                for x in range(1, sheet.nrows):
                    try:
                        msg = sheet.row_values(x)
                        #这是之间段之内完成的工单数据
                        if msg[9] != 'order_status_6' and msg[3] == '宽带装机' and utc_str_to_timestamp(msg[15]) >= utc_str_to_timestamp(
                                starttime) and utc_str_to_timestamp(msg[15]) <= utc_str_to_timestamp(endtime) \
                                and msg[19] != '普服小区' and msg[19] != '普遍服务':
                            finshed=[find_area(msg[1], msg[11])]
                            msg_list1.append(finshed)
                        #这是时间段之内受理工单数据
                        if msg[9] != 'order_status_6' and msg[3] == '宽带装机' and utc_str_to_timestamp(msg[12]) >= utc_str_to_timestamp(
                                starttime) and utc_str_to_timestamp(msg[12]) <= utc_str_to_timestamp(endtime) \
                                and msg[19] != '普服小区' and msg[19] != '普遍服务':
                            result = [find_area(msg[1], msg[11]), get_status(msg[15],starttime,endtime),
                                      get_timeout_8(msg[12], msg[15], msg[19]), downdan(msg[12]),
                                      time_for_end(msg[12], msg[15])]
                            # print(result)
                            msg_list.append(result)

                    except:
                        pass
                # print(len([x for x in msg_list if x[0] == '枝江']))
                # print(len([x for x in msg_list if x[0] == '枝江' and x[1]=='完成']))
                # print(len([x for x in msg_list if x[0] == '枝江' and x[1]=='完成' and x[2]=='是']))
                # print(len([x for x in msg_list if x[0] == '枝江' and x[1]=='未完成' and x[2]=='是']))
                # print(len([x for x in msg_list if x[0] == '枝江' and x[1]=='未完成' and x[3]==1]))
                all_time = 0
                print(len([x for x in msg_list if x[0] == '夷陵' and x[1] == '完成']))
                for i in [x for x in msg_list if x[0] == '夷陵' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                # print(all_time)
                # print(av_time(all_time,len([x for x in msg_list if x[0] == '夷陵' and x[1] == '完成'])))
                print('%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '完成']))))

                workbook_m = xlwt.Workbook(encoding='utf-8')
                xlsheet = workbook_m.add_sheet('装机8小时日报', cell_overwrite_ok=True)
                # 格式1 （有自动换行）
                style1 = xlwt.easyxf('pattern: pattern solid, fore_colour white')
                style1.font.height = 200
                style1.font.name = u'文泉驿点阵正黑'
                style1.font.colour_index = 0
                style1.borders.left = xlwt.Borders.THIN
                style1.borders.right = xlwt.Borders.THIN
                style1.borders.top = xlwt.Borders.THIN
                style1.borders.bottom = xlwt.Borders.THIN
                # style1.font.bold = True
                style1.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
                style1.alignment.horz = xlwt.Alignment.HORZ_CENTER

                # 格式2  （没有自动换行）
                style2 = xlwt.easyxf('pattern: pattern solid, fore_colour white')
                style2.font.height = 200
                style2.font.name = u'文泉驿点阵正黑'
                style2.font.colour_index = 0
                style2.borders.left = xlwt.Borders.THIN
                style2.borders.right = xlwt.Borders.THIN
                style2.borders.top = xlwt.Borders.THIN
                style2.borders.bottom = xlwt.Borders.THIN

                # style2.font.bold = True
                # style2.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
                # style2.alignment.horz = xlwt.Alignment.HORZ_CENTER

                # 格式3 黄色背景色

                style3 = xlwt.easyxf('pattern: pattern solid, fore_colour yellow')
                style3.font.height = 200
                style3.font.name = u'文泉驿点阵正黑'
                style3.font.colour_index = 0
                # style3.borders.left = xlwt.Borders.THIN
                # style3.borders.right = xlwt.Borders.THIN
                # style3.borders.top = xlwt.Borders.THIN
                # style3.borders.bottom = xlwt.Borders.THIN

                # style4 格式4 0.00%

                style4 = xlwt.easyxf('pattern: pattern solid, fore_colour white')
                style4.font.height = 200
                style4.font.name = u'文泉驿点阵正黑'
                style4.font.colour_index = 0
                style4.borders.left = xlwt.Borders.THIN
                style4.borders.right = xlwt.Borders.THIN
                style4.borders.top = xlwt.Borders.THIN
                style4.borders.bottom = xlwt.Borders.THIN
                # style1.font.bold = True
                style4.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
                style4.alignment.horz = xlwt.Alignment.HORZ_CENTER
                style4.num_format_str = '0.00%'

                # style2.font.bold = True
                # style2.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
                # style2.alignment.horz = xlwt.Alignment.HORZ_CENTER
                # 写excel表头
                # 设置单元格
                xlsheet.write(0, 0, '起始时间：', style3)
                xlsheet.write(0, 1, starttime, style1)
                xlsheet.write(0, 3, '截止时间：', style3)
                xlsheet.write(0, 4, endtime, style1)
                xlsheet.write(0, 6, '工单类型：', style3)
                xlsheet.write(0, 7, choose_type, style3)
                xlsheet.write(1, 0, '区县（区域属性）', style1)
                xlsheet.write(1, 1, '当日受理工单量', style1)
                xlsheet.write(1, 2, '当日装机完成量', style1)
                xlsheet.write(1, 3, '已装超时量', style1)
                xlsheet.write(1, 4, '未装超时量', style1)
                xlsheet.write(1, 5, '压单量', style1)
                xlsheet.write(1, 6, '装机及时率', style1)
                xlsheet.write(1, 7, '平均装机时长（小时）', style1)
                xlsheet.write(2, 0, '备注', style1)
                xlsheet.write(2, 1, '本月受理的所有单子', style1)
                xlsheet.write(2, 2, '本月完成的所有单子', style1)
                xlsheet.write(2, 3, '已完成的超时工单（城区24小时、乡镇36小时）', style1)
                xlsheet.write(2, 4, '未完成的超时工单', style1)
                xlsheet.write(2, 5, '本月之前受理，且还没完成', style1)
                xlsheet.write(2, 6, '(受理工单量-已装超时量-未装超时量-本月以前压单量)/受理工单量', style1)
                xlsheet.write(2, 7, '已完成单子共花费时间/完成单子数', style1)
                xlsheet.write(3, 0, '城区', style1)
                xlsheet.write(3, 1, len([x for x in msg_list if x[0] == '宜昌城区']), style1)
                xlsheet.write(3, 2, len([x for x in msg_list1 if x[0] == '宜昌城区']), style1)
                xlsheet.write(3, 3, len([x for x in msg_list if x[0] == '宜昌城区' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(3, 4, len([x for x in msg_list if x[0] == '宜昌城区' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(3, 5, len([x for x in msg_list if x[0] == '宜昌城区' and x[1] == '未完成' and x[3] == 1]),
                              style1)
                xlsheet.write(3, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(4, 4, 4, 4, 4)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '宜昌城区' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(3, 7, '%.2f' % (
                    av_time(all_time, len([x for x in msg_list if x[0] == '宜昌城区' and x[1] == '完成']))), style1)

                xlsheet.write(4, 0, '当阳', style1)
                xlsheet.write(4, 1, len([x for x in msg_list if x[0] == '当阳']), style1)
                xlsheet.write(4, 2, len([x for x in msg_list1 if x[0] == '当阳' ]), style1)
                xlsheet.write(4, 3, len([x for x in msg_list if x[0] == '当阳' and x[1] == '完成' and x[2] == '是']), style1)
                xlsheet.write(4, 4, len([x for x in msg_list if x[0] == '当阳' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(4, 5, len([x for x in msg_list if x[0] == '当阳' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(4, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(5, 5, 5, 5, 5)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '当阳' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(4, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '当阳' and x[1] == '完成']))),
                              style1)
                xlsheet.write(5, 0, '开发区', style1)
                xlsheet.write(5, 1, len([x for x in msg_list if x[0] == '宜昌开发区']), style1)
                xlsheet.write(5, 2, len([x for x in msg_list1 if x[0] == '宜昌开发区']), style1)
                xlsheet.write(5, 3, len([x for x in msg_list if x[0] == '宜昌开发区' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(5, 4, len([x for x in msg_list if x[0] == '宜昌开发区' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(5, 5, len([x for x in msg_list if x[0] == '宜昌开发区' and x[1] == '未完成' and x[3] == 1]),
                              style1)
                xlsheet.write(5, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(6, 6, 6, 6, 6)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '宜昌开发区' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(5, 7, '%.2f' % (
                    av_time(all_time, len([x for x in msg_list if x[0] == '宜昌开发区' and x[1] == '完成']))),
                              style1)
                xlsheet.write(6, 0, '五峰', style1)
                xlsheet.write(6, 1, len([x for x in msg_list if x[0] == '五峰']), style1)
                xlsheet.write(6, 2, len([x for x in msg_list1 if x[0] == '五峰' ]), style1)
                xlsheet.write(6, 3, len([x for x in msg_list if x[0] == '五峰' and x[1] == '完成' and x[2] == '是']), style1)
                xlsheet.write(6, 4, len([x for x in msg_list if x[0] == '五峰' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(6, 5, len([x for x in msg_list if x[0] == '五峰' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(6, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(7, 7, 7, 7, 7)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '五峰' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(6, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '五峰' and x[1] == '完成']))),
                              style1)
                xlsheet.write(7, 0, '兴山', style1)
                xlsheet.write(7, 1, len([x for x in msg_list if x[0] == '兴山']), style1)
                xlsheet.write(7, 2, len([x for x in msg_list1 if x[0] == '兴山' ]), style1)
                xlsheet.write(7, 3, len([x for x in msg_list if x[0] == '兴山' and x[1] == '完成' and x[2] == '是']), style1)
                xlsheet.write(7, 4, len([x for x in msg_list if x[0] == '兴山' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(7, 5, len([x for x in msg_list if x[0] == '兴山' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(7, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(8, 8, 8, 8, 8)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '兴山' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(7, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '兴山' and x[1] == '完成']))),
                              style1)
                xlsheet.write(8, 0, '夷陵', style1)
                xlsheet.write(8, 1, len([x for x in msg_list if x[0] == '夷陵']), style1)
                xlsheet.write(8, 2, len([x for x in msg_list1 if x[0] == '夷陵' ]), style1)
                xlsheet.write(8, 3, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '完成' and x[2] == '是']), style1)
                xlsheet.write(8, 4, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(8, 5, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(8, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(9, 9, 9, 9, 9)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '夷陵' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(8, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '完成']))),
                              style1)
                xlsheet.write(9, 0, '宜都', style1)
                xlsheet.write(9, 1, len([x for x in msg_list if x[0] == '宜都']), style1)
                xlsheet.write(9, 2, len([x for x in msg_list1 if x[0] == '宜都' ]), style1)
                xlsheet.write(9, 3, len([x for x in msg_list if x[0] == '宜都' and x[1] == '完成' and x[2] == '是']), style1)
                xlsheet.write(9, 4, len([x for x in msg_list if x[0] == '宜都' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(9, 5, len([x for x in msg_list if x[0] == '宜都' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(9, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(10, 10, 10, 10, 10)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '宜都' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(9, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '宜都' and x[1] == '完成']))),
                              style1)
                xlsheet.write(10, 0, '远安', style1)
                xlsheet.write(10, 1, len([x for x in msg_list if x[0] == '远安']), style1)
                xlsheet.write(10, 2, len([x for x in msg_list1 if x[0] == '远安' ]), style1)
                xlsheet.write(10, 3, len([x for x in msg_list if x[0] == '远安' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(10, 4, len([x for x in msg_list if x[0] == '远安' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(10, 5, len([x for x in msg_list if x[0] == '远安' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(10, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(11, 11, 11, 11, 11)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '远安' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(10, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '远安' and x[1] == '完成']))),
                              style1)

                xlsheet.write(11, 0, '长阳', style1)
                xlsheet.write(11, 1, len([x for x in msg_list if x[0] == '长阳']), style1)
                xlsheet.write(11, 2, len([x for x in msg_list1 if x[0] == '长阳' ]), style1)
                xlsheet.write(11, 3, len([x for x in msg_list if x[0] == '长阳' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(11, 4, len([x for x in msg_list if x[0] == '长阳' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(11, 5, len([x for x in msg_list if x[0] == '长阳' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(11, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(12, 12, 12, 12, 12)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '长阳' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(11, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '长阳' and x[1] == '完成']))),
                              style1)

                xlsheet.write(12, 0, '枝江', style1)
                xlsheet.write(12, 1, len([x for x in msg_list if x[0] == '枝江']), style1)
                xlsheet.write(12, 2, len([x for x in msg_list1 if x[0] == '枝江' ]), style1)
                xlsheet.write(12, 3, len([x for x in msg_list if x[0] == '枝江' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(12, 4, len([x for x in msg_list if x[0] == '枝江' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(12, 5, len([x for x in msg_list if x[0] == '枝江' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(12, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(13, 13, 13, 13, 13)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '枝江' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(12, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '枝江' and x[1] == '完成']))),
                              style1)

                xlsheet.write(13, 0, '秭归', style1)
                xlsheet.write(13, 1, len([x for x in msg_list if x[0] == '秭归']), style1)
                xlsheet.write(13, 2, len([x for x in msg_list1 if x[0] == '秭归']), style1)
                xlsheet.write(13, 3, len([x for x in msg_list if x[0] == '秭归' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(13, 4, len([x for x in msg_list if x[0] == '秭归' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(13, 5, len([x for x in msg_list if x[0] == '秭归' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(13, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(14, 14, 14, 14, 14)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '秭归' and x[1] == '完成']:
                    all_time = all_time + i[-1]

                xlsheet.write(13, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '秭归' and x[1] == '完成']))),
                              style1)

                xlsheet.write(14, 0, '全市', style1)
                xlsheet.write(14, 1, xlwt.Formula("(B4+B5+B6+B7+B8+B9+B10+B11+B12+B13+B14)"), style1)
                xlsheet.write(14, 2, xlwt.Formula("(C4+C5+C6+C7+C8+C9+C10+C11+C12+C13+C14)"), style1)
                xlsheet.write(14, 3, xlwt.Formula("(D4+D5+D6+D7+D8+D9+D10+D11+D12+D13+D14)"), style1)
                xlsheet.write(14, 4, xlwt.Formula("(E4+E5+E6+E7+E8+E9+E10+E11+E12+E13+E14)"), style1)
                xlsheet.write(14, 5, xlwt.Formula("(F4+F5+F6+F7+F8+F9+F10+F11+F12+F13+F14)"), style1)
                xlsheet.write(14, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(15, 15, 15, 15, 15)), style4)
                xlsheet.write(14, 7, xlwt.Formula("(H4+H5+H6+H7+H8+H9+H10+H11+H12+H13+H14)/11"), style1)
                xlsname=choose_type + str(int(time.time()))
                workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
                return ('mail.itlaolang.com/downfile/{}.xls'.format(xlsname))

        if type=='农普及时率':

            if choose_type == '宽带装机':
                for x in range(1, sheet.nrows):
                    try:
                        msg = sheet.row_values(x)
                        #这是之间段之内完成的工单数据
                        if msg[9] != 'order_status_6' and msg[3] == '宽带装机' and utc_str_to_timestamp(msg[15]) >= utc_str_to_timestamp(
                                starttime) and utc_str_to_timestamp(msg[15]) <= utc_str_to_timestamp(endtime) \
                                and msg[19] == '普服小区' or msg[19] == '普遍服务':
                            finshed=[find_area(msg[1], msg[11])]
                            msg_list1.append(finshed)
                        #这是时间段之内受理工单数据
                        if msg[9] != 'order_status_6' and msg[3] == '宽带装机' and utc_str_to_timestamp(msg[12]) >= utc_str_to_timestamp(
                                starttime) and utc_str_to_timestamp(msg[12]) <= utc_str_to_timestamp(endtime) \
                                and msg[19] == '普服小区' or msg[19] == '普遍服务':
                            result = [find_area(msg[1], msg[11]), get_status(msg[15],starttime,endtime),
                                      get_timeout(msg[12], msg[15], msg[19]), downdan(msg[12]),
                                      time_for_end(msg[12], msg[15])]
                            # print(result)
                            msg_list.append(result)

                    except:
                        pass
                # print(len([x for x in msg_list if x[0] == '枝江']))
                # print(len([x for x in msg_list if x[0] == '枝江' and x[1]=='完成']))
                # print(len([x for x in msg_list if x[0] == '枝江' and x[1]=='完成' and x[2]=='是']))
                # print(len([x for x in msg_list if x[0] == '枝江' and x[1]=='未完成' and x[2]=='是']))
                # print(len([x for x in msg_list if x[0] == '枝江' and x[1]=='未完成' and x[3]==1]))
                all_time = 0
                print(len([x for x in msg_list if x[0] == '夷陵' and x[1] == '完成']))
                for i in [x for x in msg_list if x[0] == '夷陵' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                # print(all_time)
                # print(av_time(all_time,len([x for x in msg_list if x[0] == '夷陵' and x[1] == '完成'])))
                print('%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '完成']))))

                workbook_m = xlwt.Workbook(encoding='utf-8')
                xlsheet = workbook_m.add_sheet('农普及时率', cell_overwrite_ok=True)
                # 格式1 （有自动换行）
                style1 = xlwt.easyxf('pattern: pattern solid, fore_colour white')
                style1.font.height = 200
                style1.font.name = u'文泉驿点阵正黑'
                style1.font.colour_index = 0
                style1.borders.left = xlwt.Borders.THIN
                style1.borders.right = xlwt.Borders.THIN
                style1.borders.top = xlwt.Borders.THIN
                style1.borders.bottom = xlwt.Borders.THIN
                # style1.font.bold = True
                style1.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
                style1.alignment.horz = xlwt.Alignment.HORZ_CENTER

                # 格式2  （没有自动换行）
                style2 = xlwt.easyxf('pattern: pattern solid, fore_colour white')
                style2.font.height = 200
                style2.font.name = u'文泉驿点阵正黑'
                style2.font.colour_index = 0
                style2.borders.left = xlwt.Borders.THIN
                style2.borders.right = xlwt.Borders.THIN
                style2.borders.top = xlwt.Borders.THIN
                style2.borders.bottom = xlwt.Borders.THIN

                # style2.font.bold = True
                # style2.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
                # style2.alignment.horz = xlwt.Alignment.HORZ_CENTER

                # 格式3 黄色背景色

                style3 = xlwt.easyxf('pattern: pattern solid, fore_colour yellow')
                style3.font.height = 200
                style3.font.name = u'文泉驿点阵正黑'
                style3.font.colour_index = 0
                # style3.borders.left = xlwt.Borders.THIN
                # style3.borders.right = xlwt.Borders.THIN
                # style3.borders.top = xlwt.Borders.THIN
                # style3.borders.bottom = xlwt.Borders.THIN

                # style4 格式4 0.00%

                style4 = xlwt.easyxf('pattern: pattern solid, fore_colour white')
                style4.font.height = 200
                style4.font.name = u'文泉驿点阵正黑'
                style4.font.colour_index = 0
                style4.borders.left = xlwt.Borders.THIN
                style4.borders.right = xlwt.Borders.THIN
                style4.borders.top = xlwt.Borders.THIN
                style4.borders.bottom = xlwt.Borders.THIN
                # style1.font.bold = True
                style4.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
                style4.alignment.horz = xlwt.Alignment.HORZ_CENTER
                style4.num_format_str = '0.00%'

                # style2.font.bold = True
                # style2.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
                # style2.alignment.horz = xlwt.Alignment.HORZ_CENTER
                # 写excel表头
                # 设置单元格
                xlsheet.write(0, 0, '起始时间：', style3)
                xlsheet.write(0, 1, starttime, style1)
                xlsheet.write(0, 3, '截止时间：', style3)
                xlsheet.write(0, 4, endtime, style1)
                xlsheet.write(0, 6, '工单类型：', style3)
                xlsheet.write(0, 7, choose_type, style3)
                xlsheet.write(1, 0, '区县（区域属性）', style1)
                xlsheet.write(1, 1, '当日受理工单量', style1)
                xlsheet.write(1, 2, '当日装机完成量', style1)
                xlsheet.write(1, 3, '已装超时量', style1)
                xlsheet.write(1, 4, '未装超时量', style1)
                xlsheet.write(1, 5, '压单量', style1)
                xlsheet.write(1, 6, '装机及时率', style1)
                xlsheet.write(1, 7, '平均装机时长（小时）', style1)
                xlsheet.write(2, 0, '备注', style1)
                xlsheet.write(2, 1, '农普受理量', style1)
                xlsheet.write(2, 2, '农普完成量', style1)
                xlsheet.write(2, 3, '装机时长大于7天的已完成工单', style1)
                xlsheet.write(2, 4, '没完成工单中，已超时7天', style1)
                xlsheet.write(2, 5, '本月以前受理，未完成', style1)
                xlsheet.write(2, 6, '(农普受理量-已装超时量-未装超时量-本月以前压单量)/农普受理量', style1)
                xlsheet.write(2, 7, '累计完成时长/装机完成量', style1)
                xlsheet.write(3, 0, '城区', style1)
                xlsheet.write(3, 1, len([x for x in msg_list if x[0] == '宜昌城区']), style1)
                xlsheet.write(3, 2, len([x for x in msg_list1 if x[0] == '宜昌城区']), style1)
                xlsheet.write(3, 3, len([x for x in msg_list if x[0] == '宜昌城区' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(3, 4, len([x for x in msg_list if x[0] == '宜昌城区' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(3, 5, len([x for x in msg_list if x[0] == '宜昌城区' and x[1] == '未完成' and x[3] == 1]),
                              style1)
                xlsheet.write(3, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(4, 4, 4, 4, 4)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '宜昌城区' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(3, 7, '%.2f' % (
                    av_time(all_time, len([x for x in msg_list if x[0] == '宜昌城区' and x[1] == '完成']))), style1)

                xlsheet.write(4, 0, '当阳', style1)
                xlsheet.write(4, 1, len([x for x in msg_list if x[0] == '当阳']), style1)
                xlsheet.write(4, 2, len([x for x in msg_list1 if x[0] == '当阳' ]), style1)
                xlsheet.write(4, 3, len([x for x in msg_list if x[0] == '当阳' and x[1] == '完成' and x[2] == '是']), style1)
                xlsheet.write(4, 4, len([x for x in msg_list if x[0] == '当阳' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(4, 5, len([x for x in msg_list if x[0] == '当阳' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(4, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(5, 5, 5, 5, 5)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '当阳' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(4, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '当阳' and x[1] == '完成']))),
                              style1)
                xlsheet.write(5, 0, '开发区', style1)
                xlsheet.write(5, 1, len([x for x in msg_list if x[0] == '宜昌开发区']), style1)
                xlsheet.write(5, 2, len([x for x in msg_list1 if x[0] == '宜昌开发区']), style1)
                xlsheet.write(5, 3, len([x for x in msg_list if x[0] == '宜昌开发区' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(5, 4, len([x for x in msg_list if x[0] == '宜昌开发区' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(5, 5, len([x for x in msg_list if x[0] == '宜昌开发区' and x[1] == '未完成' and x[3] == 1]),
                              style1)
                xlsheet.write(5, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(6, 6, 6, 6, 6)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '宜昌开发区' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(5, 7, '%.2f' % (
                    av_time(all_time, len([x for x in msg_list if x[0] == '宜昌开发区' and x[1] == '完成']))),
                              style1)
                xlsheet.write(6, 0, '五峰', style1)
                xlsheet.write(6, 1, len([x for x in msg_list if x[0] == '五峰']), style1)
                xlsheet.write(6, 2, len([x for x in msg_list1 if x[0] == '五峰' ]), style1)
                xlsheet.write(6, 3, len([x for x in msg_list if x[0] == '五峰' and x[1] == '完成' and x[2] == '是']), style1)
                xlsheet.write(6, 4, len([x for x in msg_list if x[0] == '五峰' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(6, 5, len([x for x in msg_list if x[0] == '五峰' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(6, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(7, 7, 7, 7, 7)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '五峰' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(6, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '五峰' and x[1] == '完成']))),
                              style1)
                xlsheet.write(7, 0, '兴山', style1)
                xlsheet.write(7, 1, len([x for x in msg_list if x[0] == '兴山']), style1)
                xlsheet.write(7, 2, len([x for x in msg_list1 if x[0] == '兴山' ]), style1)
                xlsheet.write(7, 3, len([x for x in msg_list if x[0] == '兴山' and x[1] == '完成' and x[2] == '是']), style1)
                xlsheet.write(7, 4, len([x for x in msg_list if x[0] == '兴山' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(7, 5, len([x for x in msg_list if x[0] == '兴山' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(7, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(8, 8, 8, 8, 8)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '兴山' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(7, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '兴山' and x[1] == '完成']))),
                              style1)
                xlsheet.write(8, 0, '夷陵', style1)
                xlsheet.write(8, 1, len([x for x in msg_list if x[0] == '夷陵']), style1)
                xlsheet.write(8, 2, len([x for x in msg_list1 if x[0] == '夷陵' ]), style1)
                xlsheet.write(8, 3, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '完成' and x[2] == '是']), style1)
                xlsheet.write(8, 4, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(8, 5, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(8, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(9, 9, 9, 9, 9)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '夷陵' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(8, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '完成']))),
                              style1)
                xlsheet.write(9, 0, '宜都', style1)
                xlsheet.write(9, 1, len([x for x in msg_list if x[0] == '宜都']), style1)
                xlsheet.write(9, 2, len([x for x in msg_list1 if x[0] == '宜都' ]), style1)
                xlsheet.write(9, 3, len([x for x in msg_list if x[0] == '宜都' and x[1] == '完成' and x[2] == '是']), style1)
                xlsheet.write(9, 4, len([x for x in msg_list if x[0] == '宜都' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(9, 5, len([x for x in msg_list if x[0] == '宜都' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(9, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(10, 10, 10, 10, 10)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '宜都' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(9, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '宜都' and x[1] == '完成']))),
                              style1)
                xlsheet.write(10, 0, '远安', style1)
                xlsheet.write(10, 1, len([x for x in msg_list if x[0] == '远安']), style1)
                xlsheet.write(10, 2, len([x for x in msg_list1 if x[0] == '远安' ]), style1)
                xlsheet.write(10, 3, len([x for x in msg_list if x[0] == '远安' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(10, 4, len([x for x in msg_list if x[0] == '远安' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(10, 5, len([x for x in msg_list if x[0] == '远安' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(10, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(11, 11, 11, 11, 11)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '远安' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(10, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '远安' and x[1] == '完成']))),
                              style1)

                xlsheet.write(11, 0, '长阳', style1)
                xlsheet.write(11, 1, len([x for x in msg_list if x[0] == '长阳']), style1)
                xlsheet.write(11, 2, len([x for x in msg_list1 if x[0] == '长阳' ]), style1)
                xlsheet.write(11, 3, len([x for x in msg_list if x[0] == '长阳' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(11, 4, len([x for x in msg_list if x[0] == '长阳' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(11, 5, len([x for x in msg_list if x[0] == '长阳' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(11, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(12, 12, 12, 12, 12)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '长阳' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(11, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '长阳' and x[1] == '完成']))),
                              style1)

                xlsheet.write(12, 0, '枝江', style1)
                xlsheet.write(12, 1, len([x for x in msg_list if x[0] == '枝江']), style1)
                xlsheet.write(12, 2, len([x for x in msg_list1 if x[0] == '枝江' ]), style1)
                xlsheet.write(12, 3, len([x for x in msg_list if x[0] == '枝江' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(12, 4, len([x for x in msg_list if x[0] == '枝江' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(12, 5, len([x for x in msg_list if x[0] == '枝江' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(12, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(13, 13, 13, 13, 13)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '枝江' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(12, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '枝江' and x[1] == '完成']))),
                              style1)

                xlsheet.write(13, 0, '秭归', style1)
                xlsheet.write(13, 1, len([x for x in msg_list if x[0] == '秭归']), style1)
                xlsheet.write(13, 2, len([x for x in msg_list1 if x[0] == '秭归']), style1)
                xlsheet.write(13, 3, len([x for x in msg_list if x[0] == '秭归' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(13, 4, len([x for x in msg_list if x[0] == '秭归' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(13, 5, len([x for x in msg_list if x[0] == '秭归' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(13, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(14, 14, 14, 14, 14)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '秭归' and x[1] == '完成']:
                    all_time = all_time + i[-1]

                xlsheet.write(13, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '秭归' and x[1] == '完成']))),
                              style1)

                xlsheet.write(14, 0, '全市', style1)
                xlsheet.write(14, 1, xlwt.Formula("(B4+B5+B6+B7+B8+B9+B10+B11+B12+B13+B14)"), style1)
                xlsheet.write(14, 2, xlwt.Formula("(C4+C5+C6+C7+C8+C9+C10+C11+C12+C13+C14)"), style1)
                xlsheet.write(14, 3, xlwt.Formula("(D4+D5+D6+D7+D8+D9+D10+D11+D12+D13+D14)"), style1)
                xlsheet.write(14, 4, xlwt.Formula("(E4+E5+E6+E7+E8+E9+E10+E11+E12+E13+E14)"), style1)
                xlsheet.write(14, 5, xlwt.Formula("(F4+F5+F6+F7+F8+F9+F10+F11+F12+F13+F14)"), style1)
                xlsheet.write(14, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(15, 15, 15, 15, 15)), style4)
                xlsheet.write(14, 7, xlwt.Formula("(H4+H5+H6+H7+H8+H9+H10+H11+H12+H13+H14)/11"), style1)
                xlsname=choose_type + str(int(time.time()))
                workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
                return ('mail.itlaolang.com/downfile/{}.xls'.format(xlsname))
            if choose_type == 'TV单独安装':
                for x in range(1, sheet.nrows):
                    try:
                        msg = sheet.row_values(x)
                        #这是之间段之内完成的工单数据
                        if msg[9] != 'order_status_6' and msg[3] == '和TV单独安装' and utc_str_to_timestamp(msg[15]) >= utc_str_to_timestamp(
                                starttime) and utc_str_to_timestamp(msg[15]) <= utc_str_to_timestamp(endtime) \
                                and msg[19] == '普服小区' or msg[19] == '普遍服务':
                            finshed=[find_area(msg[1], msg[11])]
                            msg_list1.append(finshed)
                        #这是时间段之内受理工单数据
                        if msg[9] != 'order_status_6' and msg[3] == '和TV单独安装' and utc_str_to_timestamp(msg[12]) >= utc_str_to_timestamp(
                                starttime) and utc_str_to_timestamp(msg[12]) <= utc_str_to_timestamp(endtime) \
                                and msg[19] == '普服小区' or msg[19] == '普遍服务':
                            result = [find_area(msg[1], msg[11]), get_status(msg[15],starttime,endtime),
                                      get_timeout(msg[12], msg[15], msg[19]), downdan(msg[12]),
                                      time_for_end(msg[12], msg[15])]
                            # print(result)
                            msg_list.append(result)

                    except:
                        pass
                # print(len([x for x in msg_list if x[0] == '枝江']))
                # print(len([x for x in msg_list if x[0] == '枝江' and x[1]=='完成']))
                # print(len([x for x in msg_list if x[0] == '枝江' and x[1]=='完成' and x[2]=='是']))
                # print(len([x for x in msg_list if x[0] == '枝江' and x[1]=='未完成' and x[2]=='是']))
                # print(len([x for x in msg_list if x[0] == '枝江' and x[1]=='未完成' and x[3]==1]))
                all_time = 0
                print(len([x for x in msg_list if x[0] == '夷陵' and x[1] == '完成']))
                for i in [x for x in msg_list if x[0] == '夷陵' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                # print(all_time)
                # print(av_time(all_time,len([x for x in msg_list if x[0] == '夷陵' and x[1] == '完成'])))
                print('%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '完成']))))

                workbook_m = xlwt.Workbook(encoding='utf-8')
                xlsheet = workbook_m.add_sheet('农普及时率', cell_overwrite_ok=True)
                # 格式1 （有自动换行）
                style1 = xlwt.easyxf('pattern: pattern solid, fore_colour white')
                style1.font.height = 200
                style1.font.name = u'文泉驿点阵正黑'
                style1.font.colour_index = 0
                style1.borders.left = xlwt.Borders.THIN
                style1.borders.right = xlwt.Borders.THIN
                style1.borders.top = xlwt.Borders.THIN
                style1.borders.bottom = xlwt.Borders.THIN
                # style1.font.bold = True
                style1.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
                style1.alignment.horz = xlwt.Alignment.HORZ_CENTER

                # 格式2  （没有自动换行）
                style2 = xlwt.easyxf('pattern: pattern solid, fore_colour white')
                style2.font.height = 200
                style2.font.name = u'文泉驿点阵正黑'
                style2.font.colour_index = 0
                style2.borders.left = xlwt.Borders.THIN
                style2.borders.right = xlwt.Borders.THIN
                style2.borders.top = xlwt.Borders.THIN
                style2.borders.bottom = xlwt.Borders.THIN

                # style2.font.bold = True
                # style2.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
                # style2.alignment.horz = xlwt.Alignment.HORZ_CENTER

                # 格式3 黄色背景色

                style3 = xlwt.easyxf('pattern: pattern solid, fore_colour yellow')
                style3.font.height = 200
                style3.font.name = u'文泉驿点阵正黑'
                style3.font.colour_index = 0
                # style3.borders.left = xlwt.Borders.THIN
                # style3.borders.right = xlwt.Borders.THIN
                # style3.borders.top = xlwt.Borders.THIN
                # style3.borders.bottom = xlwt.Borders.THIN

                # style4 格式4 0.00%

                style4 = xlwt.easyxf('pattern: pattern solid, fore_colour white')
                style4.font.height = 200
                style4.font.name = u'文泉驿点阵正黑'
                style4.font.colour_index = 0
                style4.borders.left = xlwt.Borders.THIN
                style4.borders.right = xlwt.Borders.THIN
                style4.borders.top = xlwt.Borders.THIN
                style4.borders.bottom = xlwt.Borders.THIN
                # style1.font.bold = True
                style4.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
                style4.alignment.horz = xlwt.Alignment.HORZ_CENTER
                style4.num_format_str = '0.00%'

                # style2.font.bold = True
                # style2.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
                # style2.alignment.horz = xlwt.Alignment.HORZ_CENTER
                # 写excel表头
                # 设置单元格
                xlsheet.write(0, 0, '起始时间：', style3)
                xlsheet.write(0, 1, starttime, style1)
                xlsheet.write(0, 3, '截止时间：', style3)
                xlsheet.write(0, 4, endtime, style1)
                xlsheet.write(0, 6, '工单类型：', style3)
                xlsheet.write(0, 7, choose_type, style3)
                xlsheet.write(1, 0, '区县（区域属性）', style1)
                xlsheet.write(1, 1, '当日受理工单量', style1)
                xlsheet.write(1, 2, '当日装机完成量', style1)
                xlsheet.write(1, 3, '已装超时量', style1)
                xlsheet.write(1, 4, '未装超时量', style1)
                xlsheet.write(1, 5, '压单量', style1)
                xlsheet.write(1, 6, '装机及时率', style1)
                xlsheet.write(1, 7, '平均装机时长（小时）', style1)
                xlsheet.write(2, 0, '备注', style1)
                xlsheet.write(2, 1, '农普受理量', style1)
                xlsheet.write(2, 2, '农普完成量', style1)
                xlsheet.write(2, 3, '装机时长大于7天的已完成工单', style1)
                xlsheet.write(2, 4, '没完成工单中，已超时7天', style1)
                xlsheet.write(2, 5, '本月以前受理，未完成', style1)
                xlsheet.write(2, 6, '(农普受理量-已装超时量-未装超时量-本月以前压单量)/农普受理量', style1)
                xlsheet.write(2, 7, '累计完成时长/装机完成量', style1)
                xlsheet.write(3, 0, '城区', style1)
                xlsheet.write(3, 1, len([x for x in msg_list if x[0] == '宜昌城区']), style1)
                xlsheet.write(3, 2, len([x for x in msg_list1 if x[0] == '宜昌城区']), style1)
                xlsheet.write(3, 3, len([x for x in msg_list if x[0] == '宜昌城区' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(3, 4, len([x for x in msg_list if x[0] == '宜昌城区' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(3, 5, len([x for x in msg_list if x[0] == '宜昌城区' and x[1] == '未完成' and x[3] == 1]),
                              style1)
                xlsheet.write(3, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(4, 4, 4, 4, 4)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '宜昌城区' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(3, 7, '%.2f' % (
                    av_time(all_time, len([x for x in msg_list if x[0] == '宜昌城区' and x[1] == '完成']))), style1)

                xlsheet.write(4, 0, '当阳', style1)
                xlsheet.write(4, 1, len([x for x in msg_list if x[0] == '当阳']), style1)
                xlsheet.write(4, 2, len([x for x in msg_list1 if x[0] == '当阳' ]), style1)
                xlsheet.write(4, 3, len([x for x in msg_list if x[0] == '当阳' and x[1] == '完成' and x[2] == '是']), style1)
                xlsheet.write(4, 4, len([x for x in msg_list if x[0] == '当阳' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(4, 5, len([x for x in msg_list if x[0] == '当阳' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(4, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(5, 5, 5, 5, 5)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '当阳' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(4, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '当阳' and x[1] == '完成']))),
                              style1)
                xlsheet.write(5, 0, '开发区', style1)
                xlsheet.write(5, 1, len([x for x in msg_list if x[0] == '宜昌开发区']), style1)
                xlsheet.write(5, 2, len([x for x in msg_list1 if x[0] == '宜昌开发区']), style1)
                xlsheet.write(5, 3, len([x for x in msg_list if x[0] == '宜昌开发区' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(5, 4, len([x for x in msg_list if x[0] == '宜昌开发区' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(5, 5, len([x for x in msg_list if x[0] == '宜昌开发区' and x[1] == '未完成' and x[3] == 1]),
                              style1)
                xlsheet.write(5, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(6, 6, 6, 6, 6)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '宜昌开发区' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(5, 7, '%.2f' % (
                    av_time(all_time, len([x for x in msg_list if x[0] == '宜昌开发区' and x[1] == '完成']))),
                              style1)
                xlsheet.write(6, 0, '五峰', style1)
                xlsheet.write(6, 1, len([x for x in msg_list if x[0] == '五峰']), style1)
                xlsheet.write(6, 2, len([x for x in msg_list1 if x[0] == '五峰' ]), style1)
                xlsheet.write(6, 3, len([x for x in msg_list if x[0] == '五峰' and x[1] == '完成' and x[2] == '是']), style1)
                xlsheet.write(6, 4, len([x for x in msg_list if x[0] == '五峰' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(6, 5, len([x for x in msg_list if x[0] == '五峰' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(6, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(7, 7, 7, 7, 7)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '五峰' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(6, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '五峰' and x[1] == '完成']))),
                              style1)
                xlsheet.write(7, 0, '兴山', style1)
                xlsheet.write(7, 1, len([x for x in msg_list if x[0] == '兴山']), style1)
                xlsheet.write(7, 2, len([x for x in msg_list1 if x[0] == '兴山' ]), style1)
                xlsheet.write(7, 3, len([x for x in msg_list if x[0] == '兴山' and x[1] == '完成' and x[2] == '是']), style1)
                xlsheet.write(7, 4, len([x for x in msg_list if x[0] == '兴山' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(7, 5, len([x for x in msg_list if x[0] == '兴山' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(7, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(8, 8, 8, 8, 8)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '兴山' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(7, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '兴山' and x[1] == '完成']))),
                              style1)
                xlsheet.write(8, 0, '夷陵', style1)
                xlsheet.write(8, 1, len([x for x in msg_list if x[0] == '夷陵']), style1)
                xlsheet.write(8, 2, len([x for x in msg_list1 if x[0] == '夷陵' ]), style1)
                xlsheet.write(8, 3, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '完成' and x[2] == '是']), style1)
                xlsheet.write(8, 4, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(8, 5, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(8, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(9, 9, 9, 9, 9)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '夷陵' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(8, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '完成']))),
                              style1)
                xlsheet.write(9, 0, '宜都', style1)
                xlsheet.write(9, 1, len([x for x in msg_list if x[0] == '宜都']), style1)
                xlsheet.write(9, 2, len([x for x in msg_list1 if x[0] == '宜都' ]), style1)
                xlsheet.write(9, 3, len([x for x in msg_list if x[0] == '宜都' and x[1] == '完成' and x[2] == '是']), style1)
                xlsheet.write(9, 4, len([x for x in msg_list if x[0] == '宜都' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(9, 5, len([x for x in msg_list if x[0] == '宜都' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(9, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(10, 10, 10, 10, 10)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '宜都' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(9, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '宜都' and x[1] == '完成']))),
                              style1)
                xlsheet.write(10, 0, '远安', style1)
                xlsheet.write(10, 1, len([x for x in msg_list if x[0] == '远安']), style1)
                xlsheet.write(10, 2, len([x for x in msg_list1 if x[0] == '远安' ]), style1)
                xlsheet.write(10, 3, len([x for x in msg_list if x[0] == '远安' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(10, 4, len([x for x in msg_list if x[0] == '远安' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(10, 5, len([x for x in msg_list if x[0] == '远安' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(10, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(11, 11, 11, 11, 11)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '远安' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(10, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '远安' and x[1] == '完成']))),
                              style1)

                xlsheet.write(11, 0, '长阳', style1)
                xlsheet.write(11, 1, len([x for x in msg_list if x[0] == '长阳']), style1)
                xlsheet.write(11, 2, len([x for x in msg_list1 if x[0] == '长阳' ]), style1)
                xlsheet.write(11, 3, len([x for x in msg_list if x[0] == '长阳' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(11, 4, len([x for x in msg_list if x[0] == '长阳' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(11, 5, len([x for x in msg_list if x[0] == '长阳' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(11, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(12, 12, 12, 12, 12)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '长阳' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(11, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '长阳' and x[1] == '完成']))),
                              style1)

                xlsheet.write(12, 0, '枝江', style1)
                xlsheet.write(12, 1, len([x for x in msg_list if x[0] == '枝江']), style1)
                xlsheet.write(12, 2, len([x for x in msg_list1 if x[0] == '枝江' ]), style1)
                xlsheet.write(12, 3, len([x for x in msg_list if x[0] == '枝江' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(12, 4, len([x for x in msg_list if x[0] == '枝江' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(12, 5, len([x for x in msg_list if x[0] == '枝江' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(12, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(13, 13, 13, 13, 13)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '枝江' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(12, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '枝江' and x[1] == '完成']))),
                              style1)

                xlsheet.write(13, 0, '秭归', style1)
                xlsheet.write(13, 1, len([x for x in msg_list if x[0] == '秭归']), style1)
                xlsheet.write(13, 2, len([x for x in msg_list1 if x[0] == '秭归']), style1)
                xlsheet.write(13, 3, len([x for x in msg_list if x[0] == '秭归' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(13, 4, len([x for x in msg_list if x[0] == '秭归' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(13, 5, len([x for x in msg_list if x[0] == '秭归' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(13, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(14, 14, 14, 14, 14)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '秭归' and x[1] == '完成']:
                    all_time = all_time + i[-1]

                xlsheet.write(13, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '秭归' and x[1] == '完成']))),
                              style1)

                xlsheet.write(14, 0, '全市', style1)
                xlsheet.write(14, 1, xlwt.Formula("(B4+B5+B6+B7+B8+B9+B10+B11+B12+B13+B14)"), style1)
                xlsheet.write(14, 2, xlwt.Formula("(C4+C5+C6+C7+C8+C9+C10+C11+C12+C13+C14)"), style1)
                xlsheet.write(14, 3, xlwt.Formula("(D4+D5+D6+D7+D8+D9+D10+D11+D12+D13+D14)"), style1)
                xlsheet.write(14, 4, xlwt.Formula("(E4+E5+E6+E7+E8+E9+E10+E11+E12+E13+E14)"), style1)
                xlsheet.write(14, 5, xlwt.Formula("(F4+F5+F6+F7+F8+F9+F10+F11+F12+F13+F14)"), style1)
                xlsheet.write(14, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(15, 15, 15, 15, 15)), style4)
                xlsheet.write(14, 7, xlwt.Formula("(H4+H5+H6+H7+H8+H9+H10+H11+H12+H13+H14)/11"), style1)
                xlsname=choose_type + str(int(time.time()))
                workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
                return ('mail.itlaolang.com/downfile/{}.xls'.format(xlsname))
            if choose_type == 'IMS单独安装':
                for x in range(1, sheet.nrows):
                    try:
                        msg = sheet.row_values(x)
                        #这是之间段之内完成的工单数据
                        if msg[9] != 'order_status_6' and msg[3] == 'IMS单独安装' and utc_str_to_timestamp(msg[15]) >= utc_str_to_timestamp(
                                starttime) and utc_str_to_timestamp(msg[15]) <= utc_str_to_timestamp(endtime) \
                                and msg[19] == '普服小区' or msg[19] == '普遍服务':
                            finshed=[find_area(msg[1], msg[11])]
                            msg_list1.append(finshed)
                        #这是时间段之内受理工单数据
                        if msg[9] != 'order_status_6' and msg[3] == 'IMS单独安装' and utc_str_to_timestamp(msg[12]) >= utc_str_to_timestamp(
                                starttime) and utc_str_to_timestamp(msg[12]) <= utc_str_to_timestamp(endtime) \
                                and msg[19] == '普服小区' or msg[19] == '普遍服务':
                            result = [find_area(msg[1], msg[11]), get_status(msg[15],starttime,endtime),
                                      get_timeout(msg[12], msg[15], msg[19]), downdan(msg[12]),
                                      time_for_end(msg[12], msg[15])]
                            # print(result)
                            msg_list.append(result)

                    except:
                        pass
                # print(len([x for x in msg_list if x[0] == '枝江']))
                # print(len([x for x in msg_list if x[0] == '枝江' and x[1]=='完成']))
                # print(len([x for x in msg_list if x[0] == '枝江' and x[1]=='完成' and x[2]=='是']))
                # print(len([x for x in msg_list if x[0] == '枝江' and x[1]=='未完成' and x[2]=='是']))
                # print(len([x for x in msg_list if x[0] == '枝江' and x[1]=='未完成' and x[3]==1]))
                all_time = 0
                print(len([x for x in msg_list if x[0] == '夷陵' and x[1] == '完成']))
                for i in [x for x in msg_list if x[0] == '夷陵' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                # print(all_time)
                # print(av_time(all_time,len([x for x in msg_list if x[0] == '夷陵' and x[1] == '完成'])))
                print('%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '完成']))))

                workbook_m = xlwt.Workbook(encoding='utf-8')
                xlsheet = workbook_m.add_sheet('农普及时率', cell_overwrite_ok=True)
                # 格式1 （有自动换行）
                style1 = xlwt.easyxf('pattern: pattern solid, fore_colour white')
                style1.font.height = 200
                style1.font.name = u'文泉驿点阵正黑'
                style1.font.colour_index = 0
                style1.borders.left = xlwt.Borders.THIN
                style1.borders.right = xlwt.Borders.THIN
                style1.borders.top = xlwt.Borders.THIN
                style1.borders.bottom = xlwt.Borders.THIN
                # style1.font.bold = True
                style1.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
                style1.alignment.horz = xlwt.Alignment.HORZ_CENTER

                # 格式2  （没有自动换行）
                style2 = xlwt.easyxf('pattern: pattern solid, fore_colour white')
                style2.font.height = 200
                style2.font.name = u'文泉驿点阵正黑'
                style2.font.colour_index = 0
                style2.borders.left = xlwt.Borders.THIN
                style2.borders.right = xlwt.Borders.THIN
                style2.borders.top = xlwt.Borders.THIN
                style2.borders.bottom = xlwt.Borders.THIN

                # style2.font.bold = True
                # style2.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
                # style2.alignment.horz = xlwt.Alignment.HORZ_CENTER

                # 格式3 黄色背景色

                style3 = xlwt.easyxf('pattern: pattern solid, fore_colour yellow')
                style3.font.height = 200
                style3.font.name = u'文泉驿点阵正黑'
                style3.font.colour_index = 0
                # style3.borders.left = xlwt.Borders.THIN
                # style3.borders.right = xlwt.Borders.THIN
                # style3.borders.top = xlwt.Borders.THIN
                # style3.borders.bottom = xlwt.Borders.THIN

                # style4 格式4 0.00%

                style4 = xlwt.easyxf('pattern: pattern solid, fore_colour white')
                style4.font.height = 200
                style4.font.name = u'文泉驿点阵正黑'
                style4.font.colour_index = 0
                style4.borders.left = xlwt.Borders.THIN
                style4.borders.right = xlwt.Borders.THIN
                style4.borders.top = xlwt.Borders.THIN
                style4.borders.bottom = xlwt.Borders.THIN
                # style1.font.bold = True
                style4.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
                style4.alignment.horz = xlwt.Alignment.HORZ_CENTER
                style4.num_format_str = '0.00%'

                # style2.font.bold = True
                # style2.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
                # style2.alignment.horz = xlwt.Alignment.HORZ_CENTER
                # 写excel表头
                # 设置单元格
                xlsheet.write(0, 0, '起始时间：', style3)
                xlsheet.write(0, 1, starttime, style1)
                xlsheet.write(0, 3, '截止时间：', style3)
                xlsheet.write(0, 4, endtime, style1)
                xlsheet.write(0, 6, '工单类型：', style3)
                xlsheet.write(0, 7, choose_type, style3)
                xlsheet.write(1, 0, '区县（区域属性）', style1)
                xlsheet.write(1, 1, '当日受理工单量', style1)
                xlsheet.write(1, 2, '当日装机完成量', style1)
                xlsheet.write(1, 3, '已装超时量', style1)
                xlsheet.write(1, 4, '未装超时量', style1)
                xlsheet.write(1, 5, '压单量', style1)
                xlsheet.write(1, 6, '装机及时率', style1)
                xlsheet.write(1, 7, '平均装机时长（小时）', style1)
                xlsheet.write(2, 0, '备注', style1)
                xlsheet.write(2, 1, '农普受理量', style1)
                xlsheet.write(2, 2, '农普完成量', style1)
                xlsheet.write(2, 3, '装机时长大于7天的已完成工单', style1)
                xlsheet.write(2, 4, '没完成工单中，已超时7天', style1)
                xlsheet.write(2, 5, '本月以前受理，未完成', style1)
                xlsheet.write(2, 6, '(农普受理量-已装超时量-未装超时量-本月以前压单量)/农普受理量', style1)
                xlsheet.write(2, 7, '累计完成时长/装机完成量', style1)
                xlsheet.write(3, 0, '城区', style1)
                xlsheet.write(3, 1, len([x for x in msg_list if x[0] == '宜昌城区']), style1)
                xlsheet.write(3, 2, len([x for x in msg_list1 if x[0] == '宜昌城区']), style1)
                xlsheet.write(3, 3, len([x for x in msg_list if x[0] == '宜昌城区' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(3, 4, len([x for x in msg_list if x[0] == '宜昌城区' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(3, 5, len([x for x in msg_list if x[0] == '宜昌城区' and x[1] == '未完成' and x[3] == 1]),
                              style1)
                xlsheet.write(3, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(4, 4, 4, 4, 4)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '宜昌城区' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(3, 7, '%.2f' % (
                    av_time(all_time, len([x for x in msg_list if x[0] == '宜昌城区' and x[1] == '完成']))), style1)

                xlsheet.write(4, 0, '当阳', style1)
                xlsheet.write(4, 1, len([x for x in msg_list if x[0] == '当阳']), style1)
                xlsheet.write(4, 2, len([x for x in msg_list1 if x[0] == '当阳' ]), style1)
                xlsheet.write(4, 3, len([x for x in msg_list if x[0] == '当阳' and x[1] == '完成' and x[2] == '是']), style1)
                xlsheet.write(4, 4, len([x for x in msg_list if x[0] == '当阳' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(4, 5, len([x for x in msg_list if x[0] == '当阳' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(4, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(5, 5, 5, 5, 5)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '当阳' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(4, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '当阳' and x[1] == '完成']))),
                              style1)
                xlsheet.write(5, 0, '开发区', style1)
                xlsheet.write(5, 1, len([x for x in msg_list if x[0] == '宜昌开发区']), style1)
                xlsheet.write(5, 2, len([x for x in msg_list1 if x[0] == '宜昌开发区']), style1)
                xlsheet.write(5, 3, len([x for x in msg_list if x[0] == '宜昌开发区' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(5, 4, len([x for x in msg_list if x[0] == '宜昌开发区' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(5, 5, len([x for x in msg_list if x[0] == '宜昌开发区' and x[1] == '未完成' and x[3] == 1]),
                              style1)
                xlsheet.write(5, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(6, 6, 6, 6, 6)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '宜昌开发区' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(5, 7, '%.2f' % (
                    av_time(all_time, len([x for x in msg_list if x[0] == '宜昌开发区' and x[1] == '完成']))),
                              style1)
                xlsheet.write(6, 0, '五峰', style1)
                xlsheet.write(6, 1, len([x for x in msg_list if x[0] == '五峰']), style1)
                xlsheet.write(6, 2, len([x for x in msg_list1 if x[0] == '五峰' ]), style1)
                xlsheet.write(6, 3, len([x for x in msg_list if x[0] == '五峰' and x[1] == '完成' and x[2] == '是']), style1)
                xlsheet.write(6, 4, len([x for x in msg_list if x[0] == '五峰' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(6, 5, len([x for x in msg_list if x[0] == '五峰' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(6, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(7, 7, 7, 7, 7)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '五峰' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(6, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '五峰' and x[1] == '完成']))),
                              style1)
                xlsheet.write(7, 0, '兴山', style1)
                xlsheet.write(7, 1, len([x for x in msg_list if x[0] == '兴山']), style1)
                xlsheet.write(7, 2, len([x for x in msg_list1 if x[0] == '兴山' ]), style1)
                xlsheet.write(7, 3, len([x for x in msg_list if x[0] == '兴山' and x[1] == '完成' and x[2] == '是']), style1)
                xlsheet.write(7, 4, len([x for x in msg_list if x[0] == '兴山' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(7, 5, len([x for x in msg_list if x[0] == '兴山' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(7, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(8, 8, 8, 8, 8)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '兴山' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(7, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '兴山' and x[1] == '完成']))),
                              style1)
                xlsheet.write(8, 0, '夷陵', style1)
                xlsheet.write(8, 1, len([x for x in msg_list if x[0] == '夷陵']), style1)
                xlsheet.write(8, 2, len([x for x in msg_list1 if x[0] == '夷陵' ]), style1)
                xlsheet.write(8, 3, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '完成' and x[2] == '是']), style1)
                xlsheet.write(8, 4, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(8, 5, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(8, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(9, 9, 9, 9, 9)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '夷陵' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(8, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '完成']))),
                              style1)
                xlsheet.write(9, 0, '宜都', style1)
                xlsheet.write(9, 1, len([x for x in msg_list if x[0] == '宜都']), style1)
                xlsheet.write(9, 2, len([x for x in msg_list1 if x[0] == '宜都' ]), style1)
                xlsheet.write(9, 3, len([x for x in msg_list if x[0] == '宜都' and x[1] == '完成' and x[2] == '是']), style1)
                xlsheet.write(9, 4, len([x for x in msg_list if x[0] == '宜都' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(9, 5, len([x for x in msg_list if x[0] == '宜都' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(9, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(10, 10, 10, 10, 10)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '宜都' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(9, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '宜都' and x[1] == '完成']))),
                              style1)
                xlsheet.write(10, 0, '远安', style1)
                xlsheet.write(10, 1, len([x for x in msg_list if x[0] == '远安']), style1)
                xlsheet.write(10, 2, len([x for x in msg_list1 if x[0] == '远安' ]), style1)
                xlsheet.write(10, 3, len([x for x in msg_list if x[0] == '远安' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(10, 4, len([x for x in msg_list if x[0] == '远安' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(10, 5, len([x for x in msg_list if x[0] == '远安' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(10, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(11, 11, 11, 11, 11)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '远安' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(10, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '远安' and x[1] == '完成']))),
                              style1)

                xlsheet.write(11, 0, '长阳', style1)
                xlsheet.write(11, 1, len([x for x in msg_list if x[0] == '长阳']), style1)
                xlsheet.write(11, 2, len([x for x in msg_list1 if x[0] == '长阳' ]), style1)
                xlsheet.write(11, 3, len([x for x in msg_list if x[0] == '长阳' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(11, 4, len([x for x in msg_list if x[0] == '长阳' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(11, 5, len([x for x in msg_list if x[0] == '长阳' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(11, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(12, 12, 12, 12, 12)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '长阳' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(11, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '长阳' and x[1] == '完成']))),
                              style1)

                xlsheet.write(12, 0, '枝江', style1)
                xlsheet.write(12, 1, len([x for x in msg_list if x[0] == '枝江']), style1)
                xlsheet.write(12, 2, len([x for x in msg_list1 if x[0] == '枝江' ]), style1)
                xlsheet.write(12, 3, len([x for x in msg_list if x[0] == '枝江' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(12, 4, len([x for x in msg_list if x[0] == '枝江' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(12, 5, len([x for x in msg_list if x[0] == '枝江' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(12, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(13, 13, 13, 13, 13)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '枝江' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(12, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '枝江' and x[1] == '完成']))),
                              style1)

                xlsheet.write(13, 0, '秭归', style1)
                xlsheet.write(13, 1, len([x for x in msg_list if x[0] == '秭归']), style1)
                xlsheet.write(13, 2, len([x for x in msg_list1 if x[0] == '秭归']), style1)
                xlsheet.write(13, 3, len([x for x in msg_list if x[0] == '秭归' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(13, 4, len([x for x in msg_list if x[0] == '秭归' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(13, 5, len([x for x in msg_list if x[0] == '秭归' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(13, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(14, 14, 14, 14, 14)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '秭归' and x[1] == '完成']:
                    all_time = all_time + i[-1]

                xlsheet.write(13, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '秭归' and x[1] == '完成']))),
                              style1)

                xlsheet.write(14, 0, '全市', style1)
                xlsheet.write(14, 1, xlwt.Formula("(B4+B5+B6+B7+B8+B9+B10+B11+B12+B13+B14)"), style1)
                xlsheet.write(14, 2, xlwt.Formula("(C4+C5+C6+C7+C8+C9+C10+C11+C12+C13+C14)"), style1)
                xlsheet.write(14, 3, xlwt.Formula("(D4+D5+D6+D7+D8+D9+D10+D11+D12+D13+D14)"), style1)
                xlsheet.write(14, 4, xlwt.Formula("(E4+E5+E6+E7+E8+E9+E10+E11+E12+E13+E14)"), style1)
                xlsheet.write(14, 5, xlwt.Formula("(F4+F5+F6+F7+F8+F9+F10+F11+F12+F13+F14)"), style1)
                xlsheet.write(14, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(15, 15, 15, 15, 15)), style4)
                xlsheet.write(14, 7, xlwt.Formula("(H4+H5+H6+H7+H8+H9+H10+H11+H12+H13+H14)/11"), style1)
                xlsname=choose_type + str(int(time.time()))
                workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
                return ('mail.itlaolang.com/downfile/{}.xls'.format(xlsname))
            if choose_type == '移机装':
                for x in range(1, sheet.nrows):
                    try:
                        msg = sheet.row_values(x)
                        #这是之间段之内完成的工单数据
                        if msg[9] != 'order_status_6' and msg[3] == '移机装' and utc_str_to_timestamp(msg[15]) >= utc_str_to_timestamp(
                                starttime) and utc_str_to_timestamp(msg[15]) <= utc_str_to_timestamp(endtime) \
                                and msg[19] == '普服小区' or msg[19] == '普遍服务':
                            finshed=[find_area(msg[1], msg[11])]
                            msg_list1.append(finshed)
                        #这是时间段之内受理工单数据
                        if msg[9] != 'order_status_6' and msg[3] == '移机装' and utc_str_to_timestamp(msg[12]) >= utc_str_to_timestamp(
                                starttime) and utc_str_to_timestamp(msg[12]) <= utc_str_to_timestamp(endtime) \
                                and msg[19] == '普服小区' or msg[19] == '普遍服务':
                            result = [find_area(msg[1], msg[11]), get_status(msg[15],starttime,endtime),
                                      get_timeout(msg[12], msg[15], msg[19]), downdan(msg[12]),
                                      time_for_end(msg[12], msg[15])]
                            # print(result)
                            msg_list.append(result)

                    except:
                        pass
                # print(len([x for x in msg_list if x[0] == '枝江']))
                # print(len([x for x in msg_list if x[0] == '枝江' and x[1]=='完成']))
                # print(len([x for x in msg_list if x[0] == '枝江' and x[1]=='完成' and x[2]=='是']))
                # print(len([x for x in msg_list if x[0] == '枝江' and x[1]=='未完成' and x[2]=='是']))
                # print(len([x for x in msg_list if x[0] == '枝江' and x[1]=='未完成' and x[3]==1]))
                all_time = 0
                print(len([x for x in msg_list if x[0] == '夷陵' and x[1] == '完成']))
                for i in [x for x in msg_list if x[0] == '夷陵' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                # print(all_time)
                # print(av_time(all_time,len([x for x in msg_list if x[0] == '夷陵' and x[1] == '完成'])))
                print('%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '完成']))))

                workbook_m = xlwt.Workbook(encoding='utf-8')
                xlsheet = workbook_m.add_sheet('农普及时率', cell_overwrite_ok=True)
                # 格式1 （有自动换行）
                style1 = xlwt.easyxf('pattern: pattern solid, fore_colour white')
                style1.font.height = 200
                style1.font.name = u'文泉驿点阵正黑'
                style1.font.colour_index = 0
                style1.borders.left = xlwt.Borders.THIN
                style1.borders.right = xlwt.Borders.THIN
                style1.borders.top = xlwt.Borders.THIN
                style1.borders.bottom = xlwt.Borders.THIN
                # style1.font.bold = True
                style1.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
                style1.alignment.horz = xlwt.Alignment.HORZ_CENTER

                # 格式2  （没有自动换行）
                style2 = xlwt.easyxf('pattern: pattern solid, fore_colour white')
                style2.font.height = 200
                style2.font.name = u'文泉驿点阵正黑'
                style2.font.colour_index = 0
                style2.borders.left = xlwt.Borders.THIN
                style2.borders.right = xlwt.Borders.THIN
                style2.borders.top = xlwt.Borders.THIN
                style2.borders.bottom = xlwt.Borders.THIN

                # style2.font.bold = True
                # style2.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
                # style2.alignment.horz = xlwt.Alignment.HORZ_CENTER

                # 格式3 黄色背景色

                style3 = xlwt.easyxf('pattern: pattern solid, fore_colour yellow')
                style3.font.height = 200
                style3.font.name = u'文泉驿点阵正黑'
                style3.font.colour_index = 0
                # style3.borders.left = xlwt.Borders.THIN
                # style3.borders.right = xlwt.Borders.THIN
                # style3.borders.top = xlwt.Borders.THIN
                # style3.borders.bottom = xlwt.Borders.THIN

                # style4 格式4 0.00%

                style4 = xlwt.easyxf('pattern: pattern solid, fore_colour white')
                style4.font.height = 200
                style4.font.name = u'文泉驿点阵正黑'
                style4.font.colour_index = 0
                style4.borders.left = xlwt.Borders.THIN
                style4.borders.right = xlwt.Borders.THIN
                style4.borders.top = xlwt.Borders.THIN
                style4.borders.bottom = xlwt.Borders.THIN
                # style1.font.bold = True
                style4.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
                style4.alignment.horz = xlwt.Alignment.HORZ_CENTER
                style4.num_format_str = '0.00%'

                # style2.font.bold = True
                # style2.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
                # style2.alignment.horz = xlwt.Alignment.HORZ_CENTER
                # 写excel表头
                # 设置单元格
                xlsheet.write(0, 0, '起始时间：', style3)
                xlsheet.write(0, 1, starttime, style1)
                xlsheet.write(0, 3, '截止时间：', style3)
                xlsheet.write(0, 4, endtime, style1)
                xlsheet.write(0, 6, '工单类型：', style3)
                xlsheet.write(0, 7, choose_type, style3)
                xlsheet.write(1, 0, '区县（区域属性）', style1)
                xlsheet.write(1, 1, '当日受理工单量', style1)
                xlsheet.write(1, 2, '当日装机完成量', style1)
                xlsheet.write(1, 3, '已装超时量', style1)
                xlsheet.write(1, 4, '未装超时量', style1)
                xlsheet.write(1, 5, '压单量', style1)
                xlsheet.write(1, 6, '装机及时率', style1)
                xlsheet.write(1, 7, '平均装机时长（小时）', style1)
                xlsheet.write(2, 0, '备注', style1)
                xlsheet.write(2, 1, '农普受理量', style1)
                xlsheet.write(2, 2, '农普完成量', style1)
                xlsheet.write(2, 3, '装机时长大于7天的已完成工单', style1)
                xlsheet.write(2, 4, '没完成工单中，已超时7天', style1)
                xlsheet.write(2, 5, '本月以前受理，未完成', style1)
                xlsheet.write(2, 6, '(农普受理量-已装超时量-未装超时量-本月以前压单量)/农普受理量', style1)
                xlsheet.write(2, 7, '累计完成时长/装机完成量', style1)
                xlsheet.write(3, 0, '城区', style1)
                xlsheet.write(3, 1, len([x for x in msg_list if x[0] == '宜昌城区']), style1)
                xlsheet.write(3, 2, len([x for x in msg_list1 if x[0] == '宜昌城区']), style1)
                xlsheet.write(3, 3, len([x for x in msg_list if x[0] == '宜昌城区' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(3, 4, len([x for x in msg_list if x[0] == '宜昌城区' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(3, 5, len([x for x in msg_list if x[0] == '宜昌城区' and x[1] == '未完成' and x[3] == 1]),
                              style1)
                xlsheet.write(3, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(4, 4, 4, 4, 4)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '宜昌城区' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(3, 7, '%.2f' % (
                    av_time(all_time, len([x for x in msg_list if x[0] == '宜昌城区' and x[1] == '完成']))), style1)

                xlsheet.write(4, 0, '当阳', style1)
                xlsheet.write(4, 1, len([x for x in msg_list if x[0] == '当阳']), style1)
                xlsheet.write(4, 2, len([x for x in msg_list1 if x[0] == '当阳' ]), style1)
                xlsheet.write(4, 3, len([x for x in msg_list if x[0] == '当阳' and x[1] == '完成' and x[2] == '是']), style1)
                xlsheet.write(4, 4, len([x for x in msg_list if x[0] == '当阳' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(4, 5, len([x for x in msg_list if x[0] == '当阳' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(4, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(5, 5, 5, 5, 5)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '当阳' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(4, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '当阳' and x[1] == '完成']))),
                              style1)
                xlsheet.write(5, 0, '开发区', style1)
                xlsheet.write(5, 1, len([x for x in msg_list if x[0] == '宜昌开发区']), style1)
                xlsheet.write(5, 2, len([x for x in msg_list1 if x[0] == '宜昌开发区']), style1)
                xlsheet.write(5, 3, len([x for x in msg_list if x[0] == '宜昌开发区' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(5, 4, len([x for x in msg_list if x[0] == '宜昌开发区' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(5, 5, len([x for x in msg_list if x[0] == '宜昌开发区' and x[1] == '未完成' and x[3] == 1]),
                              style1)
                xlsheet.write(5, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(6, 6, 6, 6, 6)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '宜昌开发区' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(5, 7, '%.2f' % (
                    av_time(all_time, len([x for x in msg_list if x[0] == '宜昌开发区' and x[1] == '完成']))),
                              style1)
                xlsheet.write(6, 0, '五峰', style1)
                xlsheet.write(6, 1, len([x for x in msg_list if x[0] == '五峰']), style1)
                xlsheet.write(6, 2, len([x for x in msg_list1 if x[0] == '五峰' ]), style1)
                xlsheet.write(6, 3, len([x for x in msg_list if x[0] == '五峰' and x[1] == '完成' and x[2] == '是']), style1)
                xlsheet.write(6, 4, len([x for x in msg_list if x[0] == '五峰' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(6, 5, len([x for x in msg_list if x[0] == '五峰' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(6, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(7, 7, 7, 7, 7)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '五峰' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(6, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '五峰' and x[1] == '完成']))),
                              style1)
                xlsheet.write(7, 0, '兴山', style1)
                xlsheet.write(7, 1, len([x for x in msg_list if x[0] == '兴山']), style1)
                xlsheet.write(7, 2, len([x for x in msg_list1 if x[0] == '兴山' ]), style1)
                xlsheet.write(7, 3, len([x for x in msg_list if x[0] == '兴山' and x[1] == '完成' and x[2] == '是']), style1)
                xlsheet.write(7, 4, len([x for x in msg_list if x[0] == '兴山' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(7, 5, len([x for x in msg_list if x[0] == '兴山' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(7, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(8, 8, 8, 8, 8)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '兴山' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(7, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '兴山' and x[1] == '完成']))),
                              style1)
                xlsheet.write(8, 0, '夷陵', style1)
                xlsheet.write(8, 1, len([x for x in msg_list if x[0] == '夷陵']), style1)
                xlsheet.write(8, 2, len([x for x in msg_list1 if x[0] == '夷陵' ]), style1)
                xlsheet.write(8, 3, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '完成' and x[2] == '是']), style1)
                xlsheet.write(8, 4, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(8, 5, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(8, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(9, 9, 9, 9, 9)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '夷陵' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(8, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '完成']))),
                              style1)
                xlsheet.write(9, 0, '宜都', style1)
                xlsheet.write(9, 1, len([x for x in msg_list if x[0] == '宜都']), style1)
                xlsheet.write(9, 2, len([x for x in msg_list1 if x[0] == '宜都' ]), style1)
                xlsheet.write(9, 3, len([x for x in msg_list if x[0] == '宜都' and x[1] == '完成' and x[2] == '是']), style1)
                xlsheet.write(9, 4, len([x for x in msg_list if x[0] == '宜都' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(9, 5, len([x for x in msg_list if x[0] == '宜都' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(9, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(10, 10, 10, 10, 10)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '宜都' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(9, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '宜都' and x[1] == '完成']))),
                              style1)
                xlsheet.write(10, 0, '远安', style1)
                xlsheet.write(10, 1, len([x for x in msg_list if x[0] == '远安']), style1)
                xlsheet.write(10, 2, len([x for x in msg_list1 if x[0] == '远安' ]), style1)
                xlsheet.write(10, 3, len([x for x in msg_list if x[0] == '远安' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(10, 4, len([x for x in msg_list if x[0] == '远安' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(10, 5, len([x for x in msg_list if x[0] == '远安' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(10, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(11, 11, 11, 11, 11)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '远安' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(10, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '远安' and x[1] == '完成']))),
                              style1)

                xlsheet.write(11, 0, '长阳', style1)
                xlsheet.write(11, 1, len([x for x in msg_list if x[0] == '长阳']), style1)
                xlsheet.write(11, 2, len([x for x in msg_list1 if x[0] == '长阳' ]), style1)
                xlsheet.write(11, 3, len([x for x in msg_list if x[0] == '长阳' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(11, 4, len([x for x in msg_list if x[0] == '长阳' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(11, 5, len([x for x in msg_list if x[0] == '长阳' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(11, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(12, 12, 12, 12, 12)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '长阳' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(11, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '长阳' and x[1] == '完成']))),
                              style1)

                xlsheet.write(12, 0, '枝江', style1)
                xlsheet.write(12, 1, len([x for x in msg_list if x[0] == '枝江']), style1)
                xlsheet.write(12, 2, len([x for x in msg_list1 if x[0] == '枝江' ]), style1)
                xlsheet.write(12, 3, len([x for x in msg_list if x[0] == '枝江' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(12, 4, len([x for x in msg_list if x[0] == '枝江' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(12, 5, len([x for x in msg_list if x[0] == '枝江' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(12, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(13, 13, 13, 13, 13)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '枝江' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(12, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '枝江' and x[1] == '完成']))),
                              style1)

                xlsheet.write(13, 0, '秭归', style1)
                xlsheet.write(13, 1, len([x for x in msg_list if x[0] == '秭归']), style1)
                xlsheet.write(13, 2, len([x for x in msg_list1 if x[0] == '秭归']), style1)
                xlsheet.write(13, 3, len([x for x in msg_list if x[0] == '秭归' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(13, 4, len([x for x in msg_list if x[0] == '秭归' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(13, 5, len([x for x in msg_list if x[0] == '秭归' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(13, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(14, 14, 14, 14, 14)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '秭归' and x[1] == '完成']:
                    all_time = all_time + i[-1]

                xlsheet.write(13, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '秭归' and x[1] == '完成']))),
                              style1)

                xlsheet.write(14, 0, '全市', style1)
                xlsheet.write(14, 1, xlwt.Formula("(B4+B5+B6+B7+B8+B9+B10+B11+B12+B13+B14)"), style1)
                xlsheet.write(14, 2, xlwt.Formula("(C4+C5+C6+C7+C8+C9+C10+C11+C12+C13+C14)"), style1)
                xlsheet.write(14, 3, xlwt.Formula("(D4+D5+D6+D7+D8+D9+D10+D11+D12+D13+D14)"), style1)
                xlsheet.write(14, 4, xlwt.Formula("(E4+E5+E6+E7+E8+E9+E10+E11+E12+E13+E14)"), style1)
                xlsheet.write(14, 5, xlwt.Formula("(F4+F5+F6+F7+F8+F9+F10+F11+F12+F13+F14)"), style1)
                xlsheet.write(14, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(15, 15, 15, 15, 15)), style4)
                xlsheet.write(14, 7, xlwt.Formula("(H4+H5+H6+H7+H8+H9+H10+H11+H12+H13+H14)/11"), style1)
                xlsname=choose_type + str(int(time.time()))
                workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
                return ('mail.itlaolang.com/downfile/{}.xls'.format(xlsname))
            if choose_type == '全量工单':
                for x in range(1, sheet.nrows):
                    try:
                        msg = sheet.row_values(x)
                        #这是之间段之内完成的工单数据
                        if msg[9] != 'order_status_6'  and utc_str_to_timestamp(msg[15]) >= utc_str_to_timestamp(
                                starttime) and utc_str_to_timestamp(msg[15]) <= utc_str_to_timestamp(endtime) \
                                and msg[19] == '普服小区' or msg[19] == '普遍服务':
                            finshed=[find_area(msg[1], msg[11])]
                            msg_list1.append(finshed)
                        #这是时间段之内受理工单数据
                        if msg[9] != 'order_status_6'  and utc_str_to_timestamp(msg[12]) >= utc_str_to_timestamp(
                                starttime) and utc_str_to_timestamp(msg[12]) <= utc_str_to_timestamp(endtime) \
                                and msg[19] == '普服小区' or msg[19] == '普遍服务':
                            result = [find_area(msg[1], msg[11]), get_status(msg[15],starttime,endtime),
                                      get_timeout(msg[12], msg[15], msg[19]), downdan(msg[12]),
                                      time_for_end(msg[12], msg[15])]
                            # print(result)
                            msg_list.append(result)

                    except:
                        pass
                # print(len([x for x in msg_list if x[0] == '枝江']))
                # print(len([x for x in msg_list if x[0] == '枝江' and x[1]=='完成']))
                # print(len([x for x in msg_list if x[0] == '枝江' and x[1]=='完成' and x[2]=='是']))
                # print(len([x for x in msg_list if x[0] == '枝江' and x[1]=='未完成' and x[2]=='是']))
                # print(len([x for x in msg_list if x[0] == '枝江' and x[1]=='未完成' and x[3]==1]))
                all_time = 0
                print(len([x for x in msg_list if x[0] == '夷陵' and x[1] == '完成']))
                for i in [x for x in msg_list if x[0] == '夷陵' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                # print(all_time)
                # print(av_time(all_time,len([x for x in msg_list if x[0] == '夷陵' and x[1] == '完成'])))
                print('%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '完成']))))

                workbook_m = xlwt.Workbook(encoding='utf-8')
                xlsheet = workbook_m.add_sheet('农普及时率', cell_overwrite_ok=True)
                # 格式1 （有自动换行）
                style1 = xlwt.easyxf('pattern: pattern solid, fore_colour white')
                style1.font.height = 200
                style1.font.name = u'文泉驿点阵正黑'
                style1.font.colour_index = 0
                style1.borders.left = xlwt.Borders.THIN
                style1.borders.right = xlwt.Borders.THIN
                style1.borders.top = xlwt.Borders.THIN
                style1.borders.bottom = xlwt.Borders.THIN
                # style1.font.bold = True
                style1.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
                style1.alignment.horz = xlwt.Alignment.HORZ_CENTER

                # 格式2  （没有自动换行）
                style2 = xlwt.easyxf('pattern: pattern solid, fore_colour white')
                style2.font.height = 200
                style2.font.name = u'文泉驿点阵正黑'
                style2.font.colour_index = 0
                style2.borders.left = xlwt.Borders.THIN
                style2.borders.right = xlwt.Borders.THIN
                style2.borders.top = xlwt.Borders.THIN
                style2.borders.bottom = xlwt.Borders.THIN

                # style2.font.bold = True
                # style2.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
                # style2.alignment.horz = xlwt.Alignment.HORZ_CENTER

                # 格式3 黄色背景色

                style3 = xlwt.easyxf('pattern: pattern solid, fore_colour yellow')
                style3.font.height = 200
                style3.font.name = u'文泉驿点阵正黑'
                style3.font.colour_index = 0
                # style3.borders.left = xlwt.Borders.THIN
                # style3.borders.right = xlwt.Borders.THIN
                # style3.borders.top = xlwt.Borders.THIN
                # style3.borders.bottom = xlwt.Borders.THIN

                # style4 格式4 0.00%

                style4 = xlwt.easyxf('pattern: pattern solid, fore_colour white')
                style4.font.height = 200
                style4.font.name = u'文泉驿点阵正黑'
                style4.font.colour_index = 0
                style4.borders.left = xlwt.Borders.THIN
                style4.borders.right = xlwt.Borders.THIN
                style4.borders.top = xlwt.Borders.THIN
                style4.borders.bottom = xlwt.Borders.THIN
                # style1.font.bold = True
                style4.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
                style4.alignment.horz = xlwt.Alignment.HORZ_CENTER
                style4.num_format_str = '0.00%'

                # style2.font.bold = True
                # style2.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
                # style2.alignment.horz = xlwt.Alignment.HORZ_CENTER
                # 写excel表头
                # 设置单元格
                xlsheet.write(0, 0, '起始时间：', style3)
                xlsheet.write(0, 1, starttime, style1)
                xlsheet.write(0, 3, '截止时间：', style3)
                xlsheet.write(0, 4, endtime, style1)
                xlsheet.write(0, 6, '工单类型：', style3)
                xlsheet.write(0, 7, choose_type, style3)
                xlsheet.write(1, 0, '区县（区域属性）', style1)
                xlsheet.write(1, 1, '当日受理工单量', style1)
                xlsheet.write(1, 2, '当日装机完成量', style1)
                xlsheet.write(1, 3, '已装超时量', style1)
                xlsheet.write(1, 4, '未装超时量', style1)
                xlsheet.write(1, 5, '压单量', style1)
                xlsheet.write(1, 6, '装机及时率', style1)
                xlsheet.write(1, 7, '平均装机时长（小时）', style1)
                xlsheet.write(2, 0, '备注', style1)
                xlsheet.write(2, 1, '农普受理量', style1)
                xlsheet.write(2, 2, '农普完成量', style1)
                xlsheet.write(2, 3, '装机时长大于7天的已完成工单', style1)
                xlsheet.write(2, 4, '没完成工单中，已超时7天', style1)
                xlsheet.write(2, 5, '本月以前受理，未完成', style1)
                xlsheet.write(2, 6, '(农普受理量-已装超时量-未装超时量-本月以前压单量)/农普受理量', style1)
                xlsheet.write(2, 7, '累计完成时长/装机完成量', style1)
                xlsheet.write(3, 0, '城区', style1)
                xlsheet.write(3, 1, len([x for x in msg_list if x[0] == '宜昌城区']), style1)
                xlsheet.write(3, 2, len([x for x in msg_list1 if x[0] == '宜昌城区']), style1)
                xlsheet.write(3, 3, len([x for x in msg_list if x[0] == '宜昌城区' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(3, 4, len([x for x in msg_list if x[0] == '宜昌城区' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(3, 5, len([x for x in msg_list if x[0] == '宜昌城区' and x[1] == '未完成' and x[3] == 1]),
                              style1)
                xlsheet.write(3, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(4, 4, 4, 4, 4)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '宜昌城区' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(3, 7, '%.2f' % (
                    av_time(all_time, len([x for x in msg_list if x[0] == '宜昌城区' and x[1] == '完成']))), style1)

                xlsheet.write(4, 0, '当阳', style1)
                xlsheet.write(4, 1, len([x for x in msg_list if x[0] == '当阳']), style1)
                xlsheet.write(4, 2, len([x for x in msg_list1 if x[0] == '当阳' ]), style1)
                xlsheet.write(4, 3, len([x for x in msg_list if x[0] == '当阳' and x[1] == '完成' and x[2] == '是']), style1)
                xlsheet.write(4, 4, len([x for x in msg_list if x[0] == '当阳' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(4, 5, len([x for x in msg_list if x[0] == '当阳' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(4, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(5, 5, 5, 5, 5)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '当阳' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(4, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '当阳' and x[1] == '完成']))),
                              style1)
                xlsheet.write(5, 0, '开发区', style1)
                xlsheet.write(5, 1, len([x for x in msg_list if x[0] == '宜昌开发区']), style1)
                xlsheet.write(5, 2, len([x for x in msg_list1 if x[0] == '宜昌开发区']), style1)
                xlsheet.write(5, 3, len([x for x in msg_list if x[0] == '宜昌开发区' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(5, 4, len([x for x in msg_list if x[0] == '宜昌开发区' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(5, 5, len([x for x in msg_list if x[0] == '宜昌开发区' and x[1] == '未完成' and x[3] == 1]),
                              style1)
                xlsheet.write(5, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(6, 6, 6, 6, 6)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '宜昌开发区' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(5, 7, '%.2f' % (
                    av_time(all_time, len([x for x in msg_list if x[0] == '宜昌开发区' and x[1] == '完成']))),
                              style1)
                xlsheet.write(6, 0, '五峰', style1)
                xlsheet.write(6, 1, len([x for x in msg_list if x[0] == '五峰']), style1)
                xlsheet.write(6, 2, len([x for x in msg_list1 if x[0] == '五峰' ]), style1)
                xlsheet.write(6, 3, len([x for x in msg_list if x[0] == '五峰' and x[1] == '完成' and x[2] == '是']), style1)
                xlsheet.write(6, 4, len([x for x in msg_list if x[0] == '五峰' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(6, 5, len([x for x in msg_list if x[0] == '五峰' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(6, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(7, 7, 7, 7, 7)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '五峰' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(6, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '五峰' and x[1] == '完成']))),
                              style1)
                xlsheet.write(7, 0, '兴山', style1)
                xlsheet.write(7, 1, len([x for x in msg_list if x[0] == '兴山']), style1)
                xlsheet.write(7, 2, len([x for x in msg_list1 if x[0] == '兴山' ]), style1)
                xlsheet.write(7, 3, len([x for x in msg_list if x[0] == '兴山' and x[1] == '完成' and x[2] == '是']), style1)
                xlsheet.write(7, 4, len([x for x in msg_list if x[0] == '兴山' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(7, 5, len([x for x in msg_list if x[0] == '兴山' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(7, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(8, 8, 8, 8, 8)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '兴山' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(7, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '兴山' and x[1] == '完成']))),
                              style1)
                xlsheet.write(8, 0, '夷陵', style1)
                xlsheet.write(8, 1, len([x for x in msg_list if x[0] == '夷陵']), style1)
                xlsheet.write(8, 2, len([x for x in msg_list1 if x[0] == '夷陵' ]), style1)
                xlsheet.write(8, 3, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '完成' and x[2] == '是']), style1)
                xlsheet.write(8, 4, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(8, 5, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(8, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(9, 9, 9, 9, 9)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '夷陵' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(8, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '完成']))),
                              style1)
                xlsheet.write(9, 0, '宜都', style1)
                xlsheet.write(9, 1, len([x for x in msg_list if x[0] == '宜都']), style1)
                xlsheet.write(9, 2, len([x for x in msg_list1 if x[0] == '宜都' ]), style1)
                xlsheet.write(9, 3, len([x for x in msg_list if x[0] == '宜都' and x[1] == '完成' and x[2] == '是']), style1)
                xlsheet.write(9, 4, len([x for x in msg_list if x[0] == '宜都' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(9, 5, len([x for x in msg_list if x[0] == '宜都' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(9, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(10, 10, 10, 10, 10)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '宜都' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(9, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '宜都' and x[1] == '完成']))),
                              style1)
                xlsheet.write(10, 0, '远安', style1)
                xlsheet.write(10, 1, len([x for x in msg_list if x[0] == '远安']), style1)
                xlsheet.write(10, 2, len([x for x in msg_list1 if x[0] == '远安' ]), style1)
                xlsheet.write(10, 3, len([x for x in msg_list if x[0] == '远安' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(10, 4, len([x for x in msg_list if x[0] == '远安' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(10, 5, len([x for x in msg_list if x[0] == '远安' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(10, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(11, 11, 11, 11, 11)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '远安' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(10, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '远安' and x[1] == '完成']))),
                              style1)

                xlsheet.write(11, 0, '长阳', style1)
                xlsheet.write(11, 1, len([x for x in msg_list if x[0] == '长阳']), style1)
                xlsheet.write(11, 2, len([x for x in msg_list1 if x[0] == '长阳' ]), style1)
                xlsheet.write(11, 3, len([x for x in msg_list if x[0] == '长阳' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(11, 4, len([x for x in msg_list if x[0] == '长阳' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(11, 5, len([x for x in msg_list if x[0] == '长阳' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(11, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(12, 12, 12, 12, 12)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '长阳' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(11, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '长阳' and x[1] == '完成']))),
                              style1)

                xlsheet.write(12, 0, '枝江', style1)
                xlsheet.write(12, 1, len([x for x in msg_list if x[0] == '枝江']), style1)
                xlsheet.write(12, 2, len([x for x in msg_list1 if x[0] == '枝江' ]), style1)
                xlsheet.write(12, 3, len([x for x in msg_list if x[0] == '枝江' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(12, 4, len([x for x in msg_list if x[0] == '枝江' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(12, 5, len([x for x in msg_list if x[0] == '枝江' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(12, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(13, 13, 13, 13, 13)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '枝江' and x[1] == '完成']:
                    all_time = all_time + i[-1]
                xlsheet.write(12, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '枝江' and x[1] == '完成']))),
                              style1)

                xlsheet.write(13, 0, '秭归', style1)
                xlsheet.write(13, 1, len([x for x in msg_list if x[0] == '秭归']), style1)
                xlsheet.write(13, 2, len([x for x in msg_list1 if x[0] == '秭归']), style1)
                xlsheet.write(13, 3, len([x for x in msg_list if x[0] == '秭归' and x[1] == '完成' and x[2] == '是']),
                              style1)
                xlsheet.write(13, 4, len([x for x in msg_list if x[0] == '秭归' and x[1] == '未完成' and x[2] == '是']),
                              style1)
                xlsheet.write(13, 5, len([x for x in msg_list if x[0] == '秭归' and x[1] == '未完成' and x[3] == 1]), style1)
                xlsheet.write(13, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(14, 14, 14, 14, 14)), style4)
                all_time = 0
                for i in [x for x in msg_list if x[0] == '秭归' and x[1] == '完成']:
                    all_time = all_time + i[-1]

                xlsheet.write(13, 7,
                              '%.2f' % (av_time(all_time, len([x for x in msg_list if x[0] == '秭归' and x[1] == '完成']))),
                              style1)

                xlsheet.write(14, 0, '全市', style1)
                xlsheet.write(14, 1, xlwt.Formula("(B4+B5+B6+B7+B8+B9+B10+B11+B12+B13+B14)"), style1)
                xlsheet.write(14, 2, xlwt.Formula("(C4+C5+C6+C7+C8+C9+C10+C11+C12+C13+C14)"), style1)
                xlsheet.write(14, 3, xlwt.Formula("(D4+D5+D6+D7+D8+D9+D10+D11+D12+D13+D14)"), style1)
                xlsheet.write(14, 4, xlwt.Formula("(E4+E5+E6+E7+E8+E9+E10+E11+E12+E13+E14)"), style1)
                xlsheet.write(14, 5, xlwt.Formula("(F4+F5+F6+F7+F8+F9+F10+F11+F12+F13+F14)"), style1)
                xlsheet.write(14, 6, xlwt.Formula("(B{}-D{}-E{}-F{})/(B{})".format(15, 15, 15, 15, 15)), style4)
                xlsheet.write(14, 7, xlwt.Formula("(H4+H5+H6+H7+H8+H9+H10+H11+H12+H13+H14)/11"), style1)
                workbook_m.save('var/www/downfile/{}.xls'.format(choose_type))
    print('mail.itlaolang.com/downfile/{}.xls'.format(choose_type))
    return ('mail.itlaolang.com/downfile/{}.xls'.format(choose_type))



#投诉报表生成
def make_file1(file_path,type,starttime,endtime,choose_type):
    workbook_r = xlrd.open_workbook(file_path)
    msg_list = []
    msg_list1=[]

    if type=='投诉24小时报表':
        if choose_type=='EMOS':

            sheet = workbook_r.sheet_by_name('EMOS')
            for x in range(1, sheet.nrows):

                msg = sheet.row_values(x)
                #这是完成的工单量
                if msg[8] == '归档' and msg[18] != '' and utc_str_to_timestamp(
                        str(xlrd.xldate_as_datetime(msg[18], 0))) >= utc_str_to_timestamp(
                        starttime) and utc_str_to_timestamp(
                        str(xlrd.xldate_as_datetime(msg[18], 0))) <= utc_str_to_timestamp(endtime):
                    msg_list1.append([find_area1(msg[-1], msg[2])])
                #这是接受的工单量
                if msg[8] != '待回访' and msg[18]!='' and utc_str_to_timestamp(str(xlrd.xldate_as_datetime(msg[16], 0))) >= utc_str_to_timestamp(starttime) and utc_str_to_timestamp(str(xlrd.xldate_as_datetime(msg[16], 0))) <= utc_str_to_timestamp(endtime):
                    result = [find_area1(msg[-1], msg[2]), msg[8], get_timeout1(msg[8], msg[16], msg[18]),
                              time_for_end1(msg[16], msg[18]), msg[2]]#地区，状态，超时（包括运行中，归档），投诉时长,投诉地址
                    msg_list.append(result)


            workbook_m = xlwt.Workbook(encoding='utf-8')
            xlsheet = workbook_m.add_sheet('24小时投诉日报', cell_overwrite_ok=True)
            # 格式1 （有自动换行）
            style1 = xlwt.easyxf('pattern: pattern solid, fore_colour white')
            style1.font.height = 200
            style1.font.name = u'文泉驿点阵正黑'
            style1.font.colour_index = 0
            style1.borders.left = xlwt.Borders.THIN
            style1.borders.right = xlwt.Borders.THIN
            style1.borders.top = xlwt.Borders.THIN
            style1.borders.bottom = xlwt.Borders.THIN
            # style1.font.bold = True
            style1.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
            style1.alignment.horz = xlwt.Alignment.HORZ_CENTER
            style1.num_format_str ='0.00'

            # 格式2  （没有自动换行）
            style2 = xlwt.easyxf('pattern: pattern solid, fore_colour white')
            style2.font.height = 200
            style2.font.name = u'文泉驿点阵正黑'
            style2.font.colour_index = 0
            style2.borders.left = xlwt.Borders.THIN
            style2.borders.right = xlwt.Borders.THIN
            style2.borders.top = xlwt.Borders.THIN
            style2.borders.bottom = xlwt.Borders.THIN

            # style2.font.bold = True
            # style2.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
            # style2.alignment.horz = xlwt.Alignment.HORZ_CENTER

            # 格式3 黄色背景色

            style3 = xlwt.easyxf('pattern: pattern solid, fore_colour yellow')
            style3.font.height = 200
            style3.font.name = u'文泉驿点阵正黑'
            style3.font.colour_index = 0
            # style3.borders.left = xlwt.Borders.THIN
            # style3.borders.right = xlwt.Borders.THIN
            # style3.borders.top = xlwt.Borders.THIN
            # style3.borders.bottom = xlwt.Borders.THIN

            # style4 格式4 0.00%

            style4 = xlwt.easyxf('pattern: pattern solid, fore_colour white')
            style4.font.height = 200
            style4.font.name = u'文泉驿点阵正黑'
            style4.font.colour_index = 0
            style4.borders.left = xlwt.Borders.THIN
            style4.borders.right = xlwt.Borders.THIN
            style4.borders.top = xlwt.Borders.THIN
            style4.borders.bottom = xlwt.Borders.THIN
            # style1.font.bold = True
            style4.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
            style4.alignment.horz = xlwt.Alignment.HORZ_CENTER
            style4.num_format_str = '0.00%'

            # style2.font.bold = True
            # style2.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
            # style2.alignment.horz = xlwt.Alignment.HORZ_CENTER
            # 写excel表头
            # 设置单元格
            xlsheet.write(0, 1, '起始时间：', style3)
            xlsheet.write(0, 2, starttime, style3)
            xlsheet.write(0, 3, '', style3)
            xlsheet.write(0, 4, '截止时间：', style3)
            xlsheet.write(0, 5, endtime, style3)
            xlsheet.write(0, 6, '', style3)
            xlsheet.write(0, 7, '工单类型：', style3)
            xlsheet.write(0, 8, choose_type, style3)

            xlsheet.write_merge(2, 2, 0, 9, '宜昌分公司家宽投诉日报（24小时）', style2)
            xlsheet.write(3, 0, '区县', style1)
            xlsheet.write(3, 1, '受理量', style1)
            xlsheet.write(3, 2, '完成量', style1)
            xlsheet.write(3, 3, '未完成超时', style1)
            xlsheet.write(3, 4, '已完成超时', style1)
            xlsheet.write(3, 5, '投诉处理及时率', style1)
            xlsheet.write(3, 6, '平均处理时长', style1)
            xlsheet.write(3, 7, '重复量', style1)
            xlsheet.write(3, 8, '重复投诉率', style1)
            xlsheet.write(3, 9, '万投比', style1)
            xlsheet.write(4, 0, '备注', style1)
            xlsheet.write(4, 1, '派发工单量', style1)
            xlsheet.write(4, 2, '归档完成工单量', style1)
            xlsheet.write(4, 3, '工单状态为“运行中”，超过派单时间24小时工单', style1)
            xlsheet.write(4, 4, '工单状态为“归档”，处理时长超24小时工单', style1)
            xlsheet.write(4, 5, '1-超时量/受理量', style1)
            xlsheet.write(4, 6, '时长=T2操作时间-T1派发时间', style1)
            xlsheet.write(4, 7, '5天内同一用户（客户电话一致）发生过2次及2次以上的投诉', style1)
            xlsheet.write(4, 8, '重复量/受理量', style1)
            xlsheet.write(4, 9, '10000*受理量/用户数', style1)

            xlsheet.write(5,0,'城区',style1)
            xlsheet.write(5,1,len([x for x in msg_list if x[0] == '城区']),style1)
            xlsheet.write(5,2,len([x for x in msg_list1 if x[0] == '城区']),style1)
            xlsheet.write(5,3,len([x for x in msg_list if x[0] == '城区' and x[1] =='运行中' and x[2] == '是']),style1)
            xlsheet.write(5,4,len([x for x in msg_list if x[0] == '城区' and x[1] =='归档' and x[2] == '是']),style1)
            xlsheet.write(5,5,xlwt.Formula("1-((D6+E6)/(B6))"),style4)
            all_time=0
            for i in [x for x in msg_list if x[0] == '城区']:
                all_time = all_time + i[-2]
            xlsheet.write(5, 6, '%.2f' % (
                av_time(all_time, len([x for x in msg_list if x[0] == '城区']))), style1)
            xlsheet.write(5,7,1,style1)
            xlsheet.write(5,8,xlwt.Formula("(H6/B6)"),style4)
            xlsheet.write(5, 9, xlwt.Formula("(B6*10000)/ 25171" ), style1)

            xlsheet.write(6, 0, '当阳', style1)
            xlsheet.write(6, 1, len([x for x in msg_list if x[0] == '当阳']), style1)
            xlsheet.write(6, 2, len([x for x in msg_list1 if x[0] == '当阳']), style1)
            xlsheet.write(6, 3, len([x for x in msg_list if x[0] == '当阳' and x[1] == '运行中' and x[2] == '是']), style1)
            xlsheet.write(6, 4, len([x for x in msg_list if x[0] == '当阳' and x[1] == '归档' and x[2] == '是']), style1)
            xlsheet.write(6, 5, xlwt.Formula("1-((D7+E7)/(B7))"), style4)
            all_time = 0
            for i in [x for x in msg_list if x[0] == '当阳']:
                all_time = all_time + i[-2]
            xlsheet.write(6, 6, '%.2f' % (
                av_time(all_time, len([x for x in msg_list if x[0] == '当阳']))), style1)
            xlsheet.write(6, 7, 1, style1)
            xlsheet.write(6, 8, xlwt.Formula("(H7/B7)"), style4)
            xlsheet.write(6, 9, xlwt.Formula("(B7*10000)/ 25349" ), style1)

            xlsheet.write(7, 0, '开发区', style1)
            xlsheet.write(7, 1, len([x for x in msg_list if x[0] == '开发区']), style1)
            xlsheet.write(7, 2, len([x for x in msg_list1 if x[0] == '开发区' ]), style1)
            xlsheet.write(7, 3, len([x for x in msg_list if x[0] == '开发区' and x[1] == '运行中' and x[2] == '是']), style1)
            xlsheet.write(7, 4, len([x for x in msg_list if x[0] == '开发区' and x[1] == '归档' and x[2] == '是']), style1)
            xlsheet.write(7, 5, xlwt.Formula("1-((D8+E8)/(B8))"), style4)
            all_time = 0
            for i in [x for x in msg_list if x[0] == '开发区']:
                all_time = all_time + i[-2]
            xlsheet.write(7, 6, '%.2f' % (
                av_time(all_time, len([x for x in msg_list if x[0] == '开发区']))), style1)
            xlsheet.write(7, 7, 1, style1)
            xlsheet.write(7, 8, xlwt.Formula("(H8/B8)"), style4)
            xlsheet.write(7, 9, xlwt.Formula("(B8*10000)/ 34313"), style1)

            xlsheet.write(8, 0, '五峰', style1)
            xlsheet.write(8, 1, len([x for x in msg_list if x[0] == '五峰']), style1)
            xlsheet.write(8, 2, len([x for x in msg_list1 if x[0] == '五峰' ]), style1)
            xlsheet.write(8, 3, len([x for x in msg_list if x[0] == '五峰' and x[1] == '运行中' and x[2] == '是']), style1)
            xlsheet.write(8, 4, len([x for x in msg_list if x[0] == '五峰' and x[1] == '归档' and x[2] == '是']), style1)
            xlsheet.write(8, 5, xlwt.Formula("1-((D9+E9)/(B9))"), style4)
            all_time = 0
            for i in [x for x in msg_list if x[0] == '五峰']:
                all_time = all_time + i[-2]
            xlsheet.write(8, 6, '%.2f' % (
                av_time(all_time, len([x for x in msg_list if x[0] == '五峰']))), style1)
            xlsheet.write(8, 7, 1, style1)
            xlsheet.write(8, 8, xlwt.Formula("(H9/B9)"), style4)
            xlsheet.write(8, 9, xlwt.Formula("(B9*10000)/ 7985" ), style1)

            xlsheet.write(9, 0, '兴山', style1)
            xlsheet.write(9, 1, len([x for x in msg_list if x[0] == '兴山']), style1)
            xlsheet.write(9, 2, len([x for x in msg_list1 if x[0] == '兴山' ]), style1)
            xlsheet.write(9, 3, len([x for x in msg_list if x[0] == '兴山' and x[1] == '运行中' and x[2] == '是']), style1)
            xlsheet.write(9, 4, len([x for x in msg_list if x[0] == '兴山' and x[1] == '归档' and x[2] == '是']), style1)
            xlsheet.write(9, 5, xlwt.Formula("1-((D10+E10)/(B10))"), style4)
            all_time = 0
            for i in [x for x in msg_list if x[0] == '兴山']:

                all_time = all_time + i[-2]
            xlsheet.write(9, 6, '%.2f' % (
                av_time(all_time, len([x for x in msg_list if x[0] == '兴山']))), style1)
            xlsheet.write(9, 7, 1, style1)
            xlsheet.write(9, 8, xlwt.Formula("(H10/B10)"), style4)
            xlsheet.write(9, 9, xlwt.Formula(("(B10*10000)/ 7453") ), style1)

            xlsheet.write(10, 0, '夷陵', style1)
            xlsheet.write(10, 1, len([x for x in msg_list if x[0] == '夷陵']), style1)
            xlsheet.write(10, 2, len([x for x in msg_list1 if x[0] == '夷陵' ]), style1)
            xlsheet.write(10, 3, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '运行中' and x[2] == '是']), style1)
            xlsheet.write(10, 4, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '归档' and x[2] == '是']), style1)
            xlsheet.write(10, 5, xlwt.Formula("1-((D11+E11)/(B11))"), style4)
            all_time = 0
            for i in [x for x in msg_list if x[0] == '夷陵']:

                all_time = all_time + i[-2]
            xlsheet.write(10, 6, '%.2f' % (
                av_time(all_time, len([x for x in msg_list if x[0] == '夷陵']))), style1)
            xlsheet.write(10, 7, 1, style1)
            xlsheet.write(10, 8, xlwt.Formula("(H11/B11)"), style4)
            xlsheet.write(10, 9, xlwt.Formula("(B11*10000)/ 27196" ), style1)

            xlsheet.write(11, 0, '宜都', style1)
            xlsheet.write(11, 1, len([x for x in msg_list if x[0] == '宜都']), style1)
            xlsheet.write(11, 2, len([x for x in msg_list1 if x[0] == '宜都']), style1)
            xlsheet.write(11, 3, len([x for x in msg_list if x[0] == '宜都' and x[1] == '运行中' and x[2] == '是']), style1)
            xlsheet.write(11, 4, len([x for x in msg_list if x[0] == '宜都' and x[1] == '归档' and x[2] == '是']), style1)
            xlsheet.write(11, 5, xlwt.Formula("1-((D12+E12)/(B12))"), style4)
            all_time = 0
            for i in [x for x in msg_list if x[0] == '宜都']:
                all_time = all_time + i[-2]
            xlsheet.write(11, 6, '%.2f' % (
                av_time(all_time, len([x for x in msg_list if x[0] == '宜都']))), style1)
            xlsheet.write(11, 7, 1, style1)
            xlsheet.write(11, 8, xlwt.Formula("(H12/B12)"), style4)
            xlsheet.write(11, 9, xlwt.Formula("(B12*10000)/ 17538"), style1)

            xlsheet.write(12, 0, '远安', style1)
            xlsheet.write(12, 1, len([x for x in msg_list if x[0] == '远安']), style1)
            xlsheet.write(12, 2, len([x for x in msg_list1 if x[0] == '远安']), style1)
            xlsheet.write(12, 3, len([x for x in msg_list if x[0] == '远安' and x[1] == '运行中' and x[2] == '是']), style1)
            xlsheet.write(12, 4, len([x for x in msg_list if x[0] == '远安' and x[1] == '归档' and x[2] == '是']), style1)
            xlsheet.write(12, 5, xlwt.Formula("1-((D13+E13)/(B13))"), style4)
            all_time = 0
            for i in [x for x in msg_list if x[0] == '远安']:

                all_time = all_time + i[-2]

            xlsheet.write(12, 6, '%.2f' % (
                av_time(all_time, len([x for x in msg_list if x[0] == '远安']))), style1)
            xlsheet.write(12, 7, 1, style1)
            xlsheet.write(12, 8, xlwt.Formula("(H13/B13)"), style4)
            xlsheet.write(12, 9, xlwt.Formula("(B13*10000)/ 12884"), style1)

            xlsheet.write(13, 0, '长阳', style1)
            xlsheet.write(13, 1, len([x for x in msg_list if x[0] == '长阳']), style1)
            xlsheet.write(13, 2, len([x for x in msg_list1 if x[0] == '长阳']), style1)
            xlsheet.write(13, 3, len([x for x in msg_list if x[0] == '长阳' and x[1] == '运行中' and x[2] == '是']), style1)
            xlsheet.write(13, 4, len([x for x in msg_list if x[0] == '长阳' and x[1] == '归档' and x[2] == '是']), style1)
            xlsheet.write(13, 5, xlwt.Formula("1-((D14+E14)/(B14))"), style4)
            all_time = 0
            for i in [x for x in msg_list if x[0] == '城区']:
                all_time = all_time + i[-2]
            xlsheet.write(13, 6, '%.2f' % (
                av_time(all_time, len([x for x in msg_list if x[0] == '长阳']))), style1)
            xlsheet.write(13, 7, 1, style1)
            xlsheet.write(13, 8, xlwt.Formula("(H14/B14)"), style4)
            xlsheet.write(13, 9, xlwt.Formula("(B14*10000)/ 18385" ), style1)

            xlsheet.write(14, 0, '枝江', style1)
            xlsheet.write(14, 1, len([x for x in msg_list if x[0] == '枝江']), style1)
            xlsheet.write(14, 2, len([x for x in msg_list1 if x[0] == '枝江']), style1)
            xlsheet.write(14, 3, len([x for x in msg_list if x[0] == '枝江' and x[1] == '运行中' and x[2] == '是']), style1)
            xlsheet.write(14, 4, len([x for x in msg_list if x[0] == '枝江' and x[1] == '归档' and x[2] == '是']), style1)
            xlsheet.write(14, 5, xlwt.Formula("1-((D15+E15)/(B15))"), style4)
            all_time = 0
            for i in [x for x in msg_list if x[0] == '枝江']:
                all_time = all_time + i[-2]
            xlsheet.write(14, 6, '%.2f' % (
                av_time(all_time, len([x for x in msg_list if x[0] == '枝江']))), style1)
            xlsheet.write(14, 7, 1, style1)
            xlsheet.write(14, 8, xlwt.Formula("(H15/B15)"), style4)
            xlsheet.write(14, 9, xlwt.Formula("(B15*10000)/25378" ), style1)

            xlsheet.write(15, 0, '秭归', style1)
            xlsheet.write(15, 1, len([x for x in msg_list if x[0] == '秭归']), style1)
            xlsheet.write(15, 2, len([x for x in msg_list1 if x[0] == '秭归']), style1)
            xlsheet.write(15, 3, len([x for x in msg_list if x[0] == '秭归' and x[1] == '运行中' and x[2] == '是']), style1)
            xlsheet.write(15, 4, len([x for x in msg_list if x[0] == '秭归' and x[1] == '归档' and x[2] == '是']), style1)
            xlsheet.write(15, 5, xlwt.Formula("1-((D15+E15)/(B15))"), style4)
            all_time = 0
            for i in [x for x in msg_list if x[0] == '秭归']:
                all_time = all_time + i[-2]

            xlsheet.write(15, 6, '%.2f' % (
                av_time(all_time, len([x for x in msg_list if x[0] == '秭归']))), style1)
            xlsheet.write(15, 7, 1, style1)
            xlsheet.write(15, 8, xlwt.Formula("(H16/B16)"), style4)
            xlsheet.write(15, 9, xlwt.Formula("(B16*10000)/18203"), style1)

            xlsheet.write(16, 0, '全市', style1)
            xlsheet.write(16, 1, xlwt.Formula("(B6+B7+B8+B9+B10+B11+B12+B13+B14+B15+B16)"), style1)
            xlsheet.write(16, 2, xlwt.Formula("(C6+C7+C8+C9+C10+C11+C12+C13+C14+C15+C16)"), style1)
            xlsheet.write(16, 3, xlwt.Formula("(D6+D7+D8+D9+D10+D11+D12+D13+D14+D15+D16)"), style1)
            xlsheet.write(16, 4, xlwt.Formula("(E6+E7+E8+E9+E10+E11+E12+E13+E14+E15+E16)"), style1)
            xlsheet.write(16, 5, xlwt.Formula("1-((D17+E17)/(B17))"), style4)
            xlsheet.write(16, 6, xlwt.Formula("(G6+G7+G8+G9+G10+G11+G12+G13+G14+G15+G16)/11"), style1)
            xlsheet.write(16, 7, 1, style1)
            xlsheet.write(16, 8, xlwt.Formula("(H17/B17)"), style4)
            xlsheet.write(16, 9, xlwt.Formula("(B17*10000)/219855"), style1)

            xlsname=choose_type + str(int(time.time()))
            workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
            return ('mail.itlaolang.com/downfile/{}.xls'.format(xlsname))

        if choose_type=='一键报障':
            sheet = workbook_r.sheet_by_name('一键报障')
            for x in range(1, sheet.nrows):

                msg = sheet.row_values(x)
                # 这是完成的工单量
                if msg[11] == '归档' and msg[25] != '' and utc_str_to_timestamp(
                        str(msg[25])) >= utc_str_to_timestamp(
                    starttime) and utc_str_to_timestamp(
                    str(msg[25])) <= utc_str_to_timestamp(endtime):
                    msg_list1.append([find_area2(msg[8])])
                # 这是接受的工单量
                if  msg[25] != '' and utc_str_to_timestamp(
                        str(msg[22])) >= utc_str_to_timestamp(
                        starttime) and utc_str_to_timestamp(
                        str(msg[22])) <= utc_str_to_timestamp(endtime):
                    result = [find_area2(msg[8]), msg[11], get_timeout2(msg[11], msg[22], msg[25]),
                              time_for_end2(msg[22], msg[25]), msg[10]]  # 地区，状态，超时（包括运行中，归档），投诉时长,投诉地址
                    msg_list.append(result)

            workbook_m = xlwt.Workbook(encoding='utf-8')
            xlsheet = workbook_m.add_sheet('24小时投诉日报', cell_overwrite_ok=True)
            # 格式1 （有自动换行）
            style1 = xlwt.easyxf('pattern: pattern solid, fore_colour white')
            style1.font.height = 200
            style1.font.name = u'文泉驿点阵正黑'
            style1.font.colour_index = 0
            style1.borders.left = xlwt.Borders.THIN
            style1.borders.right = xlwt.Borders.THIN
            style1.borders.top = xlwt.Borders.THIN
            style1.borders.bottom = xlwt.Borders.THIN
            # style1.font.bold = True
            style1.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
            style1.alignment.horz = xlwt.Alignment.HORZ_CENTER
            style1.num_format_str = '0.00'

            # 格式2  （没有自动换行）
            style2 = xlwt.easyxf('pattern: pattern solid, fore_colour white')
            style2.font.height = 200
            style2.font.name = u'文泉驿点阵正黑'
            style2.font.colour_index = 0
            style2.borders.left = xlwt.Borders.THIN
            style2.borders.right = xlwt.Borders.THIN
            style2.borders.top = xlwt.Borders.THIN
            style2.borders.bottom = xlwt.Borders.THIN

            # style2.font.bold = True
            # style2.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
            # style2.alignment.horz = xlwt.Alignment.HORZ_CENTER

            # 格式3 黄色背景色

            style3 = xlwt.easyxf('pattern: pattern solid, fore_colour yellow')
            style3.font.height = 200
            style3.font.name = u'文泉驿点阵正黑'
            style3.font.colour_index = 0
            # style3.borders.left = xlwt.Borders.THIN
            # style3.borders.right = xlwt.Borders.THIN
            # style3.borders.top = xlwt.Borders.THIN
            # style3.borders.bottom = xlwt.Borders.THIN

            # style4 格式4 0.00%

            style4 = xlwt.easyxf('pattern: pattern solid, fore_colour white')
            style4.font.height = 200
            style4.font.name = u'文泉驿点阵正黑'
            style4.font.colour_index = 0
            style4.borders.left = xlwt.Borders.THIN
            style4.borders.right = xlwt.Borders.THIN
            style4.borders.top = xlwt.Borders.THIN
            style4.borders.bottom = xlwt.Borders.THIN
            # style1.font.bold = True
            style4.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
            style4.alignment.horz = xlwt.Alignment.HORZ_CENTER
            style4.num_format_str = '0.00%'

            # style2.font.bold = True
            # style2.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
            # style2.alignment.horz = xlwt.Alignment.HORZ_CENTER
            # 写excel表头
            # 设置单元格
            xlsheet.write(0, 1, '起始时间：', style3)
            xlsheet.write(0, 2, starttime, style3)
            xlsheet.write(0, 3, '', style3)
            xlsheet.write(0, 4, '截止时间：', style3)
            xlsheet.write(0, 5, endtime, style3)
            xlsheet.write(0, 6, '', style3)
            xlsheet.write(0, 7, '工单类型：', style3)
            xlsheet.write(0, 8, choose_type, style3)

            xlsheet.write_merge(2, 2, 0, 9, '宜昌分公司家宽投诉日报（24小时）', style2)
            xlsheet.write(3, 0, '区县', style1)
            xlsheet.write(3, 1, '受理量', style1)
            xlsheet.write(3, 2, '完成量', style1)
            xlsheet.write(3, 3, '未完成超时', style1)
            xlsheet.write(3, 4, '已完成超时', style1)
            xlsheet.write(3, 5, '投诉处理及时率', style1)
            xlsheet.write(3, 6, '平均处理时长', style1)
            xlsheet.write(3, 7, '重复量', style1)
            xlsheet.write(3, 8, '重复投诉率', style1)
            xlsheet.write(3, 9, '万投比', style1)
            xlsheet.write(4, 0, '备注', style1)
            xlsheet.write(4, 1, '派发工单量', style1)
            xlsheet.write(4, 2, '归档完成工单量', style1)
            xlsheet.write(4, 3, '工单状态为“运行中”，超过派单时间24小时工单', style1)
            xlsheet.write(4, 4, '工单状态为“归档”，处理时长超24小时工单', style1)
            xlsheet.write(4, 5, '1-超时量/受理量', style1)
            xlsheet.write(4, 6, '时长=T2操作时间-T1派发时间', style1)
            xlsheet.write(4, 7, '5天内同一用户（客户电话一致）发生过2次及2次以上的投诉', style1)
            xlsheet.write(4, 8, '重复量/受理量', style1)
            xlsheet.write(4, 9, '10000*受理量/用户数', style1)

            xlsheet.write(5, 0, '城区', style1)
            xlsheet.write(5, 1, len([x for x in msg_list if x[0] == '城区']), style1)
            xlsheet.write(5, 2, len([x for x in msg_list1 if x[0] == '城区']), style1)
            xlsheet.write(5, 3, len([x for x in msg_list if x[0] == '城区' and x[1] == '运行中' and x[2] == '是']), style1)
            xlsheet.write(5, 4, len([x for x in msg_list if x[0] == '城区' and x[1] == '归档' and x[2] == '是']), style1)
            xlsheet.write(5, 5, xlwt.Formula("1-((D6+E6)/(B6))"), style4)
            all_time = 0
            for i in [x for x in msg_list if x[0] == '城区']:
                all_time = all_time + i[-2]
            xlsheet.write(5, 6, '%.2f' % (
                av_time(all_time, len([x for x in msg_list if x[0] == '城区']))), style1)
            xlsheet.write(5, 7, 1, style1)
            xlsheet.write(5, 8, xlwt.Formula("(H6/B6)"), style4)
            xlsheet.write(5, 9, xlwt.Formula("(B6*10000)/ 25171"), style1)

            xlsheet.write(6, 0, '当阳', style1)
            xlsheet.write(6, 1, len([x for x in msg_list if x[0] == '当阳']), style1)
            xlsheet.write(6, 2, len([x for x in msg_list1 if x[0] == '当阳']), style1)
            xlsheet.write(6, 3, len([x for x in msg_list if x[0] == '当阳' and x[1] == '运行中' and x[2] == '是']), style1)
            xlsheet.write(6, 4, len([x for x in msg_list if x[0] == '当阳' and x[1] == '归档' and x[2] == '是']), style1)
            xlsheet.write(6, 5, xlwt.Formula("1-((D7+E7)/(B7))"), style4)
            all_time = 0
            for i in [x for x in msg_list if x[0] == '当阳']:
                all_time = all_time + i[-2]
            xlsheet.write(6, 6, '%.2f' % (
                av_time(all_time, len([x for x in msg_list if x[0] == '当阳']))), style1)
            xlsheet.write(6, 7, 1, style1)
            xlsheet.write(6, 8, xlwt.Formula("(H7/B7)"), style4)
            xlsheet.write(6, 9, xlwt.Formula("(B7*10000)/ 25349"), style1)

            xlsheet.write(7, 0, '开发区', style1)
            xlsheet.write(7, 1, len([x for x in msg_list if x[0] == '开发区']), style1)
            xlsheet.write(7, 2, len([x for x in msg_list1 if x[0] == '开发区']), style1)
            xlsheet.write(7, 3, len([x for x in msg_list if x[0] == '开发区' and x[1] == '运行中' and x[2] == '是']), style1)
            xlsheet.write(7, 4, len([x for x in msg_list if x[0] == '开发区' and x[1] == '归档' and x[2] == '是']), style1)
            xlsheet.write(7, 5, xlwt.Formula("1-((D8+E8)/(B8))"), style4)
            all_time = 0
            for i in [x for x in msg_list if x[0] == '开发区']:
                all_time = all_time + i[-2]
            xlsheet.write(7, 6, '%.2f' % (
                av_time(all_time, len([x for x in msg_list if x[0] == '开发区']))), style1)
            xlsheet.write(7, 7, 1, style1)
            xlsheet.write(7, 8, xlwt.Formula("(H8/B8)"), style4)
            xlsheet.write(7, 9, xlwt.Formula("(B8*10000)/ 34313"), style1)

            xlsheet.write(8, 0, '五峰', style1)
            xlsheet.write(8, 1, len([x for x in msg_list if x[0] == '五峰']), style1)
            xlsheet.write(8, 2, len([x for x in msg_list1 if x[0] == '五峰']), style1)
            xlsheet.write(8, 3, len([x for x in msg_list if x[0] == '五峰' and x[1] == '运行中' and x[2] == '是']), style1)
            xlsheet.write(8, 4, len([x for x in msg_list if x[0] == '五峰' and x[1] == '归档' and x[2] == '是']), style1)
            xlsheet.write(8, 5, xlwt.Formula("1-((D9+E9)/(B9))"), style4)
            all_time = 0
            for i in [x for x in msg_list if x[0] == '五峰']:
                all_time = all_time + i[-2]
            xlsheet.write(8, 6, '%.2f' % (
                av_time(all_time, len([x for x in msg_list if x[0] == '五峰']))), style1)
            xlsheet.write(8, 7, 1, style1)
            xlsheet.write(8, 8, xlwt.Formula("(H9/B9)"), style4)
            xlsheet.write(8, 9, xlwt.Formula("(B9*10000)/ 7985"), style1)

            xlsheet.write(9, 0, '兴山', style1)
            xlsheet.write(9, 1, len([x for x in msg_list if x[0] == '兴山']), style1)
            xlsheet.write(9, 2, len([x for x in msg_list1 if x[0] == '兴山']), style1)
            xlsheet.write(9, 3, len([x for x in msg_list if x[0] == '兴山' and x[1] == '运行中' and x[2] == '是']), style1)
            xlsheet.write(9, 4, len([x for x in msg_list if x[0] == '兴山' and x[1] == '归档' and x[2] == '是']), style1)
            xlsheet.write(9, 5, xlwt.Formula("1-((D10+E10)/(B10))"), style4)
            all_time = 0
            for i in [x for x in msg_list if x[0] == '兴山']:
                all_time = all_time + i[-2]
            xlsheet.write(9, 6, '%.2f' % (
                av_time(all_time, len([x for x in msg_list if x[0] == '兴山']))), style1)
            xlsheet.write(9, 7, 1, style1)
            xlsheet.write(9, 8, xlwt.Formula("(H10/B10)"), style4)
            xlsheet.write(9, 9, xlwt.Formula(("(B10*10000)/ 7453")), style1)

            xlsheet.write(10, 0, '夷陵', style1)
            xlsheet.write(10, 1, len([x for x in msg_list if x[0] == '夷陵']), style1)
            xlsheet.write(10, 2, len([x for x in msg_list1 if x[0] == '夷陵']), style1)
            xlsheet.write(10, 3, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '运行中' and x[2] == '是']), style1)
            xlsheet.write(10, 4, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '归档' and x[2] == '是']), style1)
            xlsheet.write(10, 5, xlwt.Formula("1-((D11+E11)/(B11))"), style4)
            all_time = 0
            for i in [x for x in msg_list if x[0] == '夷陵']:
                all_time = all_time + i[-2]
            xlsheet.write(10, 6, '%.2f' % (
                av_time(all_time, len([x for x in msg_list if x[0] == '夷陵']))), style1)
            xlsheet.write(10, 7, 1, style1)
            xlsheet.write(10, 8, xlwt.Formula("(H11/B11)"), style4)
            xlsheet.write(10, 9, xlwt.Formula("(B11*10000)/ 27196"), style1)

            xlsheet.write(11, 0, '宜都', style1)
            xlsheet.write(11, 1, len([x for x in msg_list if x[0] == '宜都']), style1)
            xlsheet.write(11, 2, len([x for x in msg_list1 if x[0] == '宜都']), style1)
            xlsheet.write(11, 3, len([x for x in msg_list if x[0] == '宜都' and x[1] == '运行中' and x[2] == '是']), style1)
            xlsheet.write(11, 4, len([x for x in msg_list if x[0] == '宜都' and x[1] == '归档' and x[2] == '是']), style1)
            xlsheet.write(11, 5, xlwt.Formula("1-((D12+E12)/(B12))"), style4)
            all_time = 0
            for i in [x for x in msg_list if x[0] == '宜都']:
                all_time = all_time + i[-2]
            xlsheet.write(11, 6, '%.2f' % (
                av_time(all_time, len([x for x in msg_list if x[0] == '宜都']))), style1)
            xlsheet.write(11, 7, 1, style1)
            xlsheet.write(11, 8, xlwt.Formula("(H12/B12)"), style4)
            xlsheet.write(11, 9, xlwt.Formula("(B12*10000)/ 17538"), style1)

            xlsheet.write(12, 0, '远安', style1)
            xlsheet.write(12, 1, len([x for x in msg_list if x[0] == '远安']), style1)
            xlsheet.write(12, 2, len([x for x in msg_list1 if x[0] == '远安']), style1)
            xlsheet.write(12, 3, len([x for x in msg_list if x[0] == '远安' and x[1] == '运行中' and x[2] == '是']), style1)
            xlsheet.write(12, 4, len([x for x in msg_list if x[0] == '远安' and x[1] == '归档' and x[2] == '是']), style1)
            xlsheet.write(12, 5, xlwt.Formula("1-((D13+E13)/(B13))"), style4)
            all_time = 0
            for i in [x for x in msg_list if x[0] == '远安']:
                all_time = all_time + i[-2]

            xlsheet.write(12, 6, '%.2f' % (
                av_time(all_time, len([x for x in msg_list if x[0] == '远安']))), style1)
            xlsheet.write(12, 7, 1, style1)
            xlsheet.write(12, 8, xlwt.Formula("(H13/B13)"), style4)
            xlsheet.write(12, 9, xlwt.Formula("(B13*10000)/ 12884"), style1)

            xlsheet.write(13, 0, '长阳', style1)
            xlsheet.write(13, 1, len([x for x in msg_list if x[0] == '长阳']), style1)
            xlsheet.write(13, 2, len([x for x in msg_list1 if x[0] == '长阳']), style1)
            xlsheet.write(13, 3, len([x for x in msg_list if x[0] == '长阳' and x[1] == '运行中' and x[2] == '是']), style1)
            xlsheet.write(13, 4, len([x for x in msg_list if x[0] == '长阳' and x[1] == '归档' and x[2] == '是']), style1)
            xlsheet.write(13, 5, xlwt.Formula("1-((D14+E14)/(B14))"), style4)
            all_time = 0
            for i in [x for x in msg_list if x[0] == '城区']:
                all_time = all_time + i[-2]
            xlsheet.write(13, 6, '%.2f' % (
                av_time(all_time, len([x for x in msg_list if x[0] == '长阳']))), style1)
            xlsheet.write(13, 7, 1, style1)
            xlsheet.write(13, 8, xlwt.Formula("(H14/B14)"), style4)
            xlsheet.write(13, 9, xlwt.Formula("(B14*10000)/ 18385"), style1)

            xlsheet.write(14, 0, '枝江', style1)
            xlsheet.write(14, 1, len([x for x in msg_list if x[0] == '枝江']), style1)
            xlsheet.write(14, 2, len([x for x in msg_list1 if x[0] == '枝江']), style1)
            xlsheet.write(14, 3, len([x for x in msg_list if x[0] == '枝江' and x[1] == '运行中' and x[2] == '是']), style1)
            xlsheet.write(14, 4, len([x for x in msg_list if x[0] == '枝江' and x[1] == '归档' and x[2] == '是']), style1)
            xlsheet.write(14, 5, xlwt.Formula("1-((D15+E15)/(B15))"), style4)
            all_time = 0
            for i in [x for x in msg_list if x[0] == '枝江']:
                all_time = all_time + i[-2]
            xlsheet.write(14, 6, '%.2f' % (
                av_time(all_time, len([x for x in msg_list if x[0] == '枝江']))), style1)
            xlsheet.write(14, 7, 1, style1)
            xlsheet.write(14, 8, xlwt.Formula("(H15/B15)"), style4)
            xlsheet.write(14, 9, xlwt.Formula("(B15*10000)/25378"), style1)

            xlsheet.write(15, 0, '秭归', style1)
            xlsheet.write(15, 1, len([x for x in msg_list if x[0] == '秭归']), style1)
            xlsheet.write(15, 2, len([x for x in msg_list1 if x[0] == '秭归']), style1)
            xlsheet.write(15, 3, len([x for x in msg_list if x[0] == '秭归' and x[1] == '运行中' and x[2] == '是']), style1)
            xlsheet.write(15, 4, len([x for x in msg_list if x[0] == '秭归' and x[1] == '归档' and x[2] == '是']), style1)
            xlsheet.write(15, 5, xlwt.Formula("1-((D15+E15)/(B15))"), style4)
            all_time = 0
            for i in [x for x in msg_list if x[0] == '秭归']:
                all_time = all_time + i[-2]

            xlsheet.write(15, 6, '%.2f' % (
                av_time(all_time, len([x for x in msg_list if x[0] == '秭归']))), style1)
            xlsheet.write(15, 7, 1, style1)
            xlsheet.write(15, 8, xlwt.Formula("(H16/B16)"), style4)
            xlsheet.write(15, 9, xlwt.Formula("(B16*10000)/18203"), style1)

            xlsheet.write(16, 0, '全市', style1)
            xlsheet.write(16, 1, xlwt.Formula("(B6+B7+B8+B9+B10+B11+B12+B13+B14+B15+B16)"), style1)
            xlsheet.write(16, 2, xlwt.Formula("(C6+C7+C8+C9+C10+C11+C12+C13+C14+C15+C16)"), style1)
            xlsheet.write(16, 3, xlwt.Formula("(D6+D7+D8+D9+D10+D11+D12+D13+D14+D15+D16)"), style1)
            xlsheet.write(16, 4, xlwt.Formula("(E6+E7+E8+E9+E10+E11+E12+E13+E14+E15+E16)"), style1)
            xlsheet.write(16, 5, xlwt.Formula("1-((D17+E17)/(B17))"), style4)
            xlsheet.write(16, 6, xlwt.Formula("(G6+G7+G8+G9+G10+G11+G12+G13+G14+G15+G16)/11"), style1)
            xlsheet.write(16, 7, 1, style1)
            xlsheet.write(16, 8, xlwt.Formula("(H17/B17)"), style4)
            xlsheet.write(16, 9, xlwt.Formula("(B17*10000)/219855"), style1)
            xlsname=choose_type + str(int(time.time()))
            workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
            return ('mail.itlaolang.com/downfile/{}.xls'.format(xlsname))

        if choose_type=='CRM':
            sheet = workbook_r.sheet_by_name('CRM')
            for x in range(1, sheet.nrows):

                msg = sheet.row_values(x)
                # 这是完成的工单量
                if msg[7] == '是'  and msg[6]!='' and utc_str_to_timestamp(str(xlrd.xldate_as_datetime(msg[6],0))) >= utc_str_to_timestamp(
                    starttime) and utc_str_to_timestamp(str(xlrd.xldate_as_datetime(msg[6], 0))) <= utc_str_to_timestamp(endtime):
                    msg_list1.append([msg[0]])
                # 这是接受的工单量
                if utc_str_to_timestamp(str(xlrd.xldate_as_datetime(msg[1],0))) >= utc_str_to_timestamp(
                    starttime) and utc_str_to_timestamp(
                    str(xlrd.xldate_as_datetime(msg[1], 0))) <= utc_str_to_timestamp(endtime):
                    result = [msg[0], msg[7],msg[8],0,msg[3]]  # 地区，状态，超时（包括运行中，归档），投诉时长,投诉地址
                    msg_list.append(result)
            workbook_m = xlwt.Workbook(encoding='utf-8')
            xlsheet = workbook_m.add_sheet('24小时投诉日报', cell_overwrite_ok=True)
            # 格式1 （有自动换行）
            style1 = xlwt.easyxf('pattern: pattern solid, fore_colour white')
            style1.font.height = 200
            style1.font.name = u'文泉驿点阵正黑'
            style1.font.colour_index = 0
            style1.borders.left = xlwt.Borders.THIN
            style1.borders.right = xlwt.Borders.THIN
            style1.borders.top = xlwt.Borders.THIN
            style1.borders.bottom = xlwt.Borders.THIN
            # style1.font.bold = True
            style1.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
            style1.alignment.horz = xlwt.Alignment.HORZ_CENTER
            style1.num_format_str = '0.00'

            # 格式2  （没有自动换行）
            style2 = xlwt.easyxf('pattern: pattern solid, fore_colour white')
            style2.font.height = 200
            style2.font.name = u'文泉驿点阵正黑'
            style2.font.colour_index = 0
            style2.borders.left = xlwt.Borders.THIN
            style2.borders.right = xlwt.Borders.THIN
            style2.borders.top = xlwt.Borders.THIN
            style2.borders.bottom = xlwt.Borders.THIN

            # style2.font.bold = True
            # style2.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
            # style2.alignment.horz = xlwt.Alignment.HORZ_CENTER

            # 格式3 黄色背景色

            style3 = xlwt.easyxf('pattern: pattern solid, fore_colour yellow')
            style3.font.height = 200
            style3.font.name = u'文泉驿点阵正黑'
            style3.font.colour_index = 0
            # style3.borders.left = xlwt.Borders.THIN
            # style3.borders.right = xlwt.Borders.THIN
            # style3.borders.top = xlwt.Borders.THIN
            # style3.borders.bottom = xlwt.Borders.THIN

            # style4 格式4 0.00%

            style4 = xlwt.easyxf('pattern: pattern solid, fore_colour white')
            style4.font.height = 200
            style4.font.name = u'文泉驿点阵正黑'
            style4.font.colour_index = 0
            style4.borders.left = xlwt.Borders.THIN
            style4.borders.right = xlwt.Borders.THIN
            style4.borders.top = xlwt.Borders.THIN
            style4.borders.bottom = xlwt.Borders.THIN
            # style1.font.bold = True
            style4.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
            style4.alignment.horz = xlwt.Alignment.HORZ_CENTER
            style4.num_format_str = '0.00%'

            # style2.font.bold = True
            # style2.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
            # style2.alignment.horz = xlwt.Alignment.HORZ_CENTER
            # 写excel表头
            # 设置单元格
            xlsheet.write(0, 1, '起始时间：', style3)
            xlsheet.write(0, 2, starttime, style3)
            xlsheet.write(0, 3, '', style3)
            xlsheet.write(0, 4, '截止时间：', style3)
            xlsheet.write(0, 5, endtime, style3)
            xlsheet.write(0, 6, '', style3)
            xlsheet.write(0, 7, '工单类型：', style3)
            xlsheet.write(0, 8, choose_type, style3)

            xlsheet.write_merge(2, 2, 0, 9, '宜昌分公司家宽投诉日报（24小时）', style2)
            xlsheet.write(3, 0, '区县', style1)
            xlsheet.write(3, 1, '受理量', style1)
            xlsheet.write(3, 2, '完成量', style1)
            xlsheet.write(3, 3, '未完成超时', style1)
            xlsheet.write(3, 4, '已完成超时', style1)
            xlsheet.write(3, 5, '投诉处理及时率', style1)
            xlsheet.write(3, 6, '平均处理时长', style1)
            xlsheet.write(3, 7, '重复量', style1)
            xlsheet.write(3, 8, '重复投诉率', style1)
            xlsheet.write(3, 9, '万投比', style1)
            xlsheet.write(4, 0, '备注', style1)
            xlsheet.write(4, 1, '派发工单量', style1)
            xlsheet.write(4, 2, '归档完成工单量', style1)
            xlsheet.write(4, 3, '工单状态为“运行中”，超过派单时间24小时工单', style1)
            xlsheet.write(4, 4, '工单状态为“归档”，处理时长超24小时工单', style1)
            xlsheet.write(4, 5, '1-超时量/受理量', style1)
            xlsheet.write(4, 6, '时长=T2操作时间-T1派发时间', style1)
            xlsheet.write(4, 7, '5天内同一用户（客户电话一致）发生过2次及2次以上的投诉', style1)
            xlsheet.write(4, 8, '重复量/受理量', style1)
            xlsheet.write(4, 9, '10000*受理量/用户数', style1)

            xlsheet.write(5, 0, '城区', style1)
            xlsheet.write(5, 1, len([x for x in msg_list if x[0] == '城区']), style1)
            xlsheet.write(5, 2, len([x for x in msg_list1 if x[0] == '城区']), style1)
            xlsheet.write(5, 3, len([x for x in msg_list if x[0] == '城区' and x[1] == '运行中' and x[2] == '是']), style1)
            xlsheet.write(5, 4, len([x for x in msg_list if x[0] == '城区' and x[1] == '归档' and x[2] == '是']), style1)
            xlsheet.write(5, 5, xlwt.Formula("1-((D6+E6)/(B6))"), style4)
            all_time = 0
            for i in [x for x in msg_list if x[0] == '城区']:
                all_time = all_time + i[-2]
            xlsheet.write(5, 6, '%.2f' % (
                av_time(all_time, len([x for x in msg_list if x[0] == '城区']))), style1)
            xlsheet.write(5, 7, 1, style1)
            xlsheet.write(5, 8, xlwt.Formula("(H6/B6)"), style4)
            xlsheet.write(5, 9, xlwt.Formula("(B6*10000)/ 25171"), style1)

            xlsheet.write(6, 0, '当阳', style1)
            xlsheet.write(6, 1, len([x for x in msg_list if x[0] == '当阳']), style1)
            xlsheet.write(6, 2, len([x for x in msg_list1 if x[0] == '当阳']), style1)
            xlsheet.write(6, 3, len([x for x in msg_list if x[0] == '当阳' and x[1] == '运行中' and x[2] == '是']), style1)
            xlsheet.write(6, 4, len([x for x in msg_list if x[0] == '当阳' and x[1] == '归档' and x[2] == '是']), style1)
            xlsheet.write(6, 5, xlwt.Formula("1-((D7+E7)/(B7))"), style4)
            all_time = 0
            for i in [x for x in msg_list if x[0] == '当阳']:
                all_time = all_time + i[-2]
            xlsheet.write(6, 6, '%.2f' % (
                av_time(all_time, len([x for x in msg_list if x[0] == '当阳']))), style1)
            xlsheet.write(6, 7, 1, style1)
            xlsheet.write(6, 8, xlwt.Formula("(H7/B7)"), style4)
            xlsheet.write(6, 9, xlwt.Formula("(B7*10000)/ 25349"), style1)

            xlsheet.write(7, 0, '开发区', style1)
            xlsheet.write(7, 1, len([x for x in msg_list if x[0] == '开发区']), style1)
            xlsheet.write(7, 2, len([x for x in msg_list1 if x[0] == '开发区']), style1)
            xlsheet.write(7, 3, len([x for x in msg_list if x[0] == '开发区' and x[1] == '运行中' and x[2] == '是']), style1)
            xlsheet.write(7, 4, len([x for x in msg_list if x[0] == '开发区' and x[1] == '归档' and x[2] == '是']), style1)
            xlsheet.write(7, 5, xlwt.Formula("1-((D8+E8)/(B8))"), style4)
            all_time = 0
            for i in [x for x in msg_list if x[0] == '开发区']:
                all_time = all_time + i[-2]
            xlsheet.write(7, 6, '%.2f' % (
                av_time(all_time, len([x for x in msg_list if x[0] == '开发区']))), style1)
            xlsheet.write(7, 7, 1, style1)
            xlsheet.write(7, 8, xlwt.Formula("(H8/B8)"), style4)
            xlsheet.write(7, 9, xlwt.Formula("(B8*10000)/ 34313"), style1)

            xlsheet.write(8, 0, '五峰', style1)
            xlsheet.write(8, 1, len([x for x in msg_list if x[0] == '五峰']), style1)
            xlsheet.write(8, 2, len([x for x in msg_list1 if x[0] == '五峰']), style1)
            xlsheet.write(8, 3, len([x for x in msg_list if x[0] == '五峰' and x[1] == '运行中' and x[2] == '是']), style1)
            xlsheet.write(8, 4, len([x for x in msg_list if x[0] == '五峰' and x[1] == '归档' and x[2] == '是']), style1)
            xlsheet.write(8, 5, xlwt.Formula("1-((D9+E9)/(B9))"), style4)
            all_time = 0
            for i in [x for x in msg_list if x[0] == '五峰']:
                all_time = all_time + i[-2]
            xlsheet.write(8, 6, '%.2f' % (
                av_time(all_time, len([x for x in msg_list if x[0] == '五峰']))), style1)
            xlsheet.write(8, 7, 1, style1)
            xlsheet.write(8, 8, xlwt.Formula("(H9/B9)"), style4)
            xlsheet.write(8, 9, xlwt.Formula("(B9*10000)/ 7985"), style1)

            xlsheet.write(9, 0, '兴山', style1)
            xlsheet.write(9, 1, len([x for x in msg_list if x[0] == '兴山']), style1)
            xlsheet.write(9, 2, len([x for x in msg_list1 if x[0] == '兴山']), style1)
            xlsheet.write(9, 3, len([x for x in msg_list if x[0] == '兴山' and x[1] == '运行中' and x[2] == '是']), style1)
            xlsheet.write(9, 4, len([x for x in msg_list if x[0] == '兴山' and x[1] == '归档' and x[2] == '是']), style1)
            xlsheet.write(9, 5, xlwt.Formula("1-((D10+E10)/(B10))"), style4)
            all_time = 0
            for i in [x for x in msg_list if x[0] == '兴山']:
                all_time = all_time + i[-2]
            xlsheet.write(9, 6, '%.2f' % (
                av_time(all_time, len([x for x in msg_list if x[0] == '兴山']))), style1)
            xlsheet.write(9, 7, 1, style1)
            xlsheet.write(9, 8, xlwt.Formula("(H10/B10)"), style4)
            xlsheet.write(9, 9, xlwt.Formula(("(B10*10000)/ 7453")), style1)

            xlsheet.write(10, 0, '夷陵', style1)
            xlsheet.write(10, 1, len([x for x in msg_list if x[0] == '夷陵']), style1)
            xlsheet.write(10, 2, len([x for x in msg_list1 if x[0] == '夷陵']), style1)
            xlsheet.write(10, 3, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '运行中' and x[2] == '是']), style1)
            xlsheet.write(10, 4, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '归档' and x[2] == '是']), style1)
            xlsheet.write(10, 5, xlwt.Formula("1-((D11+E11)/(B11))"), style4)
            all_time = 0
            for i in [x for x in msg_list if x[0] == '夷陵']:
                all_time = all_time + i[-2]
            xlsheet.write(10, 6, '%.2f' % (
                av_time(all_time, len([x for x in msg_list if x[0] == '夷陵']))), style1)
            xlsheet.write(10, 7, 1, style1)
            xlsheet.write(10, 8, xlwt.Formula("(H11/B11)"), style4)
            xlsheet.write(10, 9, xlwt.Formula("(B11*10000)/ 27196"), style1)

            xlsheet.write(11, 0, '宜都', style1)
            xlsheet.write(11, 1, len([x for x in msg_list if x[0] == '宜都']), style1)
            xlsheet.write(11, 2, len([x for x in msg_list1 if x[0] == '宜都']), style1)
            xlsheet.write(11, 3, len([x for x in msg_list if x[0] == '宜都' and x[1] == '运行中' and x[2] == '是']), style1)
            xlsheet.write(11, 4, len([x for x in msg_list if x[0] == '宜都' and x[1] == '归档' and x[2] == '是']), style1)
            xlsheet.write(11, 5, xlwt.Formula("1-((D12+E12)/(B12))"), style4)
            all_time = 0
            for i in [x for x in msg_list if x[0] == '宜都']:
                all_time = all_time + i[-2]
            xlsheet.write(11, 6, '%.2f' % (
                av_time(all_time, len([x for x in msg_list if x[0] == '宜都']))), style1)
            xlsheet.write(11, 7, 1, style1)
            xlsheet.write(11, 8, xlwt.Formula("(H12/B12)"), style4)
            xlsheet.write(11, 9, xlwt.Formula("(B12*10000)/ 17538"), style1)

            xlsheet.write(12, 0, '远安', style1)
            xlsheet.write(12, 1, len([x for x in msg_list if x[0] == '远安']), style1)
            xlsheet.write(12, 2, len([x for x in msg_list1 if x[0] == '远安']), style1)
            xlsheet.write(12, 3, len([x for x in msg_list if x[0] == '远安' and x[1] == '运行中' and x[2] == '是']), style1)
            xlsheet.write(12, 4, len([x for x in msg_list if x[0] == '远安' and x[1] == '归档' and x[2] == '是']), style1)
            xlsheet.write(12, 5, xlwt.Formula("1-((D13+E13)/(B13))"), style4)
            all_time = 0
            for i in [x for x in msg_list if x[0] == '远安']:
                all_time = all_time + i[-2]

            xlsheet.write(12, 6, '%.2f' % (
                av_time(all_time, len([x for x in msg_list if x[0] == '远安']))), style1)
            xlsheet.write(12, 7, 1, style1)
            xlsheet.write(12, 8, xlwt.Formula("(H13/B13)"), style4)
            xlsheet.write(12, 9, xlwt.Formula("(B13*10000)/ 12884"), style1)

            xlsheet.write(13, 0, '长阳', style1)
            xlsheet.write(13, 1, len([x for x in msg_list if x[0] == '长阳']), style1)
            xlsheet.write(13, 2, len([x for x in msg_list1 if x[0] == '长阳']), style1)
            xlsheet.write(13, 3, len([x for x in msg_list if x[0] == '长阳' and x[1] == '运行中' and x[2] == '是']), style1)
            xlsheet.write(13, 4, len([x for x in msg_list if x[0] == '长阳' and x[1] == '归档' and x[2] == '是']), style1)
            xlsheet.write(13, 5, xlwt.Formula("1-((D14+E14)/(B14))"), style4)
            all_time = 0
            for i in [x for x in msg_list if x[0] == '城区']:
                all_time = all_time + i[-2]
            xlsheet.write(13, 6, '%.2f' % (
                av_time(all_time, len([x for x in msg_list if x[0] == '长阳']))), style1)
            xlsheet.write(13, 7, 1, style1)
            xlsheet.write(13, 8, xlwt.Formula("(H14/B14)"), style4)
            xlsheet.write(13, 9, xlwt.Formula("(B14*10000)/ 18385"), style1)

            xlsheet.write(14, 0, '枝江', style1)
            xlsheet.write(14, 1, len([x for x in msg_list if x[0] == '枝江']), style1)
            xlsheet.write(14, 2, len([x for x in msg_list1 if x[0] == '枝江']), style1)
            xlsheet.write(14, 3, len([x for x in msg_list if x[0] == '枝江' and x[1] == '运行中' and x[2] == '是']), style1)
            xlsheet.write(14, 4, len([x for x in msg_list if x[0] == '枝江' and x[1] == '归档' and x[2] == '是']), style1)
            xlsheet.write(14, 5, xlwt.Formula("1-((D15+E15)/(B15))"), style4)
            all_time = 0
            for i in [x for x in msg_list if x[0] == '枝江']:
                all_time = all_time + i[-2]
            xlsheet.write(14, 6, '%.2f' % (
                av_time(all_time, len([x for x in msg_list if x[0] == '枝江']))), style1)
            xlsheet.write(14, 7, 1, style1)
            xlsheet.write(14, 8, xlwt.Formula("(H15/B15)"), style4)
            xlsheet.write(14, 9, xlwt.Formula("(B15*10000)/25378"), style1)

            xlsheet.write(15, 0, '秭归', style1)
            xlsheet.write(15, 1, len([x for x in msg_list if x[0] == '秭归']), style1)
            xlsheet.write(15, 2, len([x for x in msg_list1 if x[0] == '秭归']), style1)
            xlsheet.write(15, 3, len([x for x in msg_list if x[0] == '秭归' and x[1] == '运行中' and x[2] == '是']), style1)
            xlsheet.write(15, 4, len([x for x in msg_list if x[0] == '秭归' and x[1] == '归档' and x[2] == '是']), style1)
            xlsheet.write(15, 5, xlwt.Formula("1-((D15+E15)/(B15))"), style4)
            all_time = 0
            for i in [x for x in msg_list if x[0] == '秭归']:
                all_time = all_time + i[-2]

            xlsheet.write(15, 6, '%.2f' % (
                av_time(all_time, len([x for x in msg_list if x[0] == '秭归']))), style1)
            xlsheet.write(15, 7, 1, style1)
            xlsheet.write(15, 8, xlwt.Formula("(H16/B16)"), style4)
            xlsheet.write(15, 9, xlwt.Formula("(B16*10000)/18203"), style1)

            xlsheet.write(16, 0, '全市', style1)
            xlsheet.write(16, 1, xlwt.Formula("(B6+B7+B8+B9+B10+B11+B12+B13+B14+B15+B16)"), style1)
            xlsheet.write(16, 2, xlwt.Formula("(C6+C7+C8+C9+C10+C11+C12+C13+C14+C15+C16)"), style1)
            xlsheet.write(16, 3, xlwt.Formula("(D6+D7+D8+D9+D10+D11+D12+D13+D14+D15+D16)"), style1)
            xlsheet.write(16, 4, xlwt.Formula("(E6+E7+E8+E9+E10+E11+E12+E13+E14+E15+E16)"), style1)
            xlsheet.write(16, 5, xlwt.Formula("1-((D17+E17)/(B17))"), style4)
            xlsheet.write(16, 6, xlwt.Formula("(G6+G7+G8+G9+G10+G11+G12+G13+G14+G15+G16)/11"), style1)
            xlsheet.write(16, 7, 1, style1)
            xlsheet.write(16, 8, xlwt.Formula("(H17/B17)"), style4)
            xlsheet.write(16, 9, xlwt.Formula("(B17*10000)/219855"), style1)
            xlsname=choose_type + str(int(time.time()))
            workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
            return ('mail.itlaolang.com/downfile/{}.xls'.format(xlsname))

        if choose_type=='EMOS+CRM':
            sheet = workbook_r.sheet_by_name('CRM')
            for x in range(1, sheet.nrows):

                msg = sheet.row_values(x)
                # 这是完成的工单量
                if msg[7] == '是' and msg[6] != '' and utc_str_to_timestamp(
                        str(xlrd.xldate_as_datetime(msg[6], 0))) >= utc_str_to_timestamp(
                        starttime) and utc_str_to_timestamp(
                    str(xlrd.xldate_as_datetime(msg[6], 0))) <= utc_str_to_timestamp(endtime):
                    msg_list1.append([msg[0]])
                # 这是接受的工单量
                if utc_str_to_timestamp(str(xlrd.xldate_as_datetime(msg[1], 0))) >= utc_str_to_timestamp(
                        starttime) and utc_str_to_timestamp(
                    str(xlrd.xldate_as_datetime(msg[1], 0))) <= utc_str_to_timestamp(endtime):
                    result = [msg[0], msg[7], msg[8], 0, msg[3]]  # 地区，状态，超时（包括运行中，归档），投诉时长,投诉地址
                    msg_list.append(result)

            sheet = workbook_r.sheet_by_name('EMOS')
            for x in range(1, sheet.nrows):

                msg = sheet.row_values(x)
                # 这是完成的工单量
                if msg[8] == '归档' and msg[18] != '' and utc_str_to_timestamp(
                        str(xlrd.xldate_as_datetime(msg[18], 0))) >= utc_str_to_timestamp(
                    starttime) and utc_str_to_timestamp(
                    str(xlrd.xldate_as_datetime(msg[18], 0))) <= utc_str_to_timestamp(endtime):
                    msg_list1.append([find_area1(msg[-1], msg[2])])
                # 这是接受的工单量
                if msg[8] != '待回访' and msg[18] != '' and utc_str_to_timestamp(
                        str(xlrd.xldate_as_datetime(msg[16], 0))) >= utc_str_to_timestamp(
                        starttime) and utc_str_to_timestamp(
                        str(xlrd.xldate_as_datetime(msg[16], 0))) <= utc_str_to_timestamp(endtime):
                    # print(x)
                    # print(msg[8],msg[16],msg[18])
                    result = [find_area1(msg[-1], msg[2]), msg[8], get_timeout1(msg[8], msg[16], msg[18]),
                              time_for_end1(msg[16], msg[18]), msg[2]]  # 地区，状态，超时（包括运行中，归档），投诉时长,投诉地址
                    msg_list.append(result)
            workbook_m = xlwt.Workbook(encoding='utf-8')
            xlsheet = workbook_m.add_sheet('24小时投诉日报', cell_overwrite_ok=True)
            # 格式1 （有自动换行）
            style1 = xlwt.easyxf('pattern: pattern solid, fore_colour white')
            style1.font.height = 200
            style1.font.name = u'文泉驿点阵正黑'
            style1.font.colour_index = 0
            style1.borders.left = xlwt.Borders.THIN
            style1.borders.right = xlwt.Borders.THIN
            style1.borders.top = xlwt.Borders.THIN
            style1.borders.bottom = xlwt.Borders.THIN
            # style1.font.bold = True
            style1.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
            style1.alignment.horz = xlwt.Alignment.HORZ_CENTER
            style1.num_format_str = '0.00'

            # 格式2  （没有自动换行）
            style2 = xlwt.easyxf('pattern: pattern solid, fore_colour white')
            style2.font.height = 200
            style2.font.name = u'文泉驿点阵正黑'
            style2.font.colour_index = 0
            style2.borders.left = xlwt.Borders.THIN
            style2.borders.right = xlwt.Borders.THIN
            style2.borders.top = xlwt.Borders.THIN
            style2.borders.bottom = xlwt.Borders.THIN

            # style2.font.bold = True
            # style2.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
            # style2.alignment.horz = xlwt.Alignment.HORZ_CENTER

            # 格式3 黄色背景色

            style3 = xlwt.easyxf('pattern: pattern solid, fore_colour yellow')
            style3.font.height = 200
            style3.font.name = u'文泉驿点阵正黑'
            style3.font.colour_index = 0
            # style3.borders.left = xlwt.Borders.THIN
            # style3.borders.right = xlwt.Borders.THIN
            # style3.borders.top = xlwt.Borders.THIN
            # style3.borders.bottom = xlwt.Borders.THIN

            # style4 格式4 0.00%

            style4 = xlwt.easyxf('pattern: pattern solid, fore_colour white')
            style4.font.height = 200
            style4.font.name = u'文泉驿点阵正黑'
            style4.font.colour_index = 0
            style4.borders.left = xlwt.Borders.THIN
            style4.borders.right = xlwt.Borders.THIN
            style4.borders.top = xlwt.Borders.THIN
            style4.borders.bottom = xlwt.Borders.THIN
            # style1.font.bold = True
            style4.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
            style4.alignment.horz = xlwt.Alignment.HORZ_CENTER
            style4.num_format_str = '0.00%'

            # style2.font.bold = True
            # style2.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
            # style2.alignment.horz = xlwt.Alignment.HORZ_CENTER
            # 写excel表头
            # 设置单元格
            xlsheet.write(0, 1, '起始时间：', style3)
            xlsheet.write(0, 2, starttime, style3)
            xlsheet.write(0, 3, '', style3)
            xlsheet.write(0, 4, '截止时间：', style3)
            xlsheet.write(0, 5, endtime, style3)
            xlsheet.write(0, 6, '', style3)
            xlsheet.write(0, 7, '工单类型：', style3)
            xlsheet.write(0, 8, choose_type, style3)

            xlsheet.write_merge(2, 2, 0, 9, '宜昌分公司家宽投诉日报（24小时）', style2)
            xlsheet.write(3, 0, '区县', style1)
            xlsheet.write(3, 1, '受理量', style1)
            xlsheet.write(3, 2, '完成量', style1)
            xlsheet.write(3, 3, '未完成超时', style1)
            xlsheet.write(3, 4, '已完成超时', style1)
            xlsheet.write(3, 5, '投诉处理及时率', style1)
            xlsheet.write(3, 6, '平均处理时长', style1)
            xlsheet.write(3, 7, '重复量', style1)
            xlsheet.write(3, 8, '重复投诉率', style1)
            xlsheet.write(3, 9, '万投比', style1)
            xlsheet.write(4, 0, '备注', style1)
            xlsheet.write(4, 1, '派发工单量', style1)
            xlsheet.write(4, 2, '归档完成工单量', style1)
            xlsheet.write(4, 3, '工单状态为“运行中”，超过派单时间24小时工单', style1)
            xlsheet.write(4, 4, '工单状态为“归档”，处理时长超24小时工单', style1)
            xlsheet.write(4, 5, '1-超时量/受理量', style1)
            xlsheet.write(4, 6, '时长=T2操作时间-T1派发时间', style1)
            xlsheet.write(4, 7, '5天内同一用户（客户电话一致）发生过2次及2次以上的投诉', style1)
            xlsheet.write(4, 8, '重复量/受理量', style1)
            xlsheet.write(4, 9, '10000*受理量/用户数', style1)

            xlsheet.write(5, 0, '城区', style1)
            xlsheet.write(5, 1, len([x for x in msg_list if x[0] == '城区']), style1)
            xlsheet.write(5, 2, len([x for x in msg_list1 if x[0] == '城区']), style1)
            xlsheet.write(5, 3, len([x for x in msg_list if x[0] == '城区' and x[1] == '运行中' and x[2] == '是']), style1)
            xlsheet.write(5, 4, len([x for x in msg_list if x[0] == '城区' and x[1] == '归档' and x[2] == '是']), style1)
            xlsheet.write(5, 5, xlwt.Formula("1-((D6+E6)/(B6))"), style4)
            all_time = 0
            for i in [x for x in msg_list if x[0] == '城区']:
                all_time = all_time + i[-2]
            xlsheet.write(5, 6, '%.2f' % (
                av_time(all_time, len([x for x in msg_list if x[0] == '城区']))), style1)
            xlsheet.write(5, 7, 1, style1)
            xlsheet.write(5, 8, xlwt.Formula("(H6/B6)"), style4)
            xlsheet.write(5, 9, xlwt.Formula("(B6*10000)/ 25171"), style1)

            xlsheet.write(6, 0, '当阳', style1)
            xlsheet.write(6, 1, len([x for x in msg_list if x[0] == '当阳']), style1)
            xlsheet.write(6, 2, len([x for x in msg_list1 if x[0] == '当阳']), style1)
            xlsheet.write(6, 3, len([x for x in msg_list if x[0] == '当阳' and x[1] == '运行中' and x[2] == '是']), style1)
            xlsheet.write(6, 4, len([x for x in msg_list if x[0] == '当阳' and x[1] == '归档' and x[2] == '是']), style1)
            xlsheet.write(6, 5, xlwt.Formula("1-((D7+E7)/(B7))"), style4)
            all_time = 0
            for i in [x for x in msg_list if x[0] == '当阳']:
                all_time = all_time + i[-2]
            xlsheet.write(6, 6, '%.2f' % (
                av_time(all_time, len([x for x in msg_list if x[0] == '当阳']))), style1)
            xlsheet.write(6, 7, 1, style1)
            xlsheet.write(6, 8, xlwt.Formula("(H7/B7)"), style4)
            xlsheet.write(6, 9, xlwt.Formula("(B7*10000)/ 25349"), style1)

            xlsheet.write(7, 0, '开发区', style1)
            xlsheet.write(7, 1, len([x for x in msg_list if x[0] == '开发区']), style1)
            xlsheet.write(7, 2, len([x for x in msg_list1 if x[0] == '开发区']), style1)
            xlsheet.write(7, 3, len([x for x in msg_list if x[0] == '开发区' and x[1] == '运行中' and x[2] == '是']), style1)
            xlsheet.write(7, 4, len([x for x in msg_list if x[0] == '开发区' and x[1] == '归档' and x[2] == '是']), style1)
            xlsheet.write(7, 5, xlwt.Formula("1-((D8+E8)/(B8))"), style4)
            all_time = 0
            for i in [x for x in msg_list if x[0] == '开发区']:
                all_time = all_time + i[-2]
            xlsheet.write(7, 6, '%.2f' % (
                av_time(all_time, len([x for x in msg_list if x[0] == '开发区']))), style1)
            xlsheet.write(7, 7, 1, style1)
            xlsheet.write(7, 8, xlwt.Formula("(H8/B8)"), style4)
            xlsheet.write(7, 9, xlwt.Formula("(B8*10000)/ 34313"), style1)

            xlsheet.write(8, 0, '五峰', style1)
            xlsheet.write(8, 1, len([x for x in msg_list if x[0] == '五峰']), style1)
            xlsheet.write(8, 2, len([x for x in msg_list1 if x[0] == '五峰']), style1)
            xlsheet.write(8, 3, len([x for x in msg_list if x[0] == '五峰' and x[1] == '运行中' and x[2] == '是']), style1)
            xlsheet.write(8, 4, len([x for x in msg_list if x[0] == '五峰' and x[1] == '归档' and x[2] == '是']), style1)
            xlsheet.write(8, 5, xlwt.Formula("1-((D9+E9)/(B9))"), style4)
            all_time = 0
            for i in [x for x in msg_list if x[0] == '五峰']:
                all_time = all_time + i[-2]
            xlsheet.write(8, 6, '%.2f' % (
                av_time(all_time, len([x for x in msg_list if x[0] == '五峰']))), style1)
            xlsheet.write(8, 7, 1, style1)
            xlsheet.write(8, 8, xlwt.Formula("(H9/B9)"), style4)
            xlsheet.write(8, 9, xlwt.Formula("(B9*10000)/ 7985"), style1)

            xlsheet.write(9, 0, '兴山', style1)
            xlsheet.write(9, 1, len([x for x in msg_list if x[0] == '兴山']), style1)
            xlsheet.write(9, 2, len([x for x in msg_list1 if x[0] == '兴山']), style1)
            xlsheet.write(9, 3, len([x for x in msg_list if x[0] == '兴山' and x[1] == '运行中' and x[2] == '是']), style1)
            xlsheet.write(9, 4, len([x for x in msg_list if x[0] == '兴山' and x[1] == '归档' and x[2] == '是']), style1)
            xlsheet.write(9, 5, xlwt.Formula("1-((D10+E10)/(B10))"), style4)
            all_time = 0
            for i in [x for x in msg_list if x[0] == '兴山']:
                all_time = all_time + i[-2]
            xlsheet.write(9, 6, '%.2f' % (
                av_time(all_time, len([x for x in msg_list if x[0] == '兴山']))), style1)
            xlsheet.write(9, 7, 1, style1)
            xlsheet.write(9, 8, xlwt.Formula("(H10/B10)"), style4)
            xlsheet.write(9, 9, xlwt.Formula(("(B10*10000)/ 7453")), style1)

            xlsheet.write(10, 0, '夷陵', style1)
            xlsheet.write(10, 1, len([x for x in msg_list if x[0] == '夷陵']), style1)
            xlsheet.write(10, 2, len([x for x in msg_list1 if x[0] == '夷陵']), style1)
            xlsheet.write(10, 3, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '运行中' and x[2] == '是']), style1)
            xlsheet.write(10, 4, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '归档' and x[2] == '是']), style1)
            xlsheet.write(10, 5, xlwt.Formula("1-((D11+E11)/(B11))"), style4)
            all_time = 0
            for i in [x for x in msg_list if x[0] == '夷陵']:
                all_time = all_time + i[-2]
            xlsheet.write(10, 6, '%.2f' % (
                av_time(all_time, len([x for x in msg_list if x[0] == '夷陵']))), style1)
            xlsheet.write(10, 7, 1, style1)
            xlsheet.write(10, 8, xlwt.Formula("(H11/B11)"), style4)
            xlsheet.write(10, 9, xlwt.Formula("(B11*10000)/ 27196"), style1)

            xlsheet.write(11, 0, '宜都', style1)
            xlsheet.write(11, 1, len([x for x in msg_list if x[0] == '宜都']), style1)
            xlsheet.write(11, 2, len([x for x in msg_list1 if x[0] == '宜都']), style1)
            xlsheet.write(11, 3, len([x for x in msg_list if x[0] == '宜都' and x[1] == '运行中' and x[2] == '是']), style1)
            xlsheet.write(11, 4, len([x for x in msg_list if x[0] == '宜都' and x[1] == '归档' and x[2] == '是']), style1)
            xlsheet.write(11, 5, xlwt.Formula("1-((D12+E12)/(B12))"), style4)
            all_time = 0
            for i in [x for x in msg_list if x[0] == '宜都']:
                all_time = all_time + i[-2]
            xlsheet.write(11, 6, '%.2f' % (
                av_time(all_time, len([x for x in msg_list if x[0] == '宜都']))), style1)
            xlsheet.write(11, 7, 1, style1)
            xlsheet.write(11, 8, xlwt.Formula("(H12/B12)"), style4)
            xlsheet.write(11, 9, xlwt.Formula("(B12*10000)/ 17538"), style1)

            xlsheet.write(12, 0, '远安', style1)
            xlsheet.write(12, 1, len([x for x in msg_list if x[0] == '远安']), style1)
            xlsheet.write(12, 2, len([x for x in msg_list1 if x[0] == '远安']), style1)
            xlsheet.write(12, 3, len([x for x in msg_list if x[0] == '远安' and x[1] == '运行中' and x[2] == '是']), style1)
            xlsheet.write(12, 4, len([x for x in msg_list if x[0] == '远安' and x[1] == '归档' and x[2] == '是']), style1)
            xlsheet.write(12, 5, xlwt.Formula("1-((D13+E13)/(B13))"), style4)
            all_time = 0
            for i in [x for x in msg_list if x[0] == '远安']:
                all_time = all_time + i[-2]

            xlsheet.write(12, 6, '%.2f' % (
                av_time(all_time, len([x for x in msg_list if x[0] == '远安']))), style1)
            xlsheet.write(12, 7, 1, style1)
            xlsheet.write(12, 8, xlwt.Formula("(H13/B13)"), style4)
            xlsheet.write(12, 9, xlwt.Formula("(B13*10000)/ 12884"), style1)

            xlsheet.write(13, 0, '长阳', style1)
            xlsheet.write(13, 1, len([x for x in msg_list if x[0] == '长阳']), style1)
            xlsheet.write(13, 2, len([x for x in msg_list1 if x[0] == '长阳']), style1)
            xlsheet.write(13, 3, len([x for x in msg_list if x[0] == '长阳' and x[1] == '运行中' and x[2] == '是']), style1)
            xlsheet.write(13, 4, len([x for x in msg_list if x[0] == '长阳' and x[1] == '归档' and x[2] == '是']), style1)
            xlsheet.write(13, 5, xlwt.Formula("1-((D14+E14)/(B14))"), style4)
            all_time = 0
            for i in [x for x in msg_list if x[0] == '城区']:
                all_time = all_time + i[-2]
            xlsheet.write(13, 6, '%.2f' % (
                av_time(all_time, len([x for x in msg_list if x[0] == '长阳']))), style1)
            xlsheet.write(13, 7, 1, style1)
            xlsheet.write(13, 8, xlwt.Formula("(H14/B14)"), style4)
            xlsheet.write(13, 9, xlwt.Formula("(B14*10000)/ 18385"), style1)

            xlsheet.write(14, 0, '枝江', style1)
            xlsheet.write(14, 1, len([x for x in msg_list if x[0] == '枝江']), style1)
            xlsheet.write(14, 2, len([x for x in msg_list1 if x[0] == '枝江']), style1)
            xlsheet.write(14, 3, len([x for x in msg_list if x[0] == '枝江' and x[1] == '运行中' and x[2] == '是']), style1)
            xlsheet.write(14, 4, len([x for x in msg_list if x[0] == '枝江' and x[1] == '归档' and x[2] == '是']), style1)
            xlsheet.write(14, 5, xlwt.Formula("1-((D15+E15)/(B15))"), style4)
            all_time = 0
            for i in [x for x in msg_list if x[0] == '枝江']:
                all_time = all_time + i[-2]
            xlsheet.write(14, 6, '%.2f' % (
                av_time(all_time, len([x for x in msg_list if x[0] == '枝江']))), style1)
            xlsheet.write(14, 7, 1, style1)
            xlsheet.write(14, 8, xlwt.Formula("(H15/B15)"), style4)
            xlsheet.write(14, 9, xlwt.Formula("(B15*10000)/25378"), style1)

            xlsheet.write(15, 0, '秭归', style1)
            xlsheet.write(15, 1, len([x for x in msg_list if x[0] == '秭归']), style1)
            xlsheet.write(15, 2, len([x for x in msg_list1 if x[0] == '秭归']), style1)
            xlsheet.write(15, 3, len([x for x in msg_list if x[0] == '秭归' and x[1] == '运行中' and x[2] == '是']), style1)
            xlsheet.write(15, 4, len([x for x in msg_list if x[0] == '秭归' and x[1] == '归档' and x[2] == '是']), style1)
            xlsheet.write(15, 5, xlwt.Formula("1-((D15+E15)/(B15))"), style4)
            all_time = 0
            for i in [x for x in msg_list if x[0] == '秭归']:
                all_time = all_time + i[-2]

            xlsheet.write(15, 6, '%.2f' % (
                av_time(all_time, len([x for x in msg_list if x[0] == '秭归']))), style1)
            xlsheet.write(15, 7, 1, style1)
            xlsheet.write(15, 8, xlwt.Formula("(H16/B16)"), style4)
            xlsheet.write(15, 9, xlwt.Formula("(B16*10000)/18203"), style1)

            xlsheet.write(16, 0, '全市', style1)
            xlsheet.write(16, 1, xlwt.Formula("(B6+B7+B8+B9+B10+B11+B12+B13+B14+B15+B16)"), style1)
            xlsheet.write(16, 2, xlwt.Formula("(C6+C7+C8+C9+C10+C11+C12+C13+C14+C15+C16)"), style1)
            xlsheet.write(16, 3, xlwt.Formula("(D6+D7+D8+D9+D10+D11+D12+D13+D14+D15+D16)"), style1)
            xlsheet.write(16, 4, xlwt.Formula("(E6+E7+E8+E9+E10+E11+E12+E13+E14+E15+E16)"), style1)
            xlsheet.write(16, 5, xlwt.Formula("1-((D17+E17)/(B17))"), style4)
            xlsheet.write(16, 6, xlwt.Formula("(G6+G7+G8+G9+G10+G11+G12+G13+G14+G15+G16)/11"), style1)
            xlsheet.write(16, 7, 1, style1)
            xlsheet.write(16, 8, xlwt.Formula("(H17/B17)"), style4)
            xlsheet.write(16, 9, xlwt.Formula("(B17*10000)/219855"), style1)
            xlsname=choose_type + str(int(time.time()))
            workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
            return ('mail.itlaolang.com/downfile/{}.xls'.format(xlsname))
    if type=='投诉8小时报表':
        if choose_type=='EMOS':

            sheet = workbook_r.sheet_by_name('EMOS')
            for x in range(1, sheet.nrows):

                msg = sheet.row_values(x)
                #这是完成的工单量
                if msg[8] == '归档' and msg[18] != '' and utc_str_to_timestamp(
                        str(xlrd.xldate_as_datetime(msg[18], 0))) >= utc_str_to_timestamp(
                        starttime) and utc_str_to_timestamp(
                        str(xlrd.xldate_as_datetime(msg[18], 0))) <= utc_str_to_timestamp(endtime):
                    msg_list1.append([find_area1(msg[-1], msg[2])])
                #这是接受的工单量
                if msg[8] != '待回访' and msg[18]!='' and utc_str_to_timestamp(str(xlrd.xldate_as_datetime(msg[16], 0))) >= utc_str_to_timestamp(starttime) and utc_str_to_timestamp(str(xlrd.xldate_as_datetime(msg[16], 0))) <= utc_str_to_timestamp(endtime):
                    result = [find_area1(msg[-1], msg[2]), msg[8], get_timeout1_8(msg[8], msg[16], msg[18]),
                              time_for_end1(msg[16], msg[18]), msg[2]]#地区，状态，超时（包括运行中，归档），投诉时长,投诉地址
                    msg_list.append(result)


            workbook_m = xlwt.Workbook(encoding='utf-8')
            xlsheet = workbook_m.add_sheet('8小时投诉日报', cell_overwrite_ok=True)
            # 格式1 （有自动换行）
            style1 = xlwt.easyxf('pattern: pattern solid, fore_colour white')
            style1.font.height = 200
            style1.font.name = u'文泉驿点阵正黑'
            style1.font.colour_index = 0
            style1.borders.left = xlwt.Borders.THIN
            style1.borders.right = xlwt.Borders.THIN
            style1.borders.top = xlwt.Borders.THIN
            style1.borders.bottom = xlwt.Borders.THIN
            # style1.font.bold = True
            style1.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
            style1.alignment.horz = xlwt.Alignment.HORZ_CENTER

            # 格式2  （没有自动换行）
            style2 = xlwt.easyxf('pattern: pattern solid, fore_colour white')
            style2.font.height = 200
            style2.font.name = u'文泉驿点阵正黑'
            style2.font.colour_index = 0
            style2.borders.left = xlwt.Borders.THIN
            style2.borders.right = xlwt.Borders.THIN
            style2.borders.top = xlwt.Borders.THIN
            style2.borders.bottom = xlwt.Borders.THIN

            # style2.font.bold = True
            # style2.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
            # style2.alignment.horz = xlwt.Alignment.HORZ_CENTER

            # 格式3 黄色背景色

            style3 = xlwt.easyxf('pattern: pattern solid, fore_colour yellow')
            style3.font.height = 200
            style3.font.name = u'文泉驿点阵正黑'
            style3.font.colour_index = 0
            # style3.borders.left = xlwt.Borders.THIN
            # style3.borders.right = xlwt.Borders.THIN
            # style3.borders.top = xlwt.Borders.THIN
            # style3.borders.bottom = xlwt.Borders.THIN

            # style4 格式4 0.00%

            style4 = xlwt.easyxf('pattern: pattern solid, fore_colour white')
            style4.font.height = 200
            style4.font.name = u'文泉驿点阵正黑'
            style4.font.colour_index = 0
            style4.borders.left = xlwt.Borders.THIN
            style4.borders.right = xlwt.Borders.THIN
            style4.borders.top = xlwt.Borders.THIN
            style4.borders.bottom = xlwt.Borders.THIN
            # style1.font.bold = True
            style4.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
            style4.alignment.horz = xlwt.Alignment.HORZ_CENTER
            style4.num_format_str = '0.00%'

            # style2.font.bold = True
            # style2.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
            # style2.alignment.horz = xlwt.Alignment.HORZ_CENTER
            # 写excel表头
            # 设置单元格
            xlsheet.write(0, 1, '起始时间：', style3)
            xlsheet.write(0, 2, starttime, style3)
            xlsheet.write(0, 3, '', style3)
            xlsheet.write(0, 4, '截止时间：', style3)
            xlsheet.write(0, 5, endtime, style3)
            xlsheet.write(0, 6, '', style3)
            xlsheet.write(0, 7, '工单类型：', style3)
            xlsheet.write(0, 8, choose_type, style3)

            xlsheet.write_merge(2, 2, 0, 6, '宜昌分公司家宽投诉日报（880）', style2)
            xlsheet.write(3, 0, '区县1', style1)
            xlsheet.write(3, 1, '受理量', style1)
            xlsheet.write(3, 2, '完成量', style1)
            xlsheet.write(3, 3, '未完成超时', style1)
            xlsheet.write(3, 4, '已完成超时', style1)
            xlsheet.write(3, 5, '投诉处理及时率', style1)
            xlsheet.write(3, 6, '平均处理时长', style1)

            xlsheet.write(4, 0, '备注', style1)
            xlsheet.write(4, 1, '派发工单量', style1)
            xlsheet.write(4, 2, '归档完成工单量', style1)
            xlsheet.write(4, 3, '工单状态为“运行中”，超过派单时间24小时工单', style1)
            xlsheet.write(4, 4, '工单状态为“归档”，处理时长超24小时工单', style1)
            xlsheet.write(4, 5, '1-超时量/受理量', style1)
            xlsheet.write(4, 6, '时长=T2操作时间-T1派发时间', style1)

            xlsheet.write(5,0,'城区',style1)
            xlsheet.write(5,1,len([x for x in msg_list if x[0] == '城区']),style1)
            xlsheet.write(5,2,len([x for x in msg_list1 if x[0] == '城区']),style1)
            xlsheet.write(5,3,len([x for x in msg_list if x[0] == '城区' and x[1] =='运行中' and x[2] == '是']),style1)
            xlsheet.write(5,4,len([x for x in msg_list if x[0] == '城区' and x[1] =='归档' and x[2] == '是']),style1)
            xlsheet.write(5,5,xlwt.Formula("1-((D6+E6)/(B6))"),style4)
            all_time=0
            for i in [x for x in msg_list if x[0] == '城区']:
                all_time = all_time + i[-2]
            xlsheet.write(5, 6, '%.2f' % (
                av_time(all_time, len([x for x in msg_list if x[0] == '城区']))), style1)


            xlsheet.write(6, 0, '当阳', style1)
            xlsheet.write(6, 1, len([x for x in msg_list if x[0] == '当阳']), style1)
            xlsheet.write(6, 2, len([x for x in msg_list1 if x[0] == '当阳']), style1)
            xlsheet.write(6, 3, len([x for x in msg_list if x[0] == '当阳' and x[1] == '运行中' and x[2] == '是']), style1)
            xlsheet.write(6, 4, len([x for x in msg_list if x[0] == '当阳' and x[1] == '归档' and x[2] == '是']), style1)
            xlsheet.write(6, 5, xlwt.Formula("1-((D7+E7)/(B7))"), style4)
            all_time = 0
            for i in [x for x in msg_list if x[0] == '当阳']:
                all_time = all_time + i[-2]
            xlsheet.write(6, 6, '%.2f' % (
                av_time(all_time, len([x for x in msg_list if x[0] == '当阳']))), style1)


            xlsheet.write(7, 0, '开发区', style1)
            xlsheet.write(7, 1, len([x for x in msg_list if x[0] == '开发区']), style1)
            xlsheet.write(7, 2, len([x for x in msg_list1 if x[0] == '开发区' ]), style1)
            xlsheet.write(7, 3, len([x for x in msg_list if x[0] == '开发区' and x[1] == '运行中' and x[2] == '是']), style1)
            xlsheet.write(7, 4, len([x for x in msg_list if x[0] == '开发区' and x[1] == '归档' and x[2] == '是']), style1)
            xlsheet.write(7, 5, xlwt.Formula("1-((D8+E8)/(B8))"), style4)
            all_time = 0
            for i in [x for x in msg_list if x[0] == '开发区']:
                all_time = all_time + i[-2]
            xlsheet.write(7, 6, '%.2f' % (
                av_time(all_time, len([x for x in msg_list if x[0] == '开发区']))), style1)


            xlsheet.write(8, 0, '五峰', style1)
            xlsheet.write(8, 1, len([x for x in msg_list if x[0] == '五峰']), style1)
            xlsheet.write(8, 2, len([x for x in msg_list1 if x[0] == '五峰' ]), style1)
            xlsheet.write(8, 3, len([x for x in msg_list if x[0] == '五峰' and x[1] == '运行中' and x[2] == '是']), style1)
            xlsheet.write(8, 4, len([x for x in msg_list if x[0] == '五峰' and x[1] == '归档' and x[2] == '是']), style1)
            xlsheet.write(8, 5, xlwt.Formula("1-((D9+E9)/(B9))"), style4)
            all_time = 0
            for i in [x for x in msg_list if x[0] == '五峰']:
                all_time = all_time + i[-2]
            xlsheet.write(8, 6, '%.2f' % (
                av_time(all_time, len([x for x in msg_list if x[0] == '五峰']))), style1)


            xlsheet.write(9, 0, '兴山', style1)
            xlsheet.write(9, 1, len([x for x in msg_list if x[0] == '兴山']), style1)
            xlsheet.write(9, 2, len([x for x in msg_list1 if x[0] == '兴山' ]), style1)
            xlsheet.write(9, 3, len([x for x in msg_list if x[0] == '兴山' and x[1] == '运行中' and x[2] == '是']), style1)
            xlsheet.write(9, 4, len([x for x in msg_list if x[0] == '兴山' and x[1] == '归档' and x[2] == '是']), style1)
            xlsheet.write(9, 5, xlwt.Formula("1-((D10+E10)/(B10))"), style4)
            all_time = 0
            for i in [x for x in msg_list if x[0] == '兴山']:

                all_time = all_time + i[-2]
            xlsheet.write(9, 6, '%.2f' % (
                av_time(all_time, len([x for x in msg_list if x[0] == '兴山']))), style1)


            xlsheet.write(10, 0, '夷陵', style1)
            xlsheet.write(10, 1, len([x for x in msg_list if x[0] == '夷陵']), style1)
            xlsheet.write(10, 2, len([x for x in msg_list1 if x[0] == '夷陵' ]), style1)
            xlsheet.write(10, 3, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '运行中' and x[2] == '是']), style1)
            xlsheet.write(10, 4, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '归档' and x[2] == '是']), style1)
            xlsheet.write(10, 5, xlwt.Formula("1-((D11+E11)/(B11))"), style4)
            all_time = 0
            for i in [x for x in msg_list if x[0] == '夷陵']:

                all_time = all_time + i[-2]
            xlsheet.write(10, 6, '%.2f' % (
                av_time(all_time, len([x for x in msg_list if x[0] == '夷陵']))), style1)


            xlsheet.write(11, 0, '宜都', style1)
            xlsheet.write(11, 1, len([x for x in msg_list if x[0] == '宜都']), style1)
            xlsheet.write(11, 2, len([x for x in msg_list1 if x[0] == '宜都']), style1)
            xlsheet.write(11, 3, len([x for x in msg_list if x[0] == '宜都' and x[1] == '运行中' and x[2] == '是']), style1)
            xlsheet.write(11, 4, len([x for x in msg_list if x[0] == '宜都' and x[1] == '归档' and x[2] == '是']), style1)
            xlsheet.write(11, 5, xlwt.Formula("1-((D12+E12)/(B12))"), style4)
            all_time = 0
            for i in [x for x in msg_list if x[0] == '宜都']:
                all_time = all_time + i[-2]
            xlsheet.write(11, 6, '%.2f' % (
                av_time(all_time, len([x for x in msg_list if x[0] == '宜都']))), style1)


            xlsheet.write(12, 0, '远安', style1)
            xlsheet.write(12, 1, len([x for x in msg_list if x[0] == '远安']), style1)
            xlsheet.write(12, 2, len([x for x in msg_list1 if x[0] == '远安']), style1)
            xlsheet.write(12, 3, len([x for x in msg_list if x[0] == '远安' and x[1] == '运行中' and x[2] == '是']), style1)
            xlsheet.write(12, 4, len([x for x in msg_list if x[0] == '远安' and x[1] == '归档' and x[2] == '是']), style1)
            xlsheet.write(12, 5, xlwt.Formula("1-((D13+E13)/(B13))"), style4)
            all_time = 0
            for i in [x for x in msg_list if x[0] == '远安']:

                all_time = all_time + i[-2]

            xlsheet.write(12, 6, '%.2f' % (
                av_time(all_time, len([x for x in msg_list if x[0] == '远安']))), style1)


            xlsheet.write(13, 0, '长阳', style1)
            xlsheet.write(13, 1, len([x for x in msg_list if x[0] == '长阳']), style1)
            xlsheet.write(13, 2, len([x for x in msg_list1 if x[0] == '长阳']), style1)
            xlsheet.write(13, 3, len([x for x in msg_list if x[0] == '长阳' and x[1] == '运行中' and x[2] == '是']), style1)
            xlsheet.write(13, 4, len([x for x in msg_list if x[0] == '长阳' and x[1] == '归档' and x[2] == '是']), style1)
            xlsheet.write(13, 5, xlwt.Formula("1-((D14+E14)/(B14))"), style4)
            all_time = 0
            for i in [x for x in msg_list if x[0] == '长阳']:
                all_time = all_time + i[-2]
            xlsheet.write(13, 6, '%.2f' % (
                av_time(all_time, len([x for x in msg_list if x[0] == '长阳']))), style1)


            xlsheet.write(14, 0, '枝江', style1)
            xlsheet.write(14, 1, len([x for x in msg_list if x[0] == '枝江']), style1)
            xlsheet.write(14, 2, len([x for x in msg_list1 if x[0] == '枝江']), style1)
            xlsheet.write(14, 3, len([x for x in msg_list if x[0] == '枝江' and x[1] == '运行中' and x[2] == '是']), style1)
            xlsheet.write(14, 4, len([x for x in msg_list if x[0] == '枝江' and x[1] == '归档' and x[2] == '是']), style1)
            xlsheet.write(14, 5, xlwt.Formula("1-((D15+E15)/(B15))"), style4)
            all_time = 0
            for i in [x for x in msg_list if x[0] == '枝江']:
                all_time = all_time + i[-2]
            xlsheet.write(14, 6, '%.2f' % (
                av_time(all_time, len([x for x in msg_list if x[0] == '枝江']))), style1)


            xlsheet.write(15, 0, '秭归', style1)
            xlsheet.write(15, 1, len([x for x in msg_list if x[0] == '秭归']), style1)
            xlsheet.write(15, 2, len([x for x in msg_list1 if x[0] == '秭归']), style1)
            xlsheet.write(15, 3, len([x for x in msg_list if x[0] == '秭归' and x[1] == '运行中' and x[2] == '是']), style1)
            xlsheet.write(15, 4, len([x for x in msg_list if x[0] == '秭归' and x[1] == '归档' and x[2] == '是']), style1)
            xlsheet.write(15, 5, xlwt.Formula("1-((D15+E15)/(B15))"), style4)
            all_time = 0
            for i in [x for x in msg_list if x[0] == '秭归']:
                all_time = all_time + i[-2]

            xlsheet.write(15, 6, '%.2f' % (
                av_time(all_time, len([x for x in msg_list if x[0] == '秭归']))), style1)


            xlsheet.write(16, 0, '全市', style1)
            xlsheet.write(16, 1, xlwt.Formula("(B6+B7+B8+B9+B10+B11+B12+B13+B14+B15+B16)"), style1)
            xlsheet.write(16, 2, xlwt.Formula("(C6+C7+C8+C9+C10+C11+C12+C13+C14+C15+C16)"), style1)
            xlsheet.write(16, 3, xlwt.Formula("(D6+D7+D8+D9+D10+D11+D12+D13+D14+D15+D16)"), style1)
            xlsheet.write(16, 4, xlwt.Formula("(E6+E7+E8+E9+E10+E11+E12+E13+E14+E15+E16)"), style1)
            xlsheet.write(16, 5, xlwt.Formula("1-((D17+E17)/(B17))"), style4)
            xlsheet.write(16, 6, xlwt.Formula("(G6+G7+G8+G9+G10+G11+G12+G13+G14+G15+G16)/11"), style1)


            workbook_m.save('/var/www/downfile/{}.xls'.format(choose_type+str(int(time.time()))))
            return ('mail.itlaolang.com/downfile/{}.xls'.format(choose_type+str(int(time.time()))))

        if choose_type=='一键报障':
            sheet = workbook_r.sheet_by_name('一键报障')
            for x in range(1, sheet.nrows):

                msg = sheet.row_values(x)
                # 这是完成的工单量
                if msg[11] == '归档' and msg[25] != '' and utc_str_to_timestamp(
                        str(msg[25])) >= utc_str_to_timestamp(
                    starttime) and utc_str_to_timestamp(
                    str(msg[25])) <= utc_str_to_timestamp(endtime):
                    msg_list1.append([find_area2(msg[8])])
                # 这是接受的工单量
                if  msg[25] != '' and utc_str_to_timestamp(
                        str(msg[22])) >= utc_str_to_timestamp(
                        starttime) and utc_str_to_timestamp(
                        str(msg[22])) <= utc_str_to_timestamp(endtime):
                    result = [find_area2(msg[8]), msg[11], get_timeout2_8(msg[11], msg[22], msg[25]),
                              time_for_end2(msg[22], msg[25]), msg[10]]  # 地区，状态，超时（包括运行中，归档），投诉时长,投诉地址
                    msg_list.append(result)

            workbook_m = xlwt.Workbook(encoding='utf-8')
            xlsheet = workbook_m.add_sheet('24小时投诉日报', cell_overwrite_ok=True)
            # 格式1 （有自动换行）
            style1 = xlwt.easyxf('pattern: pattern solid, fore_colour white')
            style1.font.height = 200
            style1.font.name = u'文泉驿点阵正黑'
            style1.font.colour_index = 0
            style1.borders.left = xlwt.Borders.THIN
            style1.borders.right = xlwt.Borders.THIN
            style1.borders.top = xlwt.Borders.THIN
            style1.borders.bottom = xlwt.Borders.THIN
            # style1.font.bold = True
            style1.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
            style1.alignment.horz = xlwt.Alignment.HORZ_CENTER

            # 格式2  （没有自动换行）
            style2 = xlwt.easyxf('pattern: pattern solid, fore_colour white')
            style2.font.height = 200
            style2.font.name = u'文泉驿点阵正黑'
            style2.font.colour_index = 0
            style2.borders.left = xlwt.Borders.THIN
            style2.borders.right = xlwt.Borders.THIN
            style2.borders.top = xlwt.Borders.THIN
            style2.borders.bottom = xlwt.Borders.THIN

            # style2.font.bold = True
            # style2.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
            # style2.alignment.horz = xlwt.Alignment.HORZ_CENTER

            # 格式3 黄色背景色

            style3 = xlwt.easyxf('pattern: pattern solid, fore_colour yellow')
            style3.font.height = 200
            style3.font.name = u'文泉驿点阵正黑'
            style3.font.colour_index = 0
            # style3.borders.left = xlwt.Borders.THIN
            # style3.borders.right = xlwt.Borders.THIN
            # style3.borders.top = xlwt.Borders.THIN
            # style3.borders.bottom = xlwt.Borders.THIN

            # style4 格式4 0.00%

            style4 = xlwt.easyxf('pattern: pattern solid, fore_colour white')
            style4.font.height = 200
            style4.font.name = u'文泉驿点阵正黑'
            style4.font.colour_index = 0
            style4.borders.left = xlwt.Borders.THIN
            style4.borders.right = xlwt.Borders.THIN
            style4.borders.top = xlwt.Borders.THIN
            style4.borders.bottom = xlwt.Borders.THIN
            # style1.font.bold = True
            style4.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
            style4.alignment.horz = xlwt.Alignment.HORZ_CENTER
            style4.num_format_str = '0.00%'

            # style2.font.bold = True
            # style2.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
            # style2.alignment.horz = xlwt.Alignment.HORZ_CENTER
            # 写excel表头
            # 设置单元格
            xlsheet.write(0, 1, '起始时间：', style3)
            xlsheet.write(0, 2, starttime, style3)
            xlsheet.write(0, 3, '', style3)
            xlsheet.write(0, 4, '截止时间：', style3)
            xlsheet.write(0, 5, endtime, style3)
            xlsheet.write(0, 6, '', style3)
            xlsheet.write(0, 7, '工单类型：', style3)
            xlsheet.write(0, 8, choose_type, style3)

            xlsheet.write_merge(2, 2, 0, 9, '宜昌分公司家宽投诉日报（24小时）', style2)
            xlsheet.write(3, 0, '区县', style1)
            xlsheet.write(3, 1, '受理量', style1)
            xlsheet.write(3, 2, '完成量', style1)
            xlsheet.write(3, 3, '未完成超时', style1)
            xlsheet.write(3, 4, '已完成超时', style1)
            xlsheet.write(3, 5, '投诉处理及时率', style1)
            xlsheet.write(3, 6, '平均处理时长', style1)
            xlsheet.write(3, 7, '重复量', style1)
            xlsheet.write(3, 8, '重复投诉率', style1)
            xlsheet.write(3, 9, '万投比', style1)
            xlsheet.write(4, 0, '备注', style1)
            xlsheet.write(4, 1, '派发工单量', style1)
            xlsheet.write(4, 2, '归档完成工单量', style1)
            xlsheet.write(4, 3, '工单状态为“运行中”，超过派单时间24小时工单', style1)
            xlsheet.write(4, 4, '工单状态为“归档”，处理时长超24小时工单', style1)
            xlsheet.write(4, 5, '1-超时量/受理量', style1)
            xlsheet.write(4, 6, '时长=T2操作时间-T1派发时间', style1)


            xlsheet.write(5, 0, '城区', style1)
            xlsheet.write(5, 1, len([x for x in msg_list if x[0] == '城区']), style1)
            xlsheet.write(5, 2, len([x for x in msg_list1 if x[0] == '城区']), style1)
            xlsheet.write(5, 3, len([x for x in msg_list if x[0] == '城区' and x[1] == '运行中' and x[2] == '是']), style1)
            xlsheet.write(5, 4, len([x for x in msg_list if x[0] == '城区' and x[1] == '归档' and x[2] == '是']), style1)
            xlsheet.write(5, 5, xlwt.Formula("1-((D6+E6)/(B6))"), style4)
            all_time = 0
            for i in [x for x in msg_list if x[0] == '城区']:
                all_time = all_time + i[-2]
            xlsheet.write(5, 6, '%.2f' % (
                av_time(all_time, len([x for x in msg_list if x[0] == '城区']))), style1)


            xlsheet.write(6, 0, '当阳', style1)
            xlsheet.write(6, 1, len([x for x in msg_list if x[0] == '当阳']), style1)
            xlsheet.write(6, 2, len([x for x in msg_list1 if x[0] == '当阳']), style1)
            xlsheet.write(6, 3, len([x for x in msg_list if x[0] == '当阳' and x[1] == '运行中' and x[2] == '是']), style1)
            xlsheet.write(6, 4, len([x for x in msg_list if x[0] == '当阳' and x[1] == '归档' and x[2] == '是']), style1)
            xlsheet.write(6, 5, xlwt.Formula("1-((D7+E7)/(B7))"), style4)
            all_time = 0
            for i in [x for x in msg_list if x[0] == '当阳']:
                all_time = all_time + i[-2]
            xlsheet.write(6, 6, '%.2f' % (
                av_time(all_time, len([x for x in msg_list if x[0] == '城区']))), style1)


            xlsheet.write(7, 0, '开发区', style1)
            xlsheet.write(7, 1, len([x for x in msg_list if x[0] == '开发区']), style1)
            xlsheet.write(7, 2, len([x for x in msg_list1 if x[0] == '开发区']), style1)
            xlsheet.write(7, 3, len([x for x in msg_list if x[0] == '开发区' and x[1] == '运行中' and x[2] == '是']), style1)
            xlsheet.write(7, 4, len([x for x in msg_list if x[0] == '开发区' and x[1] == '归档' and x[2] == '是']), style1)
            xlsheet.write(7, 5, xlwt.Formula("1-((D8+E8)/(B8))"), style4)
            all_time = 0
            for i in [x for x in msg_list if x[0] == '开发区']:
                all_time = all_time + i[-2]
            xlsheet.write(7, 6, '%.2f' % (
                av_time(all_time, len([x for x in msg_list if x[0] == '城区']))), style1)

            xlsheet.write(8, 0, '五峰', style1)
            xlsheet.write(8, 1, len([x for x in msg_list if x[0] == '五峰']), style1)
            xlsheet.write(8, 2, len([x for x in msg_list1 if x[0] == '五峰']), style1)
            xlsheet.write(8, 3, len([x for x in msg_list if x[0] == '五峰' and x[1] == '运行中' and x[2] == '是']), style1)
            xlsheet.write(8, 4, len([x for x in msg_list if x[0] == '五峰' and x[1] == '归档' and x[2] == '是']), style1)
            xlsheet.write(8, 5, xlwt.Formula("1-((D9+E9)/(B9))"), style4)
            all_time = 0
            for i in [x for x in msg_list if x[0] == '五峰']:
                all_time = all_time + i[-2]
            xlsheet.write(8, 6, '%.2f' % (
                av_time(all_time, len([x for x in msg_list if x[0] == '五峰']))), style1)


            xlsheet.write(9, 0, '兴山', style1)
            xlsheet.write(9, 1, len([x for x in msg_list if x[0] == '兴山']), style1)
            xlsheet.write(9, 2, len([x for x in msg_list1 if x[0] == '兴山']), style1)
            xlsheet.write(9, 3, len([x for x in msg_list if x[0] == '兴山' and x[1] == '运行中' and x[2] == '是']), style1)
            xlsheet.write(9, 4, len([x for x in msg_list if x[0] == '兴山' and x[1] == '归档' and x[2] == '是']), style1)
            xlsheet.write(9, 5, xlwt.Formula("1-((D10+E10)/(B10))"), style4)
            all_time = 0
            for i in [x for x in msg_list if x[0] == '兴山']:
                all_time = all_time + i[-2]
            xlsheet.write(9, 6, '%.2f' % (
                av_time(all_time, len([x for x in msg_list if x[0] == '兴山']))), style1)


            xlsheet.write(10, 0, '夷陵', style1)
            xlsheet.write(10, 1, len([x for x in msg_list if x[0] == '夷陵']), style1)
            xlsheet.write(10, 2, len([x for x in msg_list1 if x[0] == '夷陵']), style1)
            xlsheet.write(10, 3, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '运行中' and x[2] == '是']), style1)
            xlsheet.write(10, 4, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '归档' and x[2] == '是']), style1)
            xlsheet.write(10, 5, xlwt.Formula("1-((D11+E11)/(B11))"), style4)
            all_time = 0
            for i in [x for x in msg_list if x[0] == '夷陵']:
                all_time = all_time + i[-2]
            xlsheet.write(10, 6, '%.2f' % (
                av_time(all_time, len([x for x in msg_list if x[0] == '夷陵']))), style1)

            xlsheet.write(11, 0, '宜都', style1)
            xlsheet.write(11, 1, len([x for x in msg_list if x[0] == '宜都']), style1)
            xlsheet.write(11, 2, len([x for x in msg_list1 if x[0] == '宜都']), style1)
            xlsheet.write(11, 3, len([x for x in msg_list if x[0] == '宜都' and x[1] == '运行中' and x[2] == '是']), style1)
            xlsheet.write(11, 4, len([x for x in msg_list if x[0] == '宜都' and x[1] == '归档' and x[2] == '是']), style1)
            xlsheet.write(11, 5, xlwt.Formula("1-((D12+E12)/(B12))"), style4)
            all_time = 0
            for i in [x for x in msg_list if x[0] == '宜都']:
                all_time = all_time + i[-2]
            xlsheet.write(11, 6, '%.2f' % (
                av_time(all_time, len([x for x in msg_list if x[0] == '宜都']))), style1)


            xlsheet.write(12, 0, '远安', style1)
            xlsheet.write(12, 1, len([x for x in msg_list if x[0] == '远安']), style1)
            xlsheet.write(12, 2, len([x for x in msg_list1 if x[0] == '远安']), style1)
            xlsheet.write(12, 3, len([x for x in msg_list if x[0] == '远安' and x[1] == '运行中' and x[2] == '是']), style1)
            xlsheet.write(12, 4, len([x for x in msg_list if x[0] == '远安' and x[1] == '归档' and x[2] == '是']), style1)
            xlsheet.write(12, 5, xlwt.Formula("1-((D13+E13)/(B13))"), style4)
            all_time = 0
            for i in [x for x in msg_list if x[0] == '远安']:
                all_time = all_time + i[-2]

            xlsheet.write(12, 6, '%.2f' % (
                av_time(all_time, len([x for x in msg_list if x[0] == '远安']))), style1)


            xlsheet.write(13, 0, '长阳', style1)
            xlsheet.write(13, 1, len([x for x in msg_list if x[0] == '长阳']), style1)
            xlsheet.write(13, 2, len([x for x in msg_list1 if x[0] == '长阳']), style1)
            xlsheet.write(13, 3, len([x for x in msg_list if x[0] == '长阳' and x[1] == '运行中' and x[2] == '是']), style1)
            xlsheet.write(13, 4, len([x for x in msg_list if x[0] == '长阳' and x[1] == '归档' and x[2] == '是']), style1)
            xlsheet.write(13, 5, xlwt.Formula("1-((D14+E14)/(B14))"), style4)
            all_time = 0
            for i in [x for x in msg_list if x[0] == '城区']:
                all_time = all_time + i[-2]
            xlsheet.write(13, 6, '%.2f' % (
                av_time(all_time, len([x for x in msg_list if x[0] == '长阳']))), style1)


            xlsheet.write(14, 0, '枝江', style1)
            xlsheet.write(14, 1, len([x for x in msg_list if x[0] == '枝江']), style1)
            xlsheet.write(14, 2, len([x for x in msg_list1 if x[0] == '枝江']), style1)
            xlsheet.write(14, 3, len([x for x in msg_list if x[0] == '枝江' and x[1] == '运行中' and x[2] == '是']), style1)
            xlsheet.write(14, 4, len([x for x in msg_list if x[0] == '枝江' and x[1] == '归档' and x[2] == '是']), style1)
            xlsheet.write(14, 5, xlwt.Formula("1-((D15+E15)/(B15))"), style4)
            all_time = 0
            for i in [x for x in msg_list if x[0] == '枝江']:
                all_time = all_time + i[-2]
            xlsheet.write(14, 6, '%.2f' % (
                av_time(all_time, len([x for x in msg_list if x[0] == '枝江']))), style1)


            xlsheet.write(15, 0, '秭归', style1)
            xlsheet.write(15, 1, len([x for x in msg_list if x[0] == '秭归']), style1)
            xlsheet.write(15, 2, len([x for x in msg_list1 if x[0] == '秭归']), style1)
            xlsheet.write(15, 3, len([x for x in msg_list if x[0] == '秭归' and x[1] == '运行中' and x[2] == '是']), style1)
            xlsheet.write(15, 4, len([x for x in msg_list if x[0] == '秭归' and x[1] == '归档' and x[2] == '是']), style1)
            xlsheet.write(15, 5, xlwt.Formula("1-((D16+E16)/(B16))"), style4)
            all_time = 0
            for i in [x for x in msg_list if x[0] == '秭归']:
                all_time = all_time + i[-2]

            xlsheet.write(15, 6, '%.2f' % (
                av_time(all_time, len([x for x in msg_list if x[0] == '秭归']))), style1)

            xlsheet.write(16, 0, '全市', style1)
            xlsheet.write(16, 1, xlwt.Formula("(B6+B7+B8+B9+B10+B11+B12+B13+B14+B15+B16)"), style1)
            xlsheet.write(16, 2, xlwt.Formula("(C6+C7+C8+C9+C10+C11+C12+C13+C14+C15+C16)"), style1)
            xlsheet.write(16, 3, xlwt.Formula("(D6+D7+D8+D9+D10+D11+D12+D13+D14+D15+D16)"), style1)
            xlsheet.write(16, 4, xlwt.Formula("(E6+E7+E8+E9+E10+E11+E12+E13+E14+E15+E16)"), style1)
            xlsheet.write(16, 5, xlwt.Formula("1-((D17+E17)/(B17))"), style4)
            xlsheet.write(16, 6, xlwt.Formula("(G6+G7+G8+G9+G10+G11+G12+G13+G14+G15+G16)/11"), style1)


            xlsname=choose_type + str(int(time.time()))
            workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
            return ('mail.itlaolang.com/downfile/{}.xls'.format(xlsname))
        else:
            sheet = workbook_r.sheet_by_name('EMOS')
            for x in range(1, sheet.nrows):

                msg = sheet.row_values(x)
                # 这是完成的工单量
                if msg[8] == '归档' and msg[18] != '' and utc_str_to_timestamp(
                        str(xlrd.xldate_as_datetime(msg[18], 0))) >= utc_str_to_timestamp(
                    starttime) and utc_str_to_timestamp(
                    str(xlrd.xldate_as_datetime(msg[18], 0))) <= utc_str_to_timestamp(endtime):
                    msg_list1.append([find_area1(msg[-1], msg[2])])
                # 这是接受的工单量
                if msg[8] != '待回访' and msg[18] != '' and utc_str_to_timestamp(
                        str(xlrd.xldate_as_datetime(msg[16], 0))) >= utc_str_to_timestamp(
                        starttime) and utc_str_to_timestamp(
                        str(xlrd.xldate_as_datetime(msg[16], 0))) <= utc_str_to_timestamp(endtime):
                    result = [find_area1(msg[-1], msg[2]), msg[8], get_timeout1_8(msg[8], msg[16], msg[18]),
                              time_for_end1(msg[16], msg[18]), msg[2]]  # 地区，状态，超时（包括运行中，归档），投诉时长,投诉地址
                    msg_list.append(result)
            sheet = workbook_r.sheet_by_name('一键报障')
            for x in range(1, sheet.nrows):

                msg = sheet.row_values(x)
                # 这是完成的工单量
                if msg[11] == '归档' and msg[25] != '' and utc_str_to_timestamp(
                        str(msg[25])) >= utc_str_to_timestamp(
                    starttime) and utc_str_to_timestamp(
                    str(msg[25])) <= utc_str_to_timestamp(endtime):
                    msg_list1.append([find_area2(msg[8])])
                # 这是接受的工单量
                if msg[25] != '' and utc_str_to_timestamp(
                        str(msg[22])) >= utc_str_to_timestamp(
                    starttime) and utc_str_to_timestamp(
                    str(msg[22])) <= utc_str_to_timestamp(endtime):
                    result = [find_area2(msg[8]), msg[11], get_timeout2_8(msg[11], msg[22], msg[25]),
                              time_for_end2(msg[22], msg[25]), msg[10]]  # 地区，状态，超时（包括运行中，归档），投诉时长,投诉地址
                    msg_list.append(result)


            workbook_m = xlwt.Workbook(encoding='utf-8')
            xlsheet = workbook_m.add_sheet('8小时投诉日报', cell_overwrite_ok=True)
            # 格式1 （有自动换行）
            style1 = xlwt.easyxf('pattern: pattern solid, fore_colour white')
            style1.font.height = 200
            style1.font.name = u'文泉驿点阵正黑'
            style1.font.colour_index = 0
            style1.borders.left = xlwt.Borders.THIN
            style1.borders.right = xlwt.Borders.THIN
            style1.borders.top = xlwt.Borders.THIN
            style1.borders.bottom = xlwt.Borders.THIN
            # style1.font.bold = True
            style1.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
            style1.alignment.horz = xlwt.Alignment.HORZ_CENTER

            # 格式2  （没有自动换行）
            style2 = xlwt.easyxf('pattern: pattern solid, fore_colour white')
            style2.font.height = 200
            style2.font.name = u'文泉驿点阵正黑'
            style2.font.colour_index = 0
            style2.borders.left = xlwt.Borders.THIN
            style2.borders.right = xlwt.Borders.THIN
            style2.borders.top = xlwt.Borders.THIN
            style2.borders.bottom = xlwt.Borders.THIN

            # style2.font.bold = True
            # style2.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
            # style2.alignment.horz = xlwt.Alignment.HORZ_CENTER

            # 格式3 黄色背景色

            style3 = xlwt.easyxf('pattern: pattern solid, fore_colour yellow')
            style3.font.height = 200
            style3.font.name = u'文泉驿点阵正黑'
            style3.font.colour_index = 0
            # style3.borders.left = xlwt.Borders.THIN
            # style3.borders.right = xlwt.Borders.THIN
            # style3.borders.top = xlwt.Borders.THIN
            # style3.borders.bottom = xlwt.Borders.THIN

            # style4 格式4 0.00%

            style4 = xlwt.easyxf('pattern: pattern solid, fore_colour white')
            style4.font.height = 200
            style4.font.name = u'文泉驿点阵正黑'
            style4.font.colour_index = 0
            style4.borders.left = xlwt.Borders.THIN
            style4.borders.right = xlwt.Borders.THIN
            style4.borders.top = xlwt.Borders.THIN
            style4.borders.bottom = xlwt.Borders.THIN
            # style1.font.bold = True
            style4.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
            style4.alignment.horz = xlwt.Alignment.HORZ_CENTER
            style4.num_format_str = '0.00%'

            # style2.font.bold = True
            # style2.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
            # style2.alignment.horz = xlwt.Alignment.HORZ_CENTER
            # 写excel表头
            # 设置单元格
            xlsheet.write(0, 1, '起始时间：', style3)
            xlsheet.write(0, 2, starttime, style3)
            xlsheet.write(0, 3, '', style3)
            xlsheet.write(0, 4, '截止时间：', style3)
            xlsheet.write(0, 5, endtime, style3)
            xlsheet.write(0, 6, '', style3)
            xlsheet.write(0, 7, '工单类型：', style3)
            xlsheet.write(0, 8, choose_type, style3)

            xlsheet.write_merge(2, 2, 0, 9, '宜昌分公司家宽投诉日报（24小时）', style2)
            xlsheet.write(3, 0, '区县', style1)
            xlsheet.write(3, 1, '受理量', style1)
            xlsheet.write(3, 2, '完成量', style1)
            xlsheet.write(3, 3, '未完成超时', style1)
            xlsheet.write(3, 4, '已完成超时', style1)
            xlsheet.write(3, 5, '投诉处理及时率', style1)
            xlsheet.write(3, 6, '平均处理时长', style1)
            xlsheet.write(3, 7, '重复量', style1)
            xlsheet.write(3, 8, '重复投诉率', style1)
            xlsheet.write(3, 9, '万投比', style1)
            xlsheet.write(4, 0, '备注', style1)
            xlsheet.write(4, 1, '派发工单量', style1)
            xlsheet.write(4, 2, '归档完成工单量', style1)
            xlsheet.write(4, 3, '工单状态为“运行中”，超过派单时间24小时工单', style1)
            xlsheet.write(4, 4, '工单状态为“归档”，处理时长超24小时工单', style1)
            xlsheet.write(4, 5, '1-超时量/受理量', style1)
            xlsheet.write(4, 6, '时长=T2操作时间-T1派发时间', style1)


            xlsheet.write(5, 0, '城区', style1)
            xlsheet.write(5, 1, len([x for x in msg_list if x[0] == '城区']), style1)
            xlsheet.write(5, 2, len([x for x in msg_list1 if x[0] == '城区']), style1)
            xlsheet.write(5, 3, len([x for x in msg_list if x[0] == '城区' and x[1] == '运行中' and x[2] == '是']), style1)
            xlsheet.write(5, 4, len([x for x in msg_list if x[0] == '城区' and x[1] == '归档' and x[2] == '是']), style1)
            xlsheet.write(5, 5, xlwt.Formula("1-((D6+E6)/(B6))"), style4)
            all_time = 0
            for i in [x for x in msg_list if x[0] == '城区']:
                all_time = all_time + i[-2]
            xlsheet.write(5, 6, '%.2f' % (
                av_time(all_time, len([x for x in msg_list if x[0] == '城区']))), style1)


            xlsheet.write(6, 0, '当阳', style1)
            xlsheet.write(6, 1, len([x for x in msg_list if x[0] == '当阳']), style1)
            xlsheet.write(6, 2, len([x for x in msg_list1 if x[0] == '当阳']), style1)
            xlsheet.write(6, 3, len([x for x in msg_list if x[0] == '当阳' and x[1] == '运行中' and x[2] == '是']), style1)
            xlsheet.write(6, 4, len([x for x in msg_list if x[0] == '当阳' and x[1] == '归档' and x[2] == '是']), style1)
            xlsheet.write(6, 5, xlwt.Formula("1-((D7+E7)/(B7))"), style4)
            all_time = 0
            for i in [x for x in msg_list if x[0] == '当阳']:
                all_time = all_time + i[-2]
            xlsheet.write(6, 6, '%.2f' % (
                av_time(all_time, len([x for x in msg_list if x[0] == '当阳']))), style1)


            xlsheet.write(7, 0, '开发区', style1)
            xlsheet.write(7, 1, len([x for x in msg_list if x[0] == '开发区']), style1)
            xlsheet.write(7, 2, len([x for x in msg_list1 if x[0] == '开发区']), style1)
            xlsheet.write(7, 3, len([x for x in msg_list if x[0] == '开发区' and x[1] == '运行中' and x[2] == '是']), style1)
            xlsheet.write(7, 4, len([x for x in msg_list if x[0] == '开发区' and x[1] == '归档' and x[2] == '是']), style1)
            xlsheet.write(7, 5, xlwt.Formula("1-((D8+E8)/(B8))"), style4)
            all_time = 0
            for i in [x for x in msg_list if x[0] == '开发区']:
                all_time = all_time + i[-2]
            xlsheet.write(7, 6, '%.2f' % (
                av_time(all_time, len([x for x in msg_list if x[0] == '开发区']))), style1)


            xlsheet.write(8, 0, '五峰', style1)
            xlsheet.write(8, 1, len([x for x in msg_list if x[0] == '五峰']), style1)
            xlsheet.write(8, 2, len([x for x in msg_list1 if x[0] == '五峰']), style1)
            xlsheet.write(8, 3, len([x for x in msg_list if x[0] == '五峰' and x[1] == '运行中' and x[2] == '是']), style1)
            xlsheet.write(8, 4, len([x for x in msg_list if x[0] == '五峰' and x[1] == '归档' and x[2] == '是']), style1)
            xlsheet.write(8, 5, xlwt.Formula("1-((D9+E9)/(B9))"), style4)
            all_time = 0
            for i in [x for x in msg_list if x[0] == '五峰']:
                all_time = all_time + i[-2]
            xlsheet.write(8, 6, '%.2f' % (
                av_time(all_time, len([x for x in msg_list if x[0] == '五峰']))), style1)

            xlsheet.write(9, 0, '兴山', style1)
            xlsheet.write(9, 1, len([x for x in msg_list if x[0] == '兴山']), style1)
            xlsheet.write(9, 2, len([x for x in msg_list1 if x[0] == '兴山']), style1)
            xlsheet.write(9, 3, len([x for x in msg_list if x[0] == '兴山' and x[1] == '运行中' and x[2] == '是']), style1)
            xlsheet.write(9, 4, len([x for x in msg_list if x[0] == '兴山' and x[1] == '归档' and x[2] == '是']), style1)
            xlsheet.write(9, 5, xlwt.Formula("1-((D10+E10)/(B10))"), style4)
            all_time = 0
            for i in [x for x in msg_list if x[0] == '兴山']:
                all_time = all_time + i[-2]
            xlsheet.write(9, 6, '%.2f' % (
                av_time(all_time, len([x for x in msg_list if x[0] == '兴山']))), style1)


            xlsheet.write(10, 0, '夷陵', style1)
            xlsheet.write(10, 1, len([x for x in msg_list if x[0] == '夷陵']), style1)
            xlsheet.write(10, 2, len([x for x in msg_list1 if x[0] == '夷陵']), style1)
            xlsheet.write(10, 3, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '运行中' and x[2] == '是']), style1)
            xlsheet.write(10, 4, len([x for x in msg_list if x[0] == '夷陵' and x[1] == '归档' and x[2] == '是']), style1)
            xlsheet.write(10, 5, xlwt.Formula("1-((D11+E11)/(B11))"), style4)
            all_time = 0
            for i in [x for x in msg_list if x[0] == '夷陵']:
                all_time = all_time + i[-2]
            xlsheet.write(10, 6, '%.2f' % (
                av_time(all_time, len([x for x in msg_list if x[0] == '夷陵']))), style1)

            xlsheet.write(11, 0, '宜都', style1)
            xlsheet.write(11, 1, len([x for x in msg_list if x[0] == '宜都']), style1)
            xlsheet.write(11, 2, len([x for x in msg_list1 if x[0] == '宜都']), style1)
            xlsheet.write(11, 3, len([x for x in msg_list if x[0] == '宜都' and x[1] == '运行中' and x[2] == '是']), style1)
            xlsheet.write(11, 4, len([x for x in msg_list if x[0] == '宜都' and x[1] == '归档' and x[2] == '是']), style1)
            xlsheet.write(11, 5, xlwt.Formula("1-((D12+E12)/(B12))"), style4)
            all_time = 0
            for i in [x for x in msg_list if x[0] == '宜都']:
                all_time = all_time + i[-2]
            xlsheet.write(11, 6, '%.2f' % (
                av_time(all_time, len([x for x in msg_list if x[0] == '宜都']))), style1)


            xlsheet.write(12, 0, '远安', style1)
            xlsheet.write(12, 1, len([x for x in msg_list if x[0] == '远安']), style1)
            xlsheet.write(12, 2, len([x for x in msg_list1 if x[0] == '远安']), style1)
            xlsheet.write(12, 3, len([x for x in msg_list if x[0] == '远安' and x[1] == '运行中' and x[2] == '是']), style1)
            xlsheet.write(12, 4, len([x for x in msg_list if x[0] == '远安' and x[1] == '归档' and x[2] == '是']), style1)
            xlsheet.write(12, 5, xlwt.Formula("1-((D13+E13)/(B13))"), style4)
            all_time = 0
            for i in [x for x in msg_list if x[0] == '远安']:
                all_time = all_time + i[-2]

            xlsheet.write(12, 6, '%.2f' % (
                av_time(all_time, len([x for x in msg_list if x[0] == '远安']))), style1)


            xlsheet.write(13, 0, '长阳', style1)
            xlsheet.write(13, 1, len([x for x in msg_list if x[0] == '长阳']), style1)
            xlsheet.write(13, 2, len([x for x in msg_list1 if x[0] == '长阳']), style1)
            xlsheet.write(13, 3, len([x for x in msg_list if x[0] == '长阳' and x[1] == '运行中' and x[2] == '是']), style1)
            xlsheet.write(13, 4, len([x for x in msg_list if x[0] == '长阳' and x[1] == '归档' and x[2] == '是']), style1)
            xlsheet.write(13, 5, xlwt.Formula("1-((D14+E14)/(B14))"), style4)
            all_time = 0
            for i in [x for x in msg_list if x[0] == '长阳']:
                all_time = all_time + i[-2]
            xlsheet.write(13, 6, '%.2f' % (
                av_time(all_time, len([x for x in msg_list if x[0] == '长阳']))), style1)


            xlsheet.write(14, 0, '枝江', style1)
            xlsheet.write(14, 1, len([x for x in msg_list if x[0] == '枝江']), style1)
            xlsheet.write(14, 2, len([x for x in msg_list1 if x[0] == '枝江']), style1)
            xlsheet.write(14, 3, len([x for x in msg_list if x[0] == '枝江' and x[1] == '运行中' and x[2] == '是']), style1)
            xlsheet.write(14, 4, len([x for x in msg_list if x[0] == '枝江' and x[1] == '归档' and x[2] == '是']), style1)
            xlsheet.write(14, 5, xlwt.Formula("1-((D15+E15)/(B15))"), style4)
            all_time = 0
            for i in [x for x in msg_list if x[0] == '枝江']:
                all_time = all_time + i[-2]
            xlsheet.write(14, 6, '%.2f' % (
                av_time(all_time, len([x for x in msg_list if x[0] == '枝江']))), style1)


            xlsheet.write(15, 0, '秭归', style1)
            xlsheet.write(15, 1, len([x for x in msg_list if x[0] == '秭归']), style1)
            xlsheet.write(15, 2, len([x for x in msg_list1 if x[0] == '秭归']), style1)
            xlsheet.write(15, 3, len([x for x in msg_list if x[0] == '秭归' and x[1] == '运行中' and x[2] == '是']), style1)
            xlsheet.write(15, 4, len([x for x in msg_list if x[0] == '秭归' and x[1] == '归档' and x[2] == '是']), style1)
            xlsheet.write(15, 5, xlwt.Formula("1-((D15+E15)/(B15))"), style4)
            all_time = 0
            for i in [x for x in msg_list if x[0] == '秭归']:
                all_time = all_time + i[-2]

            xlsheet.write(15, 6, '%.2f' % (
                av_time(all_time, len([x for x in msg_list if x[0] == '秭归']))), style1)

            xlsheet.write(16, 0, '全市', style1)
            xlsheet.write(16, 1, xlwt.Formula("(B6+B7+B8+B9+B10+B11+B12+B13+B14+B15+B16)"), style1)
            xlsheet.write(16, 2, xlwt.Formula("(C6+C7+C8+C9+C10+C11+C12+C13+C14+C15+C16)"), style1)
            xlsheet.write(16, 3, xlwt.Formula("(D6+D7+D8+D9+D10+D11+D12+D13+D14+D15+D16)"), style1)
            xlsheet.write(16, 4, xlwt.Formula("(E6+E7+E8+E9+E10+E11+E12+E13+E14+E15+E16)"), style1)
            xlsheet.write(16, 5, xlwt.Formula("1-((D17+E17)/(B17))"), style4)
            xlsheet.write(16, 6, xlwt.Formula("(G6+G7+G8+G9+G10+G11+G12+G13+G14+G15+G16)/11"), style1)


            xlsname=choose_type + str(int(time.time()))
            workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
            return ('mail.itlaolang.com/downfile/{}.xls'.format(xlsname))


    print('mail.itlaolang.com/downfile/{}.xls'.format(choose_type))



#file_path='E:/04_我的技术学习/飞脉科技_Python实习/装机.xlsx'
#make_file(file_path=file_path,type='装机8小时报表',starttime='2018-02-16 00:00:00',endtime='2018-03-01 00:00:00',choose_type='全量工单')


#file_path='/home/user/桌面/4月份工单EMOS.xlsx'
#make_file1(file_path=file_path,type='投诉24小时报表',starttime='2018-04-05 00:00:00',endtime='2018-04-06 00:00:00',choose_type='EMOS')
#choose_type + str(int(time.time()))