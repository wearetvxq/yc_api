from swagger_server.export_report import *
import xlwt,time
from swagger_server.tool import *
from swagger_server.mysql_db import *
import random




xlstime=str(int(time.time()))
area_list=['秭归','枝江','长阳','远安','宜都','夷陵','兴山','五峰','开发区','当阳','城区']
def complain_export(starttime,endtime,choose_type,area,datatype):
    if choose_type=='EMOS':
        like='%'+area+'%'
        if datatype=='未完成超时':
            print ('yes')
            unfinished = YCcomplaints.select().where((YCcomplaints.platform == 2) & (YCcomplaints.area % like) & (
            YCcomplaints.starttime >= utc_str_to_timestamp(starttime)) & (
                                                     YCcomplaints.starttime <= utc_str_to_timestamp(endtime)) & (
                                                     YCcomplaints.status != '归档') & (
                                                     YCcomplaints.timeout == '是'))
            workbook_m = xlwt.Workbook(encoding='utf-8')
            xlsheet = workbook_m.add_sheet('24小时未完成超时工单', cell_overwrite_ok=True)
            xlsheet.write(0, 0, '工单平台')
            xlsheet.write(0, 1, '所属区')
            xlsheet.write(0, 2, '新增工单操作时间')
            xlsheet.write(0, 3, 'T2操作时间')
            xlsheet.write(0, 4, '处理时长')
            i=1

            for item in unfinished:

                xlsheet.write(i,0,'EMOS')
                xlsheet.write(i,1,area)
                xlsheet.write(i,2,utc_timestamp_to_str(item.starttime))
                xlsheet.write(i,3,utc_timestamp_to_str(item.endtime))
                xlsheet.write(i,4,item.usetime)
                i = i + 1
            xlsname='EMOS24小时'+area+'未完成超时工单'+xlstime
            workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
            return ('down.caicool.cc:89/{}.xls'.format(xlsname))

        if datatype=='已完成超时':

            completed = YCcomplaints.select().where((YCcomplaints.platform == 2) & (YCcomplaints.area % like) & (
                YCcomplaints.starttime >= utc_str_to_timestamp(starttime)) & (
                                                        YCcomplaints.starttime <= utc_str_to_timestamp(endtime)) & (
                                                        YCcomplaints.status == '归档') & (
                                                        YCcomplaints.timeout == '是'))


            workbook_m = xlwt.Workbook(encoding='utf-8')
            xlsheet = workbook_m.add_sheet('24小时已完成超时工单', cell_overwrite_ok=True)
            print ('yes',completed)
            xlsheet.write(0, 0, '工单平台')
            xlsheet.write(0, 1, '所属区')
            xlsheet.write(0, 2, '新增工单操作时间')
            xlsheet.write(0, 3, 'T2操作时间')
            xlsheet.write(0, 4, '处理时长')
            i = 1
            for item in completed:
                print(item.starttime,item.endtime,item.usetime)
            for item in completed:
                print ('-------------------------------',completed)
                xlsheet.write(i, 0, 'EMOS')
                xlsheet.write(i, 1, area)
                xlsheet.write(i, 2, utc_timestamp_to_str(item.starttime))
                xlsheet.write(i, 3, utc_timestamp_to_str(item.endtime))
                xlsheet.write(i, 4, item.usetime)
                i = i + 1
                print (i)
            xlsname='EMOS24小时' + area + '已完成超时工单' + xlstime
            workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
            return ('down.caicool.cc:89/{}.xls'.format(xlsname))

        if datatype=='重复量':
            workbook_m = xlwt.Workbook(encoding='utf-8')
            xlsheet = workbook_m.add_sheet('24小时重复率', cell_overwrite_ok=True)
            xlsheet.write(0, 0, '工单平台')
            xlsheet.write(0, 1, '所属区')
            xlsheet.write(0, 2, '新增工单操作时间')
            xlsheet.write(0, 3, 'T2操作时间')
            xlsheet.write(0, 4, '处理时长')
            xlsname='EMOS24小时' + area + '重复量' + xlstime
            workbook_m.save('/var/www/downfile/{}.xls'.format())
            return ('down.caicool.cc:89/{}.xls'.format(xlsname))
    if choose_type=='全量工单':
        like='%'+area+'%'
        if datatype=='未完成超时':
            print ('yes')
            unfinished = YCcomplaints.select().where((YCcomplaints.area % like) & (
            YCcomplaints.starttime >= utc_str_to_timestamp(starttime)) & (
                                                     YCcomplaints.starttime <= utc_str_to_timestamp(endtime)) & (
                                                     YCcomplaints.status != '归档') & (
                                                     YCcomplaints.timeout == '是'))
            workbook_m = xlwt.Workbook(encoding='utf-8')
            xlsheet = workbook_m.add_sheet('24小时未完成超时工单', cell_overwrite_ok=True)
            xlsheet.write(0, 0, '工单平台')
            xlsheet.write(0, 1, '所属区')
            xlsheet.write(0, 2, '新增工单操作时间')
            xlsheet.write(0, 3, 'T2操作时间')
            xlsheet.write(0, 4, '处理时长')
            i=1

            for item in unfinished:

                xlsheet.write(i,0,item.platform)
                xlsheet.write(i,1,area)
                xlsheet.write(i,2,utc_timestamp_to_str(item.starttime))
                xlsheet.write(i,3,utc_timestamp_to_str(item.endtime))
                xlsheet.write(i,4,item.usetime)
                i=i+1
            xlsname='全量工单24小时'+area+'未完成超时工单'+xlstime
            workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
            return ('down.caicool.cc:89/{}.xls'.format(xlsname))

        if datatype=='已完成超时':
            print (utc_str_to_timestamp(starttime))


            completed = YCcomplaints.select().where( (YCcomplaints.area % like) & (
                YCcomplaints.starttime >= utc_str_to_timestamp(starttime)) & (
                                                        YCcomplaints.starttime <= utc_str_to_timestamp(endtime)) & (
                                                        YCcomplaints.status == '归档') & (
                                                        YCcomplaints.timeout == '是'))


            workbook_m = xlwt.Workbook(encoding='utf-8')
            xlsheet = workbook_m.add_sheet('24小时已完成超时工单', cell_overwrite_ok=True)
            print ('yes',completed)
            xlsheet.write(0, 0, '工单平台')
            xlsheet.write(0, 1, '所属区')
            xlsheet.write(0, 2, '新增工单操作时间')
            xlsheet.write(0, 3, 'T2操作时间')
            xlsheet.write(0, 4, '处理时长')
            i = 1
            for item in completed:
                print(item.starttime,item.endtime,item.usetime)
            for item in completed:
                print ('-------------------------------',completed)
                xlsheet.write(i, 0, item.platform)
                xlsheet.write(i, 1, area)
                xlsheet.write(i, 2, utc_timestamp_to_str(item.starttime))
                xlsheet.write(i, 3, utc_timestamp_to_str(item.endtime))
                xlsheet.write(i, 4, item.usetime)
                i=i+1
            xlsname='全量工单24小时' + area + '已完成超时工单' + xlstime
            workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
            return ('down.caicool.cc:89/{}.xls'.format(xlsname))

        if datatype=='重复量':
            workbook_m = xlwt.Workbook(encoding='utf-8')
            xlsheet = workbook_m.add_sheet('24小时重复率', cell_overwrite_ok=True)
            xlsheet.write(0, 0, '工单平台')
            xlsheet.write(0, 1, '所属区')
            xlsheet.write(0, 2, '新增工单操作时间')
            xlsheet.write(0, 3, 'T2操作时间')
            xlsheet.write(0, 4, '处理时长')
            xlsname='全量工单24小时' + area + '重复量' + xlstime
            workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
            return ('down.caicool.cc:89/{}.xls'.format(xlsname))
    if choose_type=='一键报障' or '微信一键报障':
        like='%'+area+'%'
        if datatype=='未完成超时':
            print ('yes')
            unfinished = YCcomplaints.select().where((YCcomplaints.platform == 1) & (YCcomplaints.area % like) & (
            YCcomplaints.starttime >= utc_str_to_timestamp(starttime)) & (
                                                     YCcomplaints.starttime <= utc_str_to_timestamp(endtime)) & (
                                                     YCcomplaints.status != '归档') & (
                                                     YCcomplaints.timeout == '是'))
            workbook_m = xlwt.Workbook(encoding='utf-8')
            xlsheet = workbook_m.add_sheet('24小时未完成超时工单', cell_overwrite_ok=True)
            xlsheet.write(0, 0, '工单平台')
            xlsheet.write(0, 1, '所属区')
            xlsheet.write(0, 2, '新增工单操作时间')
            xlsheet.write(0, 3, 'T2操作时间')
            xlsheet.write(0, 4, '处理时长')
            i=1

            for item in unfinished:

                xlsheet.write(i,0,'一键报障')
                xlsheet.write(i,1,area)
                xlsheet.write(i,2,utc_timestamp_to_str(item.starttime))
                xlsheet.write(i,3,utc_timestamp_to_str(item.endtime))
                xlsheet.write(i,4,item.usetime)
                i=i+1
            xlsname='24小时一键报障' + area + '未完成超时工单' + xlstime
            workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
            return ('down.caicool.cc:89/{}.xls'.format(xlsname))

        if datatype=='已完成超时':
            print ('yes')
            completed = YCcomplaints.select().where((YCcomplaints.platform == 1) & (YCcomplaints.area % like) & (
                YCcomplaints.starttime >= utc_str_to_timestamp(starttime)) & (
                                                        YCcomplaints.starttime <= utc_str_to_timestamp(endtime)) & (
                                                        YCcomplaints.status == '归档') & (
                                                        YCcomplaints.timeout == '是'))


            workbook_m = xlwt.Workbook(encoding='utf-8')
            xlsheet = workbook_m.add_sheet('24小时已完成超时工单', cell_overwrite_ok=True)
            xlsheet.write(0, 0, '工单平台')
            xlsheet.write(0, 1, '所属区')
            xlsheet.write(0, 2, '新增工单操作时间')
            xlsheet.write(0, 3, 'T2操作时间')
            xlsheet.write(0, 4, '处理时长')
            i = 1

            for item in completed:
                xlsheet.write(i, 0, '一键报障')
                xlsheet.write(i, 1, area)
                xlsheet.write(i, 2, utc_timestamp_to_str(item.starttime))
                xlsheet.write(i, 3, utc_timestamp_to_str(item.endtime))
                xlsheet.write(i, 4, item.usetime)
                i=i+1
            xlsname='24小时一键报障' + area + '已完成超时工单' + xlstime
            workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
            return ('down.caicool.cc:89/{}.xls'.format(xlsname))
        if datatype=='重复量':
            workbook_m = xlwt.Workbook(encoding='utf-8')
            xlsheet = workbook_m.add_sheet('24小时重复量', cell_overwrite_ok=True)
            xlsheet.write(0, 0, '工单平台')
            xlsheet.write(0, 1, '所属区')
            xlsheet.write(0, 2, '新增工单操作时间')
            xlsheet.write(0, 3, 'T2操作时间')
            xlsheet.write(0, 4, '处理时长')
            xlsname='24小时一键报障' + area + '重复量' + xlstime
            workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
            return ('down.caicool.cc:89/{}.xls'.format(xlsname))
    else:
        like='%'+area+'%'
        if datatype=='未完成超时':
            print ('yes')
            unfinished = YCcomplaints.select().where((YCcomplaints.platform == 3) & (YCcomplaints.area % like) & (
            YCcomplaints.starttime >= utc_str_to_timestamp(starttime)) & (
                                                     YCcomplaints.starttime <= utc_str_to_timestamp(endtime)) & (
                                                     YCcomplaints.status != '是') & (
                                                     YCcomplaints.timeout == '是'))
            workbook_m = xlwt.Workbook(encoding='utf-8')
            xlsheet = workbook_m.add_sheet('24小时未完成超时工单', cell_overwrite_ok=True)
            xlsheet.write(0, 0, '工单平台')
            xlsheet.write(0, 1, '所属区')
            xlsheet.write(0, 2, '新增工单操作时间')
            xlsheet.write(0, 3, 'T2操作时间')
            xlsheet.write(0, 4, '处理时长')
            i=1

            for item in unfinished:

                xlsheet.write(i,0,'CRM')
                xlsheet.write(i,1,area)
                xlsheet.write(i,2,utc_timestamp_to_str(item.starttime))
                xlsheet.write(i,3,utc_timestamp_to_str(item.endtime))
                xlsheet.write(i,4,item.usetime)
                i=i+1
            xlsname='24小时CRM'+area+'未完成超时工单'+xlstime
            workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
            return ('down.caicool.cc:89/{}.xls'.format(xlsname))

        if datatype=='已完成超时':
            print ('yes')
            completed = YCcomplaints.select().where((YCcomplaints.platform == 3) & (YCcomplaints.area % like) & (
                YCcomplaints.starttime >= utc_str_to_timestamp(starttime)) & (
                                                        YCcomplaints.starttime <= utc_str_to_timestamp(endtime)) & (
                                                        YCcomplaints.status == '是') & (
                                                        YCcomplaints.timeout == '是'))


            workbook_m = xlwt.Workbook(encoding='utf-8')
            xlsheet = workbook_m.add_sheet('24小时已完成超时工单', cell_overwrite_ok=True)
            xlsheet.write(0, 0, '工单平台')
            xlsheet.write(0, 1, '所属区')
            xlsheet.write(0, 2, '新增工单操作时间')
            xlsheet.write(0, 3, 'T2操作时间')
            xlsheet.write(0, 4, '处理时长')
            i = 1

            for item in completed:
                xlsheet.write(i, 0, 'CRM')
                xlsheet.write(i, 1, area)
                xlsheet.write(i, 2, utc_timestamp_to_str(item.starttime))
                xlsheet.write(i, 3, utc_timestamp_to_str(item.endtime))
                xlsheet.write(i, 4, item.usetime)
                i=i+1
            xlsname='24小时CRM' + area + '已完成超时工单' + xlstime
            workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
            return ('down.caicool.cc:89/{}.xls'.format(xlsname))
        if datatype=='重复量':
            workbook_m = xlwt.Workbook(encoding='utf-8')
            xlsheet = workbook_m.add_sheet('24小时重复量', cell_overwrite_ok=True)
            xlsheet.write(0, 0, '工单平台')
            xlsheet.write(0, 1, '所属区')
            xlsheet.write(0, 2, '新增工单操作时间')
            xlsheet.write(0, 3, 'T2操作时间')
            xlsheet.write(0, 4, '处理时长')
            xlsname='24小时CRM' + area + '重复量' + xlstime
            workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
            return ('down.caicool.cc:89/{}.xls'.format(xlsname))
