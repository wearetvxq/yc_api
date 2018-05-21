import connexion
import six,xlrd,xlwt

from swagger_server.models.down_url import DownUrl  # noqa: E501
from swagger_server.models.home_chart import HomeChart  # noqa: E501
from swagger_server.models.installed_list import InstalledList  # noqa: E501
from swagger_server.models.installed_top_list import InstalledTopList  # noqa: E501
from swagger_server.models.orders_list import OrdersList  # noqa: E501
from swagger_server.models.retreat_list import RetreatList  # noqa: E501
from swagger_server.models.satisfaction_list import SatisfactionList  # noqa: E501
from swagger_server.export_report import *
from swagger_server.models.success import Success  # noqa: E501
from swagger_server import util
from swagger_server.mysql_db import *
from swagger_server.infoexport import *

##基础共用数据
msg_24chart_right = {
            "code": 0,
            "msg": "返回成功",
            "result": [
                {
                    "name": "宜昌城区",
                    "value": "60"
                },
                {
                    "name": "宜昌开发区",
                    "value": "75"
                },
                {
                    "name": "当阳市",
                    "value": "25"
                },
                {
                    "name": "五峰县",
                    "value": "36"
                },
                {
                    "name": "兴山县",
                    "value": "85"
                },
                {
                    "name": "夷陵区",
                    "value": "80"
                },
                {
                    "name": "宜都区",
                    "value": "79"
                },
                {
                    "name": "远安县",
                    "value": "85"
                },
                {
                    "name": "长春县",
                    "value": "93"
                },
                {
                    "name": "枝江市",
                    "value": "77"
                },
                {
                    "name": "姊归县",
                    "value": "86"
                },
                {
                    "name": "全市",
                    "value": "87"
                }
            ]
}
msg_firstchart_right = {
  "code": 0,
  "msg": "返回成功",
  "result": [
    {
      "area": "宜昌城区",
      "inside": "120",
      "ultra": "150"
    },
	{
      "area": "当阳市",
      "inside": "90",
      "ultra": "100"
    },
	{
      "area": "宜昌开发区",
      "inside": "130",
      "ultra": "80"
    },
	{
      "area": "五峰县",
      "inside": "80",
      "ultra": "120"
    },
	{
      "area": "兴山县",
      "inside": "100",
      "ultra": "90"
    },
	{
      "area": "夷陵区",
      "inside": "100",
      "ultra": "90"
    },
	{
      "area": "宜都市",
      "inside": "160",
      "ultra": "110"
    },
	{
      "area": "远安县",
      "inside": "180",
      "ultra": "100"
    },
	{
      "area": "长阳县",
      "inside": "80",
      "ultra": "100"
    },
	{
      "area": "枝江市",
      "inside": "130",
      "ultra": "80"
    },
	{
      "area": "姊归县",
      "inside": "120",
      "ultra": "100"
    },
	{
      "area": "全市",
      "inside": "120",
      "ultra": "150"
    }
  ]
}
msg_list_export = {
  "code": 0,
  "msg": "返回成功",
  "url": "down.flyminer.cn:89/test0.xls"
}

msg_top_list_right = {
  "code": 0,
  "msg": "string",
  "result": [
      {
          "id": 0,
          "top": "1",
          "area": "宜昌城区",
          "type": "宽带装机",
          "account": "1214213",
          "pboss": "124123",
          "times": "2018/02/09"
      },
      {
          "id": 0,
          "top": "1",
          "area": "宜昌城区",
          "type": "宽带装机",
          "account": "1214213",
          "pboss": "124123",
          "times": "2018/02/09"
      },
      {
          "id": 0,
          "top": "1",
          "area": "宜昌城区",
          "type": "宽带装机",
          "account": "1214213",
          "pboss": "124123",
          "times": "2018/02/09"
      },
      {
          "id": 0,
          "top": "1",
          "area": "宜昌城区",
          "type": "宽带装机",
          "account": "1214213",
          "pboss": "124123",
          "times": "2018/02/09"
      },
      {
          "id": 0,
          "top": "1",
          "area": "宜昌城区",
          "type": "宽带装机",
          "account": "1214213",
          "pboss": "124123",
          "times": "2018/02/09"
      },
      {
          "id": 0,
          "top": "1",
          "area": "宜昌城区",
          "type": "宽带装机",
          "account": "1214213",
          "pboss": "124123",
          "times": "2018/02/09"
      }, {
          "id": 0,
          "top": "1",
          "area": "宜昌城区",
          "type": "宽带装机",
          "account": "1214213",
          "pboss": "124123",
          "times": "2018/02/09"
      },
      {
          "id": 0,
          "top": "1",
          "area": "宜昌城区",
          "type": "宽带装机",
          "account": "1214213",
          "pboss": "124123",
          "times": "2018/02/09"
      },
      {
          "id": 0,
          "top": "1",
          "area": "宜昌城区",
          "type": "宽带装机",
          "account": "1214213",
          "pboss": "124123",
          "times": "2018/02/09"
      },
      {
          "id": 0,
          "top": "1",
          "area": "宜昌城区",
          "type": "宽带装机",
          "account": "1214213",
          "pboss": "124123",
          "times": "2018/02/09"
      },
      {
          "id": 0,
          "top": "1",
          "area": "宜昌城区",
          "type": "宽带装机",
          "account": "1214213",
          "pboss": "124123",
          "times": "2018/02/09"
      },
      {
          "id": 0,
          "top": "1",
          "area": "宜昌城区",
          "type": "宽带装机",
          "account": "1214213",
          "pboss": "124123",
          "times": "2018/02/09"
      },
      {
          "id": 0,
          "top": "1",
          "area": "宜昌城区",
          "type": "宽带装机",
          "account": "1214213",
          "pboss": "124123",
          "times": "2018/02/09"
      }
  ]
}

msg_agricultural_list_right = {
  "code": 0,
  "msg": "返回成功",
  "result": [
    {
      "id": 0,
       "area":"宜昌市",
      "accept": "1000",
      "complete": "800",
      "loaded": "200",
      "notLoaded": "100",
      "pressing": "50",
      "rate": "70%",
      "ave": "9"
    },
	 {
      "id": 1,
       "area": "宜昌市",
      "accept": "1000",
      "complete": "800",
      "loaded": "200",
      "notLoaded": "100",
      "pressing": "50",
      "rate": "70%",
      "ave": "9"
    },
	 {
      "id": 2,
       "area": "宜昌市",
      "accept": "1000",
      "complete": "800",
      "loaded": "200",
      "notLoaded": "100",
      "pressing": "50",
      "rate": "70%",
      "ave": "9"
    },
	 {
      "id": 3,
       "area": "宜昌市",
      "accept": "1000",
      "complete": "800",
      "loaded": "200",
      "notLoaded": "100",
      "pressing": "50",
      "rate": "70%",
      "ave": "9"
    },
	 {
      "id": 4,
       "area": "宜昌市",
      "accept": "1000",
      "complete": "800",
      "loaded": "200",
      "notLoaded": "100",
      "pressing": "50",
      "rate": "70%",
      "ave": "9"
    }, {
      "id": 5,
      "area": "宜昌市",
      "accept": "1000",
      "complete": "800",
      "loaded": "200",
      "notLoaded": "100",
      "pressing": "50",
      "rate": "70%",
      "ave": "9"
    }, {
      "id": 6,
      "area": "宜昌市",
      "accept": "1000",
      "complete": "800",
      "loaded": "200",
      "notLoaded": "100",
      "pressing": "50",
      "rate": "70%",
      "ave": "9"
    }, {
      "id": 7,
      "area": "宜昌市",
      "accept": "1000",
      "complete": "800",
      "loaded": "200",
      "notLoaded": "100",
      "pressing": "50",
      "rate": "70%",
      "ave": "9"
    }, {
      "id": 8,
      "area": "宜昌市",
      "accept": "1000",
      "complete": "800",
      "loaded": "200",
      "notLoaded": "100",
      "pressing": "50",
      "rate": "70%",
      "ave": "9"
    }, {
      "id": 9,
      "area": "宜昌市",
      "accept": "1000",
      "complete": "800",
      "loaded": "200",
      "notLoaded": "100",
      "pressing": "50",
      "rate": "70%",
      "ave": "9"
    }, {
      "id": 10,
      "area": "宜昌市",
      "accept": "1000",
      "complete": "800",
      "loaded": "200",
      "notLoaded": "100",
      "pressing": "50",
      "rate": "70%",
      "ave": "9"
    },
	 {
      "id": 11,
       "area": "宜昌市",
      "accept": "1000",
      "complete": "800",
      "loaded": "200",
      "notLoaded": "100",
      "pressing": "50",
      "rate": "70%",
      "ave": "9"
    }
  ]
}

msg_firstlist_right = {
  "code": 0,
  "msg": "返回成功",
  "result": [
    {
      "id": 0,
      "area": "宜昌城区",
      "duration": [
        {
          "total": "500",
          "one": "100",
          "oneToTwo": "100",
          "twoToTen": "100",
          "tenToTwentyFour": "100",
          "twentyFour": "100"
        }
      ],
      "accounting": [
        {
          "one1": "20%",
          "oneToTwo1": "20%",
          "twoToTen1": "20%",
          "tenToTwentyFour1": "20%",
          "twentyFour1": "20%",
          "rate": "20%",
          "ave": "5"
        }
      ]
    },
	 {
      "id": 1,
      "area": "当阳市",
      "duration": [
        {
          "total": "500",
          "one": "100",
          "oneToTwo": "100",
          "twoToTen": "100",
          "tenToTwentyFour": "100",
          "twentyFour": "100"
        }
      ],
         "accounting": [
             {
                 "one1": "20%",
                 "oneToTwo1": "20%",
                 "twoToTen1": "20%",
                 "tenToTwentyFour1": "20%",
                 "twentyFour1": "20%",
                 "rate": "20%",
                 "ave": "5"
             }
         ]
    },
	 {
      "id": 2,
      "area": "宜昌开发区",
      "duration": [
        {
          "total": "500",
          "one": "100",
          "oneToTwo": "100",
          "twoToTen": "100",
          "tenToTwentyFour": "100",
          "twentyFour": "100"
        }
      ],
         "accounting": [
             {
                 "one1": "20%",
                 "oneToTwo1": "20%",
                 "twoToTen1": "20%",
                 "tenToTwentyFour1": "20%",
                 "twentyFour1": "20%",
                 "rate": "20%",
                 "ave": "5"
             }
         ]
    },
	 {
      "id": 3,
      "area": "五峰县",
      "duration": [
        {
          "total": "500",
          "one": "100",
          "oneToTwo": "100",
          "twoToTen": "100",
          "tenToTwentyFour": "100",
          "twentyFour": "100"
        }
      ],
         "accounting": [
             {
                 "one1": "20%",
                 "oneToTwo1": "20%",
                 "twoToTen1": "20%",
                 "tenToTwentyFour1": "20%",
                 "twentyFour1": "20%",
                 "rate": "20%",
                 "ave": "5"
             }
         ]
    },
	 {
      "id": 4,
      "area": "兴山县",
      "duration": [
        {
          "total": "500",
          "one": "100",
          "oneToTwo": "100",
          "twoToTen": "100",
          "tenToTwentyFour": "100",
          "twentyFour": "100"
        }
      ],
         "accounting": [
             {
                 "one1": "20%",
                 "oneToTwo1": "20%",
                 "twoToTen1": "20%",
                 "tenToTwentyFour1": "20%",
                 "twentyFour1": "20%",
                 "rate": "20%",
                 "ave": "5"
             }
         ]
    },
	 {
      "id": 5,
      "area": "夷陵区",
      "duration": [
        {
          "total": "500",
          "one": "100",
          "oneToTwo": "100",
          "twoToTen": "100",
          "tenToTwentyFour": "100",
          "twentyFour": "100"
        }
      ],
         "accounting": [
             {
                 "one1": "20%",
                 "oneToTwo1": "20%",
                 "twoToTen1": "20%",
                 "tenToTwentyFour1": "20%",
                 "twentyFour1": "20%",
                 "rate": "20%",
                 "ave": "5"
             }
         ]
    },
	 {
      "id": 6,
      "area": "宜都市",
      "duration": [
        {
          "total": "500",
          "one": "100",
          "oneToTwo": "100",
          "twoToTen": "100",
          "tenToTwentyFour": "100",
          "twentyFour": "100"
        }
      ],
         "accounting": [
             {
                 "one1": "20%",
                 "oneToTwo1": "20%",
                 "twoToTen1": "20%",
                 "tenToTwentyFour1": "20%",
                 "twentyFour1": "20%",
                 "rate": "20%",
                 "ave": "5"
             }
         ]
    },
	 {
      "id": 7,
      "area": "远安县",
      "duration": [
        {
          "total": "500",
          "one": "100",
          "oneToTwo": "100",
          "twoToTen": "100",
          "tenToTwentyFour": "100",
          "twentyFour": "100"
        }
      ],
         "accounting": [
             {
                 "one1": "20%",
                 "oneToTwo1": "20%",
                 "twoToTen1": "20%",
                 "tenToTwentyFour1": "20%",
                 "twentyFour1": "20%",
                 "rate": "20%",
                 "ave": "5"
             }
         ]
    },
	 {
      "id": 8,
      "area": "长阳县",
      "duration": [
        {
          "total": "500",
          "one": "100",
          "oneToTwo": "100",
          "twoToTen": "100",
          "tenToTwentyFour": "100",
          "twentyFour": "100"
        }
      ],
         "accounting": [
             {
                 "one1": "20%",
                 "oneToTwo1": "20%",
                 "twoToTen1": "20%",
                 "tenToTwentyFour1": "20%",
                 "twentyFour1": "20%",
                 "rate": "20%",
                 "ave": "5"
             }
         ]
    },
	 {
      "id": 8,
      "area": "枝江市",
      "duration": [
        {
          "total": "500",
          "one": "100",
          "oneToTwo": "100",
          "twoToTen": "100",
          "tenToTwentyFour": "100",
          "twentyFour": "100"
        }
      ],
         "accounting": [
             {
                 "one1": "20%",
                 "oneToTwo1": "20%",
                 "twoToTen1": "20%",
                 "tenToTwentyFour1": "20%",
                 "twentyFour1": "20%",
                 "rate": "20%",
                 "ave": "5"
             }
         ]
    },
	 {
      "id": 9,
      "area": "姊归县",
      "duration": [
        {
          "total": "500",
          "one": "100",
          "oneToTwo": "100",
          "twoToTen": "100",
          "tenToTwentyFour": "100",
          "twentyFour": "100"
        }
      ],
         "accounting": [
             {
                 "one1": "20%",
                 "oneToTwo1": "20%",
                 "twoToTen1": "20%",
                 "tenToTwentyFour1": "20%",
                 "twentyFour1": "20%",
                 "rate": "20%",
                 "ave": "5"
             }
         ]
    },
	 {
      "id":10,
      "area": "全市",
      "duration": [
        {
          "total": "500",
          "one": "100",
          "oneToTwo": "100",
          "twoToTen": "100",
          "tenToTwentyFour": "100",
          "twentyFour": "100"
        }
      ],
         "accounting": [
             {
                 "one1": "20%",
                 "oneToTwo1": "20%",
                 "twoToTen1": "20%",
                 "tenToTwentyFour1": "20%",
                 "twentyFour1": "20%",
                 "rate": "20%",
                 "ave": "5"
             }
         ]
    }
  ]
}

