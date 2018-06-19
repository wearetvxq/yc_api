<template>
    <div style="width:100%;height:100%;" ref="myEchart"></div>
</template>

<script>
import echarts from 'echarts';
let option = {
  tooltip : {
      trigger: 'axis',
      formatter: '{b}:\n{c}%',
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
              formatter: '{value}%'
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
                          formatter: '{c}%'
                      }
                  }
            },
        }
     ]
};
export default {
    name: 'visiteVolume',
    props:['starttime','endtime','type'],
    data () {
        return {
          chart:null,
          names:[],
          values:[],
          data:[]
        };
    },
    computed:{

    },
    created(){

    },
    mounted(){
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
      Transform() {
        this.starttime =this.starttime.toString()
        this.starttime = this.endtime.toString()
        this.type = this.type.toString()
      },
      getData() {
        this.Transform()
        this.$axios.get(`${this.URL_PREFIX}/installed/eight/chart?starttime=${this.starttime}&endtime=${this.endtime}&type=${this.type}`)
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
                         this.$Spin.hide();
                     }else {
                         this.$Spin.hide()
                     }
        })
        .catch(error => {
          this.$Spin.hide()
          console.log(error)
        })
      }
    }
};
</script>
<style lang="scss" scoped>

</style>
