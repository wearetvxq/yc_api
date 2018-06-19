<template lang="html">
     <div class="eight">
       <Row>
         <Row>
             <h3>装机接单及时率</h3>
             <Form :style="{marginTop:'20px'}">
                <FormItem>
                   <Row>
                     <Col span='7'>
                       <FormItem label="起始时间:">
                               <DatePicker type="datetime" placeholder="请选择" :value="starttime" @on-change="handlechange"></DatePicker>
                       </FormItem>
                     </Col>
                     <Col span='7'>
                       <FormItem label="截止时间:">
                               <DatePicker type="datetime" placeholder="请选择" :value="endtime" @on-change="handlechange1"></DatePicker>
                       </FormItem>
                     </Col>
                     <!-- <Col span='10'>
                          <Button type="ghost" icon="ios-search-strong" :style="{backgroundColor:'#2786d3',color:'#edf6fb'}">查看</Button>
                     </Col> -->
                   </Row>
                   <Row :style="{marginTop:'15px'}">
                       <FormItem label="图形展示:">
                            <RadioGroup v-model="category">
                               <Radio label="接单时长"></Radio>
                               <Radio label="接单时长占比"></Radio>
                               <Radio label="接单平均时长"></Radio>
                           </RadioGroup>
                       </FormItem>
                   </Row>
                </FormItem>
             </Form>
         </Row>
         <Row>
            <div class="linelist" v-if="this.category=='接单时长'">
                <span>{{this.category}}</span>
                <bar-timely :starttime="this.starttime" :endtime="this.endtime" :type="this.category" :types="this.model1"></bar-timely>
            </div>
         </Row>
         <Row>
            <div class="linelist" v-if="this.category=='接单时长占比'">
                <span>{{this.category}}</span>
                <bar-propotion :starttime="this.starttime" :endtime="this.endtime" :type="this.category" :types="this.model1"></bar-propotion>
            </div>
         </Row>
         <Row>
            <div class="linelist" v-if="this.category=='接单平均时长'">
                <span>{{this.category}}</span>
                <bar-avetime :starttime="this.starttime" :endtime="this.endtime" :type="this.category" :types="this.model1"></bar-avetime>
            </div>
         </Row>
         <Row class="table">
           <Form ref="formCustom">
               <FormItem>
                   <Row>
                       <Col span="6">
                           <FormItem label="起始时间:">
                               <Col span="13">
                                   <DatePicker type="datetime" placeholder="请选择" :value="starttime" @on-change="handlechanges"></DatePicker>
                               </Col>

                           </FormItem>
                       </Col>
                       <Col span="6">
                           <FormItem label="截止时间:">
                               <Col span="13">
                                   <DatePicker type="datetime" placeholder="请选择" :value="endtime" @on-change="handlechanges1"></DatePicker>
                               </Col>
                           </FormItem>
                       </Col>
                       <Col span="6">
                           <FormItem label="选择表格工单类型">
                             <Col span="12">
                               <Select v-model="model1" style="width:110px">
                                   <Option v-for="item in typelist1" :value="item.value" :key="item.value">{{ item.label }}</Option>
                               </Select>
                             </Col>
                           </FormItem>
                       </Col>
                       <Col span="6" class="btn">
                          <Button type="ghost" icon="ios-search-strong" :style="{backgroundColor:'#2786d3',color:'#edf6fb'}" @click="Search">查看</Button>
                          <Button :loading="loading1" type="ghost" icon="ios-cloud-upload-outline" :style="{backgroundColor:'#2786d3',color:'#edf6fb'}" @click="Expor">导出</Button>
                      </Col>
                   </Row>
               </FormItem>
           </Form>
           <div>
             <Row>
                <Table class="ud-table-no-body" :columns="columns0" :data="dataNull" border :no-data-text='null'></Table>
             </Row>
             <Row :style="{marginBottom:'30px'}">
                 <Table  :columns="columns1" :data="datas" border></Table>
             </Row>
             <!-- <Row :style="{marginTop: '15px'}">
                 <Page :style="{float:'right'}" :total='dataCount' size="small" :page-size="pageSize" show-total show-elevator @on-change="changepage"></Page>
             </Row> -->
           </div>
           <Col class="demo-spin-col" span="8" v-show="loadings">
             <Spin fix>
                 <Icon type="load-c" size=18 class="demo-spin-icon-load"></Icon>
                 <div>数据查询中...</div>
             </Spin>
           </Col>
         </Row>
       </Row>
     </div>
</template>

