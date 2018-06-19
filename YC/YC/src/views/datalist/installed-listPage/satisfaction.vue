<template lang="html">
     <div class="twentyfour">
       <Row>
         <Row>
             <h3>装机满意度回访结果</h3>
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
                               <Radio label="满意率 (IVR)"></Radio>
                               <Radio label="回访成功率 (IVR)"></Radio>
                               <Radio label="满意率 (人工外呼)"></Radio>
                              <Radio label="回访成功率 (人工外呼)"></Radio>
                           </RadioGroup>
                       </FormItem>
                   </Row>
                </FormItem>
             </Form>
         </Row>
         <Row>
            <div class="linelist" v-if="this.category=='满意率 (IVR)'">
                <span>{{this.category}}</span>
                <line-satisfaction :starttime="this.starttime" :endtime="this.endtime" :type="this.category" :types="this.model1"></line-satisfaction>
            </div>
         </Row>
         <Row>
            <div class="linelist" v-if="this.category=='回访成功率 (IVR)'">
                <span>{{this.category}}</span>
                <line-return :starttime="this.starttime" :endtime="this.endtime" :type="this.category" :types="this.model1"></line-return>
            </div>
         </Row>
         <Row>
            <div class="linelist" v-if="this.category=='满意率 (人工外呼)'">
                <span>{{this.category}}</span>
                <line-artifical :starttime="this.starttime" :endtime="this.endtime" :type="this.category" :types="this.model1"></line-artifical>
            </div>
         </Row>
         <Row>
            <div class="linelist" v-if="this.category=='回访成功率 (人工外呼)'">
                <span>{{this.category}}</span>
                <line-success :starttime="this.starttime" :endtime="this.endtime" :type="this.category" :types="this.model1"></line-success>
            </div>
         </Row>
         <Row class="table">
           <Form ref="formCustom">
               <FormItem>
                   <Row >
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
                          <Button type="ghost" icon="ios-cloud-upload-outline" :style="{backgroundColor:'#2786d3',color:'#edf6fb'}" @click="Expor">导出</Button>
                       </Col>
                   </Row>
               </FormItem>
           </Form>
           <div>
             <Row>
                 <Table  :columns="columns1" :data="data1" border></Table>
             </Row>
             <Row :style="{marginTop: '15px'}">
                 <Page :style="{float:'right'}" :total='dataCount' size="small" :page-size="pageSize" show-total show-elevator @on-change="changepage"></Page>
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
import lineSatisfaction from '../components2/line_satisfaction'
import lineReturn from '../components2/line_return'
import lineArtifical from '../components2/line_artifical'
import lineSuccess from '../components2/line_success'
export default {
  data () {
      return {
          category:'满意率 (IVR)',
          loadings: false,
          ajaxHistoryData:[],
          pageSize:10,
          dataCount:0,
          starttime:'',
          endtime:'',
          starttimes:'',
          endtimes:'',
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
                  key: 'area',
                  align:'center'
              },
              {
                  title: '回访数',
                  key: 'visit',
                  align:'center'
              },
              {
                  title: '回访成功数',
                  key: 'succ',
                  align:'center'
              },
              {
                  title: '回访成功率',
                  key: 'rate',
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
                  title: '未回复',
                  key: 'unanswered',
                  align:'center'
              },
              {
                  title: '满意度',
                  key: 'satisfactionRate',
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
                                   }else{
                                     this.$axios.get(`${this.URL_PREFIX}/installed/satisfaction/info/export?type=${this.All}`)
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
          data1: [],
          data3:[],
          options:['回访成功数','满意','不满意','未回复'],
          historyData: []
      }
  },
  created (){
    //  this.handleSpinCustom()
  },
  mounted (){
      this.getDatalist()
  },
  methods: {
    /*获取数据列表*/
    getDatalist(){
      this.$axios.get(`${this.URL_PREFIX}/installed/satisfaction/list?starttime=${this.starttimes}&endtime=${this.endtimes}&type=${this.model1}`)
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
    Search() {
      this.loadings = true
      this.$axios.get(`${this.URL_PREFIX}/installed/satisfaction/list?starttime=${this.starttime}&endtime=${this.endtime}&type=${this.model1}`)
            .then(res => {
              if(res.data.code == '0'){
                this.loadings = false
                if(res.data.result.length == 0){
                        setTimeout(() => {
                          this.loadings = false
                          this.$Message.warning('未搜索到匹配信息,请重试!')
                          this.data1 = ''
                        },1500)
                      }else {
                        this.loadings = false

                           this.data1 = res.data.result
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
        this.$axios.get(`${this.URL_PREFIX}/installed/satisfaction/list/export?starttime=${this.starttimes}&endtime=${this.endtimes}&type=${this.model1}`).then(res => {
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
        }).catch( error => {
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
     lineSatisfaction,
     lineReturn,
     lineArtifical,
     lineSuccess
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
