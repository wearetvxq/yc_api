<template>
    <div style="width:100%;height:100%;" ref="myEchart"></div>
</template>

<script>
import echarts from 'echarts';
let option = {
  color:['#28e9ea'],
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
  yAxis: {
      type: 'value'
  },
  series: [{
      data: [],
      itemStyle: {
              normal: {
                  label: {
                      show: true,
                      formatter: '{c}h'
                  }
              }
      },
      type: 'line',
  }]
};
export default {
    name: 'visiteVolume',
    props:['starttime','endtime','type','types'],
    data () {
        return {
          All:'',
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
        this.All  = this.types+'_'+this.type
        console.log(this.All)
        this.$axios.get(`${this.URL_PREFIX}/installed/agricultural/chart?starttime=${this.starttime}&endtime=${this.endtime}&type=${this.All}`)
        .then(res => {
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
               this.$Spin.hide()
           }else{
             this.$Spin.hide()
           }
        })
        .catch(error => {
          this.$Spin.hide()
        })
      }
    }
};
</script>
<style lang="scss" scoped>
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
