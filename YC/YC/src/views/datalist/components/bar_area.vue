<template>
    <div style="width:100%;height:100%;" ref="myEchart"></div>
</template>

<script>
import echarts from 'echarts';
let option = {
  title : {
      text: '高频小区详情',
  },
  color:['#ed462f'],
  tooltip : {
      trigger: 'axis',
      axisPointer : {
          type : 'shadow'
      }
  },
  toolbox: {
        show: true,
        right:'50',
        feature: {
            saveAsImage: {}
        }
    },
  grid: {
      y2: 140,

  },
  xAxis: [{
      type: 'category',
      data: [],
      axisLabel:{
        interval:0,
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
      type: 'bar',
      barWidth:'50%'
  }]
};
export default {
    name: 'visiteVolume',
    props:{
      barData:{
        type:Array
      }
    },
    data () {
        return {
          All:'',
          chart:null,
          names:[],
          values:[],
          data:[],
          columns:[]
        };
    },
    mounted () {
      this.getData()
    },

    methods: {
      getData() {

           if(this.barData.length > 0){
               this.chart = echarts.init(this.$refs.myEchart);
               for(let item of this.barData){
                    this.names.push(item.name)
                    this.values.push(item.value)
               }
               option.xAxis[0].data = this.names
               option.series[0].data = this.values
               this.chart.setOption(option,true);
           }

      }
    }

};
</script>