msg_out_list_right ={
  "code": 0,
  "msg": "string",
  "result": [
    {
      "id": 0,
       "top": "1",
      "area": "宜昌城区",
      "type": "宽带装机",
      "account": "123456",
      "pboss": "123456",
      "times": "2018/03/27 12：00：00"
    },
	  {
      "id": 1,
          "top": "1",
      "area": "当阳市",
      "type": "宽带装机",
      "account": "123456",
      "pboss": "123456",
      "times": "2018/03/27 12：00：00"
    },
	  {
      "id": 2,
          "top": "1",
      "area": "宜昌开发区",
      "type": "宽带装机",
      "account": "123456",
      "pboss": "123456",
      "times": "2018/03/27 12：00：00"
    },
	  {
      "id": 3,
          "top": "1",
      "area": "五峰县",
      "type": "宽带装机",
      "account": "123456",
      "pboss": "123456",
      "times": "2018/03/27 12：00：00"
    },
	  {
      "id": 4,
          "top": "1",
      "area": "兴山县",
      "type": "宽带装机",
      "account": "123456",
      "pboss": "123456",
      "times": "2018/03/27 12：00：00"
    },
	  {
      "id": 5,
          "top": "1",
      "area": "夷陵区",
      "type": "宽带装机",
      "account": "123456",
      "pboss": "123456",
      "times": "2018/03/27 12：00：00"
    },
	  {
      "id": 6,
          "top": "1",
      "area": "宜都市",
      "type": "宽带装机",
      "account": "123456",
      "pboss": "123456",
      "times": "2018/03/27 12：00：00"
    },
	  {
      "id": 7,
          "top": "1",
      "area": "远安县",
      "type": "宽带装机",
      "account": "123456",
      "pboss": "123456",
      "times": "2018/03/27 12：00：00"
    },
	  {
      "id": 8,
          "top": "1",
      "area": "长阳县",
      "type": "宽带装机",
      "account": "123456",
      "pboss": "123456",
      "times": "2018/03/27 12：00：00"
    },
	  {
      "id": 9,
          "top": "1",
      "area": "枝江市",
      "type": "宽带装机",
      "account": "123456",
      "pboss": "123456",
      "times": "2018/03/27 12：00：00"
    },
	  {
      "id": 10,
          "top": "1",
      "area": "姊归县",
      "type": "宽带装机",
      "account": "123456",
      "pboss": "123456",
      "times": "2018/03/27 12：00：00"
    },
	{
      "id": 11,
        "top": "1",
      "area": "全市",
      "type": "宽带装机",
      "account": "123456",
      "pboss": "123456",
      "times": "2018/03/27 12：00：00"
    }
  ]
}

msg_satisfaction_list_right ={
  "code": 0,
  "msg": "string",
  "result": [
    {
      "id": 0,
      "area": "宜昌城区",
      "visit": "125",
      "succ": "100",
      "rate": "80%",
      "satisfaction": "100",
      "displeasure": "0",
      "unanswered": "0",
      "satisfactionRate": "100%"
    },
	  {
      "id": 0,
      "area": "当阳市",
      "visit": "125",
      "succ": "100",
      "rate": "80%",
      "satisfaction": "100",
      "displeasure": "0",
      "unanswered": "0",
      "satisfactionRate": "100%"
    },
	  {
      "id": 0,
      "area": "宜昌开发区",
      "visit": "125",
      "succ": "100",
      "rate": "80%",
      "satisfaction": "100",
      "displeasure": "0",
      "unanswered": "0",
      "satisfactionRate": "100%"
    },
	  {
      "id": 0,
      "area": "五峰县",
      "visit": "125",
      "succ": "100",
      "rate": "80%",
      "satisfaction": "100",
      "displeasure": "0",
      "unanswered": "0",
      "satisfactionRate": "100%"
    },
	  {
      "id": 0,
      "area": "兴山县",
      "visit": "125",
      "succ": "100",
      "rate": "80%",
      "satisfaction": "100",
      "displeasure": "0",
      "unanswered": "0",
      "satisfactionRate": "100%"
    },
	  {
      "id": 0,
      "area": "夷陵区",
      "visit": "125",
      "succ": "100",
      "rate": "80%",
      "satisfaction": "100",
      "displeasure": "0",
      "unanswered": "0",
      "satisfactionRate": "100%"
    },
	  {
      "id": 0,
      "area": "宜都市",
      "visit": "125",
      "succ": "100",
      "rate": "80%",
      "satisfaction": "100",
      "displeasure": "0",
      "unanswered": "0",
      "satisfactionRate": "100%"
    },
	  {
      "id": 0,
      "area": "远安县",
      "visit": "125",
      "succ": "100",
      "rate": "80%",
      "satisfaction": "100",
      "displeasure": "0",
      "unanswered": "0",
      "satisfactionRate": "100%"
    },
	  {
      "id": 0,
      "area": "长阳县",
      "visit": "125",
      "succ": "100",
      "rate": "80%",
      "satisfaction": "100",
      "displeasure": "0",
      "unanswered": "0",
      "satisfactionRate": "100%"
    },
	  {
      "id": 0,
      "area": "枝江市",
      "visit": "125",
      "succ": "100",
      "rate": "80%",
      "satisfaction": "100",
      "displeasure": "0",
      "unanswered": "0",
      "satisfactionRate": "100%"
    },
	  {
      "id": 0,
      "area": "姊归县",
      "visit": "125",
      "succ": "100",
      "rate": "80%",
      "satisfaction": "100",
      "displeasure": "0",
      "unanswered": "0",
      "satisfactionRate": "100%"
    },
	  {
      "id": 0,
      "area": "全市",
      "visit": "125",
      "succ": "100",
      "rate": "80%",
      "satisfaction": "100",
      "displeasure": "0",
      "unanswered": "0",
      "satisfactionRate": "100%"
    }
  ]
}

msg_retreat_list_right = {
  "code": 0,
  "msg": "string",
  "result": [
    {
      "id": 0,
      "area": "宜昌城区",
      "accept": "1000",
      "retreat": "0",
        "rate":"70%"
    },
	{
      "id": 0,
      "area": "当阳市",
      "accept": "1000",
      "retreat": "0",
        "rate":"70%"
    },
	{
      "id": 0,
      "area": "宜昌开发区",
      "accept": "1000",
      "retreat": "0",
        "rate":"70%"
    },
	{
      "id": 0,
      "area": "五峰县",
      "accept": "1000",
      "retreat": "0",
        "rate":"70%"
    },
	{
      "id": 0,
      "area": "兴山县",
      "accept": "1000",
      "retreat": "0",
        "rate":"70%"
    },
	{
      "id": 0,
      "area": "夷陵区",
      "accept": "1000",
      "retreat": "0",
        "rate":"70%"
    },
	{
      "id": 0,
      "area": "宜都市",
      "accept": "1000",
      "retreat": "0",
        "rate":"70%"
    },
	{
      "id": 0,
      "area": "远安县",
      "accept": "1000",
      "retreat": "0",
        "rate":"70%"
    },
	{
      "id": 0,
      "area": "长阳县",
      "accept": "1000",
      "retreat": "0",
        "rate":"70%"
    },
	{
      "id": 0,
      "area": "枝江市",
      "accept": "1000",
      "retreat": "0",
        "rate":"70%"
    },
	{
      "id": 0,
      "area": "姊归县",
      "accept": "1000",
      "retreat": "0",
        "rate":"70%"
    }
	,
	{
      "id": 0,
      "area": "全市",
      "accept": "1000",
      "retreat": "0",
        "rate":"70%"
    }
  ]
}

msg_8_list_right = {
  "code": 0,
  "msg": "string",
  "result": [
    {
      "id": 0,
      "area": "宜昌市",
      "accept": "1000",
      "complete": "800",
      "loaded": "200",
      "notLoaded": "100",
      "load_and_rate":"80%",
      "pressing": "80%",
      "rate": "50",
      "ave": "9"
    },
	 {
      "id": 0,
       "area": "宜昌市",
      "accept": "1000",
      "complete": "800",
      "loaded": "200",
      "notLoaded": "100",
"load_and_rate":"80%",
      "pressing": "80%",
      "rate": "50",
      "ave": "9"
    },
	 {
      "id": 0,
       "area": "宜昌市",
      "accept": "1000",
      "complete": "800",
      "loaded": "200",
      "notLoaded": "100",
"load_and_rate":"80%",
      "pressing": "80%",
      "rate": "50",
      "ave": "9"
    },
	 {
      "id": 0,
       "area": "宜昌市",
      "accept": "1000",
      "complete": "800",
      "loaded": "200",
      "notLoaded": "100",
"load_and_rate":"80%",
      "pressing": "80%",
      "rate": "50",
      "ave": "9"
    },
	 {
      "id": 0,
       "area": "宜昌市",
      "accept": "1000",
      "complete": "800",
      "loaded": "200",
      "notLoaded": "100",
"load_and_rate":"80%",
      "pressing": "80%",
      "rate": "50",
      "ave": "9"
    },
	 {
      "id": 0,
       "area": "宜昌市",
      "accept": "1000",
      "complete": "800",
      "loaded": "200",
      "notLoaded": "100",
"load_and_rate":"80%",
      "pressing": "80%",
      "rate": "50",
      "ave": "9"
    },
	 {
      "id": 0,
       "area": "宜昌市",
      "accept": "1000",
      "complete": "800",
      "loaded": "200",
      "notLoaded": "100",
"load_and_rate":"80%",
      "pressing": "80%",
      "rate": "50",
      "ave": "9"
    },
	 {
      "id": 0,
       "area": "宜昌市",
      "accept": "1000",
      "complete": "800",
      "loaded": "200",
      "notLoaded": "100",
"load_and_rate":"80%",
      "pressing": "80%",
      "rate": "50",
      "ave": "9"
    },
	 {
      "id": 0,
       "area": "宜昌市",
      "accept": "1000",
      "complete": "800",
      "loaded": "200",
      "notLoaded": "100",
"load_and_rate":"80%",
      "pressing": "80%",
      "rate": "50",
      "ave": "9"
    },
	 {
      "id": 0,
       "area": "宜昌市",
      "accept": "1000",
      "complete": "800",
      "loaded": "200",
      "notLoaded": "100",
"load_and_rate":"80%",
      "pressing": "80%",
      "rate": "50",
      "ave": "9"
    },
	 {
      "id": 0,
       "area": "宜昌市",
      "accept": "1000",
      "complete": "800",
      "loaded": "200",
      "notLoaded": "100",
"load_and_rate":"80%",
      "pressing": "80%",
      "rate": "50",
      "ave": "9"
    },
	 {
      "id": 0,
       "area": "宜昌市",
      "accept": "1000",
      "complete": "800",
      "loaded": "200",
      "notLoaded": "100",
"load_and_rate":"80%",
      "pressing": "80%",
      "rate": "50",
      "ave": "9"
    },
	 {
      "id": 0,
       "area": "宜昌市",
      "accept": "1000",
      "complete": "800",
      "loaded": "200",
      "notLoaded": "100",
"load_and_rate":"80%",
      "pressing": "80%",
      "rate": "50",
      "ave": "9"
    }
  ]
}


