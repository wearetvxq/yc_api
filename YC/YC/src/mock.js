const Mock = require('mockjs')
//使用mockjs模拟数据
var Random = Mock.Random
Random.city()
Random.integer()
Random.word()

const data = Mock.mock({
  'citys|6': [{
    'name': "@city()",
    'value':"@integer(500,1500)"
  }]
})
const data1 = Mock.mock({
  'citys|7': [{
    'name': "@city()",
    'value':"@integer(800,1800)"
  }]
})
const data2 = Mock.mock({
  'result|10': [{
    'area': "@city()",
    'accept_count':"@integer(10,50)",
    'finish_count':"@integer(10,30)",
    'unfinish_overtime':"@integer(70,130)",
    'finish_overtime':"@integer(40,80)",
    'complaint_rate':"@integer(10,80)%",
    'average_time':"@integer(5,24)"
  }]
})
const data3 = Mock.mock({
  'des|8': [{
    'name': "@word(3,5)",
    'value':"@integer(30,200)"
  }]
})
const data4 = Mock.mock({
  'Inters|8': [{
    'name': "@integer(4,100)M",
    'value':"@integer(80,400)"
  }]
})


export default
Mock.mock('/api/data', (req, res) => {
    return {
        data
    }
})

Mock.mock('/api/data1', (req, res) => {
    return {
        data1
    }
})

Mock.mock('/api/data2', (req, res) => {
    return {
        data2
    }
})
Mock.mock('/api/data3', (req, res) => {
    return {
        data3
    }
})
Mock.mock('/api/data4', (req, res) => {
    return {
        data4
    }
})
