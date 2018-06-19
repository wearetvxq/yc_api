<template lang="html">
     <div class="visited">
       <Row>
         <Row>
             <h3>家宽EMOS投诉回访满意度通报</h3>
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
                               <Radio label="投诉回访满意度"></Radio>
                               <Radio label="投诉成功率"></Radio>
                               <!-- <Radio label="投诉满意度"></Radio> -->
                               <Radio label="投诉不满意度"></Radio>
                               <Radio label="总单量"></Radio>
                           </RadioGroup>
                       </FormItem>
                   </Row>
                </FormItem>
             </Form>
         </Row>
         <Row>
            <div class="linelist" v-if="this.category=='投诉回访满意度'">
                <span>{{this.category}}</span>
                <line-satisfaction :starttime="this.starttime" :endtime="this.endtime" :type="this.category"></line-satisfaction>
            </div>
         </Row>
         <Row>
            <div class="linelist" v-if="this.category=='投诉成功率'">
                <span>{{this.category}}</span>
                <line-success :starttime="this.starttime" :endtime="this.endtime" :type="this.category"></line-success>
            </div>
         </Row>
         <!-- <Row>
            <div class="linelist" v-if="this.category=='投诉满意度'">
                <span>{{this.category}}</span>
                <line-pleased :starttime="this.starttime" :endtime="this.endtime" :type="this.category"></line-pleased>
            </div>
         </Row> -->
         <Row>
            <div class="linelist" v-if="this.category=='投诉不满意度'">
                <span>{{this.category}}</span>
                <line-unpleased :starttime="this.starttime" :endtime="this.endtime" :type="this.category"></line-unpleased>
            </div>
         </Row>
         <Row>
            <div class="linelist" v-if="this.category=='总单量'">
                <span>{{this.category}}</span>
                <line-total :starttime="this.starttime" :endtime="this.endtime" :type="this.category"></line-total>
            </div>
         </Row>
         <Row class="table">
           <Form ref="formCustom">
               <FormItem>
                   <Row>
                       <Col span="6">
                           <FormItem label="起始时间:">
                               <Col span="13">
                                   <DatePicker type="datetime" placeholder="请选择" :value="starttimes" @on-change="handlechanges"></DatePicker>
                               </Col>

                           </FormItem>
                       </Col>
                       <Col span="6">
                           <FormItem label="截止时间:">
                               <Col span="13">
                                   <DatePicker type="datetime" placeholder="请选择" :value="endtimes" @on-change="handlechanges1"></DatePicker>
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
           <div :style="{marginBottom:'30px'}">
             <Row>
                <Table class="ud-table-no-body" :columns="columns0" :data="dataNull" border :no-data-text='null'></Table>
             </Row>
             <Row>
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
import lineSatisfaction from '../components/line_satisfaction.vue'
import lineSuccess from '../components/line_success.vue'
// import linePleased from '../components/line_pleased.vue'
import lineUnpleased from '../components/line_unpleased.vue'
import lineTotal from '../components/line_total.vue'
export default {
  components:{  lineSatisfaction, lineSuccess, lineUnpleased, lineTotal},
  data () {
      return {
          category:'投诉回访满意度',
          loadings: false,
          loading1:false,
          ajaxHistoryData:[],
          pageSize:11,
          dataCount:0,
          data3:[],
          starttime:'',
          endtime:'',
          starttimes:'',
          endtimes:'',
          All:'',
          datas:[],
          artificial:{},
          ivr:{},
          Obj:{},
          options:['满意(IVR)', '不满意(IVR)', '满意(人工)', '不满意(人工)'],
          columns0: [
            { title: null ,width: 107,align: 'center' },
            { title: 'IVR自动回访',align: 'center' },
            { title: '人工回访', align: 'center' },
            { title: null ,align: 'center',width:416 }
          ],
          dataNull:[],
          columns1: [
              {
                  title: '区县',
                  key: 'area',
                  width: 108,
                  align:'center'
              },
              {
                  title: '投诉回访成功量',
                  key: 'succ',

                  align:'center'
              },
              {
                  title: '满意',
                  key: 'satisfaction',

                  align:'center'
              },
              {
                  title: '不满意',
                  key: 'displeasure',

                  align:'center'
              },
              {
                  title: '投诉回访成功量',
                  key: 'succ_',

                  align:'center'
              },
              {
                  title: '满意',
                  key: 'satisfaction_',

                  align:'center'
              },
              {
                  title: '不满意',
                  key: 'displeasure_',

                  align:'center'
              },
              {
                  title: '投诉回访满意度',
                  key: 'rate',
                  width:128,
                  align:'center'
              },
              {
                  title: '排名',
                  key: 'rank',
                  width:88,
                  align:'center'
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
                                      width:'85px',
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
                                  marginRight: '5px',
                                  display: 'inline-block'
                              },
                              on: {
                                click: () => {
                                      let area = params.row.area
                                      let time = this.starttimes
                                      let time2 = this.endtimes
                                      let types = this.data3[params.index].value
                                      this.All = time+'_'+time2+'_'+area+'_'+types
                                      if(Number.isInteger(this.data3[params.index].value)){
                                         this.$Message.error('请选择导出报表类型')
                                      }else {
                                        this.$axios.get(`${this.URL_PREFIX}/complain/visit/info/export?type=${this.All}`)
                                                   .then(res => {
                                                     if(res.data.code == '0'){
                                                       setTimeout(() => {
                                                         this.$Message.success('导出成功')
                                                         window.location.href=`http://${res.data.url}`
                                                       },1500)
                                                     }else {
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
          data1: [],
          historyData: []
      }
  },
  created (){
  },
  mounted() {
    this.getDatalist()
  },
  methods: {
    /*获取数据列表*/
    getDatalist(){
      this.$axios.get(`${this.URL_PREFIX}/complain/visit/list?starttime=${this.starttimes}&endtime=${this.endtimes}`)
            .then(res => {
              if(res.data.code == '0'){
                // for(let item of res.data.result){
                //   let area = { area : item.area }
                //   let rate = { rate : item.rate }
                //   let rank = { rank : item.rank }
                //   this.ivr = Object.assign(item.ivr[0],area,rate,rank)
                //   this.artificial =  item.artificial[0]
                //   this.Obj = Object.assign(this.ivr,this.artificial)
                //   this.datas.push(this.Obj)
                // }
                // // console.log(this.Obj)

                this.datas =  res.data.result
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
    Search(){
      this.loadings = true
      this.$axios.get(`${this.URL_PREFIX}/complain/visit/list?starttime=${this.starttimes}&endtime=${this.endtimes}`)
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
    Expor() {
        this.loading1 = true
        this.$axios.get(`${this.URL_PREFIX}/complain/visit/list/export?starttime=${this.starttimes}&endtime=${this.endtimes}`).then(res => {
          if(res.data.code == '0'){
              this.loading1 = false
              setTimeout(() => {
                this.$Message.success('导出成功')
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
  }

}
</script>
<style lang="scss" scoped>
    .visited{
      margin-left: 15px;
      overflow-y:hidden;
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
       transform: translate3d(-40%,-50%);
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
   .table_title{
     background-color: red;
   }
  .visited .table .ud-table-no-body {
    height: 40px;
    margin-bottom: -1px;
  }
</style>