##农普及时率界面接口
def installed_agricultural_chart_get(type,starttime=None, endtime=None):  # noqa: E501
    """Installed Daily

    Installed Daily # noqa: E501

    :param starttime: the starttime for user choose
    :type starttime: str
    :param endtime: the endtime for user choose
    :type endtime: str
    :param type: the user choose type
    :type type: str

    :rtype: HomeChart
    """
    msg_reslut = []
    if starttime == '':
        starttime = '2018-01-02 00:00:00'
    if endtime == '':
        endtime = '2018-01-03 00:00:00'
    choose = type.split('_')[0]
    charttype=type.split('_')[1]

    area_list = ['秭归', '枝江', '长阳', '远安', '宜都', '夷陵', '兴山', '五峰', '开发区', '当阳', '城区']
    if str(choose) == '宽带装机':
        data = YCinstalled.select().where(
            (YCinstalled.type == 1) & (YCinstalled.accept >= utc_str_to_timestamp(starttime)) & (
                YCinstalled.accept <= utc_str_to_timestamp(endtime)) & (
            YCinstalled.areaType == '普服小区' | YCinstalled.areaType == '普遍服务'))
        data1 = YCinstalled.select().where(
            (YCinstalled.type == 1) & (YCinstalled.confirm >= utc_str_to_timestamp(starttime)) & (
                YCinstalled.confirm <= utc_str_to_timestamp(endtime)) & (YCinstalled.areaType == '普服小区' |
                                                                         YCinstalled.areaType == '普遍服务'))
        if charttype=='装机及时率':
            for i in range(len(area_list)):
                area = area_list[i]
                like = "%" + area_list[i] + "%"
                complete = data1.where(YCinstalled.area % like).count()
                loaded = data1.where(
                    (YCinstalled.area % like) & (YCinstalled.confirm != 0) & (YCinstalled.timeout == '是')).count()

                try:
                    rate = (complete - loaded) / complete
                except:
                    rate = 0
                msg = {"name": area,

                       "value": '%.2f' % (rate * 100)
                    }
                msg_reslut.append(msg)
        if charttype=='平均装机时长':
            for i in range(len(area_list)):
                area = area_list[i]
                like = "%" + area_list[i] + "%"
                complete = data1.where(YCinstalled.area % like).count()

                av_time = 0
                for item in data1.where((YCinstalled.area % like) & (YCinstalled.confirm != 0)):
                    try:
                        av_time = av_time + ((item.confirm - item.accept) / 3600)
                    except:
                        pass

                try:
                    ave = av_time / complete
                except:
                    ave = 0
                msg = {"name": area,

                       "value": '%.2f' % ave, }

                msg_reslut.append(msg)


    if str(choose) == '移机装':
        data = YCinstalled.select().where(
            (YCinstalled.type == 2) & (YCinstalled.accept >= utc_str_to_timestamp(starttime)) & (
                YCinstalled.accept <= utc_str_to_timestamp(endtime)) & (
            YCinstalled.areaType == '普服小区' | YCinstalled.areaType == '普遍服务'))
        data1 = YCinstalled.select().where(
            (YCinstalled.type == 2) & (YCinstalled.confirm >= utc_str_to_timestamp(starttime)) & (
                YCinstalled.confirm <= utc_str_to_timestamp(endtime)) & (
            YCinstalled.areaType == '普服小区' | YCinstalled.areaType == '普遍服务'))

        if charttype == '装机及时率':
            for i in range(len(area_list)):
                area = area_list[i]
                like = "%" + area_list[i] + "%"
                complete = data1.where(YCinstalled.area % like).count()
                loaded = data1.where(
                    (YCinstalled.area % like) & (YCinstalled.confirm != 0) & (YCinstalled.timeout == '是')).count()

                try:
                    rate = (complete - loaded) / complete
                except:
                    rate = 0
                msg = {"name": area,

                       "value": '%.2f' % (rate * 100)
                       }
                msg_reslut.append(msg)
        if charttype == '平均装机时长':
            for i in range(len(area_list)):
                area = area_list[i]
                like = "%" + area_list[i] + "%"
                complete = data1.where(YCinstalled.area % like).count()

                av_time = 0
                for item in data1.where((YCinstalled.area % like) & (YCinstalled.confirm != 0)):
                    try:
                        av_time = av_time + ((item.confirm - item.accept) / 3600)
                    except:
                        pass

                try:
                    ave = av_time / complete
                except:
                    ave = 0
                msg = {"name": area,

                       "value": '%.2f' % ave, }

                msg_reslut.append(msg)

    if str(choose) == 'TV单独安装':
        data = YCinstalled.select().where(
            (YCinstalled.type == 3) & (YCinstalled.accept >= utc_str_to_timestamp(starttime)) & (
                YCinstalled.accept <= utc_str_to_timestamp(endtime)) & (
            YCinstalled.areaType == '普服小区' | YCinstalled.areaType == '普遍服务'))
        data1 = YCinstalled.select().where(
            (YCinstalled.type == 3) & (YCinstalled.confirm >= utc_str_to_timestamp(starttime)) & (
                YCinstalled.confirm <= utc_str_to_timestamp(endtime)) & (
            YCinstalled.areaType == '普服小区' | YCinstalled.areaType == '普遍服务'))

        if charttype == '装机及时率':
            for i in range(len(area_list)):
                area = area_list[i]
                like = "%" + area_list[i] + "%"
                complete = data1.where(YCinstalled.area % like).count()
                loaded = data1.where(
                    (YCinstalled.area % like) & (YCinstalled.confirm != 0) & (YCinstalled.timeout == '是')).count()

                try:
                    rate = (complete - loaded) / complete
                except:
                    rate = 0
                msg = {"name": area,

                       "value": '%.2f' % (rate * 100)
                       }
                msg_reslut.append(msg)
        if charttype == '平均装机时长':
            for i in range(len(area_list)):
                area = area_list[i]
                like = "%" + area_list[i] + "%"
                complete = data1.where(YCinstalled.area % like).count()

                av_time = 0
                for item in data1.where((YCinstalled.area % like) & (YCinstalled.confirm != 0)):
                    try:
                        av_time = av_time + ((item.confirm - item.accept) / 3600)
                    except:
                        pass

                try:
                    ave = av_time / complete
                except:
                    ave = 0
                msg = {"name": area,

                       "value": '%.2f' % ave, }

                msg_reslut.append(msg)
    if str(choose) == 'IMS单独安装':
        data = YCinstalled.select().where(
            (YCinstalled.type == 4) & (YCinstalled.accept >= utc_str_to_timestamp(starttime)) & (
                YCinstalled.accept <= utc_str_to_timestamp(endtime)) & (
            YCinstalled.areaType == '普服小区' | YCinstalled.areaType == '普遍服务'))
        data1 = YCinstalled.select().where(
            (YCinstalled.type == 4) & (YCinstalled.confirm >= utc_str_to_timestamp(starttime)) & (
                YCinstalled.confirm <= utc_str_to_timestamp(endtime)) & (
            YCinstalled.areaType == '普服小区' | YCinstalled.areaType == '普遍服务'))

        if charttype == '装机及时率':
            for i in range(len(area_list)):
                area = area_list[i]
                like = "%" + area_list[i] + "%"
                complete = data1.where(YCinstalled.area % like).count()
                loaded = data1.where(
                    (YCinstalled.area % like) & (YCinstalled.confirm != 0) & (YCinstalled.timeout == '是')).count()

                try:
                    rate = (complete - loaded) / complete
                except:
                    rate = 0
                msg = {"name": area,

                       "value": '%.2f' % (rate * 100)
                       }
                msg_reslut.append(msg)
        if charttype == '平均装机时长':
            for i in range(len(area_list)):
                area = area_list[i]
                like = "%" + area_list[i] + "%"
                complete = data1.where(YCinstalled.area % like).count()

                av_time = 0
                for item in data1.where((YCinstalled.area % like) & (YCinstalled.confirm != 0)):
                    try:
                        av_time = av_time + ((item.confirm - item.accept) / 3600)
                    except:
                        pass

                try:
                    ave = av_time / complete
                except:
                    ave = 0
                msg = {"name": area,

                       "value": '%.2f' % ave, }

                msg_reslut.append(msg)
    if str(choose) == '全量工单':
        print('----')
        data = YCinstalled.select().where((YCinstalled.accept >= utc_str_to_timestamp(starttime)) & (
            YCinstalled.accept <= utc_str_to_timestamp(endtime)) & (
                                          YCinstalled.areaType == '普服小区' | YCinstalled.areaType == '普遍服务'))
        data1 = YCinstalled.select().where((YCinstalled.confirm >= utc_str_to_timestamp(starttime)) & (
            YCinstalled.confirm <= utc_str_to_timestamp(endtime)) & (
                                           YCinstalled.areaType == '普服小区' | YCinstalled.areaType == '普遍服务'))

        if charttype == '装机及时率':
            for i in range(len(area_list)):
                area = area_list[i]
                like = "%" + area_list[i] + "%"
                complete = data1.where(YCinstalled.area % like).count()
                loaded = data1.where(
                    (YCinstalled.area % like) & (YCinstalled.confirm != 0) & (YCinstalled.timeout == '是')).count()

                try:
                    rate = (complete - loaded) / complete
                except:
                    rate = 0
                msg = {"name": area,

                       "value": '%.2f' % (rate * 100)
                       }
                msg_reslut.append(msg)
        if charttype == '平均装机时长':
            for i in range(len(area_list)):
                area = area_list[i]
                like = "%" + area_list[i] + "%"
                complete = data1.where(YCinstalled.area % like).count()

                av_time = 0
                for item in data1.where((YCinstalled.area % like) & (YCinstalled.confirm != 0)):
                    try:
                        av_time = av_time + ((item.confirm - item.accept) / 3600)
                    except:
                        pass

                try:
                    ave = av_time / complete
                except:
                    ave = 0
                msg = {"name": area,

                       "value": '%.2f' % ave, }

                msg_reslut.append(msg)

    msg = {"code": 0, "msg": "success", "result": msg_reslut}

    # except:
    #     msg = {"code": -1, "msg": "Error"}
    # print(msg)
    return msg
def installed_agricultural_info_export_get(type):  # noqa: E501
    """eight hour complaint daily list export

    eight hour complaint daily list export # noqa: E501

    :param type: the type for user choose
    :type type: str

    :rtype: DownUrl
    """
    starttime = type.split('_')[0]
    endtime = type.split('_')[1]
    area = type.split('_')[2]
    choose_type = type.split('_')[3]
    data_type = type.split('_')[4]
    if starttime == '':
        starttime = '2018-01-02 00:00:00'
    if endtime == '':
        endtime = '2018-01-03 00:00:00'
    url = agricultural_export(starttime, endtime, choose_type, area, data_type)
    msg = {"code": 0, "msg": 'success', "url": url}
    return msg
def installed_agricultural_list_export_get(type,starttime=None, endtime=None):  # noqa: E501
    """eight hour complaint daily list export

    eight hour complaint daily list export # noqa: E501

    :param starttime: the starttime for user choose
    :type starttime: str
    :param endtime: the endtime for user choose
    :type endtime: str
    :param type: the type for user choose
    :type type: str

    :rtype: DownUrl
    """
    try:
        if starttime == '':
            starttime = '2018-01-02 00:00:00'
        if endtime == '':
            endtime = '2018-01-03 00:00:00'
        starttime = str(starttime)
        endtime = str(endtime)
        file_path =type.split('_')[0].replace('mail.itlaolang.com/downfile/','/var/www/downfile/')
        url = make_file(file_path, type='农普及时率', starttime=starttime, endtime=endtime, choose_type=type.split('_')[1])

        msg = {"code": 0, "msg": "success", "url": url}
    except:
        msg = {"code": -1, "msg": "Error"}
    return msg
def installed_agricultural_list_get(type,starttime=None, endtime=None):  # noqa: E501
    """Installed Daily

    Installed Daily # noqa: E501

    :param starttime: the starttime for user choose
    :type starttime: str
    :param endtime: the endtime for user choose
    :type endtime: str
    :param type: the type for user choose
    :type type: str

    :rtype: InstalledList
    """
    msg_reslut = []
    if starttime == '':
        starttime = '2018-01-02 00:00:00'
    if endtime == '':
        endtime = '2018-01-03 00:00:00'
    choose = type

    area_list = ['秭归', '枝江', '长阳', '远安', '宜都', '夷陵', '兴山', '五峰', '开发区', '当阳', '城区']
    if str(choose) == '宽带装机':
        data = YCinstalled.select().where(
            (YCinstalled.type == 1) & (YCinstalled.accept >= utc_str_to_timestamp(starttime)) & (
                YCinstalled.accept <= utc_str_to_timestamp(endtime)) & (YCinstalled.areaType == '普服小区' | YCinstalled.areaType == '普遍服务'))
        data1 = YCinstalled.select().where(
            (YCinstalled.type == 1) & (YCinstalled.confirm >= utc_str_to_timestamp(starttime)) & (
                YCinstalled.confirm <= utc_str_to_timestamp(endtime)) & (YCinstalled.areaType == '普服小区' |
                YCinstalled.areaType == '普遍服务'))

        for i in range(len(area_list)):
            area = area_list[i]
            like = "%" + area_list[i] + "%"

            accept = data.where(YCinstalled.area % like).count()

            complete = data1.where(YCinstalled.area % like).count()
            loaded = data1.where(
                (YCinstalled.area % like) & (YCinstalled.confirm != 0) & (YCinstalled.timeout == '是')).count()
            notLoaded = data.where((YCinstalled.area % like) & (YCinstalled.confirm == 0)).count()
            pressing = 0

            try:
                rate = (complete - loaded) / complete
            except:
                rate = 0

            av_time = 0
            for item in data1.where((YCinstalled.area % like) & (YCinstalled.confirm != 0)):
                try:
                    av_time = av_time + ((item.confirm - item.accept) / 3600)
                    print(av_time)
                except:
                    pass

            try:
                ave = av_time / complete
            except:
                ave=0
            msg = {"area": area,
                   "accept": accept,
                   "complete": complete,
                   "loaded": loaded,
                   "notLoaded": notLoaded,
                   "pressing": pressing,
                   "rate": str('%.2f' % (rate * 100)) + '%',
                   "ave": '%.2f' % ave, }
            print(msg)
            msg_reslut.append(msg)
    if str(choose) == '移机装':
        data = YCinstalled.select().where(
            (YCinstalled.type == 2) & (YCinstalled.accept >= utc_str_to_timestamp(starttime)) & (
                YCinstalled.accept <= utc_str_to_timestamp(endtime)) & (YCinstalled.areaType == '普服小区' | YCinstalled.areaType == '普遍服务'))
        data1 = YCinstalled.select().where(
            (YCinstalled.type == 2) & (YCinstalled.confirm >= utc_str_to_timestamp(starttime)) & (
                YCinstalled.confirm <= utc_str_to_timestamp(endtime)) & (YCinstalled.areaType == '普服小区' | YCinstalled.areaType == '普遍服务'))

        for i in range(len(area_list)):
            area = area_list[i]
            like = "%" + area_list[i] + "%"

            accept = data.where(YCinstalled.area % like).count()

            complete = data1.where(YCinstalled.area % like).count()
            loaded = data1.where(
                (YCinstalled.area % like) & (YCinstalled.confirm != 0) & (YCinstalled.timeout == '是')).count()
            notLoaded = data.where((YCinstalled.area % like) & (YCinstalled.confirm == 0)).count()
            pressing = 0

            try:
                rate = (complete - loaded) / complete
            except:
                rate = 0

            av_time = 0
            for item in data1.where((YCinstalled.area % like) & (YCinstalled.confirm != 0)):
                try:
                    av_time = av_time + ((item.confirm - item.accept) / 3600)
                    print(av_time)
                except:
                    pass

            try:
                ave = av_time / complete
            except:
                ave = 0
            msg = {"area": area,
                   "accept": accept,
                   "complete": complete,
                   "loaded": loaded,
                   "notLoaded": notLoaded,
                   "pressing": pressing,
                   "rate": str('%.2f' % (rate * 100)) + '%',
                   "ave": '%.2f' % ave, }
            print(msg)
            msg_reslut.append(msg)

    if str(choose) == 'TV单独安装':
        data = YCinstalled.select().where(
            (YCinstalled.type == 3) & (YCinstalled.accept >= utc_str_to_timestamp(starttime)) & (
                YCinstalled.accept <= utc_str_to_timestamp(endtime)) & (YCinstalled.areaType == '普服小区' | YCinstalled.areaType == '普遍服务'))
        data1 = YCinstalled.select().where(
            (YCinstalled.type == 3) & (YCinstalled.confirm >= utc_str_to_timestamp(starttime)) & (
                YCinstalled.confirm <= utc_str_to_timestamp(endtime)) & (YCinstalled.areaType == '普服小区' | YCinstalled.areaType == '普遍服务'))

        for i in range(len(area_list)):
            area = area_list[i]
            like = "%" + area_list[i] + "%"

            accept = data.where(YCinstalled.area % like).count()

            complete = data1.where(YCinstalled.area % like).count()
            loaded = data1.where(
                (YCinstalled.area % like) & (YCinstalled.confirm != 0) & (YCinstalled.timeout == '是')).count()
            notLoaded = data.where((YCinstalled.area % like) & (YCinstalled.confirm == 0)).count()
            pressing = 0

            try:
                rate = (complete - loaded) / complete
            except:
                rate = 0

            av_time = 0
            for item in data1.where((YCinstalled.area % like) & (YCinstalled.confirm != 0)):
                try:
                    av_time = av_time + ((item.confirm - item.accept) / 3600)
                    print(av_time)
                except:
                    pass
            try:
                ave = av_time / complete
            except:
                ave = 0
            msg = {"area": area,
                   "accept": accept,
                   "complete": complete,
                   "loaded": loaded,
                   "notLoaded": notLoaded,
                   "pressing": pressing,
                   "rate": str('%.2f' % (rate * 100)) + '%',
                   "ave": '%.2f' % ave, }
            print(msg)
            msg_reslut.append(msg)
    if str(choose) == 'IMS单独安装':
        data = YCinstalled.select().where(
            (YCinstalled.type == 4) & (YCinstalled.accept >= utc_str_to_timestamp(starttime)) & (
                YCinstalled.accept <= utc_str_to_timestamp(endtime)) & (YCinstalled.areaType == '普服小区' | YCinstalled.areaType == '普遍服务'))
        data1 = YCinstalled.select().where(
            (YCinstalled.type == 4) & (YCinstalled.confirm >= utc_str_to_timestamp(starttime)) & (
                YCinstalled.confirm <= utc_str_to_timestamp(endtime)) & (YCinstalled.areaType == '普服小区' | YCinstalled.areaType == '普遍服务'))

        for i in range(len(area_list)):
            area = area_list[i]
            like = "%" + area_list[i] + "%"

            accept = data.where(YCinstalled.area % like).count()

            complete = data1.where(YCinstalled.area % like).count()
            loaded = data1.where(
                (YCinstalled.area % like) & (YCinstalled.confirm != 0) & (YCinstalled.timeout == '是')).count()
            notLoaded = data.where((YCinstalled.area % like) & (YCinstalled.confirm == 0)).count()
            pressing = 0

            try:
                rate = (complete - loaded) / complete
            except:
                rate = 0

            av_time = 0
            for item in data1.where((YCinstalled.area % like) & (YCinstalled.confirm != 0)):
                try:
                    av_time = av_time + ((item.confirm - item.accept) / 3600)
                    print(av_time)
                except:
                    pass

            try:
                ave = av_time / complete
            except:
                ave = 0

            msg = {"area": area,
                   "accept": accept,
                   "complete": complete,
                   "loaded": loaded,
                   "notLoaded": notLoaded,
                   "pressing": pressing,
                   "rate": str('%.2f' % (rate * 100)) + '%',
                   "ave": '%.2f' % ave, }
            print(msg)
            msg_reslut.append(msg)
    if str(choose) == '全量工单':
        print('----')
        data = YCinstalled.select().where((YCinstalled.accept >= utc_str_to_timestamp(starttime)) & (
            YCinstalled.accept <= utc_str_to_timestamp(endtime)) & (YCinstalled.areaType == '普服小区' | YCinstalled.areaType == '普遍服务'))
        data1 = YCinstalled.select().where((YCinstalled.confirm >= utc_str_to_timestamp(starttime)) & (
            YCinstalled.confirm <= utc_str_to_timestamp(endtime)) & (YCinstalled.areaType == '普服小区' | YCinstalled.areaType == '普遍服务'))

        for i in range(len(area_list)):
            av_time = 0
            area = area_list[i]
            like = "%" + area_list[i] + "%"

            accept = data.where(YCinstalled.area % like).count()

            complete = data1.where(YCinstalled.area % like).count()
            loaded = data1.where(
                (YCinstalled.area % like) & (YCinstalled.confirm != 0) & (YCinstalled.timeout == '是')).count()

            notLoaded = data.where((YCinstalled.area % like) & (YCinstalled.confirm == 0)).count()
            pressing = 0

            try:
                rate = (complete - loaded) / complete
            except:
                rate = 0

            for item in data1.where((YCinstalled.area % like) & (YCinstalled.confirm != 0)):
                try:
                    av_time = av_time + ((item.confirm - item.accept) / 3600)

                except:
                    pass
            try:
                ave = av_time / complete
            except:
                ave = 0
            msg = {"area": area,
                   "accept": accept,
                   "complete": complete,
                   "loaded": loaded,
                   "notLoaded": notLoaded,
                   "pressing": pressing,
                   "rate": str('%.2f' % (rate * 100)) + '%',
                   "ave": '%.2f' % ave, }
            msg_reslut.append(msg)

    msg = {"code": 0, "msg": "success", "result": msg_reslut}

    # except:
    #     msg = {"code": -1, "msg": "Error"}
    # print(msg)
    return msg


