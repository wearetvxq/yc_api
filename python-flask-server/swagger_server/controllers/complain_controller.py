import connexion
import six,xlrd,xlwt,requests
from collections import Counter
from swagger_server.models.down_url import DownUrl  # noqa: E501
from swagger_server.models.eight_list import EightList  # noqa: E501
from swagger_server.models.emos_first_chart import EmosFirstChart  # noqa: E501
from swagger_server.models.emos_list import EmosList  # noqa: E501
from swagger_server.models.high_chart import HighChart  # noqa: E501
from swagger_server.models.high_list import HighList  # noqa: E501
from swagger_server.models.high_list_community_column import HighListCommunityColumn  # noqa: E501
from swagger_server.models.high_list_community_total import HighListCommunityTotal  # noqa: E501
from swagger_server.models.home_chart import HomeChart  # noqa: E501
from swagger_server.models.malfunction_list import MalfunctionList  # noqa: E501
from swagger_server.models.network_list import NetworkList  # noqa: E501
from swagger_server.models.success import Success  # noqa: E501
from swagger_server.models.top_list import TopList  # noqa: E501
from swagger_server.models.twenty_list import TwentyList  # noqa: E501
from swagger_server.models.visit_list import VisitList  # noqa: E501
from swagger_server import util
import random
from swagger_server.mysql_db import *
from swagger_server.importsql import get_type
from swagger_server.export_report import *
from swagger_server.infoexport import *
from swagger_server.tool import *

##24小时投诉日报数据
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
msg_24list_right = {
    "code": 0,
    "msg": "返回成功",
    "result": [
        {
            "area": "宜昌城区",
            "acceptance": "800",
            "complete": "500",
            "unfinished": "200",
            "completed": "100",
            "timely": "60%",
            "average": "8",
            "repeat": "30",
            "repeatrate": "6%",
            "investment": "300"
        },
        {
            "area": "当阳市",
            "acceptance": "800",
            "complete": "500",
            "unfinished": "200",
            "completed": "100",
            "timely": "60%",
            "average": "8",
            "repeat": "30",
            "repeatrate": "6%",
            "investment": "300"
        },
        {
            "area": "宜昌开发区",
            "acceptance": "800",
            "complete": "500",
            "unfinished": "200",
            "completed": "100",
            "timely": "60%",
            "average": "8",
            "repeat": "30",
            "repeatrate": "6%",
            "investment": "300"
        },
        {
            "area": "五峰县",
            "acceptance": "800",
            "complete": "500",
            "unfinished": "200",
            "completed": "100",
            "timely": "60%",
            "average": "8",
            "repeat": "30",
            "repeatrate": "6%",
            "investment": "300"
        },
		 {
            "area": "兴山县",
            "acceptance": "800",
            "complete": "500",
            "unfinished": "200",
            "completed": "100",
            "timely": "60%",
            "average": "8",
            "repeat": "30",
            "repeatrate": "6%",
            "investment": "300"
        },
        {
            "area": "夷陵区",
            "acceptance": "800",
            "complete": "500",
            "unfinished": "200",
            "completed": "100",
            "timely": "60%",
            "average": "8",
            "repeat": "30",
            "repeatrate": "6%",
            "investment": "300"
        },
        {
            "area": "宜都市",
            "acceptance": "800",
            "complete": "500",
            "unfinished": "200",
            "completed": "100",
            "timely": "60%",
            "average": "8",
            "repeat": "30",
            "repeatrate": "6%",
            "investment": "300"
        },
        {
            "area": "远安县",
            "acceptance": "800",
            "complete": "500",
            "unfinished": "200",
            "completed": "100",
            "timely": "60%",
            "average": "8",
            "repeat": "30",
            "repeatrate": "6%",
            "investment": "300"
        },
		 {
            "area": "长阳县",
            "acceptance": "800",
            "complete": "500",
            "unfinished": "200",
            "completed": "100",
            "timely": "60%",
            "average": "8",
            "repeat": "30",
            "repeatrate": "6%",
            "investment": "300"
        },
        {
            "area": "枝江市",
            "acceptance": "800",
            "complete": "500",
            "unfinished": "200",
            "completed": "100",
            "timely": "60%",
            "average": "8",
            "repeat": "30",
            "repeatrate": "6%",
            "investment": "300"
        },
        {
            "area": "姊归县",
            "acceptance": "800",
            "complete": "500",
            "unfinished": "200",
            "completed": "100",
            "timely": "60%",
            "average": "8",
            "repeat": "30",
            "repeatrate": "6%",
            "investment": "300"
        },
        {
            "area": "全市",
            "acceptance": "800",
            "complete": "500",
            "unfinished": "200",
            "completed": "100",
            "timely": "60%",
            "average": "8",
            "repeat": "30",
            "repeatrate": "6%",
            "investment": "300"
        }
    ]
}
msg_list_export = {
  "code": 0,
  "msg": "返回成功",
  "url": "mail.itlaolang.com/downfile/test0.xls"
}


##8小时投诉日报数据
msg_8list_right = {
  "code": 0,
  "msg": "返回成功",
  "result": [
    {
      "area": "宜昌城区",
      "acceptance": "800",
      "complete": "500",
      "undone": "100",
      "completed": "100",
      "rate": "70%",
      "processing": "9"
    },
      {
          "area": "当阳市",
          "acceptance": "800",
          "complete": "500",
          "undone": "100",
          "completed": "100",
          "rate": "70%",
          "processing": "9"
      },
      {
          "area": "宜昌开发区",
          "acceptance": "800",
          "complete": "500",
          "undone": "100",
          "completed": "100",
          "rate": "70%",
          "processing": "9"
      },
      {
          "area": "五峰县",
          "acceptance": "800",
          "complete": "500",
          "undone": "100",
          "completed": "100",
          "rate": "70%",
          "processing": "9"
      },
      {
          "area": "兴山县",
          "acceptance": "800",
          "complete": "500",
          "undone": "100",
          "completed": "100",
          "rate": "70%",
          "processing": "9"
      },
	   {
      "area": "夷陵区",
      "acceptance": "800",
      "complete": "500",
      "undone": "100",
      "completed": "100",
      "rate": "70%",
      "processing": "9"
    },
      {
          "area": "宜都市",
          "acceptance": "800",
          "complete": "500",
          "undone": "100",
          "completed": "100",
          "rate": "70%",
          "processing": "9"
      },
      {
          "area": "远安县",
          "acceptance": "800",
          "complete": "500",
          "undone": "100",
          "completed": "100",
          "rate": "70%",
          "processing": "9"
      },
      {
          "area": "长阳县",
          "acceptance": "800",
          "complete": "500",
          "undone": "100",
          "completed": "100",
          "rate": "70%",
          "processing": "9"
      },
	   {
          "area": "枝江市",
          "acceptance": "800",
          "complete": "500",
          "undone": "100",
          "completed": "100",
          "rate": "70%",
          "processing": "9"
      },
      {
          "area": "姊归县",
          "acceptance": "800",
          "complete": "500",
          "undone": "100",
          "completed": "100",
          "rate": "70%",
          "processing": "9"
      },
      {
          "area": "全市",
          "acceptance": "800",
          "complete": "500",
          "undone": "100",
          "completed": "100",
          "rate": "70%",
          "processing": "9"
      }
  ]
}


##首次联系用户及时率数据
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

##高频小区统计数据
msg_high_chart_right = {
  "code": 0,
  "msg": "返回成功",
  "result": [
    {
      "map": [
        {
          "name": "西陵区",
          "value": "20"
        }
      ],
      "column": [
        {
          "name": "高频小区A",
          "value": "60"
        }
      ]
    },
	 {
      "map": [
        {
          "name": "点军区",
          "value": "10"
        }
      ],
      "column": [
        {
          "name": "高频小区B",
          "value": "65"
        }
      ]
    },
	 {
      "map": [
        {
          "name": "伍家岗区",
          "value": "15"
        }
      ],
      "column": [
        {
          "name": "高频小区C",
          "value": "50"
        }
      ]
    }
  ]
}
msg_high_list_right = {
  "code": 0,
  "msg": "返回成功",
  "result": [
    {
      "id": 1,
      "area": "宜昌城区",
      "community": [
        {
          "id": 1,
          "name": "北门外正街99号",
          "total": "100"
        }
      ]
    },
	 {
      "id": 2,
      "area": "当阳市",
      "community": [
        {
          "id": 2,
          "name": "北门外正街99号",
          "total": "100"
        }
      ]
    },
	 {
      "id": 3,
      "area": "宜昌开发区",
      "community": [
        {
          "id": 3,
          "name": "北门外正街99号",
          "total": "100"
        }
      ]
    },
	 {
      "id": 4,
      "area": "五峰县",
      "community": [
        {
          "id": 4,
          "name": "北门外正街99号",
          "total": "100"
        }
      ]
    },
	 {
      "id": 5,
      "area": "兴山县",
      "community": [
        {
          "id": 5,
          "name": "北门外正街99号",
          "total": "100"
        }
      ]
    },
	 {
      "id": 6,
      "area": "夷陵区",
      "community": [
        {
          "id": 6,
          "name": "北门外正街99号",
          "total": "100"
        }
      ]
    },
	 {
      "id": 7,
      "area": "宜都市",
      "community": [
        {
          "id": 7,
          "name": "北门外正街99号",
          "total": "100"
        }
      ]
    },
	 {
      "id": 7,
      "area": "远安县",
      "community": [
        {
          "id": 7,
          "name": "北门外正街99号",
          "total": "100"
        }
      ]
    },
	 {
      "id": 7,
      "area": "长阳县",
      "community": [
        {
          "id": 7,
          "name": "北门外正街99号",
          "total": "100"
        }
      ]
    },
	 {
      "id": 8,
      "area": "枝江市",
      "community": [
        {
          "id": 8,
          "name": "北门外正街99号",
          "total": "100"
        }
      ]
    },
	 {
      "id": 9,
      "area": "姊归县",
      "community": [
        {
          "id": 9,
          "name": "北门外正街99号",
          "total": "100"
        }
      ]
    },
	 {
      "id": 10,
      "area": "全市",
      "community": [
        {
          "id": 10,
          "name": "北门外正街99号",
          "total": "100"
        }
      ]
    }
  ]
}
msg_high_commuity = {
  "code": 0,
  "msg": "返回成功",
  "total": "18"
}
msg_high_column = {
    "code": 0,
    "msg": "返回成功",
    "result": [
        {
            "name": "高频小区A",
            "value": "60"
        },
        {
            "name": "高频小区B",
            "value": "55"
        },
        {
            "name": "高频小区C",
            "value": "63"
        },
        {
            "name": "高频小区D",
            "value": "68"
        },
        {
            "name": "高频小区E",
            "value": "40"
        },
        {
            "name": "高频小区F",
            "value": "35"
        }
    ]
}

##投诉回访页面数据
msg_visit_list_right = {
  "code": 0,
  "msg": "返回成功",
  "result": [
    {
      "id": 1,
        "area": "宜昌城区",
        "rate": "100%",
        "rank": "1"
       ,
      "ivr": [
        {
          "succ": "10",
          "satisfaction": "10",
          "displeasure": "0"
        }
      ],
      "artificial": [
        {
          "succ1": "10",
          "satisfaction1": "0",
          "displeasure1": "100%"
        }
      ]
    },
	 {
      "id": 2,
         "area": "宜昌城区",
         "rate": "100%",
         "rank": "1"
         ,
      "ivr": [
        {
          "succ": "10",
          "satisfaction": "10",
          "displeasure": "0"
        }
      ],
      "artificial": [
        {
          "succ1": "10",
          "satisfaction1": "0",
          "displeasure1": "100%"
        }
      ]
    },
	{
      "id": 3,
        "area": "宜昌城区",
        "rate": "100%",
        "rank": "1"
        ,
      "ivr": [
        {
          "succ": "10",
          "satisfaction": "10",
          "displeasure": "0"
        }
      ],
      "artificial": [
        {
          "succ1": "10",
          "satisfaction1": "0",
          "displeasure1": "100%"
        }
      ]
    },
	{
      "id": 4,
        "area": "宜昌城区",
        "rate": "100%",
        "rank": "1"
        ,
      "ivr": [
        {
          "succ": "10",
          "satisfaction": "10",
          "displeasure": "0"
        }
      ],
      "artificial": [
        {
          "succ1": "10",
          "satisfaction1": "0",
          "displeasure1": "100%"
        }
      ]
    },
	{
      "id": 5,
        "area": "宜昌城区",
        "rate": "100%",
        "rank": "1"
        ,
      "ivr": [
        {
          "succ1": "10",
          "satisfaction1": "10",
          "displeasure1": "0"
        }
      ],
      "artificial": [
        {
          "succ": "10",
          "satisfaction": "0",
          "displeasure": "100%"
        }
      ]
    },
	{
      "id": 6,
        "area": "宜昌城区",
        "rate": "100%",
        "rank": "1"
        ,
      "ivr": [
        {
          "succ": "10",
          "satisfaction": "10",
          "displeasure": "0"
        }
      ],
      "artificial": [
        {
          "succ1": "10",
          "satisfaction1": "0",
          "displeasure1": "100%"
        }
      ]
    },
	{
      "id": 7,
        "area": "宜昌城区",
        "rate": "100%",
        "rank": "1"
        ,
      "ivr": [
        {
          "succ": "10",
          "satisfaction": "10",
          "displeasure": "0"
        }
      ],
      "artificial": [
        {
          "succ1": "10",
          "satisfaction1": "0",
          "displeasure1": "100%"
        }
      ]
    },
	{
      "id": 8,
        "area": "宜昌城区",
        "rate": "100%",
        "rank": "1"
        ,
      "ivr": [
        {
          "succ": "10",
          "satisfaction": "10",
          "displeasure": "0"
        }
      ],
      "artificial": [
        {
          "succ1": "10",
          "satisfaction1": "0",
          "displeasure1": "100%"
        }
      ]
    },
		{
      "id": 9,
      "area": "长阳县",
      "rate": "100%",
      "rank": "1",
      "ivr": [
        {
          "succ": "10",
          "satisfaction": "10",
          "displeasure": "0"
        }
      ],
      "artificial": [
        {
          "succ1": "10",
          "satisfaction1": "0",
          "displeasure1": "100%"
        }
      ]
    },
		{
      "id": 10,
            "area": "宜昌城区",
            "rate": "100%",
            "rank": "1"
            ,
      "ivr": [
        {
          "succ": "10",
          "satisfaction": "10",
          "displeasure": "0"
        }
      ],
      "artificial": [
        {
          "succ1": "10",
          "satisfaction1": "0",
          "displeasure1": "100%"
        }
      ]
    },
		{
      "id": 11,

            "area": "宜昌城区",
            "rate": "100%",
            "rank": "1"
            ,

      "ivr": [
        {
          "succ": "10",
          "satisfaction": "10",
          "displeasure": "0"
        }
      ],
      "artificial": [
        {
          "succ1": "10",
          "satisfaction1": "0",
          "displeasure1": "100%"
        }
      ]
    },
	{
      "id": 12,
        "area": "宜昌城区",
        "rate": "100%",
        "rank": "1"
        ,
      "ivr": [
        {
          "succ": "10",
          "satisfaction": "10",
          "displeasure": "0"
        }
      ],
      "artificial": [
        {
          "succ1": "10",
          "satisfaction1": "0",
          "displeasure1": "100%"
        }
      ]
    }
  ]
}

