import random, time
import requests
import json


def get_num():
    num = ''.join(str(random.choice(range(8))) for _ in range(8))
    return num


def get_id():
    num = random.choice(range(1, 5))
    return num


if __name__ == '__main__':
    model_list = ['HG8546M',
                  'HG8545M',
                  'HS8545V',
                  'HS8546V',
                  'cm115z',
                  '中兴B760',
                  '创维E820',
                  '中兴B760',
                  'UNT200',
                  'cm101',
                  'C15',
                  'C13C',
                  'C21',
                  'C13',
                  'C11',
                  'D11',
                  'D13',
                  'D31',
                  ]
    people_list = [ '彭万里',
                    '高大山',
                    '谢大海',
                    '马宏宇',
                    '林莽',
                    '黄强辉',
                    '章汉夫',
                    '范长江',
                    '林君雄',
                    '谭平山',
                    '朱希亮',
                    '李四光',
                    '甘铁生',]


    work_list = ['全市',
                 '宜昌城区',
                 '当阳市',
                 '宜昌开发区',
                 '五峰县',
                 '兴山县',
                 '夷陵区',
                 '宜都市',
                 '远安县',
                 '长阳县',
                 '枝江市',
                 '秭归县']
    type_list = ['光猫',             '智能网关',            '和TV机顶盒',             '和目',            '固话（移动产权）',           ]
    use_list = ['扫描入库', '装机使用', '装维申领', '维护使用', '维护使用']
    factory_list = [     '杭研',       '中兴',  '华为',     '贝尔',]
    headers = {'Content-Type': 'application/json'}
    for i in range(50):
        print(get_num())
    # for i in range (1,12):
    #     headers = {'Content-Type': 'application/json'}
    #     url = 'http://0.0.0.0:7000/v1/supplies/storage'
    #     data = {
    #         "work": work_list[i],
    #         "type": type_list[1],
    #         "factory": factory_list[3],
    #         "model": 'cm115z',
    #         "principal": people_list[i],
    #         # "code": get_num()
    #         "code": 'nbel'+get_num()
    #     }
    #     data = json.dumps(data)
    #     r = requests.post(url, data=data, headers=headers)
    #     print(r.text)
    #
    # url = 'http://0.0.0.0:7000/v1/supplies/out'
    #
    # data = {
    #     "code": "4793159953",
    #     "factory": "华为",
    #     "id": 22,
    #     "model": "HS8545V",
    #     "posttime": "2018-05-16 15:14:23",
    #     "principal": "小王",
    #     "type": "固话（移动产权）",
    #     "work": "五峰县"
    # }
    # url ='http://0.0.0.0:7000/v1/supplies/storage?page=1&size=50'
    # r=requests.get(url)
    # data=json.loads(r.text)
    # for i in data['result']:
    #     info={}
    #     info['code']=i['code']
    #     info['model'] = i['model']
    #     info['type'] = i['type']
    #     info['work'] = i['work']
    #     info['people'] = i['principal']
    #     url2 = 'http://0.0.0.0:7000/v1/supplies/out'
    #     datas = json.dumps(info)
    #     r = requests.post(url2, data=datas, headers=headers)
    #     print(r.status_code)
    #     print(r.text)
    #




    # YCoutbound.insert(work=get_id(), type=get_id(), factory='1号工厂',
    #                   model=get_id(), people=people_list[get_id()], code=get_num(),
    #                   posttime=int(time.time())).execute()
    #
    # YCstorage.insert(work=get_id(), type=get_id(), factory='1号工厂',
    #                  model=get_id(), people=people_list[get_id()], code=num,
    #                  posttime=int(time.time()),
    #                  status=0).execute()
    #
    # YCstatus.insert(work=get_id(), use=use_list[get_id()], people=people_list[get_id()], code=get_num(),
    #                 posttime=int(time.time())).execute()
    #
    # YCmaintain.insert(work=get_id(),
    #                   order=get_num(),
    #                   ocode=get_num(),
    #                   type=get_id(),
    #                   people=people_list[get_id()],
    #                   code=get_num(),
    #                   posttime=int(time.time())).execute()

    # YCwaste.insert(work=get_id(),
    #                type=get_id(),
    #                code=get_num(),
    #                factory='1号工厂',
    #                model=get_id(),
    #                posttime=int(time.time()),
    #                status=2
    #                ).execute()

    # YCuse.insert(work=get_id(),
    #              business=get_id(),
    #              order=get_num(),
    #              modem=get_id(),
    #              gateway=get_num(),
    #              box=get_num(),
    #              hemu=get_num(),
    #              phone=get_num(),
    #              people=get_num(),
    #              posttime=int(time.time())).execute()

    # YCstorage.insert(
    #     work=1,
    #
    # )
    # print(data.count())
    # for item in data:
    #     print(item.name)
    #     print(item.list)
