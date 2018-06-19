<template lang="html">
     <div class="Tops" :style="{marginTop:'-50px'}">
         <Row class="table">
           <Form ref="formCustom">
               <FormItem>
                   <Row>
                        <h3 :style="{marginBottom:'10px'}">装机时长TOP20</h3>
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
                          <Button :loading="loading1" type="ghost" icon="ios-cloud-upload-outline"  :style="{backgroundColor:'#2786d3',color:'#edf6fb'}" @click="Expor">导出</Button>
                      </Col>
                   </Row>
               </FormItem>
           </Form>
           <div>
             <Row>
                 <Table  :columns="columns1" :data="data1" border ref="table"></Table>
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
          model1:'',
          starttime:'',
          endtime:'',
          data3:[],
          typelist1:[
            { value:'宽带装机',label:'宽带装机'},
            { value:'和TV',label:'和TV'},
            { value:'移装机',label:'移装机'},
            { value:'IMS装机',label:'IMS装机'}
          ],
          columns1: [
            {
              title: 'Top',
              key: 'id',
              width: 80,
              align:'center'
            },
            {
                title: '区县',
                key: 'area',
                width:120,
                align:'center',

            },
            {
                title: '工单类型',
                align:'center',
                key: 'type'
            },
            {
                title: '服务账号',
                align:'center',
                key: 'account'
            },
            {
                title: 'PBOSS地址',
                width:400,
                align:'left',
                key: 'pboss'
            },
            {
                title: '受理时间',
                align:'center',
                key: 'times'
            },
              {
                  title: '详单',
                  key: 'operating',
                  width: 150,
                  align:'center',
                  render: (h, params) => {
                      return h('div', [
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
                                   //console.log(params.row.ID)
                                   this.$axios.get(`${this.URL_PREFIX}/installed/top/info/export?type=${params.row.ID}`)
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
    //  this.handleSpinCustom()
  },
  mounted() {
    this.handleSpinCustom()
  },
  methods: {
    /*获取数据列表*/
    getDatalist(){
      this.$axios.get(`${this.URL_PREFIX}/installed/top/list?starttime=${this.starttime}&endtime=${this.endtime}&type=${this.model1}`)
            .then(res => {
              if(res.data.code == '0'){
                //将获取的数据保存到data1空数组中
                this.data1 = res.data.result
                this.dataCount = res.data.result.length
                this.ajaxHistoryData = this.data1
                this.handleListApproveHistory()
                this.$Spin.hide()
                let len = this.data1.length
                for(let i=0;i<len; i++){
                  this.data3.push({'value': i })
                }
              }else{
                this.$Spin.hide()
              }
            })
            .catch(error => {
              this.$Spin.hide()
              console.log(error)
            })
    },
    Search() {
      this.loadings = true
      this.$axios.get(`${this.URL_PREFIX}/installed/top/list?starttime=${this.starttime}&endtime=${this.endtime}&type=${this.model1}`)
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
                           // let len = this.data1.length
                           //  for(let i=0;i<len; i++){
                           //    this.data3.push({'value': i })
                           //  }
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
        this.$axios.get(`${this.URL_PREFIX}/installed/top/list/export?starttime=${this.starttime}&endtime=${this.endtime}&type=${this.model1}`).then(res => {
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
        // setTimeout(() => {
        //                   excel(this.column1, this.$refs.table, '处理时长Top20.xlsx');
        //                   this.$Message.success('导出成功!')
        //           },1500)
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
<style scoped lang="scss">
    .Tops{
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
   .eight .table .ud-table-no-body {
     height: 40px;
     margin-bottom: -1px;
   }
</style>
