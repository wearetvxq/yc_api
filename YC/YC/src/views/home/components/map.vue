<template>
    <div style="width:calc(100% - 1px);height:525px;" id="home_page_map"></div>
</template>

<script>
import echarts from 'echarts';
import geoData from '../map-data/get-geography-value.js';
export default {
    name: 'homeMap',
    props: {
        cityData: Array
    },
    mounted () {
        var convertData = function (data) {
            let res = [];
            let len = data.length;
            for (var i = 0; i < len; i++) {
                var geoCoord = geoData[data[i].name];
                if (geoCoord) {
                    res.push({
                        name: data[i].name,
                        value: geoCoord.concat(data[i].value)
                    });
                }
            }
            return res;
        };
        var map = echarts.init(document.getElementById('home_page_map'));
        const yichangJson = require('../map-data/yichang.json');
        echarts.registerMap('yc', yichangJson );
        map.setOption( {
            backgroundColor: '#FFF',
            geo: {
                map: 'yc',
                label: {
                    normal: {
                      show:true,
                      color:'#fff'
                    },
                    emphasis: {
                      show: true,
                      color:'#fff'
                    }

                },
                itemStyle: {
                    normal: {
                        areaColor: '#5aa8eb',
                        borderColor: '#CCC'
                    },
                    emphasis: {
                        areaColor: '#ede22f'
                    }
                }
            },
            grid: {
                top: 0,
                left: '2%',
                right: '2%',
                bottom: '0',
                containLabel: true
            },
            series: [{
                type: 'map',
                coordinateSystem: 'geo',
                data: convertData(this.cityData),
                symbolSize: function (val) {
                    return val[2] / 10;
                },
                label: {
                    normal: {
                        formatter: '{b}',
                        position: 'right',
                        show: false
                    },
                    emphasis: {
                        show: true
                    }
                },
                itemStyle: {
                    normal: {
                        color: '#0099CC'
                    }
                }
            }]
        });
        window.addEventListener('resize', function () {
            map.resize();
        });
    }
};
</script>
<style lang="scss" scoped>
  #home_page_map{
    margin-left: -38px;
  }
</style>