def complain_export_8(starttime,endtime,choose_type,area,datatype):
    if choose_type=='EMOS':
        like='%'+area+'%'
        if datatype=='未完成超时':
            print ('yes')
            unfinished = YCcomplaints.select().where((YCcomplaints.platform == 2) & (YCcomplaints.area % like) & (
            YCcomplaints.starttime >= utc_str_to_timestamp(starttime)) & (
                                                     YCcomplaints.starttime <= utc_str_to_timestamp(endtime)) & (
                                                     YCcomplaints.status != '归档') & (
                                                     YCcomplaints.timeout == '是'))
            workbook_m = xlwt.Workbook(encoding='utf-8')
            xlsheet = workbook_m.add_sheet('8小时未完成超时工单', cell_overwrite_ok=True)
            xlsheet.write(0, 0, '工单平台')
            xlsheet.write(0, 1, '所属区')
            xlsheet.write(0, 2, '新增工单操作时间')
            xlsheet.write(0, 3, 'T2操作时间')
            xlsheet.write(0, 4, '处理时长')
            i=1

            for item in unfinished:

                xlsheet.write(i,0,'EMOS')
                xlsheet.write(i,1,area)
                xlsheet.write(i,2,utc_timestamp_to_str(item.starttime))
                xlsheet.write(i,3,utc_timestamp_to_str(item.endtime))
                xlsheet.write(i,4,item.usetime)
                i=i+1
            xlsname='EMOS8小时'+area+'未完成超时工单'+xlstime
            workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
            return ('down.caicool.cc:89/{}.xls'.format(xlsname))

        if datatype=='已完成超时':
            print (utc_str_to_timestamp(starttime))
            completed = YCcomplaints.select().where((YCcomplaints.platform == 2) & (YCcomplaints.area % like) & (
                YCcomplaints.starttime >= utc_str_to_timestamp(starttime)) & (
                                                        YCcomplaints.starttime <= utc_str_to_timestamp(endtime)) & (
                                                        YCcomplaints.status == '归档') & (YCcomplaints.usetime >= 20))



            workbook_m = xlwt.Workbook(encoding='utf-8')
            xlsheet = workbook_m.add_sheet('8小时已完成超时工单', cell_overwrite_ok=True)
            print ('yes',completed)
            xlsheet.write(0, 0, '工单平台')
            xlsheet.write(0, 1, '所属区')
            xlsheet.write(0, 2, '新增工单操作时间')
            xlsheet.write(0, 3, 'T2操作时间')
            xlsheet.write(0, 4, '处理时长')
            i = 1
            for item in completed:
                print(item.starttime,item.endtime,item.usetime)
            for item in completed:
                print ('-------------------------------',completed)
                xlsheet.write(i, 0, 'EMOS')
                xlsheet.write(i, 1, area)
                xlsheet.write(i, 2, utc_timestamp_to_str(item.starttime))
                xlsheet.write(i, 3, utc_timestamp_to_str(item.endtime))
                xlsheet.write(i, 4, item.usetime)
                i=i+1
            xlsname='EMOS8小时' + area + '已完成超时工单' + xlstime
            workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
            return ('down.caicool.cc:89/{}.xls'.format(xlsname))

        if datatype=='重复量':
            workbook_m = xlwt.Workbook(encoding='utf-8')
            xlsheet = workbook_m.add_sheet('8小时重复率', cell_overwrite_ok=True)
            xlsheet.write(0, 0, '工单平台')
            xlsheet.write(0, 1, '所属区')
            xlsheet.write(0, 2, '新增工单操作时间')
            xlsheet.write(0, 3, 'T2操作时间')
            xlsheet.write(0, 4, '处理时长')
            xlsname='EMOS8小时' + area + '重复量' + xlstime
            workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
            return ('down.caicool.cc:89/{}.xls'.format(xlsname))
    if choose_type=='全量工单':
        like='%'+area+'%'
        if datatype=='未完成超时':
            print ('yes')
            unfinished = YCcomplaints.select().where((YCcomplaints.area % like) & (
            YCcomplaints.starttime >= utc_str_to_timestamp(starttime)) & (
                                                     YCcomplaints.starttime <= utc_str_to_timestamp(endtime)) & (
                                                     YCcomplaints.status != '归档') & (
                                                     YCcomplaints.timeout == '是'))
            workbook_m = xlwt.Workbook(encoding='utf-8')
            xlsheet = workbook_m.add_sheet('8小时未完成超时工单', cell_overwrite_ok=True)
            xlsheet.write(0, 0, '工单平台')
            xlsheet.write(0, 1, '所属区')
            xlsheet.write(0, 2, '新增工单操作时间')
            xlsheet.write(0, 3, 'T2操作时间')
            xlsheet.write(0, 4, '处理时长')
            i=1

            for item in unfinished:

                xlsheet.write(i,0,item.platform)
                xlsheet.write(i,1,area)
                xlsheet.write(i,2,utc_timestamp_to_str(item.starttime))
                xlsheet.write(i,3,utc_timestamp_to_str(item.endtime))
                xlsheet.write(i,4,item.usetime)
                i=i+1
            xlsname='全量工单8小时'+area+'未完成超时工单'+xlstime
            workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
            return ('down.caicool.cc:89/{}.xls'.format(xlsname))

        if datatype=='已完成超时':
            completed = YCcomplaints.select().where( (YCcomplaints.area % like) & (
                YCcomplaints.starttime >= utc_str_to_timestamp(starttime)) & (
                                                        YCcomplaints.starttime <= utc_str_to_timestamp(endtime)) & (
                                                        YCcomplaints.status == '归档') & (YCcomplaints.usetime >= 20))


            workbook_m = xlwt.Workbook(encoding='utf-8')
            xlsheet = workbook_m.add_sheet('8小时已完成超时工单', cell_overwrite_ok=True)
            xlsheet.write(0, 0, '工单平台')
            xlsheet.write(0, 1, '所属区')
            xlsheet.write(0, 2, '新增工单操作时间')
            xlsheet.write(0, 3, 'T2操作时间')
            xlsheet.write(0, 4, '处理时长')
            i = 1
            for item in completed:
                print(item.starttime,item.endtime,item.usetime)
            for item in completed:
                print ('-------------------------------',completed)
                xlsheet.write(i, 0, item.platform)
                xlsheet.write(i, 1, area)
                xlsheet.write(i, 2, utc_timestamp_to_str(item.starttime))
                xlsheet.write(i, 3, utc_timestamp_to_str(item.endtime))
                xlsheet.write(i, 4, item.usetime)
                i=i+1
            xlsname='全量工单8小时' + area + '已完成超时工单' + xlstime
            workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
            return ('down.caicool.cc:89/{}.xls'.format(xlsname))

        if datatype=='重复量':
            workbook_m = xlwt.Workbook(encoding='utf-8')
            xlsheet = workbook_m.add_sheet('24小时重复率', cell_overwrite_ok=True)
            xlsheet.write(0, 0, '工单平台')
            xlsheet.write(0, 1, '所属区')
            xlsheet.write(0, 2, '新增工单操作时间')
            xlsheet.write(0, 3, 'T2操作时间')
            xlsheet.write(0, 4, '处理时长')
            xlsname='全量工单24小时' + area + '重复量' + xlstime
            workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
            return ('down.caicool.cc:89/{}.xls'.format(xlsname))
    if choose_type=='一键报障' or '微信一键报障':
        like='%'+area+'%'
        if datatype=='未完成超时':
            print ('yes')
            unfinished = YCcomplaints.select().where((YCcomplaints.platform == 1) & (YCcomplaints.area % like) & (
            YCcomplaints.starttime >= utc_str_to_timestamp(starttime)) & (
                                                     YCcomplaints.starttime <= utc_str_to_timestamp(endtime)) & (
                                                     YCcomplaints.status != '归档') & (
                                                     YCcomplaints.timeout == '是'))
            workbook_m = xlwt.Workbook(encoding='utf-8')
            xlsheet = workbook_m.add_sheet('8小时未完成超时工单', cell_overwrite_ok=True)
            xlsheet.write(0, 0, '工单平台')
            xlsheet.write(0, 1, '所属区')
            xlsheet.write(0, 2, '新增工单操作时间')
            xlsheet.write(0, 3, 'T2操作时间')
            xlsheet.write(0, 4, '处理时长')
            i=1

            for item in unfinished:

                xlsheet.write(i,0,'一键报障')
                xlsheet.write(i,1,area)
                xlsheet.write(i,2,utc_timestamp_to_str(item.starttime))
                xlsheet.write(i,3,utc_timestamp_to_str(item.endtime))
                xlsheet.write(i,4,item.usetime)
                i = i + 1
            xlsname='8小时一键报障' + area + '未完成超时工单' + xlstime
            workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
            return ('down.caicool.cc:89/{}.xls'.format(xlsname))

        if datatype=='已完成超时':
            print ('yes')
            completed = YCcomplaints.select().where((YCcomplaints.platform == 1) & (YCcomplaints.area % like) & (
                YCcomplaints.starttime >= utc_str_to_timestamp(starttime)) & (
                                                        YCcomplaints.starttime <= utc_str_to_timestamp(endtime)) & (
                                                        YCcomplaints.status == '归档') & (YCcomplaints.usetime >= 20))


            workbook_m = xlwt.Workbook(encoding='utf-8')
            xlsheet = workbook_m.add_sheet('8小时已完成超时工单', cell_overwrite_ok=True)
            xlsheet.write(0, 0, '工单平台')
            xlsheet.write(0, 1, '所属区')
            xlsheet.write(0, 2, '新增工单操作时间')
            xlsheet.write(0, 3, 'T2操作时间')
            xlsheet.write(0, 4, '处理时长')
            i = 1

            for item in completed:
                xlsheet.write(i, 0, '一键报障')
                xlsheet.write(i, 1, area)
                xlsheet.write(i, 2, utc_timestamp_to_str(item.starttime))
                xlsheet.write(i, 3, utc_timestamp_to_str(item.endtime))
                xlsheet.write(i, 4, item.usetime)
                i = i + 1
            xlsname='8小时一键报障' + area + '已完成超时工单' + xlstime
            workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
            return ('down.caicool.cc:89/{}.xls'.format(xlsname))
        if datatype=='重复量':
            workbook_m = xlwt.Workbook(encoding='utf-8')
            xlsheet = workbook_m.add_sheet('8小时重复量', cell_overwrite_ok=True)
            xlsheet.write(0, 0, '工单平台')
            xlsheet.write(0, 1, '所属区')
            xlsheet.write(0, 2, '新增工单操作时间')
            xlsheet.write(0, 3, 'T2操作时间')
            xlsheet.write(0, 4, '处理时长')
            xlsname='8小时一键报障' + area + '重复量' + xlstime
            workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
            return ('down.caicool.cc:89/{}.xls'.format(xlsname))








