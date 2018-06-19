<template>
    <div style="width:100%;height:100%;" ref="myEchart2"></div>
</template>

<script>
import echarts from 'echarts';
let option2 = {
  title:{
    show:true,
    subtext: '单位:次',
    top:20,
    subtextStyle:{
      color:'#ed462f'
    }
  },
  tooltip : {
      trigger: 'axis',
      axisPointer : {            // 坐标轴指示器，坐标轴触发有效
          type : 'shadow' ,    // 默认为直线，可选为：'line' | 'shadow'
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
      type: 'bar',
      barWidth: '50%',
      itemStyle: {
              normal: {
                  label: {
                      show: true,
                      formatter: '{c}'
                  }
              }
      },
  }]
};
export default {
    data () {
        return {
            chart2 :null,
            names:[],
            values:[],
            data:[]
        };
    },
    mounted () {
      this.$nextTick(() => {
          this.getData()
      });
    },
    methods: {
       getData() {
         this.$axios.get(`${this.URL_PREFIX}/home/bartwo`).then(res => {
            if(res.data.code == '0'){
                this.chart2 = echarts.init(this.$refs.myEchart2);
                this.data = res.data.result
                for(let item of this.data){
                   this.names.push(item.name)
                   this.values.push(item.value)
                }
                option2.xAxis[0].data = this.names
                option2.series[0].data = this.values
                this.chart2.setOption(option2,true);
            }
         })
       }
    }

    }

</script>
<style lang="scss" scoped>

<style>
