import connexion
import six

from swagger_server.controllers.supplies_controller import get_f_l_day_now
from swagger_server.models.phone_maintain_lists import PhoneMaintainLists  # noqa: E501
from swagger_server.models.outlist import Outlist  # noqa: E501
from swagger_server.models.phone_use_lists import PhoneUseLists  # noqa: E501
from swagger_server.models.phonetoken import Phonetoken  # noqa: E501
from swagger_server.models.phonetokens import Phonetokens  # noqa: E501
from swagger_server.models.storage_data import StorageData  # noqa: E501
from swagger_server.models.success import Success  # noqa: E501
from swagger_server.models.login import Login  # noqa: E501
from swagger_server.models.out_data import OutData  # noqa: E501
from swagger_server.models.phone_maintain_lists import PhoneMaintainLists  # noqa: E501
from swagger_server.models.phone_use_lists import PhoneUseLists  # noqa: E501
from swagger_server.models.storage_data import StorageData  # noqa: E501
from swagger_server.models.success import Success  # noqa: E501
from swagger_server import util
from swagger_server.mysql_db import *
from swagger_server.tool import *
from swagger_server.models.out_data import OutData  # noqa: E501
from swagger_server.models.outcommit import Outcommit  # noqa: E501


def phone_login_post(body):  # noqa: E501
    """phone Product warehousing

    phone Product warehousing # noqa: E501

    :param body: data
    :type body: dict | bytes

    :rtype: Success
    """
    if connexion.request.is_json:
        body = Login.from_dict(connexion.request.get_json())  # noqa: E501
        try:
            count=YCpeople.select().where(
                YCpeople.name==body.name,
                YCpeople.phone==body.phone
            ).count()
            if count==1 :
                return {
                    "msg": "success",
                    "code": 0
                }
        except Exception as e:
            print(e)
            return {"code": -1, "msg": "Error"}



def phone_outcommit_post(body):  # noqa: E501
    """phone Product warehousing

    phone Product warehousing # noqa: E501

    :param body: data
    :type body: dict | bytes

    :rtype: Success
    """
    try:

        if connexion.request.is_json:
            body = Outcommit.from_dict(connexion.request.get_json())
            if body.type=='-1':
                data=YCoutbound.select().where(YCoutbound.people==body.people,YCoutbound.status==-1)
            else:

                type = get_type_sort(body.type)
                model = get_model_sort(body.model)
                # noqa: E501
                data=YCoutbound.select().where(
                    YCoutbound.type==type,YCoutbound.model==model,
            YCoutbound.people==body.people,YCoutbound.status==-1)
            for item in data:
                # YCoutbound.update(status=0).where(YCoutbound.code==item.code)
                YCoutbound.update(status=0).where(YCoutbound.code == item.code).execute()
                YCstatus.insert(use='确认出库',
                                work=item.work,
                                code=item.code,
                                people=item.people,
                                posttime=int(time.time())).execute()
            msg = {
                    "msg": "success",
                    "code": 0
                }
    except Exception as e:
        print(e)
        msg = {"code": -1, "msg": "Error"}
    return msg

def phone_outlist_post(body):  # noqa: E501
    """phone Product warehousing

    phone Product warehousing # noqa: E501

    :param body: data
    :type body: dict | bytes

    :rtype: Success
    """
    if connexion.request.is_json:
        body = Outlist.from_dict(connexion.request.get_json())  # noqa: E501
        try:
            data = YCoutbound.select(YCoutbound.type, YCoutbound.model, fn.COUNT(YCoutbound.model).alias(
                'count')).where(YCoutbound.people == body.outman, YCoutbound.status == -1).group_by(YCoutbound.model)
            # for item in data:
            #     print(get_type_name(item.type))
            #     print(get_model_name(item.model))
            #     print(item.count)

            result = [{
                "type": get_type_name(item.type),
                "model": get_model_name(item.model),
                "count": item.count,
                "people": body.outman,
            } for item in data]
            msg = {
                "result":result,
                    "msg": "success",
                    "code": 0
                }
        except Exception as e:
            print(e)
            msg = {"code": -1, "msg": "Error"}
        return msg



def phone_maintain_post(body):  # noqa: E501
    """phone maintain post

    phone maintain post # noqa: E501

    :param body: data
    :type body: dict | bytes

    :rtype: Success
    """
    if connexion.request.is_json:
        body = PhoneMaintainLists.from_dict(connexion.request.get_json())  # noqa: E501
    if YCmaintain.select().where(YCmaintain.order == body.order).count() == 1:
        msg = {'code': 10003, 'msg': 'error'}
        return msg
    if body.personnel == '' or body.order == '':
        msg = {'code': 10003, 'msg': 'error'}
        return msg
    if body.ocode == None or body.ocode == '' or body.code == None or body.code == '':
        return {'code': 10003, 'msg': 'error'}

    count = YCoutbound.select().where(YCoutbound.code == body.ocode).count()
    if count < 1:
        msg = {'code': 10003, 'msg': 'error'}
        return msg
    count = YCoutbound.select().where(YCoutbound.code == body.code).count()
    if count < 1:
        msg = {'code': 10003, 'msg': 'error'}
        return msg
    item = body.__dict__
    YCmaintain.insert(work=get_work_sort(item['work']),
                      type=get_type_sort(item['type']),
                      order=item['order'],
                      code=item['code'],
                      ocode=item['ocode'],
                      people=item['personnel'],
                      posttime=utc_str_to_timestamp(item['posttime'])).execute()
    #  YCstorage.   新条码应该也是在库里的吧  处于没有 use 的状态
    # 把out 中 新code 改成2
    YCoutbound.update(status=2).where(YCoutbound.code == item['code']).execute()
    YCstatus.insert(use='维修使用',
                    work=get_work_sort(item['work']),
                    code=item['code'],
                    people=item['personnel'],
                    posttime=utc_str_to_timestamp(item['posttime'])).execute()