def installed_export(starttime,endtime,choose_type,area,datatype):
    like="%"+area+'%'
    if choose_type=='宽带装机':
        if datatype=='已装超时量':
            data1 = YCinstalled.select().where(
                (YCinstalled.type == 1) & (YCinstalled.confirm >= utc_str_to_timestamp(starttime)) & (
                    YCinstalled.confirm <= utc_str_to_timestamp(endtime)) & (YCinstalled.areaType != '普服小区') & (
                    YCinstalled.areaType != '普遍服务'))
            loaded = data1.where(
                (YCinstalled.area % like) & (YCinstalled.confirm != 0) & (YCinstalled.timeout == '是'))
            workbook_m = xlwt.Workbook(encoding='utf-8')
            xlsheet = workbook_m.add_sheet('24小时已装超时', cell_overwrite_ok=True)
            xlsheet.write(0, 0, '所属区')
            xlsheet.write(0, 1, '工单类型')
            xlsheet.write(0, 2, '服务帐号')
            xlsheet.write(0, 3, 'PBoss地址')
            xlsheet.write(0, 4, '受理时间')

            i = 1
            for item in loaded:
                xlsheet.write(i, 0, area)
                xlsheet.write(i, 1, '宽带装机')
                xlsheet.write(i, 2, item.service)
                xlsheet.write(i, 3, item.pboos)
                xlsheet.write(i, 4, utc_timestamp_to_str(item.accept))
                i = i + 1
            xlsname='装机宽带装机' + area + '已装超时量' + xlstime
            workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
            return ('down.caicool.cc:89/{}.xls'.format(xlsname))

        if datatype=='未装超时量':
            data = YCinstalled.select().where(
                (YCinstalled.type == 1) & (YCinstalled.accept >= utc_str_to_timestamp(starttime)) & (
                    YCinstalled.accept <= utc_str_to_timestamp(endtime)) & (YCinstalled.areaType != '普服小区') & (
                    YCinstalled.areaType != '普遍服务'))
            notLoaded = data.where((YCinstalled.area % like) & (YCinstalled.confirm == 0))
            workbook_m = xlwt.Workbook(encoding='utf-8')
            xlsheet = workbook_m.add_sheet('24小时已装超时', cell_overwrite_ok=True)
            xlsheet.write(0, 0, '所属区')
            xlsheet.write(0, 1, '工单类型')
            xlsheet.write(0, 2, '服务帐号')
            xlsheet.write(0, 3, 'PBoss地址')
            xlsheet.write(0, 4, '受理时间')

            i = 1
            for item in notLoaded:
                xlsheet.write(i, 0, area)
                xlsheet.write(i, 1, '宽带装机')
                xlsheet.write(i, 2, item.service)
                xlsheet.write(i, 3, item.pboos)
                xlsheet.write(i, 4, utc_timestamp_to_str(item.accept))
                i = i + 1
            xlsname='装机宽带装机' + area + '未装超时量' + xlstime
            workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
            return ('down.caicool.cc:89/{}.xls'.format(xlsname))
        if datatype=='压单量':
            workbook_m = xlwt.Workbook(encoding='utf-8')
            xlsheet = workbook_m.add_sheet('24小时已装超时', cell_overwrite_ok=True)
            xlsheet.write(0, 0, '所属区')
            xlsheet.write(0, 1, '工单类型')
            xlsheet.write(0, 2, '服务帐号')
            xlsheet.write(0, 3, 'PBoss地址')
            xlsheet.write(0, 4, '受理时间')
            xlsname='装机宽带装机' + area + '压单量' + xlstime
            workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
            return ('down.caicool.cc:89/{}.xls'.format(xlsname))
    if choose_type=='移机装':
        if datatype=='已装超时量':
            data1 = YCinstalled.select().where(
                (YCinstalled.type == 2) & (YCinstalled.confirm >= utc_str_to_timestamp(starttime)) & (
                    YCinstalled.confirm <= utc_str_to_timestamp(endtime)) & (YCinstalled.areaType != '普服小区') & (
                    YCinstalled.areaType != '普遍服务'))
            loaded = data1.where(
                (YCinstalled.area % like) & (YCinstalled.confirm != 0) & (YCinstalled.timeout == '是'))
            workbook_m = xlwt.Workbook(encoding='utf-8')
            xlsheet = workbook_m.add_sheet('24小时已装超时', cell_overwrite_ok=True)
            xlsheet.write(0, 0, '所属区')
            xlsheet.write(0, 1, '工单类型')
            xlsheet.write(0, 2, '服务帐号')
            xlsheet.write(0, 3, 'PBoss地址')
            xlsheet.write(0, 4, '受理时间')

            i = 1
            for item in loaded:
                xlsheet.write(i, 0, area)
                xlsheet.write(i, 1, '移机装')
                xlsheet.write(i, 2, item.service)
                xlsheet.write(i, 3, item.pboos)
                xlsheet.write(i, 4, utc_timestamp_to_str(item.accept))
                i = i + 1
            xlsname='装机移机装' + area + '已装超时量' + xlstime
            workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
            return ('down.caicool.cc:89/{}.xls'.format(xlsname))

        if datatype=='未装超时量':
            data = YCinstalled.select().where(
                (YCinstalled.type == 2) & (YCinstalled.accept >= utc_str_to_timestamp(starttime)) & (
                    YCinstalled.accept <= utc_str_to_timestamp(endtime)) & (YCinstalled.areaType != '普服小区') & (
                    YCinstalled.areaType != '普遍服务'))
            notLoaded = data.where((YCinstalled.area % like) & (YCinstalled.confirm == 0))
            workbook_m = xlwt.Workbook(encoding='utf-8')
            xlsheet = workbook_m.add_sheet('24小时未装超时', cell_overwrite_ok=True)
            xlsheet.write(0, 0, '所属区')
            xlsheet.write(0, 1, '工单类型')
            xlsheet.write(0, 2, '服务帐号')
            xlsheet.write(0, 3, 'PBoss地址')
            xlsheet.write(0, 4, '受理时间')

            i = 1
            for item in notLoaded:
                xlsheet.write(i, 0, area)
                xlsheet.write(i, 1, '移机装')
                xlsheet.write(i, 2, item.service)
                xlsheet.write(i, 3, item.pboos)
                xlsheet.write(i, 4, utc_timestamp_to_str(item.accept))
                i = i + 1
            xlsname='装机移机装' + area + '未装超时量' + xlstime
            workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
            return ('down.caicool.cc:89/{}.xls'.format(xlsname))
        if datatype=='压单量':
            workbook_m = xlwt.Workbook(encoding='utf-8')
            xlsheet = workbook_m.add_sheet('压单量', cell_overwrite_ok=True)
            xlsheet.write(0, 0, '所属区')
            xlsheet.write(0, 1, '工单类型')
            xlsheet.write(0, 2, '服务帐号')
            xlsheet.write(0, 3, 'PBoss地址')
            xlsheet.write(0, 4, '受理时间')
            xlsname='装机移机装' + area + '压单量' + xlstime
            workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
            return ('down.caicool.cc:89/{}.xls'.format(xlsname))
    if choose_type=='TV单独安装':
        if datatype=='已装超时量':
            data1 = YCinstalled.select().where(
                (YCinstalled.type == 3) & (YCinstalled.confirm >= utc_str_to_timestamp(starttime)) & (
                    YCinstalled.confirm <= utc_str_to_timestamp(endtime)) & (YCinstalled.areaType != '普服小区') & (
                    YCinstalled.areaType != '普遍服务'))
            loaded = data1.where(
                (YCinstalled.area % like) & (YCinstalled.confirm != 0) & (YCinstalled.timeout == '是'))
            workbook_m = xlwt.Workbook(encoding='utf-8')
            xlsheet = workbook_m.add_sheet('24小时已装超时', cell_overwrite_ok=True)
            xlsheet.write(0, 0, '所属区')
            xlsheet.write(0, 1, '工单类型')
            xlsheet.write(0, 2, '服务帐号')
            xlsheet.write(0, 3, 'PBoss地址')
            xlsheet.write(0, 4, '受理时间')

            i = 1
            for item in loaded:
                xlsheet.write(i, 0, area)
                xlsheet.write(i, 1, 'TV单独安装')
                xlsheet.write(i, 2, item.service)
                xlsheet.write(i, 3, item.pboos)
                xlsheet.write(i, 4, utc_timestamp_to_str(item.accept))
                i = i + 1
            xlsname='装机TV单独安装' + area + '已装超时量' + xlstime
            workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
            return ('down.caicool.cc:89/{}.xls'.format(xlsname))

        if datatype=='未装超时量':
            data = YCinstalled.select().where(
                (YCinstalled.type == 3) & (YCinstalled.accept >= utc_str_to_timestamp(starttime)) & (
                    YCinstalled.accept <= utc_str_to_timestamp(endtime)) & (YCinstalled.areaType != '普服小区') & (
                    YCinstalled.areaType != '普遍服务'))
            notLoaded = data.where((YCinstalled.area % like) & (YCinstalled.confirm == 0))
            workbook_m = xlwt.Workbook(encoding='utf-8')
            xlsheet = workbook_m.add_sheet('24小时未装超时', cell_overwrite_ok=True)
            xlsheet.write(0, 0, '所属区')
            xlsheet.write(0, 1, '工单类型')
            xlsheet.write(0, 2, '服务帐号')
            xlsheet.write(0, 3, 'PBoss地址')
            xlsheet.write(0, 4, '受理时间')

            i = 1
            for item in notLoaded:
                xlsheet.write(i, 0, area)
                xlsheet.write(i, 1, 'TV单独安装')
                xlsheet.write(i, 2, item.service)
                xlsheet.write(i, 3, item.pboos)
                xlsheet.write(i, 4, utc_timestamp_to_str(item.accept))
                i = i + 1
            xlsname='装机TV单独安装' + area + '未装超时量' + xlstime
            workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
            return ('down.caicool.cc:89/{}.xls'.format(xlsname))
        if datatype=='压单量':
            workbook_m = xlwt.Workbook(encoding='utf-8')
            xlsheet = workbook_m.add_sheet('压单量', cell_overwrite_ok=True)
            xlsheet.write(0, 0, '所属区')
            xlsheet.write(0, 1, '工单类型')
            xlsheet.write(0, 2, '服务帐号')
            xlsheet.write(0, 3, 'PBoss地址')
            xlsheet.write(0, 4, '受理时间')
            xlsname='装机TV单独安装' + area + '压单量' + xlstime
            workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
            return ('down.caicool.cc:89/{}.xls'.format(xlsname))
    if choose_type=='IMS单独安装':
        if datatype=='已装超时量':
            data1 = YCinstalled.select().where(
                (YCinstalled.type == 4) & (YCinstalled.confirm >= utc_str_to_timestamp(starttime)) & (
                    YCinstalled.confirm <= utc_str_to_timestamp(endtime)) & (YCinstalled.areaType != '普服小区') & (
                    YCinstalled.areaType != '普遍服务'))
            loaded = data1.where(
                (YCinstalled.area % like) & (YCinstalled.confirm != 0) & (YCinstalled.timeout == '是'))
            workbook_m = xlwt.Workbook(encoding='utf-8')
            xlsheet = workbook_m.add_sheet('24小时已装超时', cell_overwrite_ok=True)
            xlsheet.write(0, 0, '所属区')
            xlsheet.write(0, 1, '工单类型')
            xlsheet.write(0, 2, '服务帐号')
            xlsheet.write(0, 3, 'PBoss地址')
            xlsheet.write(0, 4, '受理时间')

            i = 1
            for item in loaded:
                xlsheet.write(i, 0, area)
                xlsheet.write(i, 1, 'IMS单独安装')
                xlsheet.write(i, 2, item.service)
                xlsheet.write(i, 3, item.pboos)
                xlsheet.write(i, 4, utc_timestamp_to_str(item.accept))
                i = i + 1
            xlsname='装机IMS单独安装' + area + '已装超时量' + xlstime
            workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
            return ('down.caicool.cc:89/{}.xls'.format(xlsname))

        if datatype=='未装超时量':
            data = YCinstalled.select().where(
                (YCinstalled.type == 4) & (YCinstalled.accept >= utc_str_to_timestamp(starttime)) & (
                    YCinstalled.accept <= utc_str_to_timestamp(endtime)) & (YCinstalled.areaType != '普服小区') & (
                    YCinstalled.areaType != '普遍服务'))
            notLoaded = data.where((YCinstalled.area % like) & (YCinstalled.confirm == 0))
            workbook_m = xlwt.Workbook(encoding='utf-8')
            xlsheet = workbook_m.add_sheet('24小时未装超时', cell_overwrite_ok=True)
            xlsheet.write(0, 0, '所属区')
            xlsheet.write(0, 1, '工单类型')
            xlsheet.write(0, 2, '服务帐号')
            xlsheet.write(0, 3, 'PBoss地址')
            xlsheet.write(0, 4, '受理时间')

            i = 1
            for item in notLoaded:
                xlsheet.write(i, 0, area)
                xlsheet.write(i, 1, 'IMS单独安装')
                xlsheet.write(i, 2, item.service)
                xlsheet.write(i, 3, item.pboos)
                xlsheet.write(i, 4, utc_timestamp_to_str(item.accept))
                i = i + 1
            xlsname='装机IMS单独安装' + area + '未装超时量' + xlstime
            workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
            return ('down.caicool.cc:89/{}.xls'.format(xlsname))
        if datatype=='压单量':
            workbook_m = xlwt.Workbook(encoding='utf-8')
            xlsheet = workbook_m.add_sheet('压单量', cell_overwrite_ok=True)
            xlsheet.write(0, 0, '所属区')
            xlsheet.write(0, 1, '工单类型')
            xlsheet.write(0, 2, '服务帐号')
            xlsheet.write(0, 3, 'PBoss地址')
            xlsheet.write(0, 4, '受理时间')
            xlsname='装机IMS单独安装' + area + '压单量' + xlstime
            workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
            return ('down.caicool.cc:89/{}.xls'.format(xlsname))
    if choose_type=='全量工单':
        if datatype=='已装超时量':

            data1 = YCinstalled.select().where((YCinstalled.confirm >= utc_str_to_timestamp(starttime)) & (
                YCinstalled.confirm <= utc_str_to_timestamp(endtime)) & (YCinstalled.areaType != '普服小区') & (
                                                   YCinstalled.areaType != '普遍服务'))
            loaded = data1.where(
                (YCinstalled.area % like) & (YCinstalled.confirm != 0) & (YCinstalled.timeout == '是'))
            workbook_m = xlwt.Workbook(encoding='utf-8')
            xlsheet = workbook_m.add_sheet('24小时已装超时', cell_overwrite_ok=True)
            xlsheet.write(0, 0, '所属区')
            xlsheet.write(0, 1, '工单类型')
            xlsheet.write(0, 2, '服务帐号')
            xlsheet.write(0, 3, 'PBoss地址')
            xlsheet.write(0, 4, '受理时间')
            print (area)
            i = 1
            for item in loaded:

                xlsheet.write(i, 0, area)

                xlsheet.write(i, 1, item.type)

                xlsheet.write(i, 2, item.service)

                xlsheet.write(i, 3, item.pboos)

                xlsheet.write(i, 4, utc_timestamp_to_str(item.accept))
                i = i + 1
            xlsname='装机全量工单' + area + '已装超时量' + xlstime
            workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
            return ('down.caicool.cc:89/{}.xls'.format(xlsname))

        if datatype=='未装超时量':
            data = YCinstalled.select().where((YCinstalled.accept >= utc_str_to_timestamp(starttime)) & (
                    YCinstalled.accept <= utc_str_to_timestamp(endtime)) & (YCinstalled.areaType != '普服小区') & (
                    YCinstalled.areaType != '普遍服务'))
            notLoaded = data.where((YCinstalled.area % like) & (YCinstalled.confirm == 0))
            workbook_m = xlwt.Workbook(encoding='utf-8')
            xlsheet = workbook_m.add_sheet('24小时未装超时', cell_overwrite_ok=True)
            xlsheet.write(0, 0, '所属区')
            xlsheet.write(0, 1, '工单类型')
            xlsheet.write(0, 2, '服务帐号')
            xlsheet.write(0, 3, 'PBoss地址')
            xlsheet.write(0, 4, '受理时间')

            i = 1
            for item in notLoaded:
                xlsheet.write(i, 0, area)
                xlsheet.write(i, 1, '全量工单')
                xlsheet.write(i, 2, item.service)
                xlsheet.write(i, 3, item.pboos)
                xlsheet.write(i, 4, utc_timestamp_to_str(item.accept))
                i = i + 1
            xlsname='装机全量工单' + area + '未装超时量' + xlstime
            workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
            return ('down.caicool.cc:89/{}.xls'.format(xlsname))
        if datatype=='压单量':
            workbook_m = xlwt.Workbook(encoding='utf-8')
            xlsheet = workbook_m.add_sheet('压单量', cell_overwrite_ok=True)
            xlsheet.write(0, 0, '所属区')
            xlsheet.write(0, 1, '工单类型')
            xlsheet.write(0, 2, '服务帐号')
            xlsheet.write(0, 3, 'PBoss地址')
            xlsheet.write(0, 4, '受理时间')
            xlsname='装机全量工单' + area + '压单量' + xlstime
            workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
            return ('down.caicool.cc:89/{}.xls'.format(xlsname))

