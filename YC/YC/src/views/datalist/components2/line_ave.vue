<template>
    <div class="test" ref="myEchart1"></div>
</template>

<script>
import echarts from 'echarts';
let option = {
  color:['#2786d3'],
  title:{
    show:true,
    subtext: '单位:小时(h)',
    top:20,
    left:55,
    subtextStyle:{
      color:'#ed462f'
    }
  },
  tooltip : {
      trigger: 'axis',
      formatter: '{b}:\n{c}h',
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
  xAxis: [{
      type: 'category',
      data: []
  }],
  yAxis:[
     {
        type: 'value',
        axisLabel: {
              formatter: '{value}h'
            }
      }
    ],
    series: [
        {
          data: [],
          type: 'line',
          smooth:true,
          itemStyle: {
                  normal: {
                      label: {
                          show: true,
                          formatter: '{c}h'
                      }
                  }
            },
        }
     ]
};
export default {
    name: 'visiteVolume',
    props:['starttime','endtime','type','Data'],
    data () {
        return {
          chart:null,
          names:[],
          values:[],
          data:[]
        };
    },
    mounted () {
        this.$nextTick(() => {
           this.handleSpinCustom()
        });
    },
    methods: {
      handleSpinCustom() {
                 this.$Spin.show({
                     render: (h) => {
                         return h('div', [
                             h('Icon', {
                                 'class': 'demo-spin-icon-load',
                                 props: {
                                     type: 'load-c',
                                     size: 18
                                 }
                             }),
                             h('div', '图表加载中...')
                         ])
                     }
                 });
                this.getData()
      },
      getData() {
        this.$axios.get(`${this.URL_PREFIX}/installed/eight/chart?starttime=${this.starttime}&endtime=${this.endtime}&type=${this.type}`)
        .then(res => {
           if(res.data.code == '0'){
               console.log(this.Data)
               this.chart = echarts.init(this.$refs.myEchart1);
               this.data = res.data.result
               for(let item of this.data){
                  this.names.push(item.name)
                  this.values.push(item.value)
               }
               option.xAxis[0].data = this.names
               option.series[0].data = this.values
               this.chart.setOption(option,true);
               this.$Spin.hide();
          }else {
            this.$Spin.hide();
          }
        })
        .catch(error => {
          console.log(error)
          this.$Spin.hide()
        })
      }
    }
};
</script>
<style lang="scss" scoped>
  .test{
    width: 1250px;
    height: 350px;
  }

  .demo-spin-icon-load{
      animation: ani-demo-spin 1s linear infinite;
  }
  .demo-spin-col{
     position: absolute;
     left: 40%;
     top:50%;
     z-index: 100;
     transform: translate3d(-40%,-50%);
  }
</style>
