<template>
    <div style="width:100%;height:100%;" ref="myEchart3"></div>
</template>

<script>
import echarts from 'echarts';
let option3 = {
    color: ['#54bfac'],
    tooltip : {
        trigger: 'axis',
        formatter: '{b}:\n{c}%',
        axisPointer : {            // 坐标轴指示器，坐标轴触发有效
            type : 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
        }
    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
    xAxis : [
        {
            type : 'category',
            data : [],
            axisTick: {
                alignWithLabel: true
            }
        }
    ],
    yAxis : [
        {
            type : 'value',
            axisLabel: {
                  formatter: '{value}%'
            }
        }
    ],
    series : [
        {
            type:'bar',
            barWidth: '40%',
            data:[],
            itemStyle: {
                    normal: {
                        label: {
                            show: true,
                            formatter: '{c}%'
                        }
                    }
              }
        }
    ]
};
export default {
    // name:'visiteVolume',
    data () {
        return {
            chart3:null,
            names:[],
            values:[],
            data:[]
        };
    },
    mounted () {
        this.$nextTick(() => {
            this.getBar()
            // window.addEventListener('resize', function () {
            //     visiteVolume.resize();
            // });
        });
    },
    methods: {
      getBar() {
        this.$axios.get(`${this.URL_PREFIX}/home/barone`).then(res => {
           if(res.data.code == '0'){
               this.chart3 = echarts.init(this.$refs.myEchart3);
               this.data = res.data.result
               for(let item of this.data){
                  this.names.push(item.name)
                  this.values.push(parseInt(item.value*100))
               }
               option3.xAxis[0].data = this.names
               option3.series[0].data = this.values
               this.chart3.setOption(option3,true);
           }
        })
      }
    }
};
</script>