# 装机880导出报表
def installed_export_8(starttime,endtime,choose_type,area,datatype):
    like = "%" + area + '%'
    if choose_type=='宽带装机':
        if datatype=='已装超时量':
            data1 = YCinstalled.select().where(
                (YCinstalled.type == 1) & (YCinstalled.confirm >= utc_str_to_timestamp(starttime)) & (
                    YCinstalled.confirm <= utc_str_to_timestamp(endtime)) & (YCinstalled.areaType != '普服小区') & (
                    YCinstalled.areaType != '普遍服务'))
            loaded = data1.where(
                (YCinstalled.area % like) & (YCinstalled.confirm != 0) & (
                    YCinstalled.confirm - YCinstalled.accept >= 20 * 60 * 60))
            workbook_m = xlwt.Workbook(encoding='utf-8')
            xlsheet = workbook_m.add_sheet('8小时已装超时', cell_overwrite_ok=True)
            xlsheet.write(0, 0, '所属区')
            xlsheet.write(0, 1, '工单类型')
            xlsheet.write(0, 2, '服务帐号')
            xlsheet.write(0, 3, 'PBoss地址')
            xlsheet.write(0, 4, '受理时间')

            i = 1
            for item in loaded:
                xlsheet.write(i, 0, area)
                xlsheet.write(i, 1, '宽带装机')
                xlsheet.write(i, 2, item.service)
                xlsheet.write(i, 3, item.pboos)
                xlsheet.write(i, 4, utc_timestamp_to_str(item.accept))
                i = i + 1
            xlsname='装机宽带装机880' + area + '已装超时量' + xlstime
            workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
            return ('down.caicool.cc:89/{}.xls'.format(xlsname))

        if datatype=='未装超时量':
            data = YCinstalled.select().where(
                (YCinstalled.type == 1) & (YCinstalled.accept >= utc_str_to_timestamp(starttime)) & (
                    YCinstalled.accept <= utc_str_to_timestamp(endtime)) & (YCinstalled.areaType != '普服小区') & (
                    YCinstalled.areaType != '普遍服务'))
            notLoaded = data.where((YCinstalled.area % like) & (YCinstalled.confirm == 0))
            workbook_m = xlwt.Workbook(encoding='utf-8')
            xlsheet = workbook_m.add_sheet('8小时已装超时', cell_overwrite_ok=True)
            xlsheet.write(0, 0, '所属区')
            xlsheet.write(0, 1, '工单类型')
            xlsheet.write(0, 2, '服务帐号')
            xlsheet.write(0, 3, 'PBoss地址')
            xlsheet.write(0, 4, '受理时间')

            i = 1
            for item in notLoaded:
                xlsheet.write(i, 0, area)
                xlsheet.write(i, 1, '宽带装机')
                xlsheet.write(i, 2, item.service)
                xlsheet.write(i, 3, item.pboos)
                xlsheet.write(i, 4, utc_timestamp_to_str(item.accept))
                i = i + 1
            xlsname='装机宽带装机880' + area + '未装超时量' + xlstime
            workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
            return ('down.caicool.cc:89/{}.xls'.format(xlsname))
        if datatype=='压单量':
            workbook_m = xlwt.Workbook(encoding='utf-8')
            xlsheet = workbook_m.add_sheet('压单量', cell_overwrite_ok=True)
            xlsheet.write(0, 0, '所属区')
            xlsheet.write(0, 1, '工单类型')
            xlsheet.write(0, 2, '服务帐号')
            xlsheet.write(0, 3, 'PBoss地址')
            xlsheet.write(0, 4, '受理时间')
            xlsname='装机宽带装机' + area + '压单量' + xlstime
            workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
            return ('down.caicool.cc:89/{}.xls'.format(xlsname))
    if choose_type=='移机装':
        if datatype=='已装超时量':
            data1 = YCinstalled.select().where(
                (YCinstalled.type == 2) & (YCinstalled.confirm >= utc_str_to_timestamp(starttime)) & (
                    YCinstalled.confirm <= utc_str_to_timestamp(endtime)) & (YCinstalled.areaType != '普服小区') & (
                    YCinstalled.areaType != '普遍服务'))
            loaded = data1.where(
                (YCinstalled.area % like) & (YCinstalled.confirm != 0) & (
                    YCinstalled.confirm - YCinstalled.accept >= 20 * 60 * 60))
            workbook_m = xlwt.Workbook(encoding='utf-8')
            xlsheet = workbook_m.add_sheet('8小时已装超时', cell_overwrite_ok=True)
            xlsheet.write(0, 0, '所属区')
            xlsheet.write(0, 1, '工单类型')
            xlsheet.write(0, 2, '服务帐号')
            xlsheet.write(0, 3, 'PBoss地址')
            xlsheet.write(0, 4, '受理时间')

            i = 1
            for item in loaded:
                xlsheet.write(i, 0, area)
                xlsheet.write(i, 1, '移机装')
                xlsheet.write(i, 2, item.service)
                xlsheet.write(i, 3, item.pboos)
                xlsheet.write(i, 4, utc_timestamp_to_str(item.accept))
                i = i + 1
            xlsname='装机移机装880' + area + '已装超时量' + xlstime
            workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
            return ('down.caicool.cc:89/{}.xls'.format(xlsname))

        if datatype=='未装超时量':
            data = YCinstalled.select().where(
                (YCinstalled.type == 2) & (YCinstalled.accept >= utc_str_to_timestamp(starttime)) & (
                    YCinstalled.accept <= utc_str_to_timestamp(endtime)) & (YCinstalled.areaType != '普服小区') & (
                    YCinstalled.areaType != '普遍服务'))
            notLoaded = data.where((YCinstalled.area % like) & (YCinstalled.confirm == 0))
            workbook_m = xlwt.Workbook(encoding='utf-8')
            xlsheet = workbook_m.add_sheet('8小时未装超时', cell_overwrite_ok=True)
            xlsheet.write(0, 0, '所属区')
            xlsheet.write(0, 1, '工单类型')
            xlsheet.write(0, 2, '服务帐号')
            xlsheet.write(0, 3, 'PBoss地址')
            xlsheet.write(0, 4, '受理时间')

            i = 1
            for item in notLoaded:
                xlsheet.write(i, 0, '移机装')
                xlsheet.write(i, 1, area)
                xlsheet.write(i, 2, item.service)
                xlsheet.write(i, 3, item.pboos)
                xlsheet.write(i, 4, utc_timestamp_to_str(item.accept))
                i = i + 1
            xlsname='装机移机装880' + area + '未装超时量' + xlstime
            workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
            return ('down.caicool.cc:89/{}.xls'.format(xlsname))
        if datatype=='压单量':
            workbook_m = xlwt.Workbook(encoding='utf-8')
            xlsheet = workbook_m.add_sheet('压单量', cell_overwrite_ok=True)
            xlsheet.write(0, 0, '所属区')
            xlsheet.write(0, 1, '工单类型')
            xlsheet.write(0, 2, '服务帐号')
            xlsheet.write(0, 3, 'PBoss地址')
            xlsheet.write(0, 4, '受理时间')
            xlsname='装机移机装880' + area + '压单量' + xlstime
            workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
            return ('down.caicool.cc:89/{}.xls'.format(xlsname))
    if choose_type=='TV单独安装':
        if datatype=='已装超时量':
            data1 = YCinstalled.select().where(
                (YCinstalled.type == 3) & (YCinstalled.confirm >= utc_str_to_timestamp(starttime)) & (
                    YCinstalled.confirm <= utc_str_to_timestamp(endtime)) & (YCinstalled.areaType != '普服小区') & (
                    YCinstalled.areaType != '普遍服务'))
            loaded = data1.where(
                (YCinstalled.area % like) & (YCinstalled.confirm != 0) & (
                    YCinstalled.confirm - YCinstalled.accept >= 20 * 60 * 60))
            workbook_m = xlwt.Workbook(encoding='utf-8')
            xlsheet = workbook_m.add_sheet('8小时已装超时', cell_overwrite_ok=True)
            xlsheet.write(0, 0, '所属区')
            xlsheet.write(0, 1, '工单类型')
            xlsheet.write(0, 2, '服务帐号')
            xlsheet.write(0, 3, 'PBoss地址')
            xlsheet.write(0, 4, '受理时间')

            i = 1
            for item in loaded:
                xlsheet.write(i, 0, area)
                xlsheet.write(i, 1, 'TV单独安装')
                xlsheet.write(i, 2, item.service)
                xlsheet.write(i, 3, item.pboos)
                xlsheet.write(i, 4, utc_timestamp_to_str(item.accept))
                i = i + 1
            xlsname='装机TV单独安装880' + area + '已装超时量' + xlstime
            workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
            return ('down.caicool.cc:89/{}.xls'.format(xlsname))

        if datatype=='未装超时量':
            data = YCinstalled.select().where(
                (YCinstalled.type == 3) & (YCinstalled.accept >= utc_str_to_timestamp(starttime)) & (
                    YCinstalled.accept <= utc_str_to_timestamp(endtime)) & (YCinstalled.areaType != '普服小区') & (
                    YCinstalled.areaType != '普遍服务'))
            notLoaded = data.where((YCinstalled.area % like) & (YCinstalled.confirm == 0))
            workbook_m = xlwt.Workbook(encoding='utf-8')
            xlsheet = workbook_m.add_sheet('24小时未装超时', cell_overwrite_ok=True)
            xlsheet.write(0, 0, '所属区')
            xlsheet.write(0, 1, '工单类型')
            xlsheet.write(0, 2, '服务帐号')
            xlsheet.write(0, 3, 'PBoss地址')
            xlsheet.write(0, 4, '受理时间')

            i = 1
            for item in notLoaded:
                xlsheet.write(i, 0, area)
                xlsheet.write(i, 1, 'TV单独安装')
                xlsheet.write(i, 2, item.service)
                xlsheet.write(i, 3, item.pboos)
                xlsheet.write(i, 4, utc_timestamp_to_str(item.accept))
                i = i + 1
            xlsname='装机TV单独安装880' + area + '未装超时量' + xlstime
            workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
            return ('down.caicool.cc:89/{}.xls'.format(xlsname))
        if datatype=='压单量':
            workbook_m = xlwt.Workbook(encoding='utf-8')
            xlsheet = workbook_m.add_sheet('压单量', cell_overwrite_ok=True)
            xlsheet.write(0, 0, '所属区')
            xlsheet.write(0, 1, '工单类型')
            xlsheet.write(0, 2, '服务帐号')
            xlsheet.write(0, 3, 'PBoss地址')
            xlsheet.write(0, 4, '受理时间')
            xlsname='装机TV单独安装880' + area + '压单量' + xlstime
            workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
            return ('down.caicool.cc:89/{}.xls'.format(xlsname))
    if choose_type=='IMS单独安装':
        if datatype=='已装超时量':
            data1 = YCinstalled.select().where(
                (YCinstalled.type == 4) & (YCinstalled.confirm >= utc_str_to_timestamp(starttime)) & (
                    YCinstalled.confirm <= utc_str_to_timestamp(endtime)) & (YCinstalled.areaType != '普服小区') & (
                    YCinstalled.areaType != '普遍服务'))
            loaded = data1.where(
                (YCinstalled.area % like) & (YCinstalled.confirm != 0) & (
                    YCinstalled.confirm - YCinstalled.accept >= 20 * 60 * 60))
            workbook_m = xlwt.Workbook(encoding='utf-8')
            xlsheet = workbook_m.add_sheet('8小时已装超时', cell_overwrite_ok=True)
            xlsheet.write(0, 0, '所属区')
            xlsheet.write(0, 1, '工单类型')
            xlsheet.write(0, 2, '服务帐号')
            xlsheet.write(0, 3, 'PBoss地址')
            xlsheet.write(0, 4, '受理时间')

            i = 1
            for item in loaded:
                xlsheet.write(i, 0, area)
                xlsheet.write(i, 1, 'IMS单独安装')
                xlsheet.write(i, 2, item.service)
                xlsheet.write(i, 3, item.pboos)
                xlsheet.write(i, 4, item.accept)
                i = i + 1
            xlsname='装机IMS单独安装880' + area + '已装超时量' + xlstime
            workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
            return ('down.caicool.cc:89/{}.xls'.format(xlsname))

        if datatype=='未装超时量':
            data = YCinstalled.select().where(
                (YCinstalled.type == 4) & (YCinstalled.accept >= utc_str_to_timestamp(starttime)) & (
                    YCinstalled.accept <= utc_str_to_timestamp(endtime)) & (YCinstalled.areaType != '普服小区') & (
                    YCinstalled.areaType != '普遍服务'))
            notLoaded = data.where((YCinstalled.area % like) & (YCinstalled.confirm == 0))
            workbook_m = xlwt.Workbook(encoding='utf-8')
            xlsheet = workbook_m.add_sheet('8小时未装超时', cell_overwrite_ok=True)
            xlsheet.write(0, 0, '所属区')
            xlsheet.write(0, 1, '工单类型')
            xlsheet.write(0, 2, '服务帐号')
            xlsheet.write(0, 3, 'PBoss地址')
            xlsheet.write(0, 4, '受理时间')

            i = 1
            for item in notLoaded:
                xlsheet.write(i, 0, area)
                xlsheet.write(i, 1, 'IMS单独安装')
                xlsheet.write(i, 2, item.service)
                xlsheet.write(i, 3, item.pboos)
                xlsheet.write(i, 4, utc_timestamp_to_str(item.accept))
                i = i + 1
            xlsname='装机IMS单独安装880' + area + '未装超时量' + xlstime
            workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
            return ('down.caicool.cc:89/{}.xls'.format(xlsname))
        if datatype=='压单量':
            workbook_m = xlwt.Workbook(encoding='utf-8')
            xlsheet = workbook_m.add_sheet('压单量', cell_overwrite_ok=True)
            xlsheet.write(0, 0, '所属区')
            xlsheet.write(0, 1, '工单类型')
            xlsheet.write(0, 2, '服务帐号')
            xlsheet.write(0, 3, 'PBoss地址')
            xlsheet.write(0, 4, '受理时间')
            xlsname='装机IMS单独安装880' + area + '压单量' + xlstime
            workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
            return ('down.caicool.cc:89/{}.xls'.format(xlsname))
    if choose_type=='全量工单':
        if datatype=='已装超时量':
            data1 = YCinstalled.select().where((YCinstalled.confirm >= utc_str_to_timestamp(starttime)) & (
                    YCinstalled.confirm <= utc_str_to_timestamp(endtime)) & (YCinstalled.areaType != '普服小区') & (
                    YCinstalled.areaType != '普遍服务'))
            loaded = data1.where(
                (YCinstalled.area % like) & (YCinstalled.confirm != 0) & (YCinstalled.confirm - YCinstalled.accept >= 20 * 60 * 60))
            workbook_m = xlwt.Workbook(encoding='utf-8')
            xlsheet = workbook_m.add_sheet('8小时已装超时', cell_overwrite_ok=True)
            xlsheet.write(0, 0, '所属区')
            xlsheet.write(0, 1, '工单类型')
            xlsheet.write(0, 2, '服务帐号')
            xlsheet.write(0, 3, 'PBoss地址')
            xlsheet.write(0, 4, '受理时间')

            i = 1
            for item in loaded:
                xlsheet.write(i, 0, area)
                xlsheet.write(i, 1, item.type)
                xlsheet.write(i, 2, item.service)
                xlsheet.write(i, 3, item.pboos)
                xlsheet.write(i, 4, utc_timestamp_to_str(item.accept))
                i = i + 1
            xlsname='装机全量工单880' + area + '已装超时量' + xlstime
            workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
            return ('down.caicool.cc:89/{}.xls'.format(xlsname))

        if datatype=='未装超时量':
            data = YCinstalled.select().where((YCinstalled.accept >= utc_str_to_timestamp(starttime)) & (
                    YCinstalled.accept <= utc_str_to_timestamp(endtime)) & (YCinstalled.areaType != '普服小区') & (
                    YCinstalled.areaType != '普遍服务'))
            notLoaded = data.where((YCinstalled.area % like) & (YCinstalled.confirm == 0))
            workbook_m = xlwt.Workbook(encoding='utf-8')
            xlsheet = workbook_m.add_sheet('8小时未装超时', cell_overwrite_ok=True)
            xlsheet.write(0, 0, '所属区')
            xlsheet.write(0, 1, '工单类型')
            xlsheet.write(0, 2, '服务帐号')
            xlsheet.write(0, 3, 'PBoss地址')
            xlsheet.write(0, 4, '受理时间')

            i = 1
            for item in notLoaded:
                xlsheet.write(i, 0, area)
                xlsheet.write(i, 1, item.type)
                xlsheet.write(i, 2, item.service)
                xlsheet.write(i, 3, item.pboos)
                xlsheet.write(i, 4, utc_timestamp_to_str(item.accept))
                i = i + 1
            xlsname='装机全量工单880' + area + datatype + xlstime
            workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
            return ('down.caicool.cc:89/{}.xls'.format(xlsname))
        if datatype=='压单量':
            workbook_m = xlwt.Workbook(encoding='utf-8')
            xlsheet = workbook_m.add_sheet('8小时压单量', cell_overwrite_ok=True)
            xlsheet.write(0, 0, '所属区')
            xlsheet.write(0, 1, '工单类型')
            xlsheet.write(0, 2, '服务帐号')
            xlsheet.write(0, 3, 'PBoss地址')
            xlsheet.write(0, 4, '受理时间')
            xlsname='装机全量工单880' + area + '压单量' + xlstime
            workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
            return ('down.caicool.cc:89/{}.xls'.format(xlsname))


