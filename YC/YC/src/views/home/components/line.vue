<template>
    <div style="width:100%;height:100%;" ref="myEchart1"></div>
</template>

<script>
import echarts from 'echarts';

//配置项
let option1 = {
  title:{
    show:true,
    subtext: '单位:单',
    top:20,
    subtextStyle:{
      color:'#ed462f'
    }
  },
  tooltip : {
      trigger: 'axis',
      axisPointer : {
          type : 'shadow'
      }
  },
  xAxis: [{
      type: 'category',
      data: [],
      axisLabel:{
        interval:0,
        fontSize:10,
        formatter:function(value)
         {
             return value.split("").join("\n");
         }
      }
  }],
  yAxis: {
      type: 'value'
  },
  series: [{
      data: [],
      type: 'line',
      itemStyle: {
              normal: {
                  label: {
                      show: true
                  }
              }
        }
  }]
};
export default {
    data () {
        return {
            chart1:null,
            names:[],
            values:[],
            data:[]
        };
    },
    mounted () {
      this.$nextTick(() => {
          this.getLine()
      });
    },
    methods: {
      getLine() {
        this.$axios.get(`${this.URL_PREFIX}/home/linetwo`).then(res => {
           if(res.data.code == '0'){
               this.chart1 = echarts.init(this.$refs.myEchart1);
               this.data = res.data.result
               for(let item of this.data){
                  this.names.push(item.name)
                  this.values.push(item.value)
               }
               option1.xAxis[0].data = this.names
               option1.series[0].data = this.values
               this.chart1.setOption(option1,true);
           }

        })
      }
    }
};
</script>