##装机8小时日报界面接口
def installed_eight_chart_get(type,starttime=None, endtime=None):  # noqa: E501
    """Installed Daily

    Installed Daily # noqa: E501

    :param starttime: the starttime for user choose
    :type starttime: str
    :param endtime: the endtime for user choose
    :type endtime: str
    :param type: the user choose type
    :type type: str

    :rtype: HomeChart
    """
    msg_reslut=[]
    area_list = ['秭归', '枝江', '长阳', '远安', '宜都', '夷陵', '兴山', '五峰', '开发区', '当阳', '城区']
    if starttime == '':
        starttime = '2018-01-02 00:00:00'
    if endtime == '':
        endtime = '2018-01-03 00:00:00'

    if type == '880装机及时率':
        print ('------------------------------')
        data = YCinstalled.select().where(
            (YCinstalled.type == 1) & (YCinstalled.accept >= utc_str_to_timestamp(starttime)) & (
                YCinstalled.accept <= utc_str_to_timestamp(endtime)) & (YCinstalled.areaType != '普服小区') & (
                YCinstalled.areaType != '普遍服务'))
        data1 = YCinstalled.select().where(
            (YCinstalled.type == 1) & (YCinstalled.confirm >= utc_str_to_timestamp(starttime)) & (
                YCinstalled.confirm <= utc_str_to_timestamp(endtime)) & (YCinstalled.areaType != '普服小区') & (
                YCinstalled.areaType != '普遍服务'))

        for i in range(len(area_list)):
            av_time = 0
            area = area_list[i]
            like = "%" + area + "%"

            accept = data.where(YCinstalled.area % like).count()

            complete = data1.where(YCinstalled.area % like).count()
            loaded = data1.where(
                (YCinstalled.area % like) & (YCinstalled.confirm != 0) & (
                    YCinstalled.timeout == '是')).count()
            loaded1 = data1.where(
                (YCinstalled.area % like) & (YCinstalled.confirm != 0) & (
                    YCinstalled.confirm - YCinstalled.accept >= 20 * 60 * 60)).count()
            notLoaded = data.where((YCinstalled.area % like) & (YCinstalled.confirm == 0)).count()
            pressing = 0
            # 标准
            try:
                rate = (complete - loaded) / complete
            except:
                rate = 0
            # 880及时率
            try:
                rate1 = (complete - loaded1) / complete
            except:
                rate1 = 0

            for item in data1.where((YCinstalled.area % like) & (YCinstalled.confirm != 0)):
                try:

                    av_time = av_time + ((item.confirm - item.accept) / 3600)

                except:
                    pass

            try:
                ave = av_time / complete
            except:
                ave = 0
            msg = {"name": area,

                   "value": '%.2f' % (rate1 * 100) ,
                    }
            msg_reslut.append(msg)
    if type == '平均装机时长':
        data = YCinstalled.select().where(
            (YCinstalled.type == 1) & (YCinstalled.accept >= utc_str_to_timestamp(starttime)) & (
                YCinstalled.accept <= utc_str_to_timestamp(endtime)) & (YCinstalled.areaType != '普服小区') & (
                YCinstalled.areaType != '普遍服务'))
        data1 = YCinstalled.select().where(
            (YCinstalled.type == 1) & (YCinstalled.confirm >= utc_str_to_timestamp(starttime)) & (
                YCinstalled.confirm <= utc_str_to_timestamp(endtime)) & (YCinstalled.areaType != '普服小区') & (
                YCinstalled.areaType != '普遍服务'))

        for i in range(len(area_list)):
            av_time = 0
            area = area_list[i]
            like = "%" + area + "%"

            accept = data.where(YCinstalled.area % like).count()

            complete = data1.where(YCinstalled.area % like).count()
            loaded = data1.where(
                (YCinstalled.area % like) & (YCinstalled.confirm != 0) & (
                    YCinstalled.timeout == '是')).count()
            loaded1 = data1.where(
                (YCinstalled.area % like) & (YCinstalled.confirm != 0) & (
                    YCinstalled.confirm - YCinstalled.accept >= 20 * 60 * 60)).count()
            notLoaded = data.where((YCinstalled.area % like) & (YCinstalled.confirm == 0)).count()
            pressing = 0
            # 标准
            try:
                rate = (complete - loaded) / complete
            except:
                rate = 0
            # 880及时率
            try:
                rate1 = (complete - loaded1) / complete
            except:
                rate1 = 0

            for item in data1.where((YCinstalled.area % like) & (YCinstalled.confirm != 0)):
                try:

                    av_time = av_time + ((item.confirm - item.accept) / 3600)

                except:
                    pass

            try:
                ave = av_time / complete
            except:
                ave = 0
            msg = {"name": area,


                   "value": '%.2f' % ave, }



            msg_reslut.append(msg)
    if type=='880装机及时率(含压单)':
        msg_reslut = []
        data = YCinstalled.select().where((YCinstalled.accept >= utc_str_to_timestamp(starttime)) & (
            YCinstalled.accept <= utc_str_to_timestamp(endtime)) & (YCinstalled.areaType != '普服小区') & (
                                              YCinstalled.areaType != '普遍服务'))
        data1 = YCinstalled.select().where((YCinstalled.confirm >= utc_str_to_timestamp(starttime)) & (
            YCinstalled.confirm <= utc_str_to_timestamp(endtime)) & (YCinstalled.areaType != '普服小区') & (
                                               YCinstalled.areaType != '普遍服务'))

        for i in range(len(area_list)):
            av_time = 0
            area = area_list[i]
            like = "%" + area + "%"

            complete = data1.where(YCinstalled.area % like).count()

            loaded1 = data1.where(
                (YCinstalled.area % like) & (YCinstalled.confirm != 0) & (
                    YCinstalled.confirm - YCinstalled.accept >= 20 * 60 * 60)).count()

            # 880及时率
            try:
                rate1 = (complete - loaded1) / complete
            except:
                rate1 = 0

            msg = {"name": area,

                   "value": '%.2f' % (rate1 * 100),
                   }
            msg_reslut.append(msg)
    msg = {"code": 0, "msg": "success", "result": msg_reslut}
    # except:
    #     msg={"code":-1,"msg":"Error"}
    return msg
def installed_eight_info_export_get(type):  # noqa: E501
    """eight hour complaint daily list export

    eight hour complaint daily list export # noqa: E501

    :param type: the type for user choose
    :type type: str

    :rtype: DownUrl
    """
    print(type)
    type_list = type.split('_')
    starttime = type_list[0]
    endtime = type_list[1]
    if starttime == '':
        starttime = '2018-01-02 00:00:00'
    if endtime == '':
        endtime = '2018-01-03 00:00:00'
    choose_type = type_list[3]
    area = type_list[2]
    datatype = type_list[4]
    url = installed_export_8(starttime=starttime, endtime=endtime, choose_type=choose_type, area=area, datatype=datatype)
    print (url)
    msg = {"code": 0, "msg": "success", "url": url}
    return msg
def installed_eight_list_export_get(type,starttime=None, endtime=None):  # noqa: E501
    """eight hour complaint daily list export

    eight hour complaint daily list export # noqa: E501

    :param starttime: the starttime for user choose
    :type starttime: str
    :param endtime: the endtime for user choose
    :type endtime: str
    :param type: the type for user choose
    :type type: str

    :rtype: DownUrl
    """
    try:
        if starttime == '':
            starttime = '2018-01-02 00:00:00'
        if endtime == '':
            endtime = '2018-01-03 00:00:00'
        starttime = str(starttime)
        endtime = str(endtime)
        file_path =type.split('_')[0].replace('mail.itlaolang.com/downfile/','/var/www/downfile/')
        url = make_file(file_path, type='装机8小时报表', starttime=starttime, endtime=endtime, choose_type=type.split('_')[1])

        msg = {"code": 0, "msg": "success", "url": url}
    except:
        msg = {"code": -1, "msg": "Error"}
    return msg