#首次联系用户及时率(投诉)
def first_export(starttime,endtime,area,datatype):
    like='%'+area+'%'
    if datatype=='2小时内':
        data = YCcomplaints.select().where((YCcomplaints.platform == 2) & (YCcomplaints.area % like) & (
            YCcomplaints.starttime >= utc_str_to_timestamp(starttime)) & (
                                               YCcomplaints.starttime <= utc_str_to_timestamp(endtime)))
        acceptance = YCcomplaints.select().where((YCcomplaints.platform == 2) & (YCcomplaints.area % like) & (
            YCcomplaints.starttime >= utc_str_to_timestamp(starttime)) & (
                                                     YCcomplaints.starttime <= utc_str_to_timestamp(endtime))).count()

        oneToTwo = data.where((YCcomplaints.fristtime - YCcomplaints.starttime) / 3600 <= 2)

        workbook_m = xlwt.Workbook(encoding='utf-8')
        xlsheet = workbook_m.add_sheet('首次联系用户及时率2小时内', cell_overwrite_ok=True)
        xlsheet.write(0, 0, '所属区')
        xlsheet.write(0, 1, '工单类型')
        xlsheet.write(0, 2, '工单流水号')
        xlsheet.write(0, 3, '首次联系用户时间')
        xlsheet.write(0, 4, '联系人电话')
        xlsheet.write(0, 5, '联系人')
        xlsheet.write(0, 6, '投诉地址')
        xlsheet.write(0, 7, '新增工单时间')

        i = 1
        for item in oneToTwo:
            xlsheet.write(i, 0, area)
            xlsheet.write(i, 1, 'EMOS')
            xlsheet.write(i, 2, item.serial)
            xlsheet.write(i, 3, item.fristtime)
            xlsheet.write(i, 4,  item.phone)
            xlsheet.write(i, 5,  item.contacts)
            xlsheet.write(i, 6,  item.tsaddress)
            xlsheet.write(i, 7,  item.starttime)
            i = i + 1
        xlsname='首次联系用户及时率' + area + '2小时内' + xlstime
        workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
        return ('down.caicool.cc:89/{}.xls'.format(xlsname))
    if datatype=='2-10小时':
        data = YCcomplaints.select().where((YCcomplaints.platform == 2) & (YCcomplaints.area % like) & (
            YCcomplaints.starttime >= utc_str_to_timestamp(starttime)) & (
                                               YCcomplaints.starttime <= utc_str_to_timestamp(endtime)))
        acceptance = YCcomplaints.select().where((YCcomplaints.platform == 2) & (YCcomplaints.area % like) & (
            YCcomplaints.starttime >= utc_str_to_timestamp(starttime)) & (
                                                     YCcomplaints.starttime <= utc_str_to_timestamp(endtime))).count()

        twoToTen = data.where(((YCcomplaints.fristtime - YCcomplaints.starttime) / 3600 > 2) & (
        (YCcomplaints.fristtime - YCcomplaints.starttime) / 3600 <= 10))

        workbook_m = xlwt.Workbook(encoding='utf-8')
        xlsheet = workbook_m.add_sheet('首次联系用户及时率2-10小时', cell_overwrite_ok=True)
        xlsheet.write(0, 0, '所属区')
        xlsheet.write(0, 1, '工单类型')
        xlsheet.write(0, 2, '工单流水号')
        xlsheet.write(0, 3, '首次联系用户时间')
        xlsheet.write(0, 4, '联系人电话')
        xlsheet.write(0, 5, '联系人')
        xlsheet.write(0, 6, '投诉地址')
        xlsheet.write(0, 7, '新增工单时间')

        i = 1
        for item in twoToTen:
            xlsheet.write(i, 0, area)
            xlsheet.write(i, 1, 'EMOS')
            xlsheet.write(i, 2, item.serial)
            xlsheet.write(i, 3, item.fristtime)
            xlsheet.write(i, 4, item.phone)
            xlsheet.write(i, 5, item.contacts)
            xlsheet.write(i, 6, item.tsaddress)
            xlsheet.write(i, 7, item.starttime)
            i = i + 1
        xlsname='首次联系用户及时率' + area + '2-10小时' + xlstime
        workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
        return ('down.caicool.cc:89/{}.xls'.format(xlsname))
    if datatype=='10-24小时':
        data = YCcomplaints.select().where((YCcomplaints.platform == 2) & (YCcomplaints.area % like) & (
            YCcomplaints.starttime >= utc_str_to_timestamp(starttime)) & (
                                               YCcomplaints.starttime <= utc_str_to_timestamp(endtime)))
        acceptance = YCcomplaints.select().where((YCcomplaints.platform == 2) & (YCcomplaints.area % like) & (
            YCcomplaints.starttime >= utc_str_to_timestamp(starttime)) & (
                                                     YCcomplaints.starttime <= utc_str_to_timestamp(endtime))).count()

        tenToTwentyFour = data.where(((YCcomplaints.fristtime - YCcomplaints.starttime) / 3600 > 10) & (
        (YCcomplaints.fristtime - YCcomplaints.starttime) / 3600 <= 24))

        workbook_m = xlwt.Workbook(encoding='utf-8')
        xlsheet = workbook_m.add_sheet('首次联系用户及时率10-24小时', cell_overwrite_ok=True)
        xlsheet.write(0, 0, '所属区')
        xlsheet.write(0, 1, '工单类型')
        xlsheet.write(0, 2, '工单流水号')
        xlsheet.write(0, 3, '首次联系用户时间')
        xlsheet.write(0, 4, '联系人电话')
        xlsheet.write(0, 5, '联系人')
        xlsheet.write(0, 6, '投诉地址')
        xlsheet.write(0, 7, '新增工单时间')

        i = 1
        for item in tenToTwentyFour:
            xlsheet.write(i, 0, area)
            xlsheet.write(i, 1, 'EMOS')
            xlsheet.write(i, 2, item.serial)
            xlsheet.write(i, 3, item.fristtime)
            xlsheet.write(i, 4, item.phone)
            xlsheet.write(i, 5, item.contacts)
            xlsheet.write(i, 6, item.tsaddress)
            xlsheet.write(i, 7, item.starttime)
            i = i + 1
        xlsname='首次联系用户及时率' + area + '10-24小时' + xlstime
        workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
        return ('down.caicool.cc:89/{}.xls'.format(xlsname))
    if datatype=='超24小时':
        data = YCcomplaints.select().where((YCcomplaints.platform == 2) & (YCcomplaints.area % like) & (
            YCcomplaints.starttime >= utc_str_to_timestamp(starttime)) & (
                                               YCcomplaints.starttime <= utc_str_to_timestamp(endtime)))
        acceptance = YCcomplaints.select().where((YCcomplaints.platform == 2) & (YCcomplaints.area % like) & (
            YCcomplaints.starttime >= utc_str_to_timestamp(starttime)) & (
                                                     YCcomplaints.starttime <= utc_str_to_timestamp(endtime))).count()

        twentfour = data.where((YCcomplaints.fristtime - YCcomplaints.starttime) / 3600 > 24)

        workbook_m = xlwt.Workbook(encoding='utf-8')
        xlsheet = workbook_m.add_sheet('首次联系用户及时率超24小时', cell_overwrite_ok=True)
        xlsheet.write(0, 0, '所属区')
        xlsheet.write(0, 1, '工单类型')
        xlsheet.write(0, 2, '工单流水号')
        xlsheet.write(0, 3, '首次联系用户时间')
        xlsheet.write(0, 4, '联系人电话')
        xlsheet.write(0, 5, '联系人')
        xlsheet.write(0, 6, '投诉地址')
        xlsheet.write(0, 7, '新增工单时间')

        i = 1
        for item in twentfour:
            xlsheet.write(i, 0, area)
            xlsheet.write(i, 1, 'EMOS')
            xlsheet.write(i, 2, item.serial)
            xlsheet.write(i, 3, item.fristtime)
            xlsheet.write(i, 4, item.phone)
            xlsheet.write(i, 5, item.contacts)
            xlsheet.write(i, 6, item.tsaddress)
            xlsheet.write(i, 7, item.starttime)
            i = i + 1
        xlsname='首次联系用户及时率' + area + '超24小时' + xlstime
        workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
        return ('down.caicool.cc:89/{}.xls'.format(xlsname))