##故障处理及时率通报
msg_malfunction_list_right = {
  "code": 0,
  "msg": "返回成功",
  "result": [
    {
      "id": 0,
      "area": "宜昌城区",
      "accept": "1000",
      "complete": "800",
      "timeout": "200",
      "rate": "70%",
      "ave": "9"
    },
	{
      "id": 1,
      "area": "当阳市",
      "accept": "1000",
      "complete": "800",
      "timeout": "200",
      "rate": "70%",
      "ave": "9"
    },
	{
      "id": 2,
      "area": "宜昌开发区",
      "accept": "1000",
      "complete": "800",
      "timeout": "200",
      "rate": "70%",
      "ave": "9"
    },
		{
      "id": 3,
      "area": "五峰县",
      "accept": "1000",
      "complete": "800",
      "timeout": "200",
      "rate": "70%",
      "ave": "9"
    },
		{
      "id": 4,
      "area": "兴山县",
      "accept": "1000",
      "complete": "800",
      "timeout": "200",
      "rate": "70%",
      "ave": "9"
    },
		{
      "id": 5,
      "area": "夷陵区",
      "accept": "1000",
      "complete": "800",
      "timeout": "200",
      "rate": "70%",
      "ave": "9"
    },
		{
      "id": 6,
      "area": "宜都市",
      "accept": "1000",
      "complete": "800",
      "timeout": "200",
      "rate": "70%",
      "ave": "9"
    },
		{
      "id": 7,
      "area": "远安县",
      "accept": "1000",
      "complete": "800",
      "timeout": "200",
      "rate": "70%",
      "ave": "9"
    },
		{
      "id": 8,
      "area": "长阳县",
      "accept": "1000",
      "complete": "800",
      "timeout": "200",
      "rate": "70%",
      "ave": "9"
    },
	{
      "id": 9,
      "area": "枝江市",
      "accept": "1000",
      "complete": "800",
      "timeout": "200",
      "rate": "70%",
      "ave": "9"
    },
		{
      "id": 10,
      "area": "姊归县",
      "accept": "1000",
      "complete": "800",
      "timeout": "200",
      "rate": "70%",
      "ave": "9"
    },
	{
      "id": 11,
      "area": "全市",
      "accept": "1000",
      "complete": "800",
      "timeout": "200",
      "rate": "70%",
      "ave": "9"
    }
  ]
}

##高频故障网元
msg_network_list_right = {
  "code": 0,
  "msg": "返回成功",
  "result": [
    {
      "id": 0,
      "area": "宜昌城区",
      "name": "宜昌/上海春天-OLTO30-ZX",
      "total": "23"
    },
	{
      "id": 1,
      "area": "当阳市",
      "name": "宜昌/上海春天-OLTO30-ZX",
      "total": "23"
    },
	    {
      "id": 2,
      "area": "宜昌开发区",
      "name": "宜昌/上海春天-OLTO30-ZX",
      "total": "23"
    },
	{
      "id": 3,
      "area": "五峰县",
      "name": "宜昌/上海春天-OLTO30-ZX",
      "total": "23"
    },
	 {
      "id": 4,
      "area": "兴山县",
      "name": "宜昌/上海春天-OLTO30-ZX",
      "total": "23"
    },
	{
      "id": 5,
      "area": "夷陵区",
      "name": "宜昌/上海春天-OLTO30-ZX",
      "total": "23"
    },
	 {
      "id": 6,
      "area": "宜都市",
      "name": "宜昌/上海春天-OLTO30-ZX",
      "total": "23"
    },
	{
      "id": 7,
      "area": "远安县",
      "name": "宜昌/上海春天-OLTO30-ZX",
      "total": "23"
    },
		 {
      "id": 8,
      "area": "长阳县",
      "name": "宜昌/上海春天-OLTO30-ZX",
      "total": "23"
    },
	{
      "id": 9,
      "area": "枝江市",
      "name": "宜昌/上海春天-OLTO30-ZX",
      "total": "23"
    },
			 {
      "id": 10,
      "area": "姊归县",
      "name": "宜昌/上海春天-OLTO30-ZX",
      "total": "23"
    },
	{
      "id": 11,
      "area": "全市",
      "name": "宜昌/上海春天-OLTO30-ZX",
      "total": "23"
    }
  ]
}

##投诉处理时长Top20数据
msg_top_list_right = {
  "code": 0,
  "msg": "返回成功",
  "result": [
    {
      "id": 1,
      "area": "宜昌城区",
      "number": "1234567",
      "contacts": "小明",
      "phone": "13788888888",
      "t2": "2018/03/18 12：00",
      "times": "36"
    },
	 {
      "id": 2,
      "area": "当阳市",
         "number": "1234567",
      "contacts": "小明",
      "phone": "13788888888",
      "t2": "2018/03/18 12：00",
      "times": "36"
    },
		 {
      "id": 3,
      "area": "宜昌开发区",
             "number": "1234567",
      "contacts": "小明",
      "phone": "13788888888",
      "t2": "2018/03/18 12：00",
      "times": "36"
    },
	 {
      "id": 4,
      "area": "五峰县",
        "number": "1234567",
      "contacts": "小明",
      "phone": "13788888888",
      "t2": "2018/03/18 12：00",
      "times": "36"
    },
		 {
      "id": 5,
      "area": "兴山县",
        "number": "1234567",
      "contacts": "小明",
      "phone": "13788888888",
      "t2": "2018/03/18 12：00",
      "times": "36"
    },
		 {
      "id": 6,
      "area": "夷陵区",
        "number": "1234567",
      "contacts": "小明",
      "phone": "13788888888",
      "t2": "2018/03/18 12：00",
      "times": "36"
    },
		 {
      "id": 7,
      "area": "宜都市",
        "number": "1234567",
      "contacts": "小明",
      "phone": "13788888888",
      "t2": "2018/03/18 12：00",
      "times": "36"
    },
			 {
      "id": 8,
      "area": "远安县",
        "number": "1234567",
      "contacts": "小明",
      "phone": "13788888888",
      "t2": "2018/03/18 12：00",
      "times": "36"
    },
		 {
      "id": 9,
      "area": "长阳县",
        "number": "1234567",
      "contacts": "小明",
      "phone": "13788888888",
      "t2": "2018/03/18 12：00",
      "times": "36"
    },
			 {
      "id": 10,
      "area": "枝江市",
        "number": "1234567",
      "contacts": "小明",
      "phone": "13788888888",
      "t2": "2018/03/18 12：00",
      "times": "36"
    },
		 {
      "id": 11,
      "area": "姊归县",
        "number": "1234567",
      "contacts": "小明",
      "phone": "13788888888",
      "t2": "2018/03/18 12：00",
      "times": "36"
    },
	 {
      "id": 11,
      "area": "全市",
        "number": "1234567",
      "contacts": "小明",
      "phone": "13788888888",
      "t2": "2018/03/18 12：00",
      "times": "36"
    }
  ]
}

##24小时投诉日报接口方法
def complain_twenty_four_chart_get(type='投诉处理及时率',starttime=None, endtime=None):  # noqa: E501
    """24-hour complaint daily chart

    24-hour complaint daily chart # noqa: E501

    :param starttime: the starttime for user choose
    :type starttime: str
    :param endtime: the endtime for user choose
    :type endtime: str
    :param type: the user choose type
    :type type: str

    :rtype: HomeChart
    """
    # try:
    #
    # except:
    #     msg={"code":-1,'msg':'Error'}
    if starttime == '':
        starttime = "2018-02-14 00:00:00"
    if endtime == '':
        endtime = "2018-02-15 00:00:00"

    starttime = str(starttime)
    endtime = str(endtime)
    area_list = ['秭归', '枝江', '长阳', '远安', '宜都', '夷陵', '兴山', '五峰', '开发区', '当阳', '城区']
    wtb = [18203, 25378, 18385, 12884, 17538, 27196, 7453, 7985, 34313, 25349, 25171]
    result_list = []
    print(type)
    if type == '投诉处理及时率':

        for i in range(len(area_list)):
            avetime = 0
            like = "%" + area_list[i] + "%"
            print(i)
            print(like)
            acceptance = YCcomplaints.select().where((YCcomplaints.platform == 2) & (YCcomplaints.area % like) & (
            YCcomplaints.starttime >= utc_str_to_timestamp(starttime)) & (
                                                     YCcomplaints.starttime <= utc_str_to_timestamp(endtime))).count()

            complete = YCcomplaints.select().where((YCcomplaints.platform == 2) & (YCcomplaints.area % like) & (
            YCcomplaints.endtime >= utc_str_to_timestamp(starttime)) & (
                                                   YCcomplaints.endtime <= utc_str_to_timestamp(endtime)) & (
                                                   YCcomplaints.status == '归档')).count()

            unfinished = YCcomplaints.select().where((YCcomplaints.platform == 2) & (YCcomplaints.area % like) & (
            YCcomplaints.starttime >= utc_str_to_timestamp(starttime)) & (
                                                     YCcomplaints.starttime <= utc_str_to_timestamp(endtime)) & (
                                                     YCcomplaints.status != '归档') & (
                                                     YCcomplaints.timeout == '是')).count()
            print(unfinished)
            completed = YCcomplaints.select().where((YCcomplaints.platform == 2) & (YCcomplaints.area % like) & (
                YCcomplaints.starttime >= utc_str_to_timestamp(starttime)) & (
                                                        YCcomplaints.starttime <= utc_str_to_timestamp(endtime)) & (
                                                        YCcomplaints.status == '归档') & (
                                                        YCcomplaints.timeout == '是')).count()

            print('com', completed)
            try:
                timely =1-( (unfinished+completed) / acceptance)
            except:
                timely = 1
            msg_list = {
                "name": area_list[i],
                "value": '%.2f' % (timely * 100),
            }
            print(msg_list)
            result_list.append(msg_list)
    if type == '投诉平均处理时长':

        for i in range(len(area_list)):
            avetime = 0
            like = "%" + area_list[i] + "%"
            print(i)
            print(like)
            acceptance = YCcomplaints.select().where((YCcomplaints.platform == 2) & (YCcomplaints.area % like) & (
                YCcomplaints.starttime >= utc_str_to_timestamp(starttime)) & (
                                                         YCcomplaints.starttime <= utc_str_to_timestamp(
                                                             endtime))).count()

            complete = YCcomplaints.select().where((YCcomplaints.platform == 2) & (YCcomplaints.area % like) & (
                YCcomplaints.endtime >= utc_str_to_timestamp(starttime)) & (
                                                       YCcomplaints.endtime <= utc_str_to_timestamp(endtime)) & (
                                                       YCcomplaints.status == '归档')).count()

            try:
                timely = (YCcomplaints.select().where((YCcomplaints.platform == 2) & (YCcomplaints.area % like) & (
                    YCcomplaints.starttime - YCcomplaints.endtime <= 24 * 60 * 60) & (YCcomplaints.status == '归档') & (
                                                          YCcomplaints.starttime >= utc_str_to_timestamp(starttime)) & (
                                                          YCcomplaints.starttime <= utc_str_to_timestamp(
                                                              endtime))).count()) / acceptance
            except:
                timely=0
            print(timely)
            result = YCcomplaints.select().where(
                (YCcomplaints.platform == 2) & (YCcomplaints.area % like) & (YCcomplaints.status == '归档') & (
                    YCcomplaints.endtime >= utc_str_to_timestamp(starttime)) & (
                    YCcomplaints.endtime <= utc_str_to_timestamp(endtime)))

            for item in result:
                avetime = item.usetime + avetime
            try:
                av_time = '%.2f' % (avetime / complete)
            except:
                av_time = 0

            msg_list = {
                "name": area_list[i],

                "value": av_time,

            }
            print(msg_list)
            result_list.append(msg_list)
    if type == '重复投诉率':

        for i in range(len(area_list)):
            msg_list = {
                "name": area_list[i],

                "value": 0,

            }
            print(msg_list)
            result_list.append(msg_list)
    if type == '万投比':

        for i in range(len(area_list)):
            avetime = 0
            like = "%" + area_list[i] + "%"
            print(i)
            print(like)
            acceptance = YCcomplaints.select().where((YCcomplaints.platform == 2) & (YCcomplaints.area % like) & (
                YCcomplaints.starttime >= utc_str_to_timestamp(starttime)) & (
                                                         YCcomplaints.starttime <= utc_str_to_timestamp(
                                                             endtime))).count()

            msg_list = {
                "name": area_list[i],

                "value": "%.2f" % ((acceptance * 10000) / wtb[i]),

            }
            print(msg_list)
            result_list.append(msg_list)

    msg = {"code": 0, "msg": "success", "result": result_list}
    return msg