def installed_eight_list_get(type,starttime=None, endtime=None):  # noqa: E501
    """Installed Daily

    Installed Daily # noqa: E501

    :param starttime: the starttime for user choose
    :type starttime: str
    :param endtime: the endtime for user choose
    :type endtime: str
    :param type: the type for user choose
    :type type: str

    :rtype: InstalledList
    """
    msg_reslut=[]
    if starttime == '':
        starttime = '2018-01-02 00:00:00'
    if endtime == '':
        endtime = '2018-01-03 00:00:00'
    choose = type
    print(str(choose))
    area_list = ['秭归', '枝江', '长阳', '远安', '宜都', '夷陵', '兴山', '五峰', '开发区', '当阳', '城区']
    if str(choose) == '宽带装机':

        data = YCinstalled.select().where(
            (YCinstalled.type == 1) & (YCinstalled.accept >= utc_str_to_timestamp(starttime)) & (
                YCinstalled.accept <= utc_str_to_timestamp(endtime)) & (YCinstalled.areaType != '普服小区') & (
                YCinstalled.areaType != '普遍服务'))
        data1 = YCinstalled.select().where(
            (YCinstalled.type == 1) & (YCinstalled.confirm >= utc_str_to_timestamp(starttime)) & (
                YCinstalled.confirm <= utc_str_to_timestamp(endtime)) & (YCinstalled.areaType != '普服小区') & (
                YCinstalled.areaType != '普遍服务'))

        for i in range(len(area_list)):
            av_time=0
            area = area_list[i]
            like = "%" + area+ "%"

            accept = data.where(YCinstalled.area % like).count()

            complete = data1.where(YCinstalled.area % like).count()
            loaded = data1.where(
                (YCinstalled.area % like) & (YCinstalled.confirm != 0) & (
                            YCinstalled.timeout=='是')).count()
            loaded1 = data1.where(
                (YCinstalled.area % like) & (YCinstalled.confirm != 0) & (
                            YCinstalled.confirm - YCinstalled.accept >= 20 * 60 * 60)).count()
            notLoaded = data.where((YCinstalled.area % like) & (YCinstalled.confirm == 0)).count()
            pressing = 0
            # 标准
            try:
                rate = (complete - loaded) / complete
            except:
                rate = 0
            # 880及时率
            try:
                rate1 = (complete - loaded1) / complete
            except:
                rate1 = 0

            for item in data1.where((YCinstalled.area % like) & (YCinstalled.confirm != 0)):
                try:

                    av_time = av_time + ((item.confirm - item.accept) / 3600)

                except:
                    pass

            try:
                ave = av_time / complete
            except:
                ave=0
            msg = {"area": area,
                   "accept": accept,
                   "complete": complete,
                   "loaded": loaded1,
                   "notLoaded": notLoaded,
                   "load_and_rate": str('%.2f' % (rate1 * 100)) + '%',
                   "pressing": pressing,
                   "rate": str('%.2f' % (rate1 * 100)) + '%',
                   "ave": '%.2f' % ave, }

            msg_reslut.append(msg)
    if str(choose) == '移机装':
        data = YCinstalled.select().where(
            (YCinstalled.type == 2) & (YCinstalled.accept >= utc_str_to_timestamp(starttime)) & (
                YCinstalled.accept <= utc_str_to_timestamp(endtime)) & (YCinstalled.areaType != '普服小区') & (
                YCinstalled.areaType != '普遍服务'))
        data1 = YCinstalled.select().where(
            (YCinstalled.type == 2) & (YCinstalled.confirm >= utc_str_to_timestamp(starttime)) & (
                YCinstalled.confirm <= utc_str_to_timestamp(endtime)) & (YCinstalled.areaType != '普服小区') & (
                YCinstalled.areaType != '普遍服务'))

        for i in range(len(area_list)):
            av_time=0
            area = area_list[i]
            like = "%" + area+ "%"

            accept = data.where(YCinstalled.area % like).count()

            complete = data1.where(YCinstalled.area % like).count()
            loaded = data1.where(
                (YCinstalled.area % like) & (YCinstalled.confirm != 0) & (
                            YCinstalled.confirm - YCinstalled.accept >= 20 * 60 * 60)).count()
            loaded1 = data1.where(
                (YCinstalled.area % like) & (YCinstalled.confirm != 0) & (
                            YCinstalled.confirm - YCinstalled.accept >= 20 * 60 * 60)).count()
            notLoaded = data.where((YCinstalled.area % like) & (YCinstalled.confirm == 0)).count()
            pressing = 0
            # 标准
            try:
                rate = (complete - loaded) / complete
            except:
                rate = 0
            # 880及时率
            try:
                rate1 = (complete - loaded1) / complete
            except:
                rate1 = 0

            for item in data1.where((YCinstalled.area % like) & (YCinstalled.confirm != 0) ):
                try:

                    av_time = av_time + ((item.confirm - item.accept) / 3600)

                except:
                    pass

            ave = av_time / complete
            msg = {"area": area,
                   "accept": accept,
                   "complete": complete,
                   "loaded": loaded1,
                   "notLoaded": notLoaded,
                   "load_and_rate": str('%.2f' % (rate1 * 100)) + '%',
                   "pressing": pressing,
                   "rate": str('%.2f' % (rate1 * 100)) + '%',
                   "ave": '%.2f' % ave, }

            msg_reslut.append(msg)
    if str(choose) == '和TV单独安装':
        data = YCinstalled.select().where(
            (YCinstalled.type == 3) & (YCinstalled.accept >= utc_str_to_timestamp(starttime)) & (
                YCinstalled.accept <= utc_str_to_timestamp(endtime)) & (YCinstalled.areaType != '普服小区') & (
                YCinstalled.areaType != '普遍服务'))
        data1 = YCinstalled.select().where(
            (YCinstalled.type == 3) & (YCinstalled.confirm >= utc_str_to_timestamp(starttime)) & (
                YCinstalled.confirm <= utc_str_to_timestamp(endtime)) & (YCinstalled.areaType != '普服小区') & (
                YCinstalled.areaType != '普遍服务'))

        for i in range(len(area_list)):
            av_time=0
            area = area_list[i]
            like = "%" + area+ "%"

            accept = data.where(YCinstalled.area % like).count()

            complete = data1.where(YCinstalled.area % like).count()
            loaded = data1.where(
                (YCinstalled.area % like) & (YCinstalled.confirm != 0) & (
                            YCinstalled.confirm - YCinstalled.accept >= 20 * 60 * 60)).count()
            loaded1 = data1.where(
                (YCinstalled.area % like) & (YCinstalled.confirm != 0) & (
                            YCinstalled.confirm - YCinstalled.accept >= 20 * 60 * 60)).count()
            notLoaded = data.where((YCinstalled.area % like) & (YCinstalled.confirm == 0)).count()
            pressing = 0
            # 标准
            try:
                rate = (complete - loaded) / complete
            except:
                rate = 0
            # 880及时率
            try:
                rate1 = (complete - loaded1) / complete
            except:
                rate1 = 0

            for item in data1.where((YCinstalled.area % like) & (YCinstalled.confirm != 0) ):
                try:

                    av_time = av_time + ((item.confirm - item.accept) / 3600)

                except:
                    pass

            ave = av_time / complete
            msg = {"area": area,
                   "accept": accept,
                   "complete": complete,
                   "loaded": loaded1,
                   "notLoaded": notLoaded,
                   "load_and_rate": str('%.2f' % (rate1 * 100)) + '%',
                   "pressing": pressing,
                   "rate": str('%.2f' % (rate1 * 100)) + '%',
                   "ave": '%.2f' % ave, }

            msg_reslut.append(msg)
    if str(choose) == 'IMS单独安装':
        data = YCinstalled.select().where(
            (YCinstalled.type == 4) & (YCinstalled.accept >= utc_str_to_timestamp(starttime)) & (
                YCinstalled.accept <= utc_str_to_timestamp(endtime)) & (YCinstalled.areaType != '普服小区') & (
                YCinstalled.areaType != '普遍服务'))
        data1 = YCinstalled.select().where(
            (YCinstalled.type == 4) & (YCinstalled.confirm >= utc_str_to_timestamp(starttime)) & (
                YCinstalled.confirm <= utc_str_to_timestamp(endtime)) & (YCinstalled.areaType != '普服小区') & (
                YCinstalled.areaType != '普遍服务'))

        for i in range(len(area_list)):
            av_time=0
            area = area_list[i]
            like = "%" + area+ "%"

            accept = data.where(YCinstalled.area % like).count()

            complete = data1.where(YCinstalled.area % like).count()
            loaded = data1.where(
                (YCinstalled.area % like) & (YCinstalled.confirm != 0) & (
                            YCinstalled.confirm - YCinstalled.accept >= 20 * 60 * 60)).count()
            loaded1 = data1.where(
                (YCinstalled.area % like) & (YCinstalled.confirm != 0) & (
                            YCinstalled.confirm - YCinstalled.accept >= 20 * 60 * 60)).count()
            notLoaded = data.where((YCinstalled.area % like) & (YCinstalled.confirm == 0)).count()
            pressing = 0
            # 标准
            try:
                rate = (complete - loaded) / complete
            except:
                rate = 0
            # 880及时率
            try:
                rate1 = (complete - loaded1) / complete
            except:
                rate1 = 0

            for item in data1.where((YCinstalled.area % like) & (YCinstalled.confirm != 0)):
                try:

                    av_time = av_time + ((item.confirm - item.accept) / 3600)

                except:
                    pass

            ave = av_time / complete
            msg = {"area": area,
                   "accept": accept,
                   "complete": complete,
                   "loaded": loaded1,
                   "notLoaded": notLoaded,
                   "load_and_rate": str('%.2f' % (rate1 * 100)) + '%',
                   "pressing": pressing,
                   "rate": str('%.2f' % (rate1 * 100)) + '%',
                   "ave": '%.2f' % ave, }

            msg_reslut.append(msg)
    if str(choose) == '全量工单':

        data = YCinstalled.select().where((YCinstalled.accept >= utc_str_to_timestamp(starttime)) & (
            YCinstalled.accept <= utc_str_to_timestamp(endtime)) & (YCinstalled.areaType != '普服小区') & (
                                              YCinstalled.areaType != '普遍服务'))
        data1 = YCinstalled.select().where((YCinstalled.confirm >= utc_str_to_timestamp(starttime)) & (
            YCinstalled.confirm <= utc_str_to_timestamp(endtime)) & (YCinstalled.areaType != '普服小区') & (
                                               YCinstalled.areaType != '普遍服务'))

        for i in range(len(area_list)):
            av_time=0
            area = area_list[i]
            like = "%" + area+ "%"

            accept = data.where(YCinstalled.area % like).count()

            complete = data1.where(YCinstalled.area % like).count()
            loaded = data1.where(
                (YCinstalled.area % like) & (YCinstalled.confirm != 0) & (
                            YCinstalled.confirm - YCinstalled.accept >= 20 * 60 * 60)).count()
            loaded1 = data1.where(
                (YCinstalled.area % like) & (YCinstalled.confirm != 0) & (
                            YCinstalled.confirm - YCinstalled.accept >= 20 * 60 * 60)).count()
            notLoaded = data.where((YCinstalled.area % like) & (YCinstalled.confirm == 0)).count()
            pressing = 0
            # 标准
            try:
                rate = (complete - loaded) / complete
            except:
                rate = 0
            # 880及时率
            try:
                rate1 = (complete - loaded1) / complete
            except:
                rate1 = 0

            for item in data1.where((YCinstalled.area % like) & (YCinstalled.confirm != 0)):
                try:

                    av_time = av_time + ((item.confirm - item.accept) / 3600)

                except:
                    pass

            ave = av_time / complete
            msg = {"area": area,
                   "accept": accept,
                   "complete": complete,
                   "loaded": loaded1,
                   "notLoaded": notLoaded,
                   "load_and_rate": str('%.2f' % (rate1 * 100)) + '%',
                   "pressing": pressing,
                   "rate": str('%.2f' % (rate1 * 100)) + '%',
                   "ave": '%.2f' % ave, }
            msg_reslut.append(msg)

    msg = {"code": 0, "msg": "success", "result": msg_reslut}


    # except:
    #     msg = {"code": -1, "msg": "Error"}
    # #print(msg)
    return msg


##接单及时率界面接口
def installed_orders_chart_get(type,starttime=None, endtime=None):  # noqa: E501
    """Installed Daily

    Installed Daily # noqa: E501

    :param starttime: the starttime for user choose
    :type starttime: str
    :param endtime: the endtime for user choose
    :type endtime: str
    :param type: the user choose type
    :type type: str

    :rtype: HomeChart
    """
    charttype=type.split('_')[1]
    datatype=type.split('_')[0]
    print(charttype,datatype)
    if starttime == '':
        starttime = '2018-01-02 00:00:00'
    if endtime == '':
        endtime = '2018-01-03 00:00:00'
    area_list = ['秭归', '枝江', '长阳', '远安', '宜都', '夷陵', '兴山', '五峰', '开发区', '当阳', '城区']

    if datatype == '宽带装机':
        gdtype = 1
    if datatype == '和TV':
        gdtype = 3
    if datatype == '移装机':
        gdtype = 2
    if datatype == 'IMS装机':
        gdtype = 4
    # else:
    #     gdtype = 0
    if gdtype != 0:
        dataall = YCinstalled.select().where(
            (YCinstalled.type== gdtype) & (YCinstalled.accept >= utc_str_to_timestamp(starttime)) & (
            YCinstalled.confirm <= utc_str_to_timestamp(endtime)))
    else:
        dataall = YCinstalled.select().where((YCinstalled.accept >= utc_str_to_timestamp(starttime)) & (
        YCinstalled.confirm <= utc_str_to_timestamp(endtime)))
    result = []
    if charttype=='接单时长':
        for area in area_list:
            av_time = 0
            like = "%" + area + '%'
            data = dataall.where(YCinstalled.area % like)
            for item in data:
                try:
                    av_time = ((item.orders - item.accept) / 3600) + av_time
                except:
                    av_time = av_time
            total = data.count()
            oneToTwo = data.where((YCinstalled.orders - YCinstalled.accept) / 3600 <= 2).count()

            msg_list = {"area": area,
                        "inside": oneToTwo,
                        "ultra": total-oneToTwo}
            result.append(msg_list)
    if charttype=='接单时长占比':
        for area in area_list:
            av_time = 0
            like = "%" + area + '%'
            data = dataall.where(YCinstalled.area % like)
            for item in data:
                try:
                    av_time = ((item.orders - item.accept) / 3600) + av_time
                except:
                    av_time = av_time
            total = data.count()

            oneToTwo = data.where((YCinstalled.orders - YCinstalled.accept) / 3600 <= 2).count()
            try:
                oneToTwo_1 =  oneToTwo / total
            except:
                oneToTwo_1 = 0.00

            msg_list = {"area": area,
                        "inside": '%.2f' % (oneToTwo_1*100),
                        "ultra": '%.2f' % ((1-oneToTwo_1)*100)}
            result.append(msg_list)
    if charttype=='接单平均时长':
        for area in area_list:
            av_time = 0
            like = "%" + area + '%'
            data = dataall.where(YCinstalled.area % like)
            for item in data:
                if item.orders==0:
                    item.orders=item.accept
                try:
                    av_time = ((item.orders - item.accept) / 3600) + av_time
                except:
                    av_time = av_time
            total = data.count()
            try:
                avtime = av_time / total
            except:
                avtime = 0

            msg_list = {"area": area,
                        'ultra':  'none',
                        'inside': '%.2f' % avtime}
            result.append(msg_list)



    msg = {"code": 0, "msg": "success", "result": result}
    return msg

def installed_orders_info_export_get(type):  # noqa: E501
    """eight hour complaint daily list export

    eight hour complaint daily list export # noqa: E501

    :param type: the type for user choose
    :type type: str

    :rtype: DownUrl
    """
    if type.split('_')[0] == '':
        starttime = '2018-01-02 00:00:00'
    if type.split('_')[1] == '':
        endtime = '2018-01-03 00:00:00'
    url=accept_export(starttime=starttime,endtime=endtime,choose_type=type.split('_')[2],area=type.split('_')[3],datatype=type.split('_')[4])
    msg={"code":0,"msg":"success","url":url}
    return msg
def installed_orders_list_export_get(type,starttime=None, endtime=None):  # noqa: E501
    """eight hour complaint daily list export

    eight hour complaint daily list export # noqa: E501

    :param starttime: the starttime for user choose
    :type starttime: str
    :param endtime: the endtime for user choose
    :type endtime: str
    :param type: the type for user choose
    :type type: str

    :rtype: DownUrl
    """

    if starttime == '':
        starttime = '2018-01-02 00:00:00'
    if endtime == '':
        endtime = '2018-01-03 00:00:00'
    workbook_m = xlwt.Workbook(encoding='utf-8')
    xlsheet = workbook_m.add_sheet('接单及时率', cell_overwrite_ok=True)
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
    xlsheet.write(0, 7, type, style3)
    xlsheet.write(1, 0, '区县', style1)
    xlsheet.write(1, 1, '1-2小时', style1)
    xlsheet.write(1, 2, '2-10小时', style1)
    xlsheet.write(1, 3, '10-24小时', style1)
    xlsheet.write(1, 4, '超过24小时', style1)
    xlsheet.write(1, 5, '1-2小时及时率', style1)
    xlsheet.write(1, 6, '2-10小时及时率', style1)
    xlsheet.write(1, 7, '10-24小时及时率', style1)
    xlsheet.write(1, 8, '超过24小时及时率', style1)
    xlsheet.write(1, 9, '平均处理时长', style1)
    xlsheet.write(1, 10, '平均处理及时率', style1)

    area_list = ['秭归', '枝江', '长阳', '远安', '宜都', '夷陵', '兴山', '五峰', '开发区', '当阳', '城区']
    if type == '宽带装机':
        gdtype = 1
    if type == '和TV':
        gdtype = 3
    if type == '移装机':
        gdtype = 2
    if type == 'IMS装机':
        gdtype = 4
    # if type:
    #     gdtype = 0
    print(gdtype)
    if gdtype != 0:
        dataall = YCinstalled.select().where(
            (YCinstalled.type == gdtype) & (YCinstalled.accept >= utc_str_to_timestamp(starttime)) & (
                YCinstalled.confirm <= utc_str_to_timestamp(endtime)))
    else:
        dataall = YCinstalled.select().where((YCinstalled.accept >= utc_str_to_timestamp(starttime)) & (
            YCinstalled.confirm <= utc_str_to_timestamp(endtime)))
    i=1
    for area in area_list:

        av_time = 0
        like = "%" + area + '%'
        data = dataall.where(YCinstalled.area % like)
        for item in data:
            try:
                av_time = ((item.orders - item.accept) / 3600) + av_time
            except:
                av_time = av_time
        total = data.count()
        try:
            avtime = av_time / total
        except:
            avtime = 0
        oneToTwo = data.where((YCinstalled.orders - YCinstalled.accept) / 3600 <= 2).count()
        try:
            oneToTwo_1 = '%.2f' % (oneToTwo * 100 / total)
        except:
            oneToTwo_1 = '0.00%'
        twoToTen = data.where(((YCinstalled.orders - YCinstalled.accept) / 3600 > 2) & (
            (YCinstalled.orders - YCinstalled.accept) / 3600 <= 10)).count()

        try:
            twoToTen_1 = '%.2f' % (twoToTen * 100 / total)
        except:
            twoToTen_1 = '0.00%'
        tenToTwentyFour = data.where(((YCinstalled.orders - YCinstalled.accept) / 3600 > 10) & (
            (YCinstalled.orders - YCinstalled.accept) / 3600 <= 24)).count()

        try:
            tenToTwentyFour_1 = '%.2f' % (tenToTwentyFour * 100 / total)
        except:
            tenToTwentyFour_1 = '0.00%'
        twentyFour = data.where((YCinstalled.orders - YCinstalled.accept) / 3600 > 24).count()

        try:
            twentyFour_1 = '%.2f' % (twentyFour * 100 / total)
        except:
            twentyFour_1 = '0.00%'
        xlsheet.write(i + 1, 0, area, style1)
        xlsheet.write(i + 1, 1, oneToTwo, style1)
        xlsheet.write(i + 1, 2, twoToTen, style1)
        xlsheet.write(i + 1, 3, tenToTwentyFour,
                      style1)
        xlsheet.write(i + 1, 4, twentyFour,
                      style1)
        xlsheet.write(i + 1, 5, str(oneToTwo_1) + '%',
                      style1)
        xlsheet.write(i + 1, 6, str(twoToTen_1) + '%', style1)
        xlsheet.write(i + 1, 7, str(tenToTwentyFour_1) + '%', style1)
        xlsheet.write(i + 1, 8, str(twentyFour_1) + '%', style1)
        xlsheet.write(i + 1, 9, '%.2f' % avtime, style1)
        xlsheet.write(i + 1, 10, str(oneToTwo_1) + '%')
        i = i + 1
    xlsname = type + '接单及时率' + str(int(time.time()))
    workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
    url = 'down.flyminer.cn:89/{}.xls'.format(xlsname)

    msg = {"code": 0, "msg": "success", "url": url}
    return msg