# 超时未回复（投诉）
def outexport(starttime,endtime):
    data = YCcomplaints.select().where(
        (YCcomplaints.starttime >= utc_str_to_timestamp(starttime)) & (YCcomplaints.status == '运行中') & (
        (YCcomplaints.endtime - YCcomplaints.starttime) >= 24 * 3600) & (
            YCcomplaints.endtime < utc_str_to_timestamp(endtime))).order_by(YCcomplaints.usetime.desc())
    workbook_m = xlwt.Workbook(encoding='utf-8')
    xlsheet = workbook_m.add_sheet('首次联系用户及时率2小时内', cell_overwrite_ok=True)
    xlsheet.write(0, 0, '所属区')
    xlsheet.write(0, 1, '工单类型')
    xlsheet.write(0, 2, '工单流水号')
    xlsheet.write(0, 3, '首次联系用户时间')
    xlsheet.write(0, 4, '联系人电话')
    xlsheet.write(0, 5, '联系人')
    xlsheet.write(0, 6, '投诉地址')
    xlsheet.write(0, 7, '新增工单时间')

    i = 1
    for item in data:
        xlsheet.write(i, 0, item.area)
        xlsheet.write(i, 1, item.platform)
        xlsheet.write(i, 2, item.serial)
        xlsheet.write(i, 3, item.fristtime)
        xlsheet.write(i, 4, item.phone)
        xlsheet.write(i, 5, item.contacts)
        xlsheet.write(i, 6, item.tsaddress)
        xlsheet.write(i, 7, item.starttime)
        i = i + 1
    xlsname = '超时未回复'+ xlstime
    workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
    return ('down.caicool.cc:89/{}.xls'.format(xlsname))

