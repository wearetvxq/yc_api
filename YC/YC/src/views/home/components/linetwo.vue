<template>
    <div style="width:100%;height:100%;" ref="myEchart"></div>
</template>

<script>
import echarts from 'echarts';

//配置项
let option = {
  color:['#081e1b'],
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
            chart:null,
            data:[],
            values:[],
            names:[]
        };
    },
    mounted () {
      this.$nextTick(() => {
          this.getLine()
      });
    },
    methods: {
      getLine() {
        this.$axios.get(`${this.URL_PREFIX}/home/lineone`).then(res => {
           if(res.data.code == '0'){
               this.chart = echarts.init(this.$refs.myEchart);
               this.data = res.data.result
               for(let item of this.data){
                  this.names.push(item.name)
                  this.values.push(item.value)
               }
               option.xAxis[0].data = this.names
               option.series[0].data = this.values
               this.chart.setOption(option,true);
           }


        })
      }
    }
};
</script>