def installed_orders_list_get(type,starttime=None, endtime=None):  # noqa: E501
    """Installed Daily

    Installed Daily # noqa: E501

    :param starttime: the starttime for user choose
    :type starttime: str
    :param endtime: the endtime for user choose
    :type endtime: str
    :param type: the type for user choose
    :type type: str

    :rtype: OrdersList
    """
    print('-------------------')
    if starttime == '':
        starttime = '2018-01-02 00:00:00'
    if endtime == '':
        endtime = '2018-01-03 00:00:00'
    area_list = ['秭归', '枝江', '长阳', '远安', '宜都', '夷陵', '兴山', '五峰', '开发区', '当阳', '城区']
    if type == '宽带装机':
        gdtype = 1
    if type == '和TV':
        gdtype = 3
    if type == '移装机':
        gdtype = 2
    if type == 'IMS装机':
        gdtype = 4
    # if type:
    #     gdtype = 0
    print(gdtype)
    if gdtype != 0:
        dataall = YCinstalled.select().where(
            (YCinstalled.type== gdtype) & (YCinstalled.accept >= utc_str_to_timestamp(starttime)) & (
            YCinstalled.confirm <= utc_str_to_timestamp(endtime)))
    else:
        dataall = YCinstalled.select().where((YCinstalled.accept >= utc_str_to_timestamp(starttime)) & (
        YCinstalled.confirm <= utc_str_to_timestamp(endtime)))
    result = []
    for area in area_list:
        av_time=0
        like = "%" + area + '%'
        data = dataall.where(YCinstalled.area % like)
        for item in data:
            if item.orders==0:
                item.orders=item.accept
            try:
                av_time=((item.orders-item.accept)/3600)+av_time
            except:
                av_time=av_time
        total = data.count()
        try:
           avtime= av_time / total
        except:
            avtime=0
        oneToTwo = data.where((YCinstalled.orders - YCinstalled.accept) / 3600 <= 2).count()
        try:
            oneToTwo_1 = '%.2f' % (oneToTwo*100 / total)
        except:
            oneToTwo_1 = '0.00%'
        twoToTen = data.where(((YCinstalled.orders - YCinstalled.accept) / 3600 > 2) & ((YCinstalled.orders - YCinstalled.accept) / 3600 <=10) ).count()

        try:
            twoToTen_1 = '%.2f' % (twoToTen*100 / total)
        except:
            twoToTen_1 = '0.00%'
        tenToTwentyFour =data.where(((YCinstalled.orders - YCinstalled.accept) / 3600 > 10) & ((YCinstalled.orders - YCinstalled.accept) / 3600 <=24) ).count()

        try:
            tenToTwentyFour_1 = '%.2f' % (tenToTwentyFour*100 / total)
        except:
            tenToTwentyFour_1 = '0.00%'
        twentyFour = data.where((YCinstalled.orders - YCinstalled.accept) / 3600 > 24).count()

        try:
            twentyFour_1 = '%.2f' % (twentyFour*100 / total)
        except:
            twentyFour_1 = '0.00%'
        msg_list = {"area": area,
                    "oneToTwo": oneToTwo,
                    "tenToTwentyFour": tenToTwentyFour,
                    "total": total,
                    "twentyFour": twentyFour,
                    "twoToTen": twoToTen,
                    "oneToTwo_1": str(oneToTwo_1)+'%',
                    "twoToTen_1": str(twoToTen_1)+'%',
                    "tenToTwentyFour_1": str(tenToTwentyFour_1)+'%',
                    "twentyFour_1": str(twentyFour_1)+'%',
                     'rate':str(oneToTwo_1)+'%',
                    'ave':'%.2f' % avtime}
        result.append(msg_list)
    msg = {"code": 0, "msg": "success", "result": result}
    return msg


##超时未回复界面接口
def installed_out_chart_get(type,starttime=None, endtime=None):  # noqa: E501
    """Yichang Branch Broadens Fault Daily

    Yichang Branch Broadens Fault Daily # noqa: E501

    :param starttime: the starttime for user choose
    :type starttime: str
    :param endtime: the endtime for user choose
    :type endtime: str
    :param type: the user choose type
    :type type: str

    :rtype: HomeChart
    """
    if starttime == '':
        starttime = '2018-01-02 00:00:00'
    if endtime == '':
        endtime = '2018-01-03 00:00:00'
    dataall = YCinstalled.select().where((YCinstalled.accept >= utc_str_to_timestamp(starttime)) & (
    YCinstalled.accept <= utc_str_to_timestamp(endtime)))
    data = dataall.where((YCinstalled.confirm == 0) & (YCinstalled.status == 'order_status_5'))
    msg = {"code": 0, "msg": "success", "result": [
        {'rank': 'top'+str(i + 1), "geo":getxy(data[i].pboos,data[i].area)} for i in
        range(len(data))]}
    return msg
def installed_out_info_export_get(type):  # noqa: E501
    """eight hour complaint daily list export

    eight hour complaint daily list export # noqa: E501

    :param type: the type for user choose
    :type type: str

    :rtype: DownUrl
    """
    data = YCinstalled.get(YCinstalled.id == int(type))
    workbook_m = xlwt.Workbook(encoding='utf-8')
    xlsheet = workbook_m.add_sheet('out' + type, cell_overwrite_ok=True)
    xlsheet.write(0, 0, '所属区')
    xlsheet.write(0, 1, '工单类型')
    xlsheet.write(0, 2, '服务帐号')
    xlsheet.write(0, 3, 'pboos地址')
    xlsheet.write(0, 4, '受理时间')

    xlsheet.write(1, 0, data.area)
    xlsheet.write(1, 1, getinstalledtype(data.type))
    xlsheet.write(1, 2, data.account)
    xlsheet.write(1, 3, data.pboos)
    xlsheet.write(1, 4, utc_timestamp_to_str(data.orders))

    xlsname = '超时未回复' + data.area + str(int(time.time()))
    workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
    url = 'down.flyminer.cn:89/{}.xls'.format(xlsname)
    msg = {"code": 0, "msg": "success", "url": url}
    return msg
def installed_out_list_export_get(type,starttime=None, endtime=None):  # noqa: E501
    """eight hour complaint daily list export

    eight hour complaint daily list export # noqa: E501

    :param starttime: the starttime for user choose
    :type starttime: str
    :param endtime: the endtime for user choose
    :type endtime: str
    :param type: the type for user choose
    :type type: str

    :rtype: DownUrl
    """
    if starttime == '':
        starttime = '2018-01-02 00:00:00'
    if endtime == '':
        endtime = '2018-01-03 00:00:00'
    workbook_m = xlwt.Workbook(encoding='utf-8')
    xlsheet = workbook_m.add_sheet('超时未回复', cell_overwrite_ok=True)
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
    xlsheet.write(0, 7, type, style3)
    xlsheet.write(1, 0, '区县', style1)
    xlsheet.write(1, 1, '工单类型', style1)
    xlsheet.write(1, 2, '服务帐号', style1)
    xlsheet.write(1, 3, 'PBOSS地址', style1)
    xlsheet.write(1, 4, '受理时间', style1)
    xlsheet.write(1, 5, 'top', style1)


    if type == '宽带装机':
        gdtype = 1
    if type == '和TV':
        gdtype = 3
    if type == '移装机':
        gdtype = 2
    if type == 'IMS装机':
        gdtype = 4
    else:
        gdtype=0
    if gdtype != 0:
        dataall = YCinstalled.select().where(
            (YCinstalled.type== gdtype) & (YCinstalled.accept >= utc_str_to_timestamp(starttime)) & (
            YCinstalled.accept <= utc_str_to_timestamp(endtime)))
    if gdtype==0:
        dataall = YCinstalled.select().where((YCinstalled.accept >= utc_str_to_timestamp(starttime)) & (
        YCinstalled.accept <= utc_str_to_timestamp(endtime)))
    data=dataall.where((YCinstalled.confirm==0) & (YCinstalled.status=='order_status_5'))
    i=1
    for item in data:
        xlsheet.write(i+1, 0, item.area, style1)
        xlsheet.write(i+1, 1, getinstalledtype(item.type), style1)
        xlsheet.write(i+1, 2, item.account, style1)
        xlsheet.write(i+1, 3, item.pboos, style1)
        xlsheet.write(i+1, 4, utc_timestamp_to_str(item.orders), style1)
        xlsheet.write(i+1, 5, i, style1)
        i=i+1
    xlsname = type + '超时未回复' + str(int(time.time()))
    workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
    url = 'down.flyminer.cn:89/{}.xls'.format(xlsname)

    msg = {"code": 0, "msg": "success", "url": url}
    return msg
def installed_out_list_get(type, starttime=None, endtime=None):  # noqa: E501
    """Yichang Branch Broadens Fault Daily

    Yichang Branch Broadens Fault Daily # noqa: E501

    :param starttime: the starttime for user choose
    :type starttime: str
    :param endtime: the endtime for user choose
    :type endtime: str

    :rtype: InstalledTopList
    """
    if starttime == '':
        starttime = '2018-01-02 00:00:00'
    if endtime == '':
        endtime = '2018-01-03 00:00:00'
    area_list = ['秭归', '枝江', '长阳', '远安', '宜都', '夷陵', '兴山', '五峰', '开发区', '当阳', '城区']
    gdtype=0
    if type == '宽带装机':
        gdtype = 1
    if type == '和TV':
        gdtype = 3
    if type == '移装机':
        gdtype = 2
    if type == 'IMS装机':
        gdtype = 4

    if gdtype != 0:
        dataall = YCinstalled.select().where(
            (YCinstalled.type== gdtype) & (YCinstalled.accept >= utc_str_to_timestamp(starttime)) & (
            YCinstalled.accept <= utc_str_to_timestamp(endtime)))
    else:
        dataall = YCinstalled.select().where((YCinstalled.accept >= utc_str_to_timestamp(starttime)) & (
        YCinstalled.accept<= utc_str_to_timestamp(endtime)))
    data = dataall.where(YCinstalled.confirm == 0)
    msg = {"code": 0, "msg": "success", "result": [
        {'id': i + 1, 'ID': data[i].id, "area": data[i].area, "type": getinstalledtype(data[i].type),
         "account": data[i].account, "pboss": data[i].pboos, "times": utc_timestamp_to_str(data[i].accept)} for i in
        range(len(data))]}
    return msg




##退单率界面接口
def installed_retreat_chart_get(type,starttime=None, endtime=None):  # noqa: E501
    """Installed Daily

    Installed Daily # noqa: E501

    :param starttime: the starttime for user choose
    :type starttime: str
    :param endtime: the endtime for user choose
    :type endtime: str
    :param type: the user choose type
    :type type: str

    :rtype: HomeChart
    """
    if starttime == '':
        starttime = '2018-01-02 00:00:00'
    if endtime == '':
        endtime = '2018-01-03 00:00:00'
    result=[]
    datatype=type.split('_')[0]
    area_list = ['秭归', '枝江', '长阳', '远安', '宜都', '夷陵', '兴山', '五峰', '开发区', '当阳', '城区']
    if datatype == '宽带装机':
        gdtype = 1
    if datatype == '和TV':
        gdtype = 3
    if datatype == '移装机':
        gdtype = 2
    if datatype == 'IMS装机':
        gdtype = 4
    # if type:
    #     gdtype = 0
    if gdtype != 0:
        dataall = YCinstalled.select().where(
            (YCinstalled.type== gdtype) & (YCinstalled.accept >= utc_str_to_timestamp(starttime)) & (
            YCinstalled.accept <= utc_str_to_timestamp(endtime)))
    else:
        dataall = YCinstalled.select().where((YCinstalled.accept >= utc_str_to_timestamp(starttime)) & (
        YCinstalled.accept <= utc_str_to_timestamp(endtime)))
    try:
        for area in area_list:
            like='%'+area+'%'
            retreat = dataall.where((YCinstalled.status == 'order_status_6') & (YCinstalled.area % like)).count()
            accept = dataall.where(YCinstalled.area % like).count()
            try:
                rate = '%.2f' % (retreat * 100 / accept)
            except:
                rate = 0.00
            result.append({"name": area,'value': rate})
        msg = {"code": 0, "msg": "success", "result": result}
    except:
        msg = {"code": -1, "msg": "Error"}
    return msg
