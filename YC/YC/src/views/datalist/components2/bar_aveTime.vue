<template>
    <div style="width:100%;height:100%;" ref="myEchart"></div>
</template>

<script>
import echarts from 'echarts';
let  option = {
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
  calculable : true,
  xAxis : [
      {
          type : 'category',
          data : []
      }
  ],
  yAxis : [
      {
          type : 'value',
          axisLabel: {
                formatter: '{value}h'
              }
      }
  ],
  series : [
      {
          //name:'2小时内(含)',
          type:'bar',
          //barGap: 0,
          barWidth: '50%',
          data:[],
          itemStyle: {
                  normal: {
                      label: {
                          show: true,
                          formatter: '{c}h'
                      }
                  }
          },
          markPoint : {
              data : [
                  // {type : 'max', name: '最大值'},
                  // {type : 'min', name: '最小值'}
              ]
          },
          markLine : {
              data : [
                  // {type : 'average', name: '平均值'}
              ]
          }
      },
   //    {
   //        name:'超过2小时',
   //        type:'bar',
   //        data:[],
   //        itemStyle: {
   //                normal: {
   //                    label: {
   //                        show: true,
   //                        formatter: '{c}h'
   //                    }
   //                }
   //        },
   //        markPoint : {
   //            data : [
   //                // {name : '年最高', value : 182.2, xAxis: 7, yAxis: 183},
   //                // {name : '年最低', value : 2.3, xAxis: 11, yAxis: 3}
   //            ]
   //        },
   //        markLine : {
   //            data : [
   //                // {type : 'average', name : '平均值'}
   //            ]
   //        }
   // }
]
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
          values1:[],
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
        this.$axios.get(`${this.URL_PREFIX}/installed/orders/chart?starttime=${this.starttime}&endtime=${this.endtime}&type=${this.All}`)
        .then(res => {
           if(res.data.code == '0'){
               this.chart = echarts.init(this.$refs.myEchart);
               this.data = res.data.result
               for(let item of this.data){
                  this.names.push(item.area)
                  this.values.push(item.inside)
                //  this.values1.push(item.ultra)
               }
               option.xAxis[0].data = this.names
               option.series[0].data = this.values
            //   option.series[1].data = this.values1
               this.chart.setOption(option,true);
               this.$Spin.hide();
           }else {
             this.$Spin.hide();
           }
        })
        .catch(error => {
          this.$Spin.hide();
          console.log(error)
        })
      }
    }
};
</script>