#接单及时率(装机)
def accept_export(starttime,endtime,choose_type,area,datatype):
    like = '%' + area + '%'

    if choose_type=='宽带装机':
        dataall = YCinstalled.select().where((YCinstalled.area % like) &(YCinstalled.type == 1) & (YCinstalled.accept >= utc_str_to_timestamp(starttime)) & (YCinstalled.confirm <= utc_str_to_timestamp(endtime)))

        if datatype == '2小时内':
            oneToTwo=dataall.where((YCinstalled.orders - YCinstalled.accept) / 3600 <= 2)
            workbook_m = xlwt.Workbook(encoding='utf-8')
            xlsheet = workbook_m.add_sheet('接单及时率2小时内', cell_overwrite_ok=True)
            xlsheet.write(0, 0, '所属区')
            xlsheet.write(0, 1, '工单类型')
            xlsheet.write(0, 2, '服务帐号')
            xlsheet.write(0, 3, 'PBoss地址')
            xlsheet.write(0, 4, '受理时间')
            xlsheet.write(0, 5, '接单时间')

            i = 1
            for item in oneToTwo:
                xlsheet.write(i, 0, area)
                xlsheet.write(i, 1, choose_type)
                xlsheet.write(i, 2, item.service)
                xlsheet.write(i, 3, item.pboos)
                xlsheet.write(i, 4, utc_timestamp_to_str(item.accept))
                xlsheet.write(i, 5, utc_timestamp_to_str(item.orders))
                i = i + 1
            xlsname='接单及时率' + choose_type+ area + datatype + xlstime
            workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
            return ('down.caicool.cc:89/{}.xls'.format(xlsname))
        if datatype == '2-10小时':
            twoToTen = dataall.where(((YCinstalled.orders - YCinstalled.accept) / 3600 > 2) & (
            (YCinstalled.orders - YCinstalled.accept) / 3600 <= 10))
            workbook_m = xlwt.Workbook(encoding='utf-8')
            xlsheet = workbook_m.add_sheet('接单及时率2-10小时', cell_overwrite_ok=True)
            xlsheet.write(0, 0, '所属区')
            xlsheet.write(0, 1, '工单类型')
            xlsheet.write(0, 2, '服务帐号')
            xlsheet.write(0, 3, 'PBoss地址')
            xlsheet.write(0, 4, '受理时间')
            xlsheet.write(0, 5, '接单时间')

            i = 1
            for item in twoToTen:
                xlsheet.write(i, 0, area)
                xlsheet.write(i, 1, choose_type)
                xlsheet.write(i, 2, item.service)
                xlsheet.write(i, 3, item.pboos)
                xlsheet.write(i, 4, utc_timestamp_to_str(item.accept))
                xlsheet.write(i, 5, utc_timestamp_to_str(item.orders))
                i = i + 1
            xlsname='接单及时率' + choose_type+ area + datatype + xlstime
            workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
            return ('down.caicool.cc:89/{}.xls'.format(xlsname))
        if datatype == '10-24小时':
            tenToTwentyFour = dataall.where(((YCinstalled.orders - YCinstalled.accept) / 3600 > 10) & (
                (YCinstalled.orders - YCinstalled.accept) / 3600 <= 24))
            workbook_m = xlwt.Workbook(encoding='utf-8')
            xlsheet = workbook_m.add_sheet('接单及时率10-24小时', cell_overwrite_ok=True)
            xlsheet.write(0, 0, '所属区')
            xlsheet.write(0, 1, '工单类型')
            xlsheet.write(0, 2, '服务帐号')
            xlsheet.write(0, 3, 'PBoss地址')
            xlsheet.write(0, 4, '受理时间')
            xlsheet.write(0, 5, '接单时间')

            i = 1
            for item in tenToTwentyFour:
                xlsheet.write(i, 0, area)
                xlsheet.write(i, 1, choose_type)
                xlsheet.write(i, 2, item.service)
                xlsheet.write(i, 3, item.pboos)
                xlsheet.write(i, 4, utc_timestamp_to_str(item.accept))
                xlsheet.write(i, 5, utc_timestamp_to_str(item.orders))
                i = i + 1
            xlsname='接单及时率' + choose_type+ area + datatype + xlstime
            workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
            return ('down.caicool.cc:89/{}.xls'.format(xlsname))
        if datatype == '超24小时':
            twentyFour = dataall.where((YCinstalled.orders - YCinstalled.accept) / 3600 > 24)
            workbook_m = xlwt.Workbook(encoding='utf-8')
            xlsheet = workbook_m.add_sheet('接单及时率超24小时', cell_overwrite_ok=True)
            xlsheet.write(0, 0, '所属区')
            xlsheet.write(0, 1, '工单类型')
            xlsheet.write(0, 2, '服务帐号')
            xlsheet.write(0, 3, 'PBoss地址')
            xlsheet.write(0, 4, '受理时间')
            xlsheet.write(0, 5, '接单时间')

            i = 1
            for item in twentyFour:
                xlsheet.write(i, 0, area)
                xlsheet.write(i, 1, choose_type)
                xlsheet.write(i, 2, item.service)
                xlsheet.write(i, 3, item.pboos)
                xlsheet.write(i, 4, utc_timestamp_to_str(item.accept))
                xlsheet.write(i, 5, utc_timestamp_to_str(item.orders))
                i = i + 1
            xlsname='接单及时率' + choose_type+ area + datatype + xlstime
            workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
            return ('down.caicool.cc:89/{}.xls'.format(xlsname))
    if choose_type=='和tv':
        dataall = YCinstalled.select().where((YCinstalled.area % like) & (YCinstalled.type == 3) & (
        YCinstalled.accept >= utc_str_to_timestamp(starttime)) & (YCinstalled.confirm <= utc_str_to_timestamp(endtime)))

        if datatype == '2小时内':
            oneToTwo = dataall.where((YCinstalled.orders - YCinstalled.accept) / 3600 <= 2)
            workbook_m = xlwt.Workbook(encoding='utf-8')
            xlsheet = workbook_m.add_sheet('接单及时率2小时内', cell_overwrite_ok=True)
            xlsheet.write(0, 0, '所属区')
            xlsheet.write(0, 1, '工单类型')
            xlsheet.write(0, 2, '服务帐号')
            xlsheet.write(0, 3, 'PBoss地址')
            xlsheet.write(0, 4, '受理时间')
            xlsheet.write(0, 5, '接单时间')

            i = 1
            for item in oneToTwo:
                xlsheet.write(i, 0, area)
                xlsheet.write(i, 1, choose_type)
                xlsheet.write(i, 2, item.service)
                xlsheet.write(i, 3, item.pboos)
                xlsheet.write(i, 4, utc_timestamp_to_str(item.accept))
                xlsheet.write(i, 5, utc_timestamp_to_str(item.orders))
                i = i + 1
            xlsname='接单及时率' + choose_type + area + datatype + xlstime
            workbook_m.save(
                '/var/www/downfile/{}.xls'.format(xlsname))
            return ('down.caicool.cc:89/{}.xls'.format(xlsname))
        if datatype == '2-10小时':
            twoToTen = dataall.where(((YCinstalled.orders - YCinstalled.accept) / 3600 > 2) & (
                (YCinstalled.orders - YCinstalled.accept) / 3600 <= 10))
            workbook_m = xlwt.Workbook(encoding='utf-8')
            xlsheet = workbook_m.add_sheet('接单及时率2-10小时', cell_overwrite_ok=True)
            xlsheet.write(0, 0, '所属区')
            xlsheet.write(0, 1, '工单类型')
            xlsheet.write(0, 2, '服务帐号')
            xlsheet.write(0, 3, 'PBoss地址')
            xlsheet.write(0, 4, '受理时间')
            xlsheet.write(0, 5, '接单时间')

            i = 1
            for item in twoToTen:
                xlsheet.write(i, 0, area)
                xlsheet.write(i, 1, choose_type)
                xlsheet.write(i, 2, item.service)
                xlsheet.write(i, 3, item.pboos)
                xlsheet.write(i, 4, utc_timestamp_to_str(item.accept))
                xlsheet.write(i, 5, utc_timestamp_to_str(item.orders))
                i = i + 1
            xlsname='接单及时率' + choose_type + area + datatype + xlstime
            workbook_m.save(
                '/var/www/downfile/{}.xls'.format(xlsname))
            return ('down.caicool.cc:89/{}.xls'.format(xlsname))
        if datatype == '10-24小时':
            tenToTwentyFour = dataall.where(((YCinstalled.orders - YCinstalled.accept) / 3600 > 10) & (
                (YCinstalled.orders - YCinstalled.accept) / 3600 <= 24))
            workbook_m = xlwt.Workbook(encoding='utf-8')
            xlsheet = workbook_m.add_sheet('接单及时率10-24小时', cell_overwrite_ok=True)
            xlsheet.write(0, 0, '所属区')
            xlsheet.write(0, 1, '工单类型')
            xlsheet.write(0, 2, '服务帐号')
            xlsheet.write(0, 3, 'PBoss地址')
            xlsheet.write(0, 4, '受理时间')
            xlsheet.write(0, 5, '接单时间')

            i = 1
            for item in tenToTwentyFour:
                xlsheet.write(i, 0, area)
                xlsheet.write(i, 1, choose_type)
                xlsheet.write(i, 2, item.service)
                xlsheet.write(i, 3, item.pboos)
                xlsheet.write(i, 4, utc_timestamp_to_str(item.accept))
                xlsheet.write(i, 5, utc_timestamp_to_str(item.orders))
                i = i + 1
            xlsname='接单及时率' + choose_type + area + datatype + xlstime
            workbook_m.save(
                '/var/www/downfile/{}.xls'.format(xlsname))
            return ('down.caicool.cc:89/{}.xls'.format(xlsname))
        if datatype == '超24小时':
            twentyFour = dataall.where((YCinstalled.orders - YCinstalled.accept) / 3600 > 24)
            workbook_m = xlwt.Workbook(encoding='utf-8')
            xlsheet = workbook_m.add_sheet('接单及时率超24小时', cell_overwrite_ok=True)
            xlsheet.write(0, 0, '所属区')
            xlsheet.write(0, 1, '工单类型')
            xlsheet.write(0, 2, '服务帐号')
            xlsheet.write(0, 3, 'PBoss地址')
            xlsheet.write(0, 4, '受理时间')
            xlsheet.write(0, 5, '接单时间')

            i = 1
            for item in twentyFour:
                xlsheet.write(i, 0, area)
                xlsheet.write(i, 1, choose_type)
                xlsheet.write(i, 2, item.service)
                xlsheet.write(i, 3, item.pboos)
                xlsheet.write(i, 4, utc_timestamp_to_str(item.accept))
                xlsheet.write(i, 5, utc_timestamp_to_str(item.orders))
                i = i + 1
            xlsname='接单及时率' + choose_type + area + datatype + xlstime
            workbook_m.save(
                '/var/www/downfile/{}.xls'.format(xlsname))
            return ('down.caicool.cc:89/{}.xls'.format(xlsname))
    if choose_type=='移装机':
        dataall = YCinstalled.select().where((YCinstalled.area % like) & (YCinstalled.type == 2) & (
        YCinstalled.accept >= utc_str_to_timestamp(starttime)) & (YCinstalled.confirm <= utc_str_to_timestamp(endtime)))

        if datatype == '2小时内':
            oneToTwo = dataall.where((YCinstalled.orders - YCinstalled.accept) / 3600 <= 2)
            workbook_m = xlwt.Workbook(encoding='utf-8')
            xlsheet = workbook_m.add_sheet('接单及时率2小时内', cell_overwrite_ok=True)
            xlsheet.write(0, 0, '所属区')
            xlsheet.write(0, 1, '工单类型')
            xlsheet.write(0, 2, '服务帐号')
            xlsheet.write(0, 3, 'PBoss地址')
            xlsheet.write(0, 4, '受理时间')
            xlsheet.write(0, 5, '接单时间')

            i = 1
            for item in oneToTwo:
                xlsheet.write(i, 0, area)
                xlsheet.write(i, 1, choose_type)
                xlsheet.write(i, 2, item.service)
                xlsheet.write(i, 3, item.pboos)
                xlsheet.write(i, 4, utc_timestamp_to_str(item.accept))
                xlsheet.write(i, 5, utc_timestamp_to_str(item.orders))
                i = i + 1
            xlsname='接单及时率' + choose_type + area + datatype + xlstime
            workbook_m.save(
                '/var/www/downfile/{}.xls'.format(xlsname))
            return ('down.caicool.cc:89/{}.xls'.format(xlsname))
        if datatype == '2-10小时':
            twoToTen = dataall.where(((YCinstalled.orders - YCinstalled.accept) / 3600 > 2) & (
                (YCinstalled.orders - YCinstalled.accept) / 3600 <= 10))
            workbook_m = xlwt.Workbook(encoding='utf-8')
            xlsheet = workbook_m.add_sheet('接单及时率2-10小时', cell_overwrite_ok=True)
            xlsheet.write(0, 0, '所属区')
            xlsheet.write(0, 1, '工单类型')
            xlsheet.write(0, 2, '服务帐号')
            xlsheet.write(0, 3, 'PBoss地址')
            xlsheet.write(0, 4, '受理时间')
            xlsheet.write(0, 5, '接单时间')

            i = 1
            for item in twoToTen:
                xlsheet.write(i, 0, area)
                xlsheet.write(i, 1, choose_type)
                xlsheet.write(i, 2, item.service)
                xlsheet.write(i, 3, item.pboos)
                xlsheet.write(i, 4, utc_timestamp_to_str(item.accept))
                xlsheet.write(i, 5, utc_timestamp_to_str(item.orders))
                i = i + 1
            xlsname='接单及时率' + choose_type + area + datatype + xlstime
            workbook_m.save(
                '/var/www/downfile/{}.xls'.format(xlsname))
            return ('down.caicool.cc:89/{}.xls'.format(xlsname))
        if datatype == '10-24小时':
            tenToTwentyFour = dataall.where(((YCinstalled.orders - YCinstalled.accept) / 3600 > 10) & (
                (YCinstalled.orders - YCinstalled.accept) / 3600 <= 24))
            workbook_m = xlwt.Workbook(encoding='utf-8')
            xlsheet = workbook_m.add_sheet('接单及时率10-24小时', cell_overwrite_ok=True)
            xlsheet.write(0, 0, '所属区')
            xlsheet.write(0, 1, '工单类型')
            xlsheet.write(0, 2, '服务帐号')
            xlsheet.write(0, 3, 'PBoss地址')
            xlsheet.write(0, 4, '受理时间')
            xlsheet.write(0, 5, '接单时间')

            i = 1
            for item in tenToTwentyFour:
                xlsheet.write(i, 0, area)
                xlsheet.write(i, 1, choose_type)
                xlsheet.write(i, 2, item.service)
                xlsheet.write(i, 3, item.pboos)
                xlsheet.write(i, 4, utc_timestamp_to_str(item.accept))
                xlsheet.write(i, 5, utc_timestamp_to_str(item.orders))
                i = i + 1
            xlsname='接单及时率' + choose_type + area + datatype + xlstime
            workbook_m.save(
                '/var/www/downfile/{}.xls'.format(xlsname))
            return ('down.caicool.cc:89/{}.xls'.format(xlsname))
        if datatype == '超24小时':
            twentyFour = dataall.where((YCinstalled.orders - YCinstalled.accept) / 3600 > 24)
            workbook_m = xlwt.Workbook(encoding='utf-8')
            xlsheet = workbook_m.add_sheet('接单及时率超24小时', cell_overwrite_ok=True)
            xlsheet.write(0, 0, '所属区')
            xlsheet.write(0, 1, '工单类型')
            xlsheet.write(0, 2, '服务帐号')
            xlsheet.write(0, 3, 'PBoss地址')
            xlsheet.write(0, 4, '受理时间')
            xlsheet.write(0, 5, '接单时间')

            i = 1
            for item in twentyFour:
                xlsheet.write(i, 0, area)
                xlsheet.write(i, 1, choose_type)
                xlsheet.write(i, 2, item.service)
                xlsheet.write(i, 3, item.pboos)
                xlsheet.write(i, 4, utc_timestamp_to_str(item.accept))
                xlsheet.write(i, 5, utc_timestamp_to_str(item.orders))
                i = i + 1
            xlsname='接单及时率' + choose_type + area + datatype + xlstime
            workbook_m.save(
                '/var/www/downfile/{}.xls'.format(xlsname))
            return ('down.caicool.cc:89/{}.xls'.format(xlsname))
    if choose_type=='IMS装机':
        dataall = YCinstalled.select().where((YCinstalled.area % like) & (YCinstalled.type == 4) & (
        YCinstalled.accept >= utc_str_to_timestamp(starttime)) & (YCinstalled.confirm <= utc_str_to_timestamp(endtime)))

        if datatype == '2小时内':
            oneToTwo = dataall.where((YCinstalled.orders - YCinstalled.accept) / 3600 <= 2)
            workbook_m = xlwt.Workbook(encoding='utf-8')
            xlsheet = workbook_m.add_sheet('接单及时率2小时内', cell_overwrite_ok=True)
            xlsheet.write(0, 0, '所属区')
            xlsheet.write(0, 1, '工单类型')
            xlsheet.write(0, 2, '服务帐号')
            xlsheet.write(0, 3, 'PBoss地址')
            xlsheet.write(0, 4, '受理时间')
            xlsheet.write(0, 5, '接单时间')

            i = 1
            for item in oneToTwo:
                xlsheet.write(i, 0, area)
                xlsheet.write(i, 1, choose_type)
                xlsheet.write(i, 2, item.service)
                xlsheet.write(i, 3, item.pboos)
                xlsheet.write(i, 4, utc_timestamp_to_str(item.accept))
                xlsheet.write(i, 5, utc_timestamp_to_str(item.orders))
                i = i + 1
            xlsname='接单及时率' + choose_type + area + datatype + xlstime
            workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
            return ('down.caicool.cc:89/{}.xls'.format(xlsname))
        if datatype == '2-10小时':
            twoToTen = dataall.where(((YCinstalled.orders - YCinstalled.accept) / 3600 > 2) & (
                (YCinstalled.orders - YCinstalled.accept) / 3600 <= 10))
            workbook_m = xlwt.Workbook(encoding='utf-8')
            xlsheet = workbook_m.add_sheet('接单及时率2-10小时', cell_overwrite_ok=True)
            xlsheet.write(0, 0, '所属区')
            xlsheet.write(0, 1, '工单类型')
            xlsheet.write(0, 2, '服务帐号')
            xlsheet.write(0, 3, 'PBoss地址')
            xlsheet.write(0, 4, '受理时间')
            xlsheet.write(0, 5, '接单时间')

            i = 1
            for item in twoToTen:
                xlsheet.write(i, 0, area)
                xlsheet.write(i, 1, choose_type)
                xlsheet.write(i, 2, item.service)
                xlsheet.write(i, 3, item.pboos)
                xlsheet.write(i, 4, utc_timestamp_to_str(item.accept))
                xlsheet.write(i, 5, utc_timestamp_to_str(item.orders))
                i = i + 1
            xlsname='接单及时率' + choose_type + area + datatype + xlstime
            workbook_m.save(
                '/var/www/downfile/{}.xls'.format(xlsname))
            return ('down.caicool.cc:89/{}.xls'.format(xlsname))
        if datatype == '10-24小时':
            tenToTwentyFour = dataall.where(((YCinstalled.orders - YCinstalled.accept) / 3600 > 10) & (
                (YCinstalled.orders - YCinstalled.accept) / 3600 <= 24))
            workbook_m = xlwt.Workbook(encoding='utf-8')
            xlsheet = workbook_m.add_sheet('接单及时率10-24小时', cell_overwrite_ok=True)
            xlsheet.write(0, 0, '所属区')
            xlsheet.write(0, 1, '工单类型')
            xlsheet.write(0, 2, '服务帐号')
            xlsheet.write(0, 3, 'PBoss地址')
            xlsheet.write(0, 4, '受理时间')
            xlsheet.write(0, 5, '接单时间')

            i = 1
            for item in tenToTwentyFour:
                xlsheet.write(i, 0, area)
                xlsheet.write(i, 1, choose_type)
                xlsheet.write(i, 2, item.service)
                xlsheet.write(i, 3, item.pboos)
                xlsheet.write(i, 4, utc_timestamp_to_str(item.accept))
                xlsheet.write(i, 5, utc_timestamp_to_str(item.orders))
                i = i + 1
            xlsname='接单及时率' + choose_type + area + datatype + xlstime
            workbook_m.save(
                '/var/www/downfile/{}.xls'.format(xlsname))
            return ('down.caicool.cc:89/{}.xls'.format(xlsname))
        if datatype == '超24小时':
            twentyFour = dataall.where((YCinstalled.orders - YCinstalled.accept) / 3600 > 24)
            workbook_m = xlwt.Workbook(encoding='utf-8')
            xlsheet = workbook_m.add_sheet('接单及时率超24小时', cell_overwrite_ok=True)
            xlsheet.write(0, 0, '所属区')
            xlsheet.write(0, 1, '工单类型')
            xlsheet.write(0, 2, '服务帐号')
            xlsheet.write(0, 3, 'PBoss地址')
            xlsheet.write(0, 4, '受理时间')
            xlsheet.write(0, 5, '接单时间')

            i = 1
            for item in twentyFour:
                xlsheet.write(i, 0, area)
                xlsheet.write(i, 1, choose_type)
                xlsheet.write(i, 2, item.service)
                xlsheet.write(i, 3, item.pboos)
                xlsheet.write(i, 4, utc_timestamp_to_str(item.accept))
                xlsheet.write(i, 5, utc_timestamp_to_str(item.orders))
                i = i + 1
            xlsname='接单及时率' + choose_type + area + datatype + xlstime
            workbook_m.save(
                '/var/www/downfile/{}.xls'.format(xlsname))
            return ('down.caicool.cc:89/{}.xls'.format(xlsname))