def installed_retreat_info_export_get(type):  # noqa: E501
    """eight hour complaint daily list export

    eight hour complaint daily list export # noqa: E501

    :param type: the type for user choose
    :type type: str

    :rtype: DownUrl
    """
    starttime = type.split('_')[0]
    endtime = type.split('_')[1]
    area = type.split('_')[2]
    datatype = type.split('_')[3]
    if starttime == '':
        starttime = '2018-01-02 00:00:00'
    if endtime == '':
        endtime = '2018-01-03 00:00:00'
    result = []
    if datatype == '宽带装机':
        gdtype = 1
    if datatype == '和TV':
        gdtype = 3
    if datatype == '移装机':
        gdtype = 2
    if datatype == 'IMS装机':
        gdtype = 4
    # if type:
    #     gdtype = 0
    if gdtype != 0:
        dataall = YCinstalled.select().where(
            (YCinstalled.type == gdtype) & (YCinstalled.accept >= utc_str_to_timestamp(starttime)) & (
                YCinstalled.accept <= utc_str_to_timestamp(endtime)))
    else:
        dataall = YCinstalled.select().where((YCinstalled.accept >= utc_str_to_timestamp(starttime)) & (
            YCinstalled.accept <= utc_str_to_timestamp(endtime)))
    try:
        like = '%' + area + '%'
        data = dataall.where((YCinstalled.status == 'order_status_6') & (YCinstalled.area % like))
        workbook_m = xlwt.Workbook(encoding='utf-8')
        xlsheet = workbook_m.add_sheet('out' + type, cell_overwrite_ok=True)
        xlsheet.write(0, 0, '所属区')
        xlsheet.write(0, 1, '工单类型')
        xlsheet.write(0, 2, '服务帐号')
        xlsheet.write(0, 3, 'pboos地址')
        xlsheet.write(0, 4, '接单时间')

        for i in range(len(data)):
            xlsheet.write(i + 1, 0, data[i].area)
            xlsheet.write(i + 1, 1, getinstalledtype(data[i].type))
            xlsheet.write(i + 1, 2, data[i].account)
            xlsheet.write(i + 1, 3, data[i].pboos)
            xlsheet.write(i + 1, 4, utc_timestamp_to_str(data[i].accept))

        xlsname = '退单详情' + area + str(int(time.time()))
        workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
        url = 'down.flyminer.cn:89/{}.xls'.format(xlsname)
        msg = {"code": 0, "msg": "success", "url": url}
    except:
        msg = {"code": -1, "msg": "Error"}
    return msg
def installed_retreat_list_export_get(type,starttime=None, endtime=None):  # noqa: E501
    """eight hour complaint daily list export

    eight hour complaint daily list export # noqa: E501

    :param starttime: the starttime for user choose
    :type starttime: str
    :param endtime: the endtime for user choose
    :type endtime: str
    :param type: the type for user choose
    :type type: str

    :rtype: DownUrl
    """
    if starttime == '':
        starttime = '2018-01-02 00:00:00'
    if endtime == '':
        endtime = '2018-01-03 00:00:00'
    result=[]
    workbook_m = xlwt.Workbook(encoding='utf-8')
    xlsheet = workbook_m.add_sheet('退单率', cell_overwrite_ok=True)
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
    xlsheet.write(0, 7, type, style3)
    xlsheet.write(1, 0, '区县', style1)
    xlsheet.write(1, 1, '退单量', style1)
    xlsheet.write(1, 2, '受理量', style1)
    xlsheet.write(1, 3, '退单率', style1)

    area_list = ['秭归', '枝江', '长阳', '远安', '宜都', '夷陵', '兴山', '五峰', '开发区', '当阳', '城区']
    if type == '宽带装机':
        gdtype = 1
    if type == '和TV':
        gdtype = 3
    if type == '移装机':
        gdtype = 2
    if type == 'IMS装机':
        gdtype = 4
    if type=='全量工单':
        gdtype = 0
    if gdtype != 0:
        dataall = YCinstalled.select().where(
            (YCinstalled.type== gdtype) & (YCinstalled.accept >= utc_str_to_timestamp(starttime)) & (
            YCinstalled.accept <= utc_str_to_timestamp(endtime)))
    else:
        dataall = YCinstalled.select().where((YCinstalled.accept >= utc_str_to_timestamp(starttime)) & (
        YCinstalled.accept <= utc_str_to_timestamp(endtime)))
    i = 1
    try:
        for area in area_list:
            like='%'+area+'%'
            retreat = dataall.where((YCinstalled.status == 'order_status_6') & (YCinstalled.area % like)).count()
            accept = dataall.where((YCinstalled.area % like) & (YCinstalled.status != 'order_status_6')).count()
            try:
                rate = '%.2f' % (retreat * 100 / accept)
            except:
                rate = '0.00%'


            xlsheet.write(i + 1, 0, area, style1)
            xlsheet.write(i + 1, 1, retreat, style1)
            xlsheet.write(i + 1, 2, accept, style1)
            xlsheet.write(i + 1, 3, str(rate)+'%', style1)
            i = i + 1
        xlsname = type + '退单率' + str(int(time.time()))
        workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
        url = 'down.flyminer.cn:89/{}.xls'.format(xlsname)

        msg = {"code": 0, "msg": "success", "url": url}
    except:
        msg = {"code": -1, "msg": "Error"}
    return msg
def installed_retreat_list_get(type,starttime=None, endtime=None):  # noqa: E501
    """Installed Daily

    Installed Daily # noqa: E501

    :param starttime: the starttime for user choose
    :type starttime: str
    :param endtime: the endtime for user choose
    :type endtime: str
    :param type: the type for user choose
    :type type: str

    :rtype: RetreatList
    """
    if starttime == '':
        starttime = '2018-01-02 00:00:00'
    if endtime == '':
        endtime = '2018-01-03 00:00:00'
    result=[]
    area_list = ['秭归', '枝江', '长阳', '远安', '宜都', '夷陵', '兴山', '五峰', '开发区', '当阳', '城区']
    if type == '宽带装机':
        gdtype = 1
    if type == '和TV':
        gdtype = 3
    if type == '移装机':
        gdtype = 2
    if type == 'IMS装机':
        gdtype = 4
    # if type:
    #     gdtype = 0
    if gdtype != 0:
        dataall = YCinstalled.select().where(
            (YCinstalled.type== gdtype) & (YCinstalled.accept >= utc_str_to_timestamp(starttime)) & (
            YCinstalled.accept <= utc_str_to_timestamp(endtime)))
    else:
        dataall = YCinstalled.select().where((YCinstalled.accept >= utc_str_to_timestamp(starttime)) & (
        YCinstalled.accept <= utc_str_to_timestamp(endtime)))
    try:
        for area in area_list:
            like='%'+area+'%'
            retreat = dataall.where((YCinstalled.status == 'order_status_6') & (YCinstalled.area % like)).count()
            accept = dataall.where(YCinstalled.area % like).count()
            try:
                rate = '%.2f' % (retreat * 100 / accept)
            except:
                rate = '0.00%'
            result.append({"area": area, "retreat": retreat, "accept": accept, 'rate': rate})
        msg = {"code": 0, "msg": "success", "result": result}
    except:
        msg = {"code": -1, "msg": "Error"}
    return msg

##满意度界面接口
def installed_satisfaction_chart_get(type,starttime=None, endtime=None):  # noqa: E501
    """Installed Daily

    Installed Daily # noqa: E501

    :param starttime: the starttime for user choose
    :type starttime: str
    :param endtime: the endtime for user choose
    :type endtime: str
    :param type: the user choose type
    :type type: str

    :rtype: HomeChart
    """
    if (starttime == "2018/3/29 00：00") & (endtime == "2018/3/29 24：00") & (type == "重复投诉率"):
        msg = msg_24chart_right
    else:
        msg = msg_24chart_right
    return msg
def installed_satisfaction_info_export_get(type):  # noqa: E501
    """eight hour complaint daily list export

    eight hour complaint daily list export # noqa: E501

    :param type: the type for user choose
    :type type: str

    :rtype: DownUrl
    """
    if (type == "已完成超时"):
        msg = msg_list_export
    else:
        msg = msg_list_export
    return msg
def installed_satisfaction_list_export_get(type,starttime=None, endtime=None):  # noqa: E501
    """eight hour complaint daily list export

    eight hour complaint daily list export # noqa: E501

    :param starttime: the starttime for user choose
    :type starttime: str
    :param endtime: the endtime for user choose
    :type endtime: str
    :param type: the type for user choose
    :type type: str

    :rtype: DownUrl
    """
    if (starttime == "2018/3/29 00：00") & (endtime == "2018/3/29 24：00") & (type == "CRM"):
        msg = msg_list_export
    else:
        msg = msg_list_export
    return msg
def installed_satisfaction_list_get(type,starttime=None, endtime=None):  # noqa: E501
    """Installed Daily

    Installed Daily # noqa: E501

    :param starttime: the starttime for user choose
    :type starttime: str
    :param endtime: the endtime for user choose
    :type endtime: str
    :param type: the type for user choose
    :type type: str

    :rtype: SatisfactionList
    """
    if (starttime == "2018/3/29 00：00") & (endtime == "2018/3/29 24：00") & (type == "CRM"):
        msg = msg_satisfaction_list_right
    else:
        msg = msg_satisfaction_list_right
    return msg


##装机时长Top20
def installed_top_chart_get(type,starttime=None, endtime=None):  # noqa: E501
    """Yichang Branch Broadens Fault Daily

    Yichang Branch Broadens Fault Daily # noqa: E501

    :param starttime: the starttime for user choose
    :type starttime: str
    :param endtime: the endtime for user choose
    :type endtime: str
    :param type: the user choose type
    :type type: str

    :rtype: HomeChart
    """
    if (starttime == "2018/3/29 00：00") & (endtime == "2018/3/29 24：00") & (type == "重复投诉率"):
        msg = msg_24chart_right
    else:
        msg = msg_24chart_right
    return msg
def installed_top_info_export_get(type):  # noqa: E501
    """eight hour complaint daily list export

    eight hour complaint daily list export # noqa: E501

    :param type: the type for user choose
    :type type: str

    :rtype: DownUrl
    """
    data=YCinstalled.get(YCinstalled.id==int(type))
    workbook_m = xlwt.Workbook(encoding='utf-8')
    xlsheet = workbook_m.add_sheet('top'+type, cell_overwrite_ok=True)
    xlsheet.write(0, 0, '所属区')
    xlsheet.write(0, 1, '工单类型')
    xlsheet.write(0, 2, '服务帐号')
    xlsheet.write(0, 3, 'pboos地址')
    xlsheet.write(0, 4, '受理时间')


    xlsheet.write(1, 0, data.area)
    xlsheet.write(1, 1, getinstalledtype(data.type))
    xlsheet.write(1, 2, data.account)
    xlsheet.write(1, 3, data.pboos)
    xlsheet.write(1, 4, utc_timestamp_to_str(data.orders))

    xlsname='装机top时长' + data.area  + str(int(time.time()))
    workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
    url= 'down.flyminer.cn:89/{}.xls'.format(xlsname)
    msg={"code":0,"msg":"success","url":url}
    return msg
def installed_top_list_export_get(type,starttime=None, endtime=None):  # noqa: E501
    """eight hour complaint daily list export

    eight hour complaint daily list export # noqa: E501

    :param starttime: the starttime for user choose
    :type starttime: str
    :param endtime: the endtime for user choose
    :type endtime: str
    :param type: the type for user choose
    :type type: str

    :rtype: DownUrl
    """
    if starttime == '':
        starttime = '2018-01-02 00:00:00'
    if endtime == '':
        endtime = '2018-01-03 00:00:00'
    workbook_m = xlwt.Workbook(encoding='utf-8')
    xlsheet = workbook_m.add_sheet('接单及时率', cell_overwrite_ok=True)
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
    xlsheet.write(0, 7, type, style3)
    xlsheet.write(1, 0, '区县', style1)
    xlsheet.write(1, 1, '工单类型', style1)
    xlsheet.write(1, 2, '服务帐号', style1)
    xlsheet.write(1, 3, 'PBOSS地址', style1)
    xlsheet.write(1, 4, '受理时间', style1)
    xlsheet.write(1, 5, 'top', style1)


    if type == '宽带装机':
        gdtype = 1
    if type == '和TV':
        gdtype = 3
    if type == '移装机':
        gdtype = 2
    if type == 'IMS装机':
        gdtype = 4
    else:
        gdtype=0
    if gdtype != 0:
        dataall = YCinstalled.select().where(YCinstalled.type== gdtype)
    else:
        dataall = YCinstalled.select().where((YCinstalled.accept >= utc_str_to_timestamp(starttime)) & (
        YCinstalled.confirm <= utc_str_to_timestamp(endtime)))

    data=dataall.select().where(YCinstalled.confirm!=0).order_by((YCinstalled.confirm-YCinstalled.accept).desc()).limit(20)
    i=1
    for item in data:
        xlsheet.write(i+1, 0, item.area, style1)
        xlsheet.write(i+1, 1, getinstalledtype(item.type), style1)
        xlsheet.write(i+1, 2, item.account, style1)
        xlsheet.write(i+1, 3, item.pboos, style1)
        xlsheet.write(i+1, 4, utc_timestamp_to_str(item.orders), style1)
        xlsheet.write(i+1, 5, i, style1)
        i=i+1
    xlsname = type + '装机时长Top20' + str(int(time.time()))
    workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
    url = 'down.flyminer.cn:89/{}.xls'.format(xlsname)

    msg = {"code": 0, "msg": "success", "url": url}
    return msg
def installed_top_list_get(type, starttime=None, endtime=None):  # noqa: E501
    """Yichang Branch Broadens Fault Daily

    Yichang Branch Broadens Fault Daily # noqa: E501

    :param starttime: the starttime for user choose
    :type starttime: str
    :param endtime: the endtime for user choose
    :type endtime: str

    :rtype: InstalledTopList
    """
    gdtype = 0
    if starttime == '':
        starttime = '2018-01-02 00:00:00'
    if endtime == '':
        endtime = '2018-01-03 00:00:00'
    if type == '宽带装机':
        gdtype = 1
    if type == '和TV':
        gdtype = 3
    if type == '移装机':
        gdtype = 2
    if type == 'IMS装机':
        gdtype = 4
    if gdtype != 0:
        dataall = YCinstalled.select().where(YCinstalled.type== gdtype)
    else:
        dataall = YCinstalled.select().where((YCinstalled.accept >= utc_str_to_timestamp(starttime)) & (
        YCinstalled.confirm <= utc_str_to_timestamp(endtime)))

    data=dataall.select().where(YCinstalled.confirm!=0).order_by((YCinstalled.confirm-YCinstalled.accept).desc()).limit(20)
    msg={"code":0,"msg":"success","result":[{'id':i+1,'ID':data[i].id,"area":data[i].area,"type":getinstalledtype(data[i].type),"account":data[i].account,"pboss":data[i].pboos,"times":utc_timestamp_to_str(data[i].orders)} for i in range(len(data))]}
    return msg