def complain_twenty_four_info_export_get(type):  # noqa: E501
    """24-hour complaint daily list export

    24-hour complaint daily list export # noqa: E501

    :param type: the type for user choose
    :type type: str

    :rtype: DownUrl
    """
    print(type)
    type_list=type.split('_')
    starttime=type_list[0]
    endtime=type_list[1]
    if starttime == '':
        starttime = "2018-02-14 00:00:00"
    if endtime == '':
        endtime = "2018-02-15 00:00:00"
    choose_type=type_list[3]
    area=type_list[2]
    datatype=type_list[4]
    url=complain_export(starttime=starttime,endtime=endtime,choose_type=choose_type,area=area,datatype=datatype)
    print (url)
    msg={"code":0,"msg":"success","url":url}
    return msg
def complain_twenty_four_list_export_get(type,starttime=None, endtime=None):  # noqa: E501
    """24-hour complaint daily list export

    24-hour complaint daily list export # noqa: E501

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
            starttime = "2018-02-14 00:00:00"
        if endtime == '':
            endtime = "2018-02-15 00:00:00"
        starttime=str(starttime)
        endtime=str(endtime)

        file_path=type.split('_')[0].replace("mail.itlaolang.com/downfile/","/var/www/downfile/")
        print(file_path,starttime,endtime,type)
        url = make_file1(file_path=file_path,type='投诉24小时报表',starttime=str(starttime), endtime=str(endtime),choose_type=str(type.split('_')[1]))
        msg={"code":0,"msg":"success","url":url}
    except:
         msg={"code":-1,"msg":"Error"}
    return msg
def complain_twenty_four_list_get(type,starttime=None, endtime=None):  # noqa: E501
    """24-hour complaint daily list

    24-hour complaint daily list # noqa: E501

    :param starttime: the starttime for user choose
    :type starttime: str
    :param endtime: the endtime for user choose
    :type endtime: str
    :param type: the type for user choose
    :type type: str

    :rtype: TwentyList
    """
    if starttime == '':
        starttime = "2018-02-14 00:00:00"
    if endtime == '':
        endtime = "2018-02-15 00:00:00"
    starttime = str(starttime)
    endtime = str(endtime)
    area_list = ['秭归', '枝江', '长阳', '远安', '宜都', '夷陵', '兴山', '五峰', '开发区', '当阳', '城区']
    wtb = [18203, 25378, 18385, 12884, 17538, 27196, 7453, 7985, 34313, 25349, 25171]
    result_list = []
    if type == 'EMOS':

        for i in range(len(area_list)):
            avetime = 0
            like = "%" + area_list[i] + "%"
            print(i)
            print(like)
            acceptance = YCcomplaints.select().where((YCcomplaints.platform == 2) & (YCcomplaints.area % like) & (
            YCcomplaints.starttime >= utc_str_to_timestamp(starttime)) & (
                                                     YCcomplaints.starttime <= utc_str_to_timestamp(endtime))).count()

            complete = YCcomplaints.select().where((YCcomplaints.platform == 2) & (YCcomplaints.area % like) & (
            YCcomplaints.endtime >= utc_str_to_timestamp(starttime)) & (
                                                   YCcomplaints.endtime <= utc_str_to_timestamp(endtime)) & (
                                                   YCcomplaints.status == '归档')).count()

            unfinished = YCcomplaints.select().where((YCcomplaints.platform == 2) & (YCcomplaints.area % like) & (
            YCcomplaints.starttime >= utc_str_to_timestamp(starttime)) & (
                                                     YCcomplaints.starttime <= utc_str_to_timestamp(endtime)) & (
                                                     YCcomplaints.status != '归档') & (
                                                     YCcomplaints.timeout == '是')).count()
            print(unfinished)
            completed = YCcomplaints.select().where((YCcomplaints.platform == 2) & (YCcomplaints.area % like) & (
                YCcomplaints.starttime >= utc_str_to_timestamp(starttime)) & (
                                                        YCcomplaints.starttime <= utc_str_to_timestamp(endtime)) & (
                                                        YCcomplaints.status == '归档') & (
                                                        YCcomplaints.timeout == '是')).count()

            try:
                timely =1-((unfinished+completed)/ acceptance)
            except:
                timely=1
            print(timely)
            result = YCcomplaints.select().where(
                (YCcomplaints.platform == 2) & (YCcomplaints.area % like) & (YCcomplaints.status == '归档') & (
                YCcomplaints.endtime >= utc_str_to_timestamp(starttime)) & (
                YCcomplaints.endtime <= utc_str_to_timestamp(endtime)))

            for item in result:
                avetime = item.usetime + avetime
            try:
                av_time = '%.2f' % (avetime / complete)
            except:
                av_time = 0

            repeat = 0
            repeatrate = '0%'
            investment = (acceptance * 10000) / wtb[i]

            msg_list = {
                "area": area_list[i],
                "acceptance": acceptance,
                "complete": complete,
                "unfinished": unfinished,
                "completed": completed,
                "timely": str('%.2f' % (timely * 100)) + '%',
                "average": av_time,
                "repeat": repeat,
                "repeatrate": repeatrate,
                "investment": '%.2f' % investment,

            }
            print(msg_list)
            result_list.append(msg_list)
    if type == '全量工单':

        for i in range(len(area_list)):
            avetime = 0
            like = "%" + area_list[i] + "%"
            print(i)
            print(like)
            acceptance = YCcomplaints.select().where(
                (YCcomplaints.area % like) & (YCcomplaints.starttime >= utc_str_to_timestamp(starttime)) & (
                YCcomplaints.starttime <= utc_str_to_timestamp(endtime))).count()

            complete = YCcomplaints.select().where(
                (YCcomplaints.area % like) & (YCcomplaints.endtime >= utc_str_to_timestamp(starttime)) & (
                YCcomplaints.endtime <= utc_str_to_timestamp(endtime)) & (YCcomplaints.status == '归档')).count()

            unfinished = YCcomplaints.select().where(
                (YCcomplaints.area % like) & (YCcomplaints.starttime >= utc_str_to_timestamp(starttime)) & (
                YCcomplaints.starttime <= utc_str_to_timestamp(endtime)) & (YCcomplaints.status != '归档') & (
                YCcomplaints.timeout == '是')).count()
            print(unfinished)
            completed = YCcomplaints.select().where((YCcomplaints.area % like) & (
                YCcomplaints.starttime >= utc_str_to_timestamp(starttime)) & (
                                                        YCcomplaints.starttime <= utc_str_to_timestamp(endtime)) & (
                                                        YCcomplaints.status == '归档') & (
                                                        YCcomplaints.timeout == '是')).count()

            print('com', completed)
            try:
                timely = 1-((unfinished+completed)/ acceptance)
            except:
                timely = 1
            result = YCcomplaints.select().where((YCcomplaints.area % like) & (YCcomplaints.status == '归档') & (
            YCcomplaints.endtime >= utc_str_to_timestamp(starttime)) & (
                                                 YCcomplaints.endtime <= utc_str_to_timestamp(endtime)))

            for item in result:
                avetime = item.usetime + avetime
            try:
                av_time = '%.2f' % (avetime / complete)
            except:
                av_time = 0

            repeat = 0
            repeatrate = '0%'
            investment = (acceptance * 10000) / wtb[i]

            msg_list = {
                "area": area_list[i],
                "acceptance": acceptance,
                "complete": complete,
                "unfinished": unfinished,
                "completed": completed,
                "timely": str('%.2f' % (timely * 100)) + '%',
                "average": av_time,
                "repeat": repeat,
                "repeatrate": repeatrate,
                "investment": '%.2f' % investment,

            }
            print(msg_list)
            result_list.append(msg_list)

    if type == 'CRM':
        avetime = 0
        for i in range(len(area_list)):
            like = "%" + area_list[i] + "%"

            acceptance = YCcomplaints.select().where((YCcomplaints.platform == 3) & (YCcomplaints.area % like) & (
                YCcomplaints.starttime >= utc_str_to_timestamp(starttime)) & (
                                                         YCcomplaints.starttime <= utc_str_to_timestamp(
                                                             endtime))).count()

            complete = YCcomplaints.select().where((YCcomplaints.platform == 3) & (YCcomplaints.area % like) & (
                YCcomplaints.endtime >= utc_str_to_timestamp(starttime)) & (
                                                       YCcomplaints.endtime <= utc_str_to_timestamp(
                                                           endtime)) & (YCcomplaints.status == '是')).count()

            unfinished = YCcomplaints.select().where((YCcomplaints.platform == 3) & (YCcomplaints.area % like) & (
                YCcomplaints.starttime >= utc_str_to_timestamp(starttime)) & (
                                                         YCcomplaints.starttime <= utc_str_to_timestamp(
                                                             endtime)) & (YCcomplaints.status != '是') & (
                                                         YCcomplaints.timeout == '是')).count()

            completed = YCcomplaints.select().where((YCcomplaints.platform == 3) & (YCcomplaints.area % like) & (
                YCcomplaints.starttime >= utc_str_to_timestamp(starttime)) & (
                                                        YCcomplaints.starttime <= utc_str_to_timestamp(
                                                            endtime)) & (
                                                        YCcomplaints.status == '是') & (
                                                        YCcomplaints.timeout == '是')).count()

            try:
                timely = 1-((unfinished+completed)/ acceptance)
            except:
                timely = 1

            av_time = 0

            repeat = 0
            repeatrate = '0%'

            investment = (acceptance * 10000) / wtb[i]

            msg_list = {
                "area": area_list[i],
                "acceptance": acceptance,
                "complete": complete,
                "unfinished": unfinished,
                "completed": completed,
                "timely": str('%.2f' % (timely * 100)) + '%',
                "average": av_time,
                "repeat": repeat,
                "repeatrate": repeatrate,
                "investment": '%.2f' % investment,

            }
            result_list.append(msg_list)
            print(msg_list)
    if type == '一键报障':

        for i in range(len(area_list)):
            avetime = 0
            like = "%" + area_list[i] + "%"

            acceptance = YCcomplaints.select().where((YCcomplaints.platform == 1) & (YCcomplaints.area % like) & (
                YCcomplaints.starttime >= utc_str_to_timestamp(starttime)) & (
                                                         YCcomplaints.starttime <= utc_str_to_timestamp(
                                                             endtime))).count()

            complete = YCcomplaints.select().where((YCcomplaints.platform == 1) & (YCcomplaints.area % like) & (
                YCcomplaints.endtime >= utc_str_to_timestamp(starttime)) & (
                                                       YCcomplaints.endtime <= utc_str_to_timestamp(
                                                           endtime)) & (YCcomplaints.status == '归档')).count()

            unfinished = YCcomplaints.select().where((YCcomplaints.platform == 1) & (YCcomplaints.area % like) & (
                YCcomplaints.starttime >= utc_str_to_timestamp(starttime)) & (
                                                         YCcomplaints.starttime <= utc_str_to_timestamp(
                                                             endtime)) & (YCcomplaints.status != '归档') & (
                                                         YCcomplaints.timeout == '是')).count()

            completed = YCcomplaints.select().where((YCcomplaints.platform == 1) & (YCcomplaints.area % like) & (
                YCcomplaints.starttime >= utc_str_to_timestamp(starttime)) & (
                                                        YCcomplaints.starttime <= utc_str_to_timestamp(
                                                            endtime)) & (
                                                        YCcomplaints.status == '归档') & (
                                                        YCcomplaints.timeout == '是')).count()
            print('------------', acceptance)

            try:
                    timely = 1 - ((unfinished + completed) / acceptance)
            except:
                    timely = 1


            result = YCcomplaints.select().where(
                (YCcomplaints.platform == 1) & (YCcomplaints.area % like) & (YCcomplaints.status == '归档') & (
                    YCcomplaints.starttime >= utc_str_to_timestamp(starttime)) & (
                    YCcomplaints.starttime <= utc_str_to_timestamp(endtime)))

            for item in result:
                avetime = item.usetime + avetime

            try:
                av_time = '%2f' % (avetime / complete)
            except:
                av_time = 0.00
            print(av_time)
            repeat = 0
            repeatrate = '0%'

            investment = (acceptance * 10000) / wtb[i]
            print(investment)
            msg_list = {
                "area": area_list[i],
                "acceptance": acceptance,
                "complete": complete,
                "unfinished": unfinished,
                "completed": completed,
                "timely": str('%.2f' % (timely * 100)) + '%',
                "average": av_time,
                "repeat": repeat,
                "repeatrate": repeatrate,
                "investment": '%.2f' % investment,

            }

            result_list.append(msg_list)

    msg = {"code": 0, "msg": "success", "result": result_list}
    #try:

    #except:
    #    msg={"code":-1,'msg':'Error'}
    return msg


##8小时投诉日报接口方法
def complain_eight_chart_get(type,starttime=None, endtime=None):  # noqa: E501
    """eight hour complaint daily chart

    eight hour complaint daily chart # noqa: E501

    :param starttime: the starttime for user choose
    :type starttime: str
    :param endtime: the endtime for user choose
    :type endtime: str
    :param type: the user choose type
    :type type: str

    :rtype: HomeChart
    """
    try:
        if starttime == '':
            starttime = "2018-02-14 00:00:00"
        if endtime == '':
            endtime = "2018-02-15 00:00:00"
        starttime = str(starttime)
        endtime = str(endtime)
        area_list = ['秭归', '枝江', '长阳', '远安', '宜都', '夷陵', '兴山', '五峰', '开发区', '当阳', '城区']
        result_list = []
        if type == '投诉处理及时率':
            for i in range(len(area_list)):
                like = "%" + area_list[i] + "%"
                acceptance = YCcomplaints.select().where((YCcomplaints.platform == 2) & (YCcomplaints.area % like) & (
                YCcomplaints.starttime >= utc_str_to_timestamp(starttime)) & (
                                                         YCcomplaints.starttime <= utc_str_to_timestamp(
                                                             endtime))).count()

                timely = (YCcomplaints.select().where((YCcomplaints.platform == 2) & (YCcomplaints.area % like) & (
                YCcomplaints.endtime - YCcomplaints.starttime <= 20 * 60 * 60) & (YCcomplaints.status == '归档') & (
                                                      YCcomplaints.starttime >= utc_str_to_timestamp(starttime)) & (
                                                      YCcomplaints.starttime <= utc_str_to_timestamp(
                                                          endtime))).count()) / acceptance


                msg_list = {
                    "name": area_list[i],
                    "value": '%.2f' % (timely * 100) ,
                }
                print(msg_list)

                result_list.append(msg_list)
        else:
            for i in range(len(area_list)):
                avetime = 0
                like = "%" + area_list[i] + "%"
                acceptance = YCcomplaints.select().where((YCcomplaints.platform == 2) & (YCcomplaints.area % like) & (
                    YCcomplaints.starttime >= utc_str_to_timestamp(starttime)) & (
                                                             YCcomplaints.starttime <= utc_str_to_timestamp(
                                                                 endtime))).count()

                complete = YCcomplaints.select().where((YCcomplaints.platform == 2) & (YCcomplaints.area % like) & (
                    YCcomplaints.endtime >= utc_str_to_timestamp(starttime)) & (
                                                           YCcomplaints.endtime <= utc_str_to_timestamp(endtime)) & (
                                                           YCcomplaints.status == '归档')).count()
                result = YCcomplaints.select().where(
                    (YCcomplaints.platform == 2) & (YCcomplaints.area % like) & (YCcomplaints.status == '归档') & (
                        YCcomplaints.endtime >= utc_str_to_timestamp(starttime)) & (
                        YCcomplaints.endtime <= utc_str_to_timestamp(endtime)))

                for item in result:
                    avetime = item.usetime + avetime
                try:
                    av_time = '%.2f' % (avetime / complete)
                except:
                    av_time = 0

                # repeat=0
                # repeatrate='0%'
                # investment=(acceptance*10000)/wtb[i]

                msg_list = {
                    "name": area_list[i],

                    "value": av_time,
                    # "repeat": repeat,
                    # "repeatrate": repeatrate,
                    # "investment": '%.2f' % investment,

                }
                result_list.append(msg_list)
        msg = {"code": 0, "msg": "success", "result": result_list}
    except:
        msg={"code":-1,"msg":"Error"}
    return msg

def complain_eight_info_export_get(type):  # noqa: E501
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
        starttime = "2018-02-14 00:00:00"
    if endtime == '':
        endtime = "2018-02-15 00:00:00"
    choose_type = type_list[3]
    area = type_list[2]
    datatype = type_list[4]
    url = complain_export_8(starttime=starttime, endtime=endtime, choose_type=choose_type, area=area, datatype=datatype)
    print (url)
    msg = {"code": 0, "msg": "success", "url": url}
    return msg
def complain_eight_list_export_get(type,starttime=None, endtime=None):  # noqa: E501
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
    # try:

    starttime=str(starttime)
    endtime=str(endtime)

    if starttime=='':
        starttime="2018-02-14 00:00:00"
    if endtime=='':
        endtime="2018-02-15 00:00:00"
    file_path =type.split('_')[0].replace('mail.itlaolang.com/downfile/','/var/www/downfile/')

    url = make_file1(file_path=file_path,type='投诉8小时报表',starttime=str(starttime), endtime=str(endtime),choose_type=str(type.split('_')[1]))
    msg={"code":0,"msg":"success","url":url}
    # except:
    #      msg={"code":-1,"msg":"Error"}
    return msg
def complain_eight_list_get(type,starttime=None, endtime=None):  # noqa: E501
    """eight hour complaint daily list

    eight hour complaint daily list # noqa: E501

    :param starttime: the starttime for user choose
    :type starttime: str
    :param endtime: the endtime for user choose
    :type endtime: str
    :param type: the type for user choose
    :type type: str

    :rtype: EightList
    """

    if starttime=='':
        starttime="2018-02-14 00:00:00"
    if endtime=='':
        endtime="2018-02-15 00:00:00"
    starttime=str(starttime)
    endtime=str(endtime)
    area_list=['秭归','枝江','长阳','远安','宜都','夷陵','兴山','五峰','开发区','当阳','城区']
    wtb=[18203,25378,18385,12884,17538,27196,7453,34313,7985,25349,25171]
    result_list=[]
    if type=='EMOS':

       for i in range(len(area_list)):
           avetime = 0
           like="%"+area_list[i]+"%"
           print(i)
           print(like)
           acceptance=YCcomplaints.select().where((YCcomplaints.platform==2) & (YCcomplaints.area % like) & (YCcomplaints.starttime>=utc_str_to_timestamp(starttime)) & (YCcomplaints.starttime<=utc_str_to_timestamp(endtime))).count()

           complete=YCcomplaints.select().where((YCcomplaints.platform==2) & (YCcomplaints.area % like) & (YCcomplaints.endtime>=utc_str_to_timestamp(starttime)) & (YCcomplaints.endtime<=utc_str_to_timestamp(endtime)) & (YCcomplaints.status=='归档')).count()

           unfinished=YCcomplaints.select().where((YCcomplaints.platform==2) & (YCcomplaints.area % like) & (YCcomplaints.starttime>=utc_str_to_timestamp(starttime)) & (YCcomplaints.starttime<=utc_str_to_timestamp(endtime)) & (YCcomplaints.status!='归档')).count()

           completed=YCcomplaints.select().where((YCcomplaints.platform == 2) & (YCcomplaints.area % like) & (
                   YCcomplaints.starttime >= utc_str_to_timestamp(starttime)) & (
                   YCcomplaints.starttime <= utc_str_to_timestamp(endtime)) & (
                                                   YCcomplaints.status == '归档') & (YCcomplaints.usetime >=20)).count()


           timely=(YCcomplaints.select().where((YCcomplaints.platform == 2) & (YCcomplaints.area % like) & (YCcomplaints.endtime-YCcomplaints.starttime <=20*60*60) & (YCcomplaints.status == '归档') &(YCcomplaints.starttime>=utc_str_to_timestamp(starttime)) & (YCcomplaints.starttime<=utc_str_to_timestamp(endtime))).count())/acceptance
           print(timely)
           result=YCcomplaints.select().where((YCcomplaints.platform == 2) & (YCcomplaints.area % like) & (YCcomplaints.status == '归档') & (YCcomplaints.endtime>=utc_str_to_timestamp(starttime)) & (YCcomplaints.endtime<=utc_str_to_timestamp(endtime)))

           for item in result:
               avetime=item.usetime+avetime
           try:
               av_time = '%.2f' % (avetime / complete)
           except:
               av_time=0


           # repeat=0
           # repeatrate='0%'
           # investment=(acceptance*10000)/wtb[i]

           msg_list = {
               "area": area_list[i],
               "acceptance": acceptance,
               "complete": complete,
               "undone": unfinished,
               "completed": completed,
               "rate": str('%.2f' % (timely * 100)) + '%',
               "processing": av_time,
               # "repeat": repeat,
               # "repeatrate": repeatrate,
               # "investment": '%.2f' % investment,

           }
           print(msg_list)
           result_list.append(msg_list)



    if type == '一键报障' or type=='微信一键报障':

        for i in range(len(area_list)):
            avetime = 0
            like = "%" + area_list[i] + "%"

            acceptance = YCcomplaints.select().where((YCcomplaints.platform == 1) & (YCcomplaints.area % like) & (
                        YCcomplaints.starttime >= utc_str_to_timestamp(starttime)) & (
                                                                 YCcomplaints.starttime <= utc_str_to_timestamp(
                                                             endtime))).count()

            complete = YCcomplaints.select().where((YCcomplaints.platform == 1) & (YCcomplaints.area % like) & (
                        YCcomplaints.endtime >= utc_str_to_timestamp(starttime)) & (
                                                               YCcomplaints.endtime <= utc_str_to_timestamp(
                                                           endtime)) & (YCcomplaints.status == '归档')).count()

            unfinished = YCcomplaints.select().where((YCcomplaints.platform == 1) & (YCcomplaints.area % like) & (
                        YCcomplaints.starttime >= utc_str_to_timestamp(starttime)) & (
                                                                 YCcomplaints.starttime <= utc_str_to_timestamp(
                                                             endtime)) & (YCcomplaints.status != '归档')).count()

            completed = YCcomplaints.select().where((YCcomplaints.platform == 1) & (YCcomplaints.area % like) & (
                    YCcomplaints.endtime >= utc_str_to_timestamp(starttime)) & (
                                                            YCcomplaints.endtime <= utc_str_to_timestamp(
                                                        endtime)) & (
                                                            YCcomplaints.status == '归档') & (YCcomplaints.usetime >=20)).count()

            if acceptance!=0:
                timely = (YCcomplaints.select().where((YCcomplaints.platform == 1) & (YCcomplaints.area % like) & (YCcomplaints.usetime <= 8) & (
                                                              YCcomplaints.status == '归档') & (
                                                              YCcomplaints.starttime >= utc_str_to_timestamp(
                                                          starttime)) & (
                                                              YCcomplaints.starttime <= utc_str_to_timestamp(
                                                          endtime))).count()) / acceptance
            else:
                timely=1

            result = YCcomplaints.select().where(
                (YCcomplaints.platform == 1) & (YCcomplaints.area % like) & (YCcomplaints.status == '归档') & (
                            YCcomplaints.starttime >= utc_str_to_timestamp(starttime)) & (
                            YCcomplaints.starttime <= utc_str_to_timestamp(endtime)))

            for item in result:
                avetime = item.usetime + avetime

            try:
                av_time = '%2f' % (avetime / complete)
            except:
                av_time=0.00
            print(av_time)
            # repeat = 0
            # repeatrate = '0%'
            #
            # investment = (acceptance * 10000) / wtb[i]

            msg_list = {
                "area": area_list[i],
                "acceptance": acceptance,
                "complete": complete,
                "undone": unfinished,
                "completed": completed,
                "rate": str('%.2f' % (timely * 100)) + '%',
                "processing": av_time,
                # "repeat": repeat,
                # "repeatrate": repeatrate,
                # "investment": '%.2f' % investment,

            }

            result_list.append(msg_list)

    msg={"code":0,"msg":"success","result":result_list}


    return msg


##首次联系用户及时率接口方法
def complain_emos_first_chart_get(type,starttime=None, endtime=None):  # noqa: E501
    """emos Timely acceptance rate

    emos Timely acceptance rate # noqa: E501

    :param starttime: the starttime for user choose
    :type starttime: str
    :param endtime: the endtime for user choose
    :type endtime: str
    :param type: the user choose type
    :type type: str

    :rtype: EmosFirstChart
    """
    result=[]
    if starttime=='':
        starttime='2018-02-14 00:00:00'
    if endtime=='':
        endtime='2018-02-15 00:00:00'
    if type=='首次联系用户时长':
        area_list = ['秭归', '枝江', '长阳', '远安', '宜都', '夷陵', '兴山', '五峰', '开发区', '当阳', '城区']
        for area in area_list:
            avetime = 0
            like = '%' + area + '%'
            data = YCcomplaints.select().where((YCcomplaints.platform == 2) & (YCcomplaints.area % like) & (
                YCcomplaints.starttime >= utc_str_to_timestamp(starttime)) & (
                                                   YCcomplaints.starttime <= utc_str_to_timestamp(endtime)))
            acceptance = YCcomplaints.select().where((YCcomplaints.platform == 2) & (YCcomplaints.area % like) & (
                YCcomplaints.starttime >= utc_str_to_timestamp(starttime)) & (
                                                         YCcomplaints.starttime <= utc_str_to_timestamp(
                                                             endtime))).count()

            oneToTwo = data.where((YCcomplaints.fristtime - YCcomplaints.starttime) / 3600 <= 2).count()
            twoToTen = data.where(((YCcomplaints.fristtime - YCcomplaints.starttime) / 3600 > 2) & (
            (YCcomplaints.fristtime - YCcomplaints.starttime) / 3600 <= 10)).count()
            tenToTwentyFour = data.where(((YCcomplaints.fristtime - YCcomplaints.starttime) / 3600 > 10) & (
            (YCcomplaints.fristtime - YCcomplaints.starttime) / 3600 <= 24)).count()
            twentfour = data.where((YCcomplaints.fristtime - YCcomplaints.starttime) / 3600 > 24).count()
            try:
                oneToTwo_1 = str('%.2f' % ((oneToTwo / acceptance) * 100)) + '%'
            except:
                oneToTwo_1 = '0.00%'
            try:
                twoToTen_1 = str('%.2f' % ((twoToTen / acceptance) * 100)) + '%'
            except:
                twoToTen_1 = '0.00%'
            try:
                tenToTwentyFour_1 = str('%.2f' % ((tenToTwentyFour / acceptance) * 100)) + '%'
            except:
                tenToTwentyFour_1 = '0.00%'
            try:
                twentfour_1 = str('%.2f' % ((twentfour / acceptance) * 100)) + '%'
            except:
                twentfour_1 = '0.00%'

            for item in data:
                try:
                    firsttime = (int(item.fristtime) - int(item.starttime)) / 3600
                except:
                    firsttime = 0
            avtime = avetime + firsttime
            try:
                av_time = avtime / acceptance
            except:
                av_time = 0
            msg_list = {"area": area,
                        "inside":oneToTwo,
                        'ultra':acceptance-oneToTwo ,
                        }
            result.append(msg_list)
        msg = {"code": 0, "msg": "success", "result": result}
    if type=='首次联系用户时长占比':
        area_list = ['秭归', '枝江', '长阳', '远安', '宜都', '夷陵', '兴山', '五峰', '开发区', '当阳', '城区']
        for area in area_list:
            avetime = 0
            like = '%' + area + '%'
            data = YCcomplaints.select().where((YCcomplaints.platform == 2) & (YCcomplaints.area % like) & (
                YCcomplaints.starttime >= utc_str_to_timestamp(starttime)) & (
                                                   YCcomplaints.starttime <= utc_str_to_timestamp(endtime)))
            acceptance = YCcomplaints.select().where((YCcomplaints.platform == 2) & (YCcomplaints.area % like) & (
                YCcomplaints.starttime >= utc_str_to_timestamp(starttime)) & (
                                                         YCcomplaints.starttime <= utc_str_to_timestamp(
                                                             endtime))).count()

            oneToTwo = data.where((YCcomplaints.fristtime - YCcomplaints.starttime) / 3600 <= 2).count()
            twoToTen = data.where(((YCcomplaints.fristtime - YCcomplaints.starttime) / 3600 > 2) & (
                (YCcomplaints.fristtime - YCcomplaints.starttime) / 3600 <= 10)).count()
            tenToTwentyFour = data.where(((YCcomplaints.fristtime - YCcomplaints.starttime) / 3600 > 10) & (
                (YCcomplaints.fristtime - YCcomplaints.starttime) / 3600 <= 24)).count()
            twentfour = data.where((YCcomplaints.fristtime - YCcomplaints.starttime) / 3600 > 24).count()
            try:
                oneToTwo_1 =oneToTwo / acceptance
            except:
                oneToTwo_1 = 0.00
            try:
                twoToTen_1 = str('%.2f' % ((twoToTen / acceptance) * 100)) + '%'
            except:
                twoToTen_1 = '0.00%'
            try:
                tenToTwentyFour_1 = str('%.2f' % ((tenToTwentyFour / acceptance) * 100)) + '%'
            except:
                tenToTwentyFour_1 = '0.00%'
            try:
                twentfour_1 = str('%.2f' % ((twentfour / acceptance) * 100)) + '%'
            except:
                twentfour_1 = '0.00%'

            for item in data:
                try:
                    firsttime = (int(item.fristtime) - int(item.starttime)) / 3600
                except:
                    firsttime = 0
            avtime = avetime + firsttime
            try:
                av_time = avtime / acceptance
            except:
                av_time = 0
            msg_list = {"area": area,
                        "inside": '%.2f' % (oneToTwo_1*100),
                        'ultra': '%.2f' %((1 - oneToTwo_1)*100),
                        }
            result.append(msg_list)
        msg = {"code": 0, "msg": "success", "result": result}
    if type=='首次联系用户平均时长':
        area_list = ['秭归', '枝江', '长阳', '远安', '宜都', '夷陵', '兴山', '五峰', '开发区', '当阳', '城区']
        for area in area_list:
            avetime = 0
            like = '%' + area + '%'
            data = YCcomplaints.select().where((YCcomplaints.platform == 2) & (YCcomplaints.area % like) & (
                YCcomplaints.starttime >= utc_str_to_timestamp(starttime)) & (
                                                   YCcomplaints.starttime <= utc_str_to_timestamp(endtime)))
            acceptance = YCcomplaints.select().where((YCcomplaints.platform == 2) & (YCcomplaints.area % like) & (
                YCcomplaints.starttime >= utc_str_to_timestamp(starttime)) & (
                                                         YCcomplaints.starttime <= utc_str_to_timestamp(
                                                             endtime))).count()

            oneToTwo = data.where((YCcomplaints.fristtime - YCcomplaints.starttime) / 3600 <= 2).count()
            twoToTen = data.where(((YCcomplaints.fristtime - YCcomplaints.starttime) / 3600 > 2) & (
                (YCcomplaints.fristtime - YCcomplaints.starttime) / 3600 <= 10)).count()
            tenToTwentyFour = data.where(((YCcomplaints.fristtime - YCcomplaints.starttime) / 3600 > 10) & (
                (YCcomplaints.fristtime - YCcomplaints.starttime) / 3600 <= 24)).count()
            twentfour = data.where((YCcomplaints.fristtime - YCcomplaints.starttime) / 3600 > 24).count()
            try:
                oneToTwo_1 = '%.2f' % ((oneToTwo / acceptance) * 100)
            except:
                oneToTwo_1 = 0.00
            try:
                twoToTen_1 = str('%.2f' % ((twoToTen / acceptance) * 100)) + '%'
            except:
                twoToTen_1 = '0.00%'
            try:
                tenToTwentyFour_1 = str('%.2f' % ((tenToTwentyFour / acceptance) * 100)) + '%'
            except:
                tenToTwentyFour_1 = '0.00%'
            try:
                twentfour_1 = str('%.2f' % ((twentfour / acceptance) * 100)) + '%'
            except:
                twentfour_1 = '0.00%'

            for item in data:
                try:
                    firsttime = (int(item.fristtime) - int(item.starttime)) / 3600
                except:
                    firsttime = 0
            avtime = avetime + firsttime
            try:
                av_time = avtime / acceptance
            except:
                av_time = 0
            msg_list = {"area": area,
                        "inside":'%.2f' % (av_time),
                        'ultra': 'none'
                        }
            result.append(msg_list)
        msg = {"code": 0, "msg": "success", "result": result}
    return msg
def complain_emos_first_info_export_get(type):  # noqa: E501
    """eight hour complaint daily list export

    eight hour complaint daily list export # noqa: E501

    :param type: the type for user choose
    :type type: str

    :rtype: DownUrl
    """
    url=first_export(type.split('_')[0],type.split('_')[1],type.split('_')[2],type.split('_')[3])
    msg={"code":0,"msg":"successs","url":url}
    return msg
def complain_emos_first_list_export_get(starttime=None, endtime=None):  # noqa: E501
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
        starttime = '2018-02-14 00:00:00'
    if endtime == '':
        endtime = '2018-02-15 00:00:00'
    workbook_m = xlwt.Workbook(encoding='utf-8')
    xlsheet = workbook_m.add_sheet('首次联系用户及时率', cell_overwrite_ok=True)
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
    xlsheet.write(0, 7, 'EMOS', style3)
    xlsheet.write(1, 0, '区县', style1)
    xlsheet.write(1, 1, '总单数', style1)
    xlsheet.write(1, 2, '2小时以内', style1)
    xlsheet.write(1, 3, '2-10小时', style1)
    xlsheet.write(1, 4, '10-24小时', style1)
    xlsheet.write(1, 5, '超过24小时', style1)
    xlsheet.write(1, 6, '2小时以内及时率', style1)
    xlsheet.write(1, 7, '2-10小时及时率', style1)
    xlsheet.write(1, 8, '10-24小时及时率', style1)
    xlsheet.write(1, 9, '超过24小时及时率', style1)
    xlsheet.write(1, 10, '平均联系时长', style1)
    xlsheet.write(1, 11, '2小时联系及时率', style1)


    area_list = ['秭归', '枝江', '长阳', '远安', '宜都', '夷陵', '兴山', '五峰', '开发区', '当阳', '城区']
    i=1
    for area in area_list:
        avetime=0
        like='%' + area + '%'
        data = YCcomplaints.select().where((YCcomplaints.platform == 2) & (YCcomplaints.area % like) & (
            YCcomplaints.starttime >= utc_str_to_timestamp(starttime)) & (
                                                     YCcomplaints.starttime <= utc_str_to_timestamp(endtime)))
        acceptance = YCcomplaints.select().where((YCcomplaints.platform == 2) & (YCcomplaints.area % like) & (
            YCcomplaints.starttime >= utc_str_to_timestamp(starttime)) & (
                                                     YCcomplaints.starttime <= utc_str_to_timestamp(endtime))).count()




        oneToTwo = data.where((YCcomplaints.fristtime-YCcomplaints.starttime)/3600 <= 2).count()
        twoToTen = data.where(((YCcomplaints.fristtime-YCcomplaints.starttime)/3600 > 2) & ((YCcomplaints.fristtime-YCcomplaints.starttime)/3600 <= 10)).count()
        tenToTwentyFour = data.where(((YCcomplaints.fristtime-YCcomplaints.starttime)/3600 > 10) & ((YCcomplaints.fristtime-YCcomplaints.starttime)/3600 <= 24)).count()
        twentfour = data.where((YCcomplaints.fristtime-YCcomplaints.starttime)/3600 > 24).count()
        try:
            oneToTwo_1=str('%.2f' % ((oneToTwo/acceptance)*100))+'%'
        except:
            oneToTwo_1='0.00%'
        try:
            twoToTen_1=str('%.2f' % ((twoToTen/acceptance)*100))+'%'
        except:
            twoToTen_1='0.00%'
        try:
            tenToTwentyFour_1=str('%.2f' % ((tenToTwentyFour/acceptance)*100))+'%'
        except:
            tenToTwentyFour_1='0.00%'
        try:
            twentfour_1=str('%.2f' % ((twentfour/acceptance)*100))+'%'
        except:
            twentfour_1='0.00%'

        for item in data:
            try:
                firsttime=(int(item.fristtime)-int(item.starttime))/3600
            except:
                firsttime=0
        avtime = avetime + firsttime
        try:
            av_time=avtime/acceptance
        except:
            av_time=0
        xlsheet.write(i + 1, 0, area, style1)
        xlsheet.write(i + 1, 1, acceptance, style1)
        xlsheet.write(i + 1, 2, oneToTwo, style1)
        xlsheet.write(i + 1, 3, twoToTen, style1)
        xlsheet.write(i + 1, 4, tenToTwentyFour,
                      style1)
        xlsheet.write(i + 1, 5, twentfour,
                      style1)
        xlsheet.write(i + 1, 6, str(oneToTwo_1) ,
                      style1)
        xlsheet.write(i + 1, 7, str(twoToTen_1) , style1)
        xlsheet.write(i + 1, 8, str(tenToTwentyFour_1) , style1)
        xlsheet.write(i + 1, 9, str(twentfour_1) , style1)
        xlsheet.write(i + 1, 10, '%.2f' % av_time, style1)
        xlsheet.write(i + 1, 11, str(oneToTwo_1) ,style1)
        i = i + 1
    xlsname = '首次联系用户及时率' + str(int(time.time()))
    workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
    url = 'down.caicool.cc:89/{}.xls'.format(xlsname)

    msg = {"code": 0, "msg": "success", "url": url}
    return msg
def complain_emos_first_list_get(starttime=None, endtime=None):  # noqa: E501
    """eight hour complaint daily list

    eight hour complaint daily list # noqa: E501

    :param starttime: the starttime for user choose
    :type starttime: str
    :param endtime: the endtime for user choose
    :type endtime: str
    :param type: the type for user choose
    :type type: str

    :rtype: EmosList
    """
    if starttime=='':
        starttime='2018-02-14 00:00:00'
    if endtime=='':
        endtime='2018-02-15 00:00:00'
    result=[]
    print(utc_str_to_timestamp(starttime),utc_str_to_timestamp(endtime))
    area_list = ['秭归', '枝江', '长阳', '远安', '宜都', '夷陵', '兴山', '五峰', '开发区', '当阳', '城区']
    for area in area_list:
        avetime=0
        like='%' + area + '%'
        data = YCcomplaints.select().where((YCcomplaints.platform == 2) & (YCcomplaints.area % like) & (
            YCcomplaints.starttime >= utc_str_to_timestamp(starttime)) & (
                                                     YCcomplaints.starttime <= utc_str_to_timestamp(endtime)))
        acceptance = YCcomplaints.select().where((YCcomplaints.platform == 2) & (YCcomplaints.area % like) & (
            YCcomplaints.starttime >= utc_str_to_timestamp(starttime)) & (
                                                     YCcomplaints.starttime <= utc_str_to_timestamp(endtime))).count()




        oneToTwo = data.where((YCcomplaints.fristtime-YCcomplaints.starttime)/3600 <= 2).count()
        twoToTen = data.where(((YCcomplaints.fristtime-YCcomplaints.starttime)/3600 > 2) & ((YCcomplaints.fristtime-YCcomplaints.starttime)/3600 <= 10)).count()
        tenToTwentyFour = data.where(((YCcomplaints.fristtime-YCcomplaints.starttime)/3600 > 10) & ((YCcomplaints.fristtime-YCcomplaints.starttime)/3600 <= 24)).count()
        twentfour = data.where((YCcomplaints.fristtime-YCcomplaints.starttime)/3600 > 24).count()
        try:
            oneToTwo_1=str('%.2f' % ((oneToTwo/acceptance)*100))+'%'
        except:
            oneToTwo_1='0.00%'
        try:
            twoToTen_1=str('%.2f' % ((twoToTen/acceptance)*100))+'%'
        except:
            twoToTen_1='0.00%'
        try:
            tenToTwentyFour_1=str('%.2f' % ((tenToTwentyFour/acceptance)*100))+'%'
        except:
            tenToTwentyFour_1='0.00%'
        try:
            twentfour_1=str('%.2f' % ((twentfour/acceptance)*100))+'%'
        except:
            twentfour_1='0.00%'

        for item in data:
            try:
                firsttime=(int(item.fristtime)-int(item.starttime))/3600
            except:
                firsttime=0
        avtime = avetime + firsttime
        try:
            av_time=avtime/acceptance
        except:
            av_time=0
        msg_list={"area": area,
         "total": acceptance,
         "oneToTwo": oneToTwo,
         'twoToTen': twoToTen,
         'tenToTwentyFour': tenToTwentyFour,
         'twentyFour': twentfour,
         "oneToTwo_1": oneToTwo_1,
         'twoToTen_1': twoToTen_1,
         'tenToTwentyFour_1': tenToTwentyFour_1,
         'twentyFour_1': twentfour_1,
         'ave': '%.2f' % (av_time),
         'rate': oneToTwo_1
         }
        result.append(msg_list)
    msg = {"code": 0,"msg":"success","result":result}
    return msg


##高频小区统计接口方法
##高频小区统计接口方法
def complain_high_chart_get(type,starttime=None, endtime=None):  # noqa: E501
    """High-frequency cell

    High-frequency cell # noqa: E501

    :param starttime: the starttime for user choose
    :type starttime: str
    :param endtime: the endtime for user choose
    :type endtime: str
    :param type: the user choose type
    :type type: str

    :rtype: HighChart
    """
    result_list=[]
    area_list = ['秭归', '枝江', '长阳', '远安', '宜都', '夷陵', '兴山', '五峰', '开发区', '当阳', '城区']
    for area in area_list:
        result_list.append({"area":area,"geo":getxy('宜昌'+area,area)})
    msg={"code":0,"msg":"success","result":result_list}
    return msg
def complain_high_column_get(lat, lon):  # noqa: E501
    """eight hour complaint daily list export

    eight hour complaint daily list export # noqa: E501

    :param lat: lat
    :type lat: str
    :param lon: lon
    :type lon: str

    :rtype: HighListCommunityColumn
    """
    x = str(lat).split('_')[0]
    starttime = str(lat).split('_')[1]
    endtime = str(lat).split('_')[2]
    choosetype = str(lat).split('_')[3]
    if x == '':
        lon = '30.294919731409415'
        x = '111.37553355504939'
    
    if starttime == '':
        starttime = '2018-02-01 00:00:00'
    if endtime == '':
        endtime = '2018-03-01 00:00:00'
    url2 = 'http://api.map.baidu.com/geocoder/v2/?location=' + str(lon) + ',' + str(
        x) + '&output=json&pois=0&ak=gRManfxm4xGfswhaIT4xGh78UpHV8kCV'
    print(url2)
    r1 = requests.get(url2)
    result1 = json.loads(r1.text)
    result = []
    area = result1['result']['addressComponent']['district'][0:-1]
    print(area)
    for item in gethigh1(area, starttime, endtime, choosetype)[0]:
        result_msg = {"name": item[0], "value": item[1]}
        result.append(result_msg)
    msg = {"code": 0, "msg": "success", "result": result}
    return msg

def complain_high_community_id_get(id):  # noqa: E501
    """eight hour complaint daily list export

    eight hour complaint daily list export # noqa: E501

    :param id: community id
    :type id: str

    :rtype: HighListCommunityTotal
    """
    msg = msg_high_commuity
    return msg
def complain_high_info_export_get(type):  # noqa: E501
    """eight hour complaint daily list export

    eight hour complaint daily list export # noqa: E501

    :param type: the type for user choose
    :type type: str

    :rtype: DownUrl
    """
    choosetype = type.split('_')[3]
    starttime = type.split('_')[0]
    endtime = type.split('_')[1]
    address = type.split('_')[2]
    if starttime == '':
        starttime = '2018-02-01 00:00:00'
    if endtime == '':
        endtime = '2018-03-01 00:00:00'
    if choosetype == 'EMOS':
        like = '%' + address + '%'
        data = YCcomplaints.select().where(
            (YCcomplaints.platform == 2) & (YCcomplaints.starttime >= utc_str_to_timestamp(starttime)) & (
                YCcomplaints.endtime < utc_str_to_timestamp(endtime)) & (YCcomplaints.type == '服务质量') & (
                YCcomplaints.tsaddress % like))
    if choosetype == '微信一键报障':
        like = '%' + address + '%'
        data = YCcomplaints.select().where(
            (YCcomplaints.platform == 1) & (YCcomplaints.starttime >= utc_str_to_timestamp(starttime)) & (
                YCcomplaints.endtime < utc_str_to_timestamp(endtime)) & (YCcomplaints.type == '服务质量') & (
                YCcomplaints.tsaddress % like))

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
    workbook_m = xlwt.Workbook(encoding='utf-8')
    xlsheet = workbook_m.add_sheet('高频小区', cell_overwrite_ok=True)
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
        xlsheet.write(i, 1, choosetype)
        xlsheet.write(i, 2, item.serial)
        xlsheet.write(i, 3, utc_timestamp_to_str(item.fristtime))
        xlsheet.write(i, 4, item.phone)
        xlsheet.write(i, 5, item.contacts)
        xlsheet.write(i, 6, item.tsaddress)
        xlsheet.write(i, 7, utc_timestamp_to_str(item.starttime))
        i = i + 1
    xlsname = '高频小区' + str(int(time.time()))
    workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
    url = 'down.caicool.cc:89/{}.xls'.format(xlsname)

    msg = {"code": 0, "msg": "success", "url": url}
    return msg
def complain_high_list_export_get(type,starttime=None, endtime=None):  # noqa: E501
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
    if starttime=='':
        starttime='2018-02-01 00:00:00'
    if endtime=='':
        endtime='2018-03-01 00:00:00'
    area_list = ['秭归', '枝江', '长阳', '远安', '宜都', '夷陵', '兴山', '五峰', '开发区', '当阳', '城区']
    workbook_m = xlwt.Workbook(encoding='utf-8')
    xlsheet = workbook_m.add_sheet('高频小区', cell_overwrite_ok=True)
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
    xlsheet.write(0, 7, 'EMOS', style3)
    xlsheet.write(1, 0, '区县', style1)
    xlsheet.write(1, 1, '小区名', style1)
    xlsheet.write(1, 2, '投诉工单量', style1)
    result=[]
    i=1
    for area in area_list:
        result_msg={"id":i,"area":area,"total":gethigh(area,starttime,endtime,type)[0][0][1],"community":gethigh(area,starttime,endtime,type)[0][0][0]}
        xlsheet.write(i+1, 0, area, style1)
        xlsheet.write(i+1, 1, gethigh(area,starttime,endtime,type)[0][0][0], style1)
        xlsheet.write(i+1, 2, gethigh(area,starttime,endtime,type)[0][0][1], style1)
        result.append(result_msg)
        i=i+1
    xlsname ='高频小区' + str(int(time.time()))
    workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
    url = 'down.caicool.cc:89/{}.xls'.format(xlsname)

    msg = {"code": 0, "msg": "success", "url": url}
    return msg
def complain_high_list_get(type,starttime=None, endtime=None):  # noqa: E501
    """eight hour complaint daily list

    eight hour complaint daily list # noqa: E501

    :param starttime: the starttime for user choose
    :type starttime: str
    :param endtime: the endtime for user choose
    :type endtime: str
    :param type: the type for user choose
    :type type: str

    :rtype: HighList
    """
    if starttime=='':
        starttime='2018-02-01 00:00:00'
    if endtime=='':
        endtime='2018-04-01 00:00:00'
    area_list = ['秭归', '枝江', '长阳', '远安', '宜都', '夷陵', '兴山', '五峰', '开发区', '当阳', '城区']
    i=1
    print(type)
    result=[]
    if type.split('_')[0]=='':
        for area in area_list:
            for msg_list in gethigh(area, starttime, endtime, type.split('_')[1]):
                result_msg = {"area": area, "total": msg_list[1], "community": msg_list[0]}
                result.append(result_msg)
    if type.split('_')[0]!='':
        for msg_list in gethigh(type.split('_')[0], starttime, endtime, type.split('_')[1]):

            result_msg = {"area": type.split('_')[0], "total": msg_list[1], "community": msg_list[0]}
            result.append(result_msg)
    #result=[{"area":"秭归","total":"3","community":'1'},{"area":"秭归","total":"3","community":'2'},{"area":"秭归","total":"3","community":'3'},{"area":"枝江","total":"3","community":'11'},{"area":"枝江","total":"3","community":'12'},{"area":"枝江","total":"3","community":'13'},{"area":"长阳","total":"3","community":'21'},{"area":"长阳","total":"3","community":'22'},{"area":"长阳","total":"3","community":'23'}]
    msg={"code":0,"msg":"success","result":result}
    return msg

##投诉回访满意度接口方法
def complain_visit_chart_get(type,starttime=None, endtime=None):  # noqa: E501
    """Return visit satisfaction

    Return visit satisfaction # noqa: E501

    :param starttime: the starttime for user choose
    :type starttime: str
    :param endtime: the endtime for user choose
    :type endtime: str
    :param type: the user choose type
    :type type: str

    :rtype: HomeChart
    """
    if starttime == '':
        starttime = '2018-02-14 00:00:00'
    if endtime == '':
        endtime = '2018-02-15 00:00:00'
    result = []
    area_list = ['秭归', '枝江', '长阳', '远安', '宜都', '夷陵', '兴山', '五峰', '开发区', '当阳', '城区']
    data = YCcomplaints.select().where(
        (YCcomplaints.platform == 2) & (YCcomplaints.starttime >= utc_str_to_timestamp(starttime)) & (
            YCcomplaints.starttime <= utc_str_to_timestamp(endtime)))
    if type == '投诉回访满意度':
        print(data.count())
        for area in area_list:
            like = '%' + area + '%'
            satisfaction = data.where((YCcomplaints.manyi == 11) & (YCcomplaints.area % like)).count()
            displeasure = data.where((YCcomplaints.manyi == 10) & (YCcomplaints.area % like)).count()
            satisfaction_ = data.where((YCcomplaints.manyi == 21) & (YCcomplaints.area % like)).count()
            displeasure_ = data.where((YCcomplaints.manyi == 20) & (YCcomplaints.area % like)).count()
            try:
                rate = (satisfaction + satisfaction_) * 100 / (
                    satisfaction + displeasure + satisfaction_ + displeasure_)
            except:
                rate = 0.00
            result.append({"name": area, "value": '%.2f' % rate})
        result = sorted(result, key=lambda result: result['value'], reverse=True)

        msg = {"code": 0,
               "msg": "success",
               'result': result,
               }
        return msg
    if type == '投诉成功率':
        print(data.count())
        for area in area_list:
            like = '%' + area + '%'
            satisfaction = data.where((YCcomplaints.manyi == 11) & (YCcomplaints.area % like)).count()
            displeasure = data.where((YCcomplaints.manyi == 10) & (YCcomplaints.area % like)).count()
            satisfaction_ = data.where((YCcomplaints.manyi == 21) & (YCcomplaints.area % like)).count()
            displeasure_ = data.where((YCcomplaints.manyi == 20) & (YCcomplaints.area % like)).count()
            try:
                rate = (satisfaction + satisfaction_) * 100 / (
                    satisfaction + displeasure + satisfaction_ + displeasure_)
            except:
                rate = 0.00
            result.append({"name": area, "value": '%.2f' % rate})
        result = sorted(result, key=lambda result: result['value'], reverse=True)

        msg = {"code": 0,
               "msg": "success",
               'result': result,
               }
        return msg
    if type == '总单量':
        print(data.count())
        for area in area_list:
            like = '%' + area + '%'
            satisfaction = data.where((YCcomplaints.manyi == 11) & (YCcomplaints.area % like)).count()
            displeasure = data.where((YCcomplaints.manyi == 10) & (YCcomplaints.area % like)).count()
            satisfaction_ = data.where((YCcomplaints.manyi == 21) & (YCcomplaints.area % like)).count()
            displeasure_ = data.where((YCcomplaints.manyi == 20) & (YCcomplaints.area % like)).count()

            result.append({"name": area, "value": satisfaction + displeasure + satisfaction_ + displeasure_})
        result = sorted(result, key=lambda result: result['value'], reverse=True)

        msg = {"code": 0,
               "msg": "success",
               'result': result,
               }
        return msg
    if type == '投诉不满意度':
        print(data.count())
        for area in area_list:
            like = '%' + area + '%'
            satisfaction = data.where((YCcomplaints.manyi == 11) & (YCcomplaints.area % like)).count()
            displeasure = data.where((YCcomplaints.manyi == 10) & (YCcomplaints.area % like)).count()
            satisfaction_ = data.where((YCcomplaints.manyi == 21) & (YCcomplaints.area % like)).count()
            displeasure_ = data.where((YCcomplaints.manyi == 20) & (YCcomplaints.area % like)).count()
            try:
                rate = (displeasure + displeasure_) * 100 / (
                    satisfaction + displeasure + satisfaction_ + displeasure_)
            except:
                rate = 0.00
            result.append({"name": area, "value": '%.2f' % rate})
        result = sorted(result, key=lambda result: result['value'], reverse=True)

        msg = {"code": 0,
               "msg": "success",
               'result': result,
               }
        return msg
def complain_visit_info_export_get(type):  # noqa: E501
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
        starttime = '2018-02-14 00:00:00'
    if endtime == '':
        endtime = '2018-02-15 00:00:00'
    data = YCcomplaints.select().where(
        (YCcomplaints.platform == 2) & (YCcomplaints.starttime >= utc_str_to_timestamp(starttime)) & (
            YCcomplaints.starttime <= utc_str_to_timestamp(endtime)))
    like = '%' + area + '%'
    satisfaction = data.where((YCcomplaints.manyi == 11) & (YCcomplaints.area % like))
    displeasure = data.where((YCcomplaints.manyi == 10) & (YCcomplaints.area % like))
    satisfaction_ = data.where((YCcomplaints.manyi == 21) & (YCcomplaints.area % like))
    displeasure_ = data.where((YCcomplaints.manyi == 20) & (YCcomplaints.area % like))
    if datatype == '满意(IVR)':
        workbook_m = xlwt.Workbook(encoding='utf-8')
        xlsheet = workbook_m.add_sheet('投诉回访满意度', cell_overwrite_ok=True)
        xlsheet.write(0, 0, '工单平台')
        xlsheet.write(0, 1, '所属区')
        xlsheet.write(0, 2, '新增工单操作时间')
        xlsheet.write(0, 3, 'T2操作时间')
        xlsheet.write(0, 4, '处理时长')
        i = 1

        for item in satisfaction:
            xlsheet.write(i, 0, 'EMOS')
            xlsheet.write(i, 1, area)
            xlsheet.write(i, 2, utc_timestamp_to_str(item.starttime))
            xlsheet.write(i, 3, utc_timestamp_to_str(item.endtime))
            xlsheet.write(i, 4, item.usetime)
            i = i + 1
        xlsname = '投诉回访满意度' + area + datatype + xlstime
        workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
        url = 'down.caicool.cc:89/{}.xls'.format(xlsname)
        msg = {"code": 0, "msg": "success", "url": url}
        return msg

    if datatype == '不满意(IVR)':
        workbook_m = xlwt.Workbook(encoding='utf-8')
        xlsheet = workbook_m.add_sheet('投诉回访满意度', cell_overwrite_ok=True)
        xlsheet.write(0, 0, '工单平台')
        xlsheet.write(0, 1, '所属区')
        xlsheet.write(0, 2, '新增工单操作时间')
        xlsheet.write(0, 3, 'T2操作时间')
        xlsheet.write(0, 4, '处理时长')
        i = 1

        for item in displeasure:
            xlsheet.write(i, 0, 'EMOS')
            xlsheet.write(i, 1, area)
            xlsheet.write(i, 2, utc_timestamp_to_str(item.starttime))
            xlsheet.write(i, 3, utc_timestamp_to_str(item.endtime))
            xlsheet.write(i, 4, item.usetime)
            i = i + 1
        xlsname = '投诉回访满意度' + area + datatype + xlstime
        workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
        url = 'down.caicool.cc:89/{}.xls'.format(xlsname)
        msg = {"code": 0, "msg": "success", "url": url}
        return msg
    if datatype == '满意(人工)':
        workbook_m = xlwt.Workbook(encoding='utf-8')
        xlsheet = workbook_m.add_sheet('投诉回访满意度', cell_overwrite_ok=True)
        xlsheet.write(0, 0, '工单平台')
        xlsheet.write(0, 1, '所属区')
        xlsheet.write(0, 2, '新增工单操作时间')
        xlsheet.write(0, 3, 'T2操作时间')
        xlsheet.write(0, 4, '处理时长')
        i = 1

        for item in satisfaction_:
            xlsheet.write(i, 0, 'EMOS')
            xlsheet.write(i, 1, area)
            xlsheet.write(i, 2, utc_timestamp_to_str(item.starttime))
            xlsheet.write(i, 3, utc_timestamp_to_str(item.endtime))
            xlsheet.write(i, 4, item.usetime)
            i = i + 1
        xlsname = '投诉回访满意度' + area + datatype + xlstime
        workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
        url = 'down.caicool.cc:89/{}.xls'.format(xlsname)
        msg = {"code": 0, "msg": "success", "url": url}
        return msg
    if datatype == '不满意(人工)':
        workbook_m = xlwt.Workbook(encoding='utf-8')
        xlsheet = workbook_m.add_sheet('投诉回访满意度', cell_overwrite_ok=True)
        xlsheet.write(0, 0, '工单平台')
        xlsheet.write(0, 1, '所属区')
        xlsheet.write(0, 2, '新增工单操作时间')
        xlsheet.write(0, 3, 'T2操作时间')
        xlsheet.write(0, 4, '处理时长')
        i = 1

        for item in displeasure_:
            xlsheet.write(i, 0, 'EMOS')
            xlsheet.write(i, 1, area)
            xlsheet.write(i, 2, utc_timestamp_to_str(item.starttime))
            xlsheet.write(i, 3, utc_timestamp_to_str(item.endtime))
            xlsheet.write(i, 4, item.usetime)
            i = i + 1
        xlsname = '投诉回访满意度' + area + datatype + xlstime
        workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
        url = 'down.caicool.cc:89/{}.xls'.format(xlsname)
        msg = {"code": 0, "msg": "success", "url": url}
        return msg
def complain_visit_list_export_get(starttime=None, endtime=None):  # noqa: E501
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
    result = []
    if starttime == '':
        starttime = '2018-02-14 00:00:00'
    if endtime == '':
        endtime = '2018-02-15 00:00:00'
    workbook_m = xlwt.Workbook(encoding='utf-8')
    xlsheet = workbook_m.add_sheet('投诉处理时长Top20', cell_overwrite_ok=True)
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
    xlsheet.write(0, 7, 'EMOS', style3)
    xlsheet.write_merge(1, 1, 0, 8, '家宽EMOS投诉回访满意度通报', style1)
    xlsheet.write_merge(2, 3, 0, 0, '县市', style1)
    xlsheet.write_merge(2, 2, 1, 3, 'IVR自动回访', style1)
    xlsheet.write_merge(2, 2, 4, 6, '人工回访', style1)
    xlsheet.write_merge(3, 3, 1, 1, '投诉回访成功量', style1)
    xlsheet.write_merge(3, 3, 2, 2, '满意', style1)
    xlsheet.write_merge(3, 3, 3, 3, '不满意', style1)
    xlsheet.write_merge(3, 3, 4, 4, '投诉回访成功量', style1)
    xlsheet.write_merge(3, 3, 5, 5, '满意', style1)
    xlsheet.write_merge(3, 3, 6, 6, '不满意', style1)
    xlsheet.write_merge(2, 3, 7, 7, '投诉回访满意度', style1)
    xlsheet.write_merge(2, 3, 8, 8, '排名', style1)
    area_list = ['秭归', '枝江', '长阳', '远安', '宜都', '夷陵', '兴山', '五峰', '开发区', '当阳', '城区']
    data = YCcomplaints.select().where(
        (YCcomplaints.platform == 2) & (YCcomplaints.starttime >= utc_str_to_timestamp(starttime)) & (
            YCcomplaints.starttime <= utc_str_to_timestamp(endtime)))
    for area in area_list:
        like = '%' + area + '%'
        satisfaction = data.where((YCcomplaints.manyi == 11) & (YCcomplaints.area % like)).count()
        displeasure = data.where((YCcomplaints.manyi == 10) & (YCcomplaints.area % like)).count()
        satisfaction_ = data.where((YCcomplaints.manyi == 21) & (YCcomplaints.area % like)).count()
        displeasure_ = data.where((YCcomplaints.manyi == 20) & (YCcomplaints.area % like)).count()
        try:
            rate = (satisfaction + satisfaction_) * 100 / (satisfaction + displeasure + satisfaction_ + displeasure_)
        except:
            rate = 0.00
        result.append(
            {"area": area, "satisfaction": satisfaction, "displeasure": displeasure, "rate": str('%.2f' % rate) + '%',
             'succ': satisfaction, 'succ_': satisfaction_, "satisfaction_": satisfaction_,
             "displeasure_": displeasure_})
    result = sorted(result, key=lambda result: result['rate'], reverse=True)
    for i in range(len(result)):
        result[i]['rank'] = i + 1
    log = 3
    for item in result:
        xlsheet.write(log + 1, 0, item['area'], style1)
        xlsheet.write(log + 1, 1, item['satisfaction'], style1)
        xlsheet.write(log + 1, 2, item['satisfaction'] + item['displeasure'], style1)
        xlsheet.write(log + 1, 3, item['displeasure'], style1)
        xlsheet.write(log + 1, 4, item['satisfaction_'] + item['displeasure_'], style1)
        xlsheet.write(log + 1, 5, item['satisfaction_'], style1)
        xlsheet.write(log + 1, 6, item['displeasure_'], style1)
        xlsheet.write(log + 1, 7, item['rate'], style1)
        xlsheet.write(log + 1, 8, item['rank'], style1)
        log = log + 1
    xlsname = '投诉回访满意度' + str(int(time.time()))
    workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
    url = 'down.caicool.cc:89/{}.xls'.format(xlsname)

    msg = {"code": 0, "msg": "success", "url": url}
    return msg
def complain_visit_list_get(starttime=None, endtime=None):  # noqa: E501
    """eight hour complaint daily list

    eight hour complaint daily list # noqa: E501

    :param starttime: the starttime for user choose
    :type starttime: str
    :param endtime: the endtime for user choose
    :type endtime: str
    :param type: the type for user choose
    :type type: str

    :rtype: VisitList
    """
    if starttime=='':
        starttime='2018-02-14 00:00:00'
    if endtime=='':
        endtime='2018-02-15 00:00:00'
    result=[]
    area_list = ['秭归', '枝江', '长阳', '远安', '宜都', '夷陵', '兴山', '五峰', '开发区', '当阳', '城区']
    data = YCcomplaints.select().where((YCcomplaints.platform==2) & (YCcomplaints.starttime >= utc_str_to_timestamp(starttime))& (
    YCcomplaints.starttime <= utc_str_to_timestamp(endtime)))
    print (data.count())
    for area in  area_list:
        like='%'+area+'%'
        satisfaction=data.where((YCcomplaints.manyi==11) & (YCcomplaints.area  % like)).count()
        displeasure=data.where((YCcomplaints.manyi==10) & (YCcomplaints.area  % like)).count()
        satisfaction_ = data.where((YCcomplaints.manyi == 21) & (YCcomplaints.area % like)).count()
        displeasure_ = data.where((YCcomplaints.manyi == 20) & (YCcomplaints.area % like)).count()
        try:
            rate = (satisfaction+satisfaction_) * 100 / (satisfaction + displeasure+satisfaction_ + displeasure_)
        except:
            rate = 0.00
        result.append({"area":area,"satisfaction":satisfaction,"displeasure":displeasure,"rate":str('%.2f' % rate)+'%','succ':satisfaction+displeasure,'succ_':satisfaction_+displeasure_,"satisfaction_":satisfaction_,"displeasure_":displeasure_})
    result=sorted(result,key=lambda result:result['rate'],reverse = True)
    for i in range(len(result)):
        result[i]['rank']=i+1
    msg={"code":0,
            "msg":"success",
            'result':result,
            }
    return msg





##故障处理页面接口方法
def complain_malfunction_chart_get(type,starttime=None, endtime=None):  # noqa: E501
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
def complain_malfunction_info_export_get(type):  # noqa: E501
    """eight hour complaint daily list export

    eight hour complaint daily list export # noqa: E501

    :param type: the type for user choose
    :type type: str

    :rtype: DownUrl
    """
    if (type == "完成量"):
        msg = msg_list_export
    else:
        msg = msg_list_export
    return msg
def complain_malfunction_list_export_get(type,starttime=None, endtime=None):  # noqa: E501
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
def complain_malfunction_list_get(type,starttime=None, endtime=None):  # noqa: E501
    """Yichang Branch Broadens Fault Daily

    Yichang Branch Broadens Fault Daily # noqa: E501

    :param starttime: the starttime for user choose
    :type starttime: str
    :param endtime: the endtime for user choose
    :type endtime: str
    :param type: the type for user choose
    :type type: str

    :rtype: MalfunctionList
    """
    if (starttime == "2018/3/29 00：00") & (endtime == "2018/3/29 24：00") & (type == "CRM"):
        msg = msg_malfunction_list_right
    else:
        msg = msg_malfunction_list_right
    return msg


##高频故障网元界面接口方法
def complain_network_info_export_get(type):  # noqa: E501
    """eight hour complaint daily list export

    eight hour complaint daily list export # noqa: E501

    :param type: the type for user choose
    :type type: str

    :rtype: DownUrl
    """
    starttime = type.split('_')[0]
    endtime = type.split('_')[1]
    network = type.split('_')[2]
    if starttime == '':
        starttime = '2018-02-01 00:00:00'
    if endtime == '':
        endtime = '2018-04-01 00:00:00'
    data = YCcomplaints.select().where(
        (YCcomplaints.platform != 3) & (YCcomplaints.starttime >= utc_str_to_timestamp(starttime)) & (
            YCcomplaints.endtime < utc_str_to_timestamp(endtime)) & (YCcomplaints.type == '服务质量') & (
        YCcomplaints.network == network))

    workbook_m = xlwt.Workbook(encoding='utf-8')
    xlsheet = workbook_m.add_sheet('高频故障网元', cell_overwrite_ok=True)
    xlsheet.write(0, 0, '工单平台')
    xlsheet.write(0, 1, '所属区')
    xlsheet.write(0, 2, '新增工单操作时间')
    xlsheet.write(0, 3, 'T2操作时间')
    xlsheet.write(0, 4, '处理时长')
    xlsheet.write(0, 5, '网元')
    i = 1

    for item in data:
        xlsheet.write(i, 0, item.platform)
        xlsheet.write(i, 1, item.area)
        xlsheet.write(i, 2, utc_timestamp_to_str(item.starttime))
        xlsheet.write(i, 3, utc_timestamp_to_str(item.endtime))
        xlsheet.write(i, 4, item.usetime)
        xlsheet.write(i, 5, item.network)
        i = i + 1
        xlsname = '高频故障网元' + network + xlstime
    workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
    url = 'down.caicool.cc:89/{}.xls'.format(xlsname)
    msg = {"code": 0, "msg": "success", "url": url}
    return msg
def complain_network_list_export_get(starttime=None, endtime=None):  # noqa: E501
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
    if starttime=='':
        starttime='2018-02-01 00:00:00'
    if endtime=='':
        endtime='2018-04-01 00:00:00'
    data = YCcomplaints.select().where( (YCcomplaints.platform!=3) &(YCcomplaints.starttime >= utc_str_to_timestamp(starttime)) & (
    YCcomplaints.endtime < utc_str_to_timestamp(endtime)) & (YCcomplaints.type=='服务质量'))
    result_list=[]
    for item in data:
        result_list.append(item.network)
    # 前top20
    msg_list=Counter(result_list).most_common(20)
    workbook_m = xlwt.Workbook(encoding='utf-8')
    xlsheet = workbook_m.add_sheet('高频故障网元', cell_overwrite_ok=True)
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
    xlsheet.write(0, 7, 'EMOS+一键报障', style3)
    xlsheet.write(1, 0, '区县', style1)
    xlsheet.write(1, 1, '高频网元', style1)
    xlsheet.write(1, 2, '总量', style1)
    xlsheet.write(1, 3, 'top', style1)

    i = 1
    for item in msg_list:
        xlsheet.write(i + 1, 0,YCcomplaints.get(YCcomplaints.network==item[0]).area, style1)
        xlsheet.write(i + 1, 1, item[0], style1)
        xlsheet.write(i + 1, 2, item[1], style1)
        xlsheet.write(i + 1, 3, i, style1)

        i = i + 1
    xlsname = '高频故障网元' + str(int(time.time()))
    workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
    url = 'down.caicool.cc:89/{}.xls'.format(xlsname)

    msg = {"code": 0, "msg": "success", "url": url}
    return msg
def complain_network_list_get(starttime=None, endtime=None):  # noqa: E501
    """Yichang Branch Broadens Fault Daily

    Yichang Branch Broadens Fault Daily # noqa: E501

    :param starttime: the starttime for user choose
    :type starttime: str
    :param endtime: the endtime for user choose
    :type endtime: str
    :param type: the type for user choose
    :type type: str

    :rtype: NetworkList
    """
    if starttime=='':
        starttime='2018-02-01 00:00:00'
    if endtime=='':
        endtime='2018-04-01 00:00:00'
    data = YCcomplaints.select().where((YCcomplaints.platform!=3) & (YCcomplaints.starttime >= utc_str_to_timestamp(starttime)) & (
    YCcomplaints.endtime < utc_str_to_timestamp(endtime)) & (YCcomplaints.type=='服务质量'))
    result_list=[]
    for item in data:
        result_list.append(item.network)
    # 前top20
    msg_list=Counter(result_list).most_common(20)
    msg={"code":0,"msg":"success","result":[{"id":i+1,"area":YCcomplaints.get(YCcomplaints.network==msg_list[i][0]).area,"name":msg_list[i][0],"total":msg_list[i][1]} for i in range(len(msg_list))]}
    return msg


##超时未回复界面接口方法
def complain_out_chart_get(type,starttime=None, endtime=None):  # noqa: E501
    """Overtime did not reply

    Overtime did not reply # noqa: E501

    :param starttime: the starttime for user choose
    :type starttime: str
    :param endtime: the endtime for user choose
    :type endtime: str
    :param type: the user choose type
    :type type: str

    :rtype: HomeChart
    """
    if starttime=='':
        starttime='2018-02-01 00:00:00'
    if endtime=='':
        endtime='2018-04-01 00:00:00'
    data = YCcomplaints.select().where(
        (YCcomplaints.starttime >= utc_str_to_timestamp(starttime)) & (YCcomplaints.status == '运行中') & (
        (YCcomplaints.endtime - YCcomplaints.starttime) >= 24 * 3600) & (
            YCcomplaints.endtime < utc_str_to_timestamp(endtime))).order_by(YCcomplaints.usetime.desc()).paginate(1, 20)
    result=[{"rank":"top"+str(i+1),'geo':getxy(data[i].tsaddress,data[i].area)} for i in range(len(data))]
    msg={"code":0,
            "msg":"success",
            'result':result,
            }
    return msg
def complain_out_info_export_get(type):  # noqa: E501
    """eight hour complaint daily list export

    eight hour complaint daily list export # noqa: E501

    :param type: the type for user choose
    :type type: str

    :rtype: DownUrl
    """
    starttime=type.split('_')[0]
    endtime=type.split('_')[1]
    if starttime=='':
        starttime='2018-02-01 00:00:00'
    if endtime=='':
        endtime='2018-04-01 00:00:00'
    url=outexport(starttime,endtime)
    msg={"code":0,"msg":'success',"url":url}
    return msg
def complain_out_list_export_get(starttime=None, endtime=None):  # noqa: E501
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
    if (starttime == "2018/3/29 00：00") & (endtime == "2018/3/29 24：00"):
        msg = msg_list_export
    else:
        msg = msg_list_export
    return msg
def complain_out_list_get(starttime=None, endtime=None):  # noqa: E501
    """Yichang Branch Broadens Fault Daily

    Yichang Branch Broadens Fault Daily # noqa: E501

    :param starttime: the starttime for user choose
    :type starttime: str
    :param endtime: the endtime for user choose
    :type endtime: str

    :rtype: TopList
    """
    if starttime=='':
        starttime='2018-02-01 00:00:00'
    if endtime=='':
        endtime='2018-04-01 00:00:00'
    data = YCcomplaints.select().where((YCcomplaints.starttime >= utc_str_to_timestamp(starttime)) & (YCcomplaints.status=='运行中') &((YCcomplaints.endtime-YCcomplaints.starttime)>=24*3600) & (
    YCcomplaints.endtime < utc_str_to_timestamp(endtime))).order_by(YCcomplaints.usetime.desc())
    result=[{"id":i+1,'area':data[i].area,'contacts':data[i].contacts,'number':data[i].serial,'phone':data[i].phone.replace('.0',''),'t2':utc_timestamp_to_str(data[i].endtime),"times":data[i].usetime} for i in range(len(data))]
    msg={"code":0,
            "msg":"success",
            'result':result,
            }
    return msg


##投诉处理时长Top20界面接口方法
def complain_top_chart_get(type,starttime=None, endtime=None):  # noqa: E501
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
    if starttime=='':
        starttime='2018-02-14 00:00:00'
    if endtime=='':
        endtime='2018-02-15 00:00:00'
    data = YCcomplaints.select().where((YCcomplaints.starttime >= utc_str_to_timestamp(starttime)) & (
    YCcomplaints.endtime < utc_str_to_timestamp(endtime))).order_by(YCcomplaints.usetime.desc()).paginate(1, 20)
    result=[{"rank":"top"+str(i+1),'geo':getxy(data[i].tsaddress,data[i].area)} for i in range(len(data))]
    msg={"code":0,
            "msg":"success",
            'result':result,
            }
    return msg
def complain_top_info_export_get(type):  # noqa: E501
    """eight hour complaint daily list export

    eight hour complaint daily list export # noqa: E501

    :param type: the type for user choose
    :type type: str

    :rtype: DownUrl
    """
    if (type == "完成量"):
        msg = msg_list_export
    else:
        msg = msg_list_export
    return msg
def complain_top_list_export_get(starttime=None, endtime=None):  # noqa: E501
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
    if starttime=='':
        starttime='2018-02-14 00:00:00'
    if endtime=='':
        endtime='2018-02-15 00:00:00'
    workbook_m = xlwt.Workbook(encoding='utf-8')
    xlsheet = workbook_m.add_sheet('投诉处理时长Top20', cell_overwrite_ok=True)
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
    xlsheet.write(0, 7, 'EMOS', style3)
    xlsheet.write(1, 0, '区县', style1)
    xlsheet.write(1, 1, '联系人', style1)
    xlsheet.write(1, 2, '服务号', style1)
    xlsheet.write(1, 3, '联系电话', style1)
    xlsheet.write(1, 4, 't2处理时间', style1)
    xlsheet.write(1, 5, '耗时', style1)
    xlsheet.write(1, 6, 'top', style1)

    data = YCcomplaints.select().where((YCcomplaints.starttime >= utc_str_to_timestamp(starttime)) & (
    YCcomplaints.endtime < utc_str_to_timestamp(endtime))).order_by(YCcomplaints.usetime.desc()).paginate(1, 20)
    i=1
    for item in data:
        xlsheet.write(i+1, 0, item.area, style1)
        xlsheet.write(i+1, 1, item.contacts, style1)
        xlsheet.write(i+1, 2, item.serial, style1)
        xlsheet.write(i+1, 3, item.phone, style1)
        xlsheet.write(i+1, 4, utc_timestamp_to_str(item.endtime), style1)
        xlsheet.write(i+1, 5, item.usetime, style1)
        xlsheet.write(i+1, 6, i, style1)
        i=i+1
    xlsname =  '投诉处理时长Top20' + str(int(time.time()))
    workbook_m.save('/var/www/downfile/{}.xls'.format(xlsname))
    url = 'down.caicool.cc:89/{}.xls'.format(xlsname)

    msg = {"code": 0, "msg": "success", "url": url}
    return msg
def complain_top_list_get(starttime=None, endtime=None):  # noqa: E501
    """Yichang Branch Broadens Fault Daily

    Yichang Branch Broadens Fault Daily # noqa: E501

    :param starttime: the starttime for user choose
    :type starttime: str
    :param endtime: the endtime for user choose
    :type endtime: str

    :rtype: TopList
    """


    if starttime=='':
        starttime='2018-02-14 00:00:00'
    if endtime=='':
        endtime='2018-02-15 00:00:00'
    data = YCcomplaints.select().where((YCcomplaints.starttime >= utc_str_to_timestamp(starttime)) & (
    YCcomplaints.endtime < utc_str_to_timestamp(endtime))).order_by(YCcomplaints.usetime.desc()).paginate(1, 20)
    result=[{"id":i+1,'area':data[i].area,'contacts':data[i].contacts,'number':data[i].serial,'phone':data[i].phone.replace('.0',''),'t2':utc_timestamp_to_str(data[i].endtime),"times":data[i].usetime} for i in range(len(data))]
    msg={"code":0,
            "msg":"success",
            'result':result,
            }
    return msg