# 农普及时率
def agricultural_export(starttime, endtime, choose_type, area, datatype):
    if choose_type == '宽带装机':
        choose_type_id = 1
    if choose_type == 'TV单独安装':
        choose_type_id = 3
    if choose_type == 'IMS单独安装':
        choose_type_id = 4
    if choose_type == '移装机':
        choose_type_id = 2
    if choose_type == '全量工单':
        choose_type_id = 0
    if choose_type_id != 0:
        data = YCinstalled.select().where(
            (YCinstalled.type == 1) & (YCinstalled.accept >= utc_str_to_timestamp(starttime)) & (
                YCinstalled.accept <= utc_str_to_timestamp(endtime)) & (
                YCinstalled.areaType == '普服小区' | YCinstalled.areaType == '普遍服务'))
        data1 = YCinstalled.select().where(
            (YCinstalled.type == 1) & (YCinstalled.confirm >= utc_str_to_timestamp(starttime)) & (
                YCinstalled.confirm <= utc_str_to_timestamp(endtime)) & (YCinstalled.areaType == '普服小区' |
                                                                         YCinstalled.areaType == '普遍服务'))
        like = "%" + area + "%"
        if datatype == '已装超时量':
            data1 = data1.where((YCinstalled.area % like) & (YCinstalled.confirm != 0) & (YCinstalled.timeout == '是'))
            workbook_m = xlwt.Workbook(encoding='utf-8')
            xlsheet = workbook_m.add_sheet('农普及时率已装超时量', cell_overwrite_ok=True)
            xlsheet.write(0, 0, '所属区')
            xlsheet.write(0, 1, '工单类型')
            xlsheet.write(0, 2, '服务帐号')
            xlsheet.write(0, 3, 'PBoss地址')
            xlsheet.write(0, 4, '受理时间')
            i = 1
            for item in data1:
                xlsheet.write(i, 0, area)
                xlsheet.write(i, 1, choose_type)
                xlsheet.write(i, 2, item.service)
                xlsheet.write(i, 3, item.pboos)
                xlsheet.write(i, 4, utc_timestamp_to_str(item.accept))

                i = i + 1
            xlsname = '农普及时率已装超时量' + choose_type + area + datatype + xlstime
            workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
            return ('down.caicool.cc:89/{}.xls'.format(xlsname))
        if datatype == '未装超时量':
            data = data.where((YCinstalled.area % like) & (YCinstalled.confirm == 0))
            workbook_m = xlwt.Workbook(encoding='utf-8')
            xlsheet = workbook_m.add_sheet('农普及时率未装超时量', cell_overwrite_ok=True)
            xlsheet.write(0, 0, '所属区')
            xlsheet.write(0, 1, '工单类型')
            xlsheet.write(0, 2, '服务帐号')
            xlsheet.write(0, 3, 'PBoss地址')
            xlsheet.write(0, 4, '受理时间')


            i = 1
            for item in data:
                xlsheet.write(i, 0, area)
                xlsheet.write(i, 1, choose_type)
                xlsheet.write(i, 2, item.service)
                xlsheet.write(i, 3, item.pboos)
                xlsheet.write(i, 4, utc_timestamp_to_str(item.accept))

                i = i + 1
            xlsname = '农普及时率未装超时量' + choose_type + area + datatype + xlstime
            workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
            return ('down.caicool.cc:89/{}.xls'.format(xlsname))
        if datatype == '压单量':
            workbook_m = xlwt.Workbook(encoding='utf-8')
            xlsheet = workbook_m.add_sheet('农普及时率压单量', cell_overwrite_ok=True)
            xlsheet.write(0, 0, '所属区')
            xlsheet.write(0, 1, '工单类型')
            xlsheet.write(0, 2, '服务帐号')
            xlsheet.write(0, 3, 'PBoss地址')
            xlsheet.write(0, 4, '受理时间')


            xlsname = '农普及时率压单量' + choose_type + area + datatype + xlstime
            workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
            return ('down.caicool.cc:89/{}.xls'.format(xlsname))
    if choose_type_id == 0:
        data = YCinstalled.select().where((YCinstalled.accept >= utc_str_to_timestamp(starttime)) & (
            YCinstalled.accept <= utc_str_to_timestamp(endtime)) & (
                                              YCinstalled.areaType == '普服小区' | YCinstalled.areaType == '普遍服务'))
        data1 = YCinstalled.select().where((YCinstalled.confirm >= utc_str_to_timestamp(starttime)) & (
            YCinstalled.confirm <= utc_str_to_timestamp(endtime)) & (YCinstalled.areaType == '普服小区' |
                                                                     YCinstalled.areaType == '普遍服务'))
        like = "%" + area + "%"
        if datatype == '已装超时量':
            data1 = data1.where((YCinstalled.area % like) & (YCinstalled.confirm != 0) & (YCinstalled.timeout == '是'))
            workbook_m = xlwt.Workbook(encoding='utf-8')
            xlsheet = workbook_m.add_sheet('农普及时率已装超时量', cell_overwrite_ok=True)
            xlsheet.write(0, 0, '所属区')
            xlsheet.write(0, 1, '工单类型')
            xlsheet.write(0, 2, '服务帐号')
            xlsheet.write(0, 3, 'PBoss地址')
            xlsheet.write(0, 4, '受理时间')


            i = 1
            for item in data1:
                xlsheet.write(i, 0, area)
                xlsheet.write(i, 1, choose_type)
                xlsheet.write(i, 2, item.service)
                xlsheet.write(i, 3, item.pboos)
                xlsheet.write(i, 4, utc_timestamp_to_str(item.accept))

                i = i + 1
            xlsname = '农普及时率已装超时量' + choose_type + area + datatype + xlstime
            workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
            return ('down.caicool.cc:89/{}.xls'.format(xlsname))
        if datatype == '未装超时量':
            data = data.where((YCinstalled.area % like) & (YCinstalled.confirm == 0))
            workbook_m = xlwt.Workbook(encoding='utf-8')
            xlsheet = workbook_m.add_sheet('农普及时率未装超时量', cell_overwrite_ok=True)
            xlsheet.write(0, 0, '所属区')
            xlsheet.write(0, 1, '工单类型')
            xlsheet.write(0, 2, '服务帐号')
            xlsheet.write(0, 3, 'PBoss地址')
            xlsheet.write(0, 4, '受理时间')


            i = 1
            for item in data:
                xlsheet.write(i, 0, area)
                xlsheet.write(i, 1, choose_type)
                xlsheet.write(i, 2, item.service)
                xlsheet.write(i, 3, item.pboos)
                xlsheet.write(i, 4, utc_timestamp_to_str(item.accept))

                i = i + 1
            xlsname = '农普及时率未装超时量' + choose_type + area + datatype + xlstime
            workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
            return ('down.caicool.cc:89/{}.xls'.format(xlsname))
        if datatype == '压单量':
            workbook_m = xlwt.Workbook(encoding='utf-8')
            xlsheet = workbook_m.add_sheet('农普及时率压单量', cell_overwrite_ok=True)
            xlsheet.write(0, 0, '所属区')
            xlsheet.write(0, 1, '工单类型')
            xlsheet.write(0, 2, '服务帐号')
            xlsheet.write(0, 3, 'PBoss地址')
            xlsheet.write(0, 4, '受理时间')


            xlsname = '农普及时率压单量' + choose_type + area + datatype + xlstime
            workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
            return ('down.caicool.cc:89/{}.xls'.format(xlsname))