##24小时装机日报界面接口
def installed_twenty_four_chart_get(type,starttime=None, endtime=None):  # noqa: E501
    """Installed Daily

    Installed Daily # noqa: E501

    :param starttime: the starttime for user choose
    :type starttime: str
    :param endtime: the endtime for user choose
    :type endtime: str
    :param type: the user choose type
    :type type: str

    :rtype: HomeChart
    """
    #msg=msg_24chart_right
    msg_reslut = []
    # try:
    if starttime == '':
        starttime = '2018-01-02 00:00:00'
    if endtime == '':
        endtime = '2018-01-03 00:00:00'

    area_list = ['秭归', '枝江', '长阳', '远安', '宜都', '夷陵', '兴山', '五峰', '开发区', '当阳', '城区']

    if type == '装机及时率':
        data = YCinstalled.select().where(
             (YCinstalled.accept >= utc_str_to_timestamp(starttime)) & (
                YCinstalled.accept <= utc_str_to_timestamp(endtime)) & (YCinstalled.areaType != '普服小区') & (
                YCinstalled.areaType != '普遍服务'))
        data1 = YCinstalled.select().where(
              (YCinstalled.confirm >= utc_str_to_timestamp(starttime)) & (
                YCinstalled.confirm <= utc_str_to_timestamp(endtime)) & (YCinstalled.areaType != '普服小区') & (
                YCinstalled.areaType != '普遍服务'))

        for i in range(len(area_list)):
            area = area_list[i]
            like = "%" + area_list[i] + "%"


            complete = data1.where(YCinstalled.area % like).count()
            loaded = data1.where(
                (YCinstalled.area % like) & (YCinstalled.confirm != 0) & (YCinstalled.timeout == '是')).count()


            try:
                rate = (complete - loaded) / complete
            except:
                rate = 0

            msg = {"name": area,

                   "value": '%.2f' % (rate * 100),
                    }

            msg_reslut.append(msg)
    else:

        area_list = ['秭归', '枝江', '长阳', '远安', '宜都', '夷陵', '兴山', '五峰', '开发区', '当阳', '城区']

        print('----')
        data = YCinstalled.select().where((YCinstalled.accept >= utc_str_to_timestamp(starttime)) & (
            YCinstalled.accept <= utc_str_to_timestamp(endtime)) & (YCinstalled.areaType != '普服小区') & (
                                              YCinstalled.areaType != '普遍服务'))
        data1 = YCinstalled.select().where((YCinstalled.confirm >= utc_str_to_timestamp(starttime)) & (
            YCinstalled.confirm <= utc_str_to_timestamp(endtime)) & (YCinstalled.areaType != '普服小区') & (
                                               YCinstalled.areaType != '普遍服务'))

        for i in range(len(area_list)):
            av_time = 0
            area = area_list[i]
            like = "%" + area_list[i] + "%"

            accept = data.where(YCinstalled.area % like).count()

            complete = data1.where(YCinstalled.area % like).count()
            loaded = data1.where(
                (YCinstalled.area % like) & (YCinstalled.confirm != 0) & (YCinstalled.timeout == '是')).count()

            notLoaded = data.where((YCinstalled.area % like) & (YCinstalled.confirm == 0)).count()
            pressing = 0

            try:
                rate = (complete - loaded) / complete
            except:
                rate = 0

            for item in data1.where((YCinstalled.area % like) & (YCinstalled.confirm != 0)):
                try:
                    av_time = av_time + ((item.confirm - item.accept) / 3600)

                except:
                    pass
            ave = av_time / complete
            msg = {"name": area,

                   "value": '%.2f' % ave, }
            msg_reslut.append(msg)


    msg = {"code": 0, "msg": "success", "result": msg_reslut}

    # except:
    #     msg = {"code": -1, "msg": "Error"}
    return msg

#installed_twenty_four_chart_get(type='宽带装机',starttime="2018-01-02 00:00:00",endtime="2018-01-03 00:00:00")
def installed_twenty_four_info_export_get(type):  # noqa: E501
    """eight hour complaint daily list export

    eight hour complaint daily list export # noqa: E501

    :param type: the type for user choose
    :type type: str

    :rtype: DownUrl
    """
    print(type)
    type_list = type.split('_')
    starttime = type_list[0]
    endtime = type_list[1]
    if starttime == '':
        starttime = '2018-01-02 00:00:00'
    if endtime == '':
        endtime = '2018-01-03 00:00:00'
    choose_type = type_list[3]
    area = type_list[2]
    datatype = type_list[4]
    url = installed_export(starttime=starttime, endtime=endtime, choose_type=choose_type, area=area, datatype=datatype)
    print (url)
    msg = {"code": 0, "msg": "success", "url": url}
    return msg
def installed_twenty_four_list_export_get(type,starttime=None, endtime=None):  # noqa: E501
    """eight hour complaint daily list export

    eight hour complaint daily list export # noqa: E501

    :param starttime: the starttime for user choose
    :type starttime: str
    :param endtime: the endtime for user choose
    :type endtime: str
    :param type: the type for user choose
    :type type: str

    :rtype: DownUrl
    """
    # if starttime == None:
    #   starttime =

    # url = make_file("sdfasf", type='装机24小时报表', starttime, endtime, type)

    try:
        if starttime == '':
            starttime = '2018-01-02 00:00:00'
        if endtime == '':
            endtime = '2018-01-03 00:00:00'
        starttime = str(starttime)
        endtime = str(endtime)
        file_path =type.split('_')[0].replace('mail.itlaolang.com/downfile/','/var/www/downfile/')
        url = make_file(file_path=file_path, type='装机24小时报表', starttime=starttime, endtime=endtime, choose_type=type.split('_')[1])
        msg = {"code": 0, "msg": "success", "url": url}
    except:
        msg = {"code": -1, "msg": "Error"}
    return msg
def installed_twenty_four_list_get(type,starttime=None, endtime=None):  # noqa: E501
    """Installed Daily

    Installed Daily # noqa: E501

    :param starttime: the starttime for user choose
    :type starttime: str
    :param endtime: the endtime for user choose
    :type endtime: str
    :param type: the type for user choose
    :type type: str

    :rtype: InstalledList
    """
    msg_reslut = []
    if starttime == '':
        starttime = '2018-01-02 00:00:00'
    if endtime == '':
        endtime = '2018-01-03 00:00:00'
    choose = type

    area_list = ['秭归', '枝江', '长阳', '远安', '宜都', '夷陵', '兴山', '五峰', '开发区', '当阳', '城区']
    if str(choose) == '宽带装机':
        data = YCinstalled.select().where(
            (YCinstalled.type == 1) & (YCinstalled.accept >= utc_str_to_timestamp(starttime)) & (
                YCinstalled.accept <= utc_str_to_timestamp(endtime)) & (YCinstalled.areaType != '普服小区') & (
                YCinstalled.areaType != '普遍服务'))
        data1 = YCinstalled.select().where(
            (YCinstalled.type == 1) & (YCinstalled.confirm >= utc_str_to_timestamp(starttime)) & (
                YCinstalled.confirm <= utc_str_to_timestamp(endtime)) & (YCinstalled.areaType != '普服小区') & (
                YCinstalled.areaType != '普遍服务'))

        for i in range(len(area_list)):
            area = area_list[i]
            like = "%" + area_list[i] + "%"

            accept = data.where(YCinstalled.area % like).count()

            complete = data1.where(YCinstalled.area % like).count()
            loaded = data1.where(
                (YCinstalled.area % like) & (YCinstalled.confirm != 0) & (YCinstalled.timeout == '是')).count()
            notLoaded = data.where((YCinstalled.area % like) & (YCinstalled.confirm == 0)).count()
            pressing = 0

            try:
                rate = (complete - loaded) / complete
            except:
                rate = 0

            av_time = 0
            for item in data1.where((YCinstalled.area % like) & (YCinstalled.confirm != 0)):
                try:
                    av_time = av_time + ((item.confirm - item.accept) / 3600)
                    print(av_time)
                except:
                    pass

            ave = av_time / complete
            msg = {"area": area,
                   "accept": accept,
                   "complete": complete,
                   "loaded": loaded,
                   "notLoaded": notLoaded,
                   "pressing": pressing,
                   "rate": str('%.2f' % (rate * 100)) + '%',
                   "ave": '%.2f' % ave, }
            print(msg)
            msg_reslut.append(msg)
    if str(choose) == '移机装':
        data = YCinstalled.select().where(
            (YCinstalled.type == 2) & (YCinstalled.accept >= utc_str_to_timestamp(starttime)) & (
                YCinstalled.accept <= utc_str_to_timestamp(endtime)) & (YCinstalled.areaType != '普服小区') & (
                YCinstalled.areaType != '普遍服务'))
        data1 = YCinstalled.select().where(
            (YCinstalled.type == 2) & (YCinstalled.confirm >= utc_str_to_timestamp(starttime)) & (
                YCinstalled.confirm <= utc_str_to_timestamp(endtime)) & (YCinstalled.areaType != '普服小区') & (
                YCinstalled.areaType != '普遍服务'))

        for i in range(len(area_list)):
            area = area_list[i]
            like = "%" + area_list[i] + "%"

            accept = data.where(YCinstalled.area % like).count()

            complete = data1.where(YCinstalled.area % like).count()
            loaded = data1.where(
                (YCinstalled.area % like) & (YCinstalled.confirm != 0) & (YCinstalled.timeout == '是')).count()
            notLoaded = data.where((YCinstalled.area % like) & (YCinstalled.confirm == 0)).count()
            pressing = 0

            try:
                rate = (complete - loaded) / complete
            except:
                rate = 0

            av_time = 0
            for item in data1.where((YCinstalled.area % like) & (YCinstalled.confirm != 0)):
                try:
                    av_time = av_time + ((item.confirm - item.accept) / 3600)
                    print(av_time)
                except:
                    pass

            try:
                ave = av_time / complete
            except:
                ave=0
            msg = {"area": area,
                   "accept": accept,
                   "complete": complete,
                   "loaded": loaded,
                   "notLoaded": notLoaded,
                   "pressing": pressing,
                   "rate": str('%.2f' % (rate * 100)) + '%',
                   "ave": '%.2f' % ave, }
            print(msg)
            msg_reslut.append(msg)

    if str(choose) == 'TV单独安装':
        data = YCinstalled.select().where(
            (YCinstalled.type == 3) & (YCinstalled.accept >= utc_str_to_timestamp(starttime)) & (
                YCinstalled.accept <= utc_str_to_timestamp(endtime)) & (YCinstalled.areaType != '普服小区') & (
                YCinstalled.areaType != '普遍服务'))
        data1 = YCinstalled.select().where(
            (YCinstalled.type == 3) & (YCinstalled.confirm >= utc_str_to_timestamp(starttime)) & (
                YCinstalled.confirm <= utc_str_to_timestamp(endtime)) & (YCinstalled.areaType != '普服小区') & (
                YCinstalled.areaType != '普遍服务'))

        for i in range(len(area_list)):
            area = area_list[i]
            like = "%" + area_list[i] + "%"

            accept = data.where(YCinstalled.area % like).count()

            complete = data1.where(YCinstalled.area % like).count()
            loaded = data1.where(
                (YCinstalled.area % like) & (YCinstalled.confirm != 0) & (YCinstalled.timeout == '是')).count()
            notLoaded = data.where((YCinstalled.area % like) & (YCinstalled.confirm == 0)).count()
            pressing = 0

            try:
                rate = (complete - loaded) / complete
            except:
                rate = 0

            av_time = 0
            for item in data1.where((YCinstalled.area % like) & (YCinstalled.confirm != 0)):
                try:
                    av_time = av_time + ((item.confirm - item.accept) / 3600)
                    print(av_time)
                except:
                    pass
            try:
               ave = av_time / complete
            except:
                ave=0
            msg = {"area": area,
                   "accept": accept,
                   "complete": complete,
                   "loaded": loaded,
                   "notLoaded": notLoaded,
                   "pressing": pressing,
                   "rate": str('%.2f' % (rate * 100)) + '%',
                   "ave": '%.2f' % ave, }
            print(msg)
            msg_reslut.append(msg)
    if str(choose) == 'IMS单独安装':
        data = YCinstalled.select().where(
            (YCinstalled.type == 4) & (YCinstalled.accept >= utc_str_to_timestamp(starttime)) & (
                YCinstalled.accept <= utc_str_to_timestamp(endtime)) & (YCinstalled.areaType != '普服小区') & (
                YCinstalled.areaType != '普遍服务'))
        data1 = YCinstalled.select().where(
            (YCinstalled.type == 4) & (YCinstalled.confirm >= utc_str_to_timestamp(starttime)) & (
                YCinstalled.confirm <= utc_str_to_timestamp(endtime)) & (YCinstalled.areaType != '普服小区') & (
                YCinstalled.areaType != '普遍服务'))

        for i in range(len(area_list)):
            area = area_list[i]
            like = "%" + area_list[i] + "%"

            accept = data.where(YCinstalled.area % like).count()

            complete = data1.where(YCinstalled.area % like).count()
            loaded = data1.where(
                (YCinstalled.area % like) & (YCinstalled.confirm != 0) & (YCinstalled.timeout == '是')).count()
            notLoaded = data.where((YCinstalled.area % like) & (YCinstalled.confirm == 0)).count()
            pressing = 0

            try:
                rate = (complete - loaded) / complete
            except:
                rate = 0

            av_time = 0
            for item in data1.where((YCinstalled.area % like) & (YCinstalled.confirm != 0)):
                try:
                    av_time = av_time + ((item.confirm - item.accept) / 3600)
                    print(av_time)
                except:
                    pass

            try:
                ave = av_time / complete
            except:
                ave=0

            msg = {"area": area,
                   "accept": accept,
                   "complete": complete,
                   "loaded": loaded,
                   "notLoaded": notLoaded,
                   "pressing": pressing,
                   "rate": str('%.2f' % (rate * 100)) + '%',
                   "ave": '%.2f' % ave, }
            print(msg)
            msg_reslut.append(msg)
    if str(choose) == '全量工单':
        print('----')
        data = YCinstalled.select().where((YCinstalled.accept >= utc_str_to_timestamp(starttime)) & (
            YCinstalled.accept <= utc_str_to_timestamp(endtime)) & (YCinstalled.areaType != '普服小区') & (
                                              YCinstalled.areaType != '普遍服务'))
        data1 = YCinstalled.select().where((YCinstalled.confirm >= utc_str_to_timestamp(starttime)) & (
            YCinstalled.confirm <= utc_str_to_timestamp(endtime)) & (YCinstalled.areaType != '普服小区') & (
                                               YCinstalled.areaType != '普遍服务'))

        for i in range(len(area_list)):
            av_time = 0
            area = area_list[i]
            like = "%" + area_list[i] + "%"

            accept = data.where(YCinstalled.area % like).count()

            complete = data1.where(YCinstalled.area % like).count()
            loaded = data1.where(
                (YCinstalled.area % like) & (YCinstalled.confirm != 0) & (YCinstalled.timeout == '是')).count()

            notLoaded = data.where((YCinstalled.area % like) & (YCinstalled.confirm == 0)).count()
            pressing = 0

            try:
                rate = (complete - loaded) / complete
            except:
                rate = 0

            for item in data1.where((YCinstalled.area % like) & (YCinstalled.confirm != 0)):
                try:
                    av_time = av_time + ((item.confirm - item.accept) / 3600)

                except:
                    pass
            try:
                ave = av_time / complete
            except:
                ave=0
            msg = {"area": area,
                   "accept": accept,
                   "complete": complete,
                   "loaded": loaded,
                   "notLoaded": notLoaded,
                   "pressing": pressing,
                   "rate": str('%.2f' % (rate * 100)) + '%',
                   "ave": '%.2f' % ave, }
            msg_reslut.append(msg)

    msg = {"code": 0, "msg": "success", "result": msg_reslut}



    # except:
    #     msg = {"code": -1, "msg": "Error"}
    #print(msg)
    return msg
#installed_twenty_four_list_get(type='全量工单',starttime='',endtime='')
