<template>
    <div id="myChart1" :style="{width:'230px',height:'230px'}"  ref="myEchart5"></div>
</template>

<script>
import echarts from 'echarts';
const option5 = {
      tooltip : {
          formatter: "{b} : {c}h"
      },
      toolbox: {
          feature: {

          }
      },
      series: [
          {
              name: '平均处理时长',
              type: 'gauge',
              min: 0,
              max: 24,
              detail: {
                formatter:'{value}h',
                fontSize: 12,
                offsetCenter: [0, '50px']
              },
              data: [],
              radius: '80%',
              title: {
                offsetCenter: [0, '80px']
              },
          }
      ]
};
export default {
    name: 'userFlows',
    data () {
        return {
            chart5:null,
            names:[],
            values:[],
            data:[]
        };
    },
    mounted () {

          this.getFlow()

    },
    methods: {
      getFlow() {
        this.$axios.get(`${this.URL_PREFIX}/home/pan`).then(res => {
           if(res.data.code == '0'){
               this.chart5 = echarts.init(this.$refs.myEchart5);
               this.data = res.data.result[1]
               option5.series[0].data = this.data
               this.chart5.setOption(option5,true);
           }
        })
      }
    }
};
</script>
<style lang="scss"  scoped>
    #myChart1{
      position: absolute;
      left: 50%;
      margin-left:-115px;
    }
</style>