<script>
import barTimely from '../components2/bar_timely.vue'
import barPropotion from  '../components2/bar_order.vue'
import barAvetime from  '../components2/bar_aveTime.vue'
export default {
  data () {
      return {
          category:'接单时长',
          loading: false,
          loadings:false,
          loading1:false,
          ajaxHistoryData:[],
          pageSize:11,
          dataCount:0,
          model1:'宽带装机',
          starttime:'',
          endtime:'',
          starttimes:'',
          endtimes:'',
          duration:{},
          accounting:{},
          columns0: [
            { title: '接单时长',width:499,align: 'center' },
            { title: '接单时长占比', align: 'center' },
            { title: '#',width:200, align: 'center' }
          ],
          dataNull:[],
          typelist1:[
            { value:'宽带装机',label:'宽带装机'},
            { value:'和TV',label:'和TV'},
            { value:'移装机',label:'移装机'},
            { value:'IMS装机',label:'IMS装机'}
          ],
          columns1: [
            {
                title: '区县',
                key: 'area',
                align:'center',
                width: 85
            },
            {
                title: '总量',
                align:'center',
                key: 'total',
                width: 83
            },

            {
                title: '2h内',
                align:'center',
                key: 'oneToTwo',
                width: 80
            },
            {
                title: '2-10h',
                align:'center',
                key: 'twoToTen',
                width: 80
            },
            {
                title: '10-24h',
                align:'center',
                key: 'tenToTwentyFour',
                width: 86
            },
            {
                title: '超24h',
                align:'center',
                key: 'twentyFour',
                width: 85
            },

            {
                title: '2h内',
                key: 'oneToTwo_1',
                align:'center'
            },
            {
                title: '2-10h',
                key: 'twoToTen_1',
                align:'center'
            },
            {
                title: '10-24h',
                key: 'tenToTwentyFour_1',
                align:'center'
            },
            {
                title: '超24h',
                key: 'twentyFour_1',
                align:'center'
            },
            {
               title:'首次联系用户平均时长',
               key:'ave',
               align:'center'
            },
            {
               title:'2h及时率',

               align:'center',
               key:'rate',
            },
              {
                  title: '详单',
                  key: 'operating',
                  width: 200,
                  align:'center',
                  render: (h, params) => {
                      return h('div', [
                        h('Select', {
                                  props:{
                                    placeholder:'点击选择',
                                    clearable:true
                                  },
                                  style: {
                                      width:'100px',
                                      height:'34px',
                                      display: 'inline-block',
                                      marginRight:'15px'
                                  },
                                  on: {
                                      'on-change':(event) => {
                                          this.data3[params.index].value= event;
                                      }
                                  },
                              },
                                  this.options.map(function(option){
                                      return h('Option', {
                                          props: {value: option}
                                      }, option);
                                  })
                          ),
                          h('Button', {
                              props: {
                                  type: 'primary',
                                  size: 'small'
                              },
                              style: {
                                  marginRight: '5px',
                                  display: 'inline-block'
                              },
                              on: {
                                click: () => {
                                  let area = params.row.area
                                  let time = this.starttimes
                                  let time2 = this.endtimes
                                  let category = this.model1
                                  let types = this.data3[params.index].value
                                  this.All = time+'_'+time2+'_'+category+'_'+area+'_'+types
                                 if(Number.isInteger(this.data3[params.index].value)){
                                    this.$Message.error('请选择导出报表类型')
                                 }else{
                                   this.$axios.get(`${this.URL_PREFIX}/installed/orders/info/export?type=${this.All}`)
                                              .then(res => {
                                                if(res.data.code == '0'){
                                                  setTimeout(() => {
                                                    this.$Message.success('导出成功')
                                                    //打开文件下载链接
                                                    window.location.href=`http://${res.data.url}`
                                                  },1500)
                                                }else{
                                                  setTimeout(() => {
                                                     this.$Message.error('导出失败')
                                                  },1500)
                                                }
                                              })
                                              .catch(error => {
                                                console.log(error)
                                              })
                                     }
                                }
                              }
                          }, '导出')
                      ]);
                  }
              }
          ],
          datas: [],
          data3:[],
          options:['2小时内', '2-10小时', '10-24小时','超24小时'],
          historyData: []
      }
  },
  created (){
    //  this.handleSpinCustom()
  },
  mounted() {
    this.getDatalist()
  },
  methods: {
    /*获取数据列表*/
    getDatalist(){
      this.$axios.get(`${this.URL_PREFIX}/installed/orders/list?starttime=${this.starttimes}&endtime=${this.endtimes}&type=${this.model1}`)
            .then(res => {
              if(res.data.code == '0'){
                 this.datas = res.data.result
                // for(let item of res.data.result){
                //   let area = { area : item.area}
                //   this.duration = Object.assign(item.duration[0],area)
                //   this.accounting =  item.accounting[0]
                //   this.Obj = Object.assign(this.duration,this.accounting)
                //   this.datas.push(this.Obj)
                // }

                let len = this.datas.length

                this.dataCount = this.datas.length
                this.ajaxHistoryData = this.datas
                this.handleListApproveHistory()
                for(let i=0;i<len; i++){
                  this.data3.push({'value': i })
                }

              }
            })
            .catch(error => {
              console.log(error)
            })
    },
    /*
       查询
    */
    Search() {
      this.loadings = true
      this.$axios.get(`${this.URL_PREFIX}/installed/orders/list?starttime=${this.starttimes}&endtime=${this.endtimes}&type=${this.model1}`)
            .then(res => {
              if(res.data.code == '0'){
                this.loadings = false
                if(res.data.result.length == 0){
                        setTimeout(() => {
                          this.loading = false
                          this.$Message.warning('未搜索到匹配信息,请重试!')
                          this.data1 = ''
                        },1500)
                      }else {
                        this.loadings = false
                           this.data1 = res.data.result
                           let len = this.data1.length
                            for(let i=0;i<len; i++){
                              this.data3.push({'value': i })
                            }
                           this.dataCount = res.data.result.length
                           this.ajaxHistoryData = this.data1
                           this.handleListApproveHistory()
                      }
              }else {
                this.loadings = false
                setTimeout(() => {
                  this.$Message.warning('未搜索到匹配信息,请重试!')
                  this.data1 = ''
                },1500)
              }
            })
            .catch(error => {
              this.loadings = false
              console.log(error)
            })
    },
    /*
        导出原始数据
    */
    Expor() {
      this.loading1 = true
        this.$axios.get(`${this.URL_PREFIX}/installed/orders/list/export?starttime=${this.starttimes}&endtime=${this.endtimes}&type=${this.model1}`).then(res => {
          if(res.data.code == '0'){
            this.loading1 = false
            setTimeout(() => {
              this.$Message.success('导出成功')
              //打开文件下载链接
                 window.location.href=`http://${res.data.url}`
            },1500)
          }else {
            this.loading1 = false
            setTimeout(() => {
              this.$Message.error('导出失败')
            },1500)
          }
        }).catch( error => {
          this.loading1 = false
          setTimeout(() => {
            this.$Message.error('系统错误')
          },1500)
          cossole.log(error)
        })
    },
    handlechange(datetime){
       this.starttime = datetime
     },
     handlechange1(datetime){
       this.endtime = datetime
     },
     handlechanges(datetime){
        this.starttimes = datetime
      },
      handlechanges1(datetime){
        this.endtimes = datetime
      },
    handleListApproveHistory(){
         //获取数据
          //this.getDatalist()
          // 初始化显示，小于每页显示条数，全显，大于每页显示条数，取前每页条数显示
          if(this.datas < this.pageSize){
              this.datas = this.ajaxHistoryData;
          }else{
              this.datas = this.ajaxHistoryData.slice(0,this.pageSize);
          }


      },
    changepage(index){
          var _start = ( index - 1 ) * this.pageSize;
          var _end = index * this.pageSize;
          this.datas = this.ajaxHistoryData.slice(_start,_end);
      },
      handleSpinCustom () {
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
                      h('div', '数据加载中...')
                  ])
              }
          });
          setTimeout(() => {
              this.getDatalist()
              this.$Spin.hide();
          }, 1000);
      }
  },
  components: {
    barTimely,
    barPropotion,
    barAvetime
  }

}
</script>
<style scoped lang="scss">
    .eight{
      margin-left: 15px;
    }
    .home{
        padding: 15px;
    }
    .Top{
      width: 100%;
      height: 500px;

      margin-bottom: 25px;
    }
   .ivu-form-item .ivu-form-item{
     margin-right: 10px;

   }
   .ivu-btn-ghost{
     margin-left: -20px;
   }
   .demo-spin-icon-load{
        animation: ani-demo-spin 1s linear infinite;
    }
    .demo-spin-col{

       position: absolute;
       left: 40%;
       top:50%;
       z-index: 100;
       transform: translate3d(-30%,-50%);
   }
   .btn{

     Button{
       margin: 0 10px;
     }
   }
   .linelist{
     height: 350px;
   }
   .table{
     margin-top: 58px;
     margin-bottom: 12px;
     padding-right: 17px;
   }
   .eight .table .ud-table-no-body {
     height: 40px;
     margin-bottom: -1px;
   }
</style>