def phone_out_post(body):  # noqa: E501
    """phone Product warehousing

    phone Product warehousing # noqa: E501

    :param body: data
    :type body: dict | bytes

    :rtype: Success
    """
    # noqa: E501
    if connexion.request.is_json:
        body = OutData.from_dict(connexion.request.get_json())  # noqa: E501
        try:
            if YCoutbound.select().where(YCoutbound.code == body.code).count() >= 1:
                msg = {"code": 10003, "msg": "code not exist"}
                return msg
        except Exception as e:
            print(e)
            msg = {"code": 10003, "msg": "code not exist"}

        try:
            work = get_work_sort(body.work)
            type = get_type_sort(body.type)
            model = get_model_sort(body.model)
            factory = YCstorage.select().where(YCstorage.code == body.code).get().factory

            fstarttime = utc_str_to_timestamp(get_f_l_day_now()[0])

            fendtime = utc_str_to_timestamp(get_f_l_day_now()[1])
            count11 = YCoutbound.select().where(YCoutbound.people == body.people, YCoutbound.status == 0,
                                                YCoutbound.posttime >= fstarttime,
                                                YCoutbound.posttime <= fendtime).count()
            count222 = YCoutbound.select().where(YCoutbound.people == body.people, YCoutbound.status == -1,
                                                 YCoutbound.posttime >= fstarttime,
                                                 YCoutbound.posttime <= fendtime).count()
            if count11 + count222 > 5:
                return {"code": 10005, "msg": "超出本月最大领取量"}

            YCoutbound.insert(work=work, type=type, factory=factory,
                              model=model, people=body.people, code=body.code,
                              posttime=int(time.time()),
                              status=-1).execute()

            YCstatus.insert(work=work, use='申领出库中', people=body.people, code=body.code,
                            posttime=int(time.time())).execute()
            YCstorage.update(status=1).where(YCstorage.code == body.code).execute()
            msg = {
                "msg": "success",
                "code": 0
            }
        except Exception as e:
            print(e)
            msg = {"code": -1, "msg": "Error"}
        return msg

def phone_storage_post(body):  # noqa: E501
    """phone Product warehousing

    phone Product warehousing # noqa: E501

    :param body: data
    :type body: dict | bytes

    :rtype: Success
    """
    if connexion.request.is_json:
        body = StorageData.from_dict(connexion.request.get_json())  # noqa: E501
    try:
        if YCstorage.select().where(YCstorage.code == body.code).count() >= 1:
            msg = {"code": 10003, "msg": "code has exist"}
            return msg
    except:
        pass

    try:
        work = get_work_sort(body.work)
        type = get_type_sort(body.type)
        model = get_model_sort(body.model)
        YCstorage.insert(work=work, type=type, factory=body.factory,
                         model=model, people=body.principal, code=body.code,
                         status=0, posttime=int(time.time())).execute()
        YCstatus.insert(work=work, use='扫码入库', people=body.principal, code=body.code,
                        posttime=int(time.time())).execute()
        msg = {
            "msg": "success",
            "code": 0
        }
    except Exception as e:
        print(e)
        msg = {"code": -1, "msg": "Error"}
    return msg


