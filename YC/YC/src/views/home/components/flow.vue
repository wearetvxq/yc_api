<template>
    <div  id="myChart" :style="{width:'230px',height:'230px'}" ref="myEchart4"></div>
</template>

<script>
import echarts from 'echarts';
//配置项
let option4 = {
      tooltip : {
          formatter: "{b} : {c}%"
      },
      toolbox: {
          feature: {

          }
      },
      series: [
          {
              name: '及时率',
              type: 'gauge',
              min: 0,
              max: 100,
              detail: {
                formatter:'{value}%',
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
    name: 'userFlow',
    data () {
        return {
            chart4:null,
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
               this.chart4 = echarts.init(this.$refs.myEchart4);
               this.data = res.data.result[0]
               option4.series[0].data = this.data
               this.chart4.setOption(option4,true);
           }

        })
      }
    }
};
</script>
<style lang="scss" scoped>
     #myChart{
        position: absolute;
        left: 50%;
        margin-left:-115px;
     }
</style>
