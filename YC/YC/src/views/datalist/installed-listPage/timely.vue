<template lang="html">
     <div class="twentyfour">
       <Row>
         <Row>
             <h3>农普及时率统计</h3>
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
                               <DatePicker type="datetime" placeholder="请选择" :value="endtime" @on-change="handlechanges"></DatePicker>
                       </FormItem>
                     </Col>
                     <Col span='10'>
                         <Button type="ghost" icon="ios-search-strong" :style="{backgroundColor:'#2786d3',color:'#edf6fb'}">查看</Button>
                     </Col>
                   </Row>
                   <Row :style="{marginTop:'15px'}">
                       <FormItem label="图形展示:">
                            <RadioGroup v-model="category">
                               <Radio label="装机及时率"></Radio>
                               <Radio label="平均装机时长"></Radio>
                           </RadioGroup>
                       </FormItem>
                   </Row>
                </FormItem>
             </Form>
         </Row>
         <Row>
            <div class="linelist" v-if="this.category=='装机及时率'">
                <span>{{this.category}}</span>
                <line-timely :starttime="this.starttime" :endtime="this.endtime" :type="this.category" :types="this.model1"></line-timely>
            </div>
         </Row>
         <Row>
            <div class="linelist" v-if="this.category=='平均装机时长'">
                <span>{{this.category}}</span>
                <ave-time :starttime="this.starttime" :endtime="this.endtime" :type="this.category" :types="this.model1"></ave-time>
            </div>
         </Row>
         <Row class="table">
           <Form ref="formCustom">
               <FormItem>
                   <Row >
                       <Col span="5">
                           <FormItem label="起始时间:">
                               <Col span="13">
                                   <DatePicker type="datetime" placeholder="请选择" :value="starttimes" @on-change="handlechanges"></DatePicker>
                               </Col>

                           </FormItem>
                       </Col>
                       <Col span="5">
                           <FormItem label="截止时间:">
                               <Col span="13">
                                   <DatePicker type="datetime" placeholder="请选择" :value="endtimes" @on-change="handlechanges1"></DatePicker>
                               </Col>
                           </FormItem>
                       </Col>
                       <Col span="5">
                           <FormItem label="原始工单名:">
                             <Col span="15">
                               <Select v-model="order" style="width:150px" clearable>
                                   <Option v-for="item in orderList" :value="item.value" :key="item.value">{{ item.value }}</Option>
                               </Select>
                             </Col>
                           </FormItem>
                       </Col>
                       <Col span="5">
                           <FormItem label="选择表格工单类型">
                             <Col span="12">
                               <Select v-model="model1" style="width:110px">
                                   <Option v-for="item in typelist1" :value="item.value" :key="item.value">{{ item.label }}</Option>
                               </Select>
                             </Col>
                           </FormItem>
                       </Col>
                       <Col span="4" class="btn">
                           <Button type="ghost" icon="ios-search-strong" :style="{backgroundColor:'#2786d3',color:'#edf6fb'}" @click="Search">查看</Button>
                           <Button :loading="loading1" type="ghost" icon="ios-cloud-upload-outline" :style="{backgroundColor:'#2786d3',color:'#edf6fb'}" @click="Expor">导出</Button>
                       </Col>
                   </Row>
               </FormItem>
           </Form>
           <div>
             <Row :style="{marginBottom:'30px'}">
                 <Table  :columns="columns1" :data="data1" border></Table>
             </Row>
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
import lineTimely from '../components2/line_timely'
import aveTime from '../components2/averagetime'
export default {
  data () {
      return {
          category:'装机及时率',
          loading: false,
          loadings:false,
          loading1:false,
          ajaxHistoryData:[],
          pageSize:11,
          dataCount:0,
          starttime:'',
          endtime:'',
          starttimes:'',
          endtimes:'',
          order:'',
          orderList:[],
          Types:'',
          typelist1:[
            { value:'宽带装机',label:'宽带装机'},
            { value:'TV单独安装',label:'TV单独安装'},
            { value:'IMS单独安装',label:'IMS单独安装'},
            { value:'移机装',label:'移机装'},
            { value:'全量工单',label:'全量工单'}
          ],
          model1:'宽带装机',
          model2:'',
          model3:'',
          model7:'',
          delystate:'',
          dely:[
            { value:'是',label:'是'},
            { value:'否',label:'否'},
          ],
          columns1: [
              {
                  title: '区县',
                  width: 80,
                  key: 'area'
              },
              {
                  title: '农普受理量',
                  key: 'accept',
                  align:'center'
              },
              {
                  title: '农普完成量',
                  key: 'complete',
                  align:'center'
              },
              {
                  title: '已装超时量',
                  key: 'loaded',
                  align:'center'
              },
              {
                  title: '未装超时量',
                  key: 'notLoaded',
                  align:'center'
              },
              {
                  title: '压单量',
                  key: 'pressing',
                  align:'center'
              },
              {
                  title: '装机及时率',
                  key: 'rate',
                  align:'center'
              },
              {
                  title: '平均装机时长(h)',
                  key: 'ave',
                  align:'center'
              },
              {
                  title: '详单',
                  key: 'operating',
                  width: 250,
                  align:'center',
                  render: (h, params) => {
                      return h('div', [
                          h('Select', {
                                    props:{
                                        placeholder:'点击选择',
                                        clearable: true
                                    },
                                    style: {
                                        width:'100px',
                                        height:'32px',
                                        display: 'inline-block',
                                        borderRadius:'20px',
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
                                  size: 'small',
                                  icon:'ios-download-outline'
                              },
                              style: {
                                  marginRight: '5px'
                              },
                              on: {
                                click: () => {
                                      let area = params.row.area
                                      let time = this.starttimes
                                      let time2 = this.endtimes
                                      let category = this.model1
                                      let types = this.data3[params.index].value
                                      this.All = time+'_'+time2+'_'+area+'_'+category+'_'+types
                                      if(Number.isInteger(this.data3[params.index].value)){
                                         this.$Message.error('请选择导出报表类型')
                                      }else {
                                        this.$axios.get(`${this.URL_PREFIX}/installed/agricultural/info/export?type=${this.All}`)
                                                   .then(res => {
                                                     if(res.data.code == '0'){
                                                       setTimeout(() => {
                                                         this.$Message.success('导出成功')
                                                         window.location.href=`http://${res.data.url}`
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
          data1: [],
          data3:[],
          options:['已装超时量', '未装超时量', '压单量'],
          historyData: []
      }
  },
  created (){
    //  this.handleSpinCustom()
  },
  mounted (){
      this.getOrderList()
      this.getDatalist()
  },
  methods: {
    getOrderList(){
      this.$axios.get(`${this.URL_PREFIX}/upload/filelist?starttime=${this.starttime}&endtime=${this.endtime}`)
                .then(res => {
                    if(res.data.code == '0'){
                      for(var i = 0;i<res.data.result.length;i++){
                        this.orderList.push({value:res.data.result[i].name,msg:res.data.result[i].url})
                      }
                      //console.log(this.orderList)
                    }
                })
                .catch(error => {
                  console.log(error)
                })
    },
    /*获取数据列表*/
    getDatalist(){
      this.$axios.get(`${this.URL_PREFIX}/installed/agricultural/list?starttime=${this.starttimes}&endtime=${this.endtimes}&type=${this.model1}`)
            .then(res => {
              if(res.data.code == '0'){
                //将获取的数据保存到data1空数组中
                this.data1 = res.data.result
                this.dataCount = res.data.result.length
                this.ajaxHistoryData = this.data1
                this.handleListApproveHistory()
                let len = this.data1.length
                for(let i=0;i<len; i++){
                  this.data3.push({'value': i })
                }
              }
            })
            .catch(error => {
              console.log(error)
            })
    },
    Search(){
      this.loadings = true
      this.$axios.get(`${this.URL_PREFIX}/installed/agricultural/list?starttime=${this.starttimes}&endtime=${this.endtimes}&type=${this.model1}`)
            .then(res => {
              if(res.data.code == '0'){
                this.loadings = false
                if(res.data.result.length == 0){
                        this.loadings = false
                        setTimeout(() => {

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
              setTimeout(() => {
                this.$Message.warning('未搜索到匹配信息,请重试!')
                this.data1 = ''
              },1500)
              console.log(error)
            })
    },
    /*
        导出原始数据
    */
    Expor() {
      if(this.order ==''||this.order == null){
         this.$Message.warning('请选择原始工单名!')
      }else{
        this.loading1 = true
        for(let item of this.orderList){
          if(this.order === item.value){
            this.url = item.msg
          }
        }
        this.Types = this.url+'_'+this.model1
        this.$axios.get(`${this.URL_PREFIX}/installed/agricultural/list/export?starttime=${this.starttimes}&endtime=${this.endtimes}&type=${this.Types}`)
        .then(res => {
          if(res.data.code == '0'){
            this.loading1 = false
            setTimeout(() => {
              this.$Message.success('导出成功')
              window.location.href=`http://${res.data.url}`
            },1500)
          }else {
            this.loading1 = false
            setTimeout(() => {
              this.$Message.success('导出失败')
            },1500)
          }
        }).catch( error => {
          this.loading1 = false
          setTimeout(() => {
            this.$Message.error('系统错误')
          },1500)
          cossole.log(error)
        })
      }

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
          // 初始化显示，小于每页显示条数，全显，大于每页显示条数，取前每页条数显示
          if(this.data1 < this.pageSize){
              this.data1 = this.ajaxHistoryData;
          }else{
              this.data1 = this.ajaxHistoryData.slice(0,this.pageSize);
          }


      },
    changepage(index){
          var _start = ( index - 1 ) * this.pageSize;
          var _end = index * this.pageSize;
          this.data1 = this.ajaxHistoryData.slice(_start,_end);
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
     lineTimely,
     aveTime
  }

}
</script>
<style scoped lang="scss">
    .twentyfour{
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
       left: 30%;
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
</style>
<style>
  .ivu-tabs .ivu-tabs-tabpane{
    background-color: #ffffff;
  }
  .ivu-tabs .ivu-tabs-tabpane{
    height: 780px;
    overflow-y: scroll;
  }
</style>