def phone_use_post(body):  # noqa: E501
    """phone use post

    phone use post # noqa: E501

    :param body: data
    :type body: dict | bytes

    :rtype: Success
    """
    if connexion.request.is_json:
        body = PhoneUseLists.from_dict(connexion.request.get_json())  # noqa: E501
    try:
        if (body.modem != None and body.modem != ''):
            now_type = 1
            count = YCstorage.select().where(YCstorage.code == body.modem).count()
            if count < 1:
                msg = {'code': 10003, 'msg': 'error'}
                return msg
        if (body.gateway != None and body.gateway != ''):
            now_type = 1
            count = YCstorage.select().where(YCstorage.code == body.gateway).count()
            if count < 1:
                msg = {'code': 10003, 'msg': 'error'}
                return msg
        if (body.box != None and body.box != ''):
            count = YCstorage.select().where(YCstorage.code == body.box).count()
            if count < 1:
                msg = {'code': 10003, 'msg': 'error'}
                return msg
        if (body.hemu != None and body.hemu != ''):
            count = YCstorage.select().where(YCstorage.code == body.hemu).count()
            if count < 1:
                msg = {'code': 10003, 'msg': 'error'}
                return msg
        if (body.phone != None and body.phone != ''):
            count = YCstorage.select().where(YCstorage.code == body.phone).count()
            if count < 1:
                msg = {'code': 10003, 'msg': 'error'}
                return msg
        item = body.__dict__
        if (item['modem'] != None and item['modem'] != ''):
            YCstatus.insert(use='装机使用',
                            work=get_work_sort(item['work']),
                            code=item['modem'],
                            people=item['personnel'],
                            posttime=utc_str_to_timestamp(item['posttime'])).execute()
            YCoutbound.update(status=1).where(YCoutbound.code == item['modem']).execute()
            factory = YCstorage.select().where(YCstorage.code == item['modem']).get().factory
            now_type = YCstorage.select().where(YCstorage.code == item['modem']).get().type
        if (item['gateway'] != None and item['gateway'] != ''):
            YCstatus.insert(use='装机使用',
                            work=get_work_sort(item['work']),
                            code=item['gateway'],
                            people=item['personnel'],
                            posttime=utc_str_to_timestamp(item['posttime'])).execute()
            YCoutbound.update(status=1).where(YCoutbound.code == item['gateway']).execute()
            factory = YCstorage.select().where(YCstorage.code == item['gateway']).get().factory
            now_type = YCstorage.select().where(YCstorage.code == item['gateway']).get().type
        if (item['box'] != None and item['box'] != ''):
            YCstatus.insert(use='装机使用',
                            work=get_work_sort(item['work']),
                            code=item['box'],
                            people=item['personnel'],
                            posttime=utc_str_to_timestamp(item['posttime'])).execute()
            YCoutbound.update(status=1).where(YCoutbound.code == item['box']).execute()
            factory = YCstorage.select().where(YCstorage.code == item['box']).get().factory
            now_type = YCstorage.select().where(YCstorage.code == item['box']).get().type
        if (item['hemu'] != None and item['hemu'] != ''):
            YCstatus.insert(use='装机使用',
                            work=get_work_sort(item['work']),
                            code=item['hemu'],
                            people=item['personnel'],
                            posttime=utc_str_to_timestamp(item['posttime'])).execute()
            YCoutbound.update(status=1).where(YCoutbound.code == item['hemu']).execute()
            factory = YCstorage.select().where(YCstorage.code == item['hemu']).get().factory
            now_type = YCstorage.select().where(YCstorage.code == item['hemu']).get().type
        if (item['phone'] != None and item['phone'] != ''):
            YCstatus.insert(use='装机使用',
                            work=get_work_sort(item['work']),
                            code=item['phone'],
                            people=item['personnel'],
                            posttime=utc_str_to_timestamp(item['posttime'])).execute()
            YCoutbound.update(status=1).where(YCoutbound.code == item['phone']).execute()
            factory = YCstorage.select().where(YCstorage.code == item['phone']).get().factory
            now_type = YCstorage.select().where(YCstorage.code == item['phone']).get().type
        YCuse.insert(
            produce=factory,
            work=get_work_sort(item['work']),
            business=get_business_sort(item['type']),
            order=item['order'],
            modem=item['modem'],
            gateway=item['gateway'],
            box=item['box'],
            hemu=item['hemu'],
            phone=item['phone'],
            people=item['personnel'],
            type=now_type,
            posttime=utc_str_to_timestamp(item['posttime'])).execute()
        msg = {"code": 0, "msg": "success"}
    except Exception as e:
        print(e)
        msg = {"code": -1, "msg": "Error"}
    return msg


def phone_token_post(body):  # noqa: E501
    """phone maintain post

    phone token post # noqa: E501

    :param body: data
    :type body: dict | bytes

    :rtype: Phonetokens
    """
    # try:
    if connexion.request.is_json:
        print('yes----')
        body = Phonetoken.from_dict(connexion.request.get_json())  # noqa: E501
        r = requests.get(
            url='https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=wxc80abcb7381515af&secret=6ef56516044dd8fbd592483a6b366007')
        data = json.loads(r.text)
        if str(data['expires_in']) != '7200':
            return {"code": -1, 'msg': 'error'}
        code = data['access_token']
        r = requests.get(
            url='https://api.weixin.qq.com/cgi-bin/ticket/getticket?access_token={}&type=jsapi'.format(code))
        data = json.loads(r.text)
        if str(data['errcode']) != '0':
            return {"code": -1, 'msg': 'error'}
        ticket = data['ticket']
        print('-----------')
        times = str(int(time.time()))
        noncestr = 'flyminer12'
        text = 'jsapi_ticket={}&noncestr={}&timestamp={}&url={}'.format(
            ticket, noncestr, times, body.url)

        code = hashlib.sha1(text.encode('UTF-8')).hexdigest()

        msg = {"code": 0, 'msg': 'success',
               "result": [{"code": code, "times": int(times), "noncestr": noncestr}]}
        return msg
        # except:
        #   return {"code": -1, 'msg': 'error'}
