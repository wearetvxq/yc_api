<template lang="html">
     <div class="eight">
       <Row>
         <Row>
             <h3>宜昌高频故障网元TOP20</h3>
         </Row>
         <Row class="table">
           <Form ref="formCustom">
               <FormItem>
                   <Row>
                       <Col span="6">
                           <FormItem label="起始时间:">
                               <Col span="13">
                                   <DatePicker type="datetime" placeholder="请选择" :value="starttime" @on-change="handlechange"></DatePicker>
                               </Col>

                           </FormItem>
                       </Col>
                       <Col span="6">
                           <FormItem label="截止时间:">
                               <Col span="13">
                                   <DatePicker type="datetime" placeholder="请选择" :value="endtime" @on-change="handlechange1"></DatePicker>
                               </Col>
                           </FormItem>
                       </Col>
                       <Col span="6" class="btn">
                          <Button type="ghost" icon="ios-search-strong" :style="{backgroundColor:'#2786d3',color:'#edf6fb'}" @click="Search">查看</Button>
                          <Button :loading='loading1' type="ghost" icon="ios-cloud-upload-outline" :style="{backgroundColor:'#2786d3',color:'#edf6fb'}" @click="Expor">导出</Button>
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
export default {
  data () {
      return {
          loadings: false,
          loading1:false,
          ajaxHistoryData:[],
          pageSize:10,
          dataCount:0,
          starttime:'',
          endtime:'',
          data3:[],
          All:'',
          datas:[],
          options:['故障工单量'],
          columns1: [
              {
                  title: 'Top',
                  key: 'id',
                  width: 60,
                  align:'center'
              },
              {
                  title: '区县',
                  key: 'area',
                  align:'center'
              },
              {
                  title: '高频故障网元',
                  key: 'name',
                  align:'center'
              },
              {
                  title: '故障工单量',
                  key: 'total',
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
                                      placeholder:'请选择',
                                      clearable:true,
                                      default:'故障工单量'
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
                                  marginRight: '5px',
                                  display: 'inline-block'
                              },
                              on: {
                                click: () => {
                                  let name = params.row.name
                                  let time = this.starttime
                                  let time2 = this.endtime
                                  let types = this.data3[params.index].value
                                  this.All = time+'_'+time2+'_'+name+'_'+types
                                  if(Number.isInteger(this.data3[params.index].value)){
                                     this.$Message.error('请选择导出报表类型')
                                  }else{
                                    this.$axios.get(`${this.URL_PREFIX}/complain/network/info/export?type=${this.All}`)
                                               .then(res => {
                                                 if(res.data.code == '0'){
                                                   setTimeout(() => {
                                                     this.$Message.success('导出成功')
                                                     window.location.href=`http://${res.data.url}`
                                                   },1500)
                                                 }else {
                                                   setTimeout(() => {
                                                      this.$Message.success('导出失败')
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
    //this.getDatalist()
    this.handleSpinCustom()
  },
  methods: {
    /*获取数据列表*/
    getDatalist(){
      this.$axios.get(`${this.URL_PREFIX}/complain/network/list?starttime=${this.starttime}&endtime=${this.endtime}`)
            .then(res => {
              if(res.data.code == '0'){
                this.data1 = res.data.result
                let len = this.data1.length
                for(let i=0;i<len; i++){
                  this.data3.push({'value': i })
                }
                this.dataCount = res.data.result.length
                this.ajaxHistoryData = this.data1
                this.handleListApproveHistory()
                this.$Spin.hide();
              }
            })
            .catch(error => {
              console.log(error)
            })
    },
    /*
    查询
    */
    Search(){
      this.loadings = true
      this.$axios.get(`${this.URL_PREFIX}/complain/network/list?starttime=${this.starttime}&endtime=${this.endtime}`)
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
        this.$axios.get(`${this.URL_PREFIX}/complain/network/list/export?starttime=${this.starttime}&endtime=${this.endtime}`).then(res => {
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
    },
    handlechange(datetime){
       this.starttime = datetime
     },
     handlechange1(datetime){
       this.endtime = datetime
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
      handleSpinCustom (){
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
          this.getDatalist()
      }
  }

}
</script>
<style lang="scss" scoped>
    .eight{
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
     margin-top: 28px;
     margin-bottom: 12px;
     padding-right: 17px;

   }
   .table_title{
     background-color: red;
   }
  .eight .table .ud-table-no-body {
    height: 40px;
    margin-bottom: -1px;
  }
  .eight .table .ud-table-no-bod .ivu-table-header{
    background-color: red;
  }
</style>
