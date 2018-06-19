<template lang="html">
      <div class="inbound">
           <Row>
              <Row>
                  <div :style="{marginLeft:'15px'}">
                    <h3>工作站入库明细表</h3>
                    <Form :style="{marginTop:'20px',marginLeft:'15px'}">
                       <FormItem>
                          <Row>
                            <Col span='6'>
                              <FormItem label="起始时间:">
                                      <DatePicker type="datetime" placeholder="请选择" :value="starttime" @on-change="handlechanges" style="width:180px"></DatePicker>
                              </FormItem>
                            </Col>
                            <Col span='7'>
                              <FormItem label="截止时间:">
                                      <DatePicker type="datetime" placeholder="请选择" :value="endtime" @on-change="handlechanges1" style="width:180px"></DatePicker>
                              </FormItem>
                            </Col>
                            <Col span='8'>
                              <FormItem label="工作站:">
                                <Select v-model="station" style="width:180px" clearable>
                                    <Option v-for="item in stationList" :value="item.value" :key="item.value">{{ item.value }}</Option>
                                </Select>
                              </FormItem>
                            </Col>
                          </Row>
                          <Row type="flex" justify="end" :style="{marginRight:'100px',marginTop:'5px'}">
                             <Button type="success" icon="ios-search-strong" :style="{color:'#edf6fb',marginRight:'10px'}" @click="Search">查找</Button>
                             <Button type="ghost" icon="ios-cloud-upload-outline" :style="{backgroundColor:'#2786d3',color:'#edf6fb'}" @click="Expor" :loading="loading1">导出</Button>
                          </Row>
                          <Row :style="{marginTop:'-15px'}">
                            <Col span='6'>
                              <FormItem label="终端类型:">
                                <Select v-model="mode" style="width:180px" clearable>
                                    <Option v-for="item in terminalList" :value="item.value" :key="item.value">{{ item.value }}</Option>
                                </Select>
                              </FormItem>
                            </Col>
                            <Col span="7" :style="{marginRight:'24px'}">
                              <FormItem label="终端型号:">
                                <Select v-model="type" style="width:180px" clearable>
                                    <Option v-for="item in typeList" :value="item.value" :key="item.value">{{ item.value }}</Option>
                                </Select>
                              </FormItem>
                            </Col>
                            <Col span='8'>
                              <FormItem label="模糊查找:" :style="{marginLeft:'-37px'}">
                                  <Input v-model="keyword" placeholder="请输入关键词进行查找" style="width:180px" clearable></Input>
                              </FormItem>
                            </Col>
                          </Row>
                       </FormItem>
                    </Form>
                  </div>
                  <div :style="{padding:'0 15px',marginTop:'30px'}" class="table">
                    <Row :style="{marginBottom:'30px'}">
                        <Table :loading="loading" :columns="columns1" :data="data1" border>
                        </Table>
                    </Row>
                    <Row :style="{marginTop: '15px'}">
                        <Page :style="{float:'right'}" :total='dataCount' size="small" :page-size="pageSize" show-total show-elevator @on-change="changepage"></Page>
                    </Row>
                  </div>
              </Row>
           </Row>
           <Modal v-model="showinfo"
           :title="title"
           width="560">
              <div class="content">
                  <ul>
                    <li v-for="item in infos" >
                        <div class="wrapper">
                           <div class="time">
                              <span>{{item.posttime}}</span>
                           </div>
                           <div class="log">
                             <div class="circle">
                                <div class="minicircle"></div>
                             </div>
                             <div class="line"></div>
                           </div>
                           <div class="status">
                               <span>{{item.work}}--{{item.use}}--{{item.receive}}</span>
                           </div>
                        </div>
                    </li>
                  </ul>
              </div>
           </Modal>
           <transition name='modal-fade'>
               <div class="stockin" v-show="isCompile">
                    <div class="modal">
                        <div class="header">
                          <p>入库信息编辑</p>
                          <p @click="CloseModal" class="close">
                             <icon type="close"></icon>
                          </p>
                        </div>
                        <div class="body">
                           <div class="station lis">
                             <Form :style="{width:'390px',height:'50px',marginLeft:'78px',marginTop:'17px'}">
                                 <FormItem label="工作站:">
                                   <Select  v-model="station1" style="width:180px" clearable>
                                       <Option v-for="item in stationList" :value="item.value" :key="item.value">{{ item.value }}</Option>
                                   </Select>
                                 </FormItem>
                             </Form>
                           </div>
                           <div class="terminal lis">
                             <Form :style="{width:'390px',height:'50px',marginLeft:'65px',marginTop:'17px'}" >
                                 <FormItem label="终端类型:">
                                   <Select v-model="terminal" style="width:180px" >
                                       <Option v-for="item in terminalList" :value="item.value" :key="item.value">{{ item.value }}</Option>
                                   </Select>
                                 </FormItem>
                             </Form>
                           </div>
                           <div class="vendor lis">
                             <Form :style="{width:'390px',height:'50px',marginLeft:'89px',marginTop:'17px'}" >
                                 <FormItem label="厂家:">
                                   <Select v-model="vendor" style="width:180px" >
                                       <Option v-for="item in factoryList" :value="item.value" :key="item.value">{{ item.value }}</Option>
                                   </Select>
                                 </FormItem>
                             </Form>
                           </div>
                           <div class="type lis">
                             <Form :style="{width:'390px',height:'50px',marginLeft:'89px',marginTop:'17px'}" >
                                 <FormItem label="型号:">
                                   <Select v-model="type1" style="width:180px" >
                                       <Option v-for="item in typeList" :value="item.value" :key="item.value">{{ item.value }}</Option>
                                   </Select>
                                 </FormItem>
                             </Form>
                           </div>
                           <div class="outer lis">
                             <Form :style="{width:'390px',height:'50px',marginLeft:'78px',marginTop:'17px'}" >
                                 <FormItem label="入库人:">
                                   <Select v-model="stocker" style="width:180px" >
                                       <Option v-for="item in personList" :value="item.value" :key="item.value">{{ item.value }}</Option>
                                   </Select>
                                 </FormItem>
                             </Form>
                           </div>
                           <div class="code lis">
                             <Form :style="{width:'390px',height:'50px',marginLeft:'78px',marginTop:'17px'}" >
                                 <FormItem label="条形码:">
                                   <Input v-model="code" placeholder="请输入条形码" style="width:180px" clearable></Input>
                                 </FormItem>
                             </Form>
                           </div>
                        </div>
                        <div class="footer">
                          <Button type="primary" icon="checkmark-round" size="small" :style="{marginRight:'20px'}" @click="Submit">提交</Button>
                          <Button type="error" icon="close-round" size="small" @click="Cancel">取消</Button>
                        </div>
                    </div>
               </div>
           </transition>
      </div>
</template>

<script>
export default {
     data(){
       return {
           loading:false,
           loading1:false,
           showinfo:false,
           isCompile:false,
           id:'',
           code:'',
           stocker:'',
           type:'',
           vendor:'',
           terminal:'',
           keyword:'',
           mode:'',
           type:'',
           type1:'',
           title:'',
           starttime:'',
           endtime:'',
           dataCount:0,
           pageSize:10,
           currentpage:1,
           station:'',
           station1:'',
           infos:[],
           personList:[],
           factoryList:[
             {name:'中兴',value:'中兴'},
             {name:'华为',value:'华为'},
             {name:'贝尔',value:'贝尔'},
             {name:'杭研',value:'杭研'}
           ],
           terminalList:[],
           stationList:[],
           typeList:[],
           data1:[],
           columns1:[
             {
                 title: '工作站',
                 key: 'work',
                 align:'center'
             },
             {
                 title: '终端类型',
                 key: 'type',
                 align:'center'
             },
             {
                 title: '厂家',
                 key: 'factory',
                 align:'center'
             },
             {
                 title: '型号',
                 key: 'model',
                 align:'center'
             },
             {
                 title: '条形码',
                 key: 'code',
                 align:'center'
             },
             {
                 title: '入库时间',
                 key: 'posttime',
                 width:160,
                 align:'center'
             },
             {
                 title: '入库人',
                 key: 'principal',
                 align:'center'
             },
             {
                 title: '终端状态',
                 key: 'operating',
                 width: 150,
                 align:'center',
                 render: (h, params) => {
                     return h('div', [
                         h('a', {
                             style: {
                                 color:'#258ee9',

                             },
                             on: {
                                 click: () => {

                                    this.$axios.get(`${this.URL_PREFIX}/supplies/query/${params.row.code}`)
                                                     .then(res => {
                                                       if(res.data.code == '0'){
                                                         let type = res.data.result[0].type
                                                         let model = res.data.result[0].model
                                                         this.title = `(${type+','+model})`

                                                         this.infos = res.data.result[0].info
                                                         console.log(this.infos)


                                                       }else{

                                                       }
                                                     }).catch(error => {
                                                         console.log(error)
                                                     })

                                    setTimeout(() => {
                                        this.showinfo = true
                                    },500)
                                 }
                             }
                         }, '查看'),
                     ]);
                 }
             },
             {
                      title: '操作',
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
                                      marginRight: '5px'
                                  },
                                  on: {
                                     click: () => {
                                          this.$axios.get(`${this.URL_PREFIX}/supplies/storage/query/${params.row.code}`)
                                                     .then(res => {
                                                       if(res.data.code == '0'){
                                                          this.station1 = res.data.result[0].work
                                                          this.stocker = res.data.result[0].principal
                                                          this.vendor =  res.data.result[0].factory
                                                          this.code = res.data.result[0].code
                                                          this.terminal = res.data.result[0].type
                                                          this.type1 = res.data.result[0].model
                                                          this.id = res.data.result[0].id
                                                          this.isCompile = true
                                                       }
                                                     }).catch(error => {
                                                         console.log(error)
                                                     })
                                      }
                                  }
                              }, '编辑')
                          ]);
                      }
                  }
           ]
       }
     },
     created(){
            this.$nextTick(function () {
                this.handleSpinCustom()
                this.Getworkstation()
                this.GetterminalList()
                this.gettypeList()
                this.getpersonList()
            })
      },
     methods:{
       /*
           遮罩层
       */
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
                              h('div', '数据加载中...')
                          ])
                      }
                  });
                 this.getDataList()
       },
       Getworkstation(){
         this.$axios.get(`${this.URL_PREFIX}/label/work`)
                    .then(res => {
                      if(res.data.code == '0'){
                         for(let item of res.data.result){
                           this.stationList.push({name:item.name,value:item.name})
                         }
                      }
                      //  console.log(this.stationList)
                    })
                    .catch(error => {
                      console.log(error)
                    })
       },
       GetterminalList(){
         this.$axios.get(`${this.URL_PREFIX}/label/terminal/type`)
                    .then(res => {
                      if(res.data.code == '0'){
                        for(let item1 of res.data.result){
                          this.terminalList.push({name:item1.name,value:item1.name})
                        }
                      }
                    })
                    .catch(error => {
                      console.log(error)
                    })

       },
       getfactoryList(){
         this.$axios.get(`${this.URL_PREFIX}/label/business`)
                    .then(res => {
                      if(res.data.code == '0'){
                        for(let item2 of res.data.result){
                          this.factoryList.push({name:item2.name,value:item2.name})
                        }
                      }
                    })
                    .catch(error => {
                      console.log(error)
                    })
       },
       gettypeList(){
         this.$axios.get(`${this.URL_PREFIX}/label/terminal/model`)
                    .then(res => {
                      if(res.data.code == '0'){
                        for(let item3 of res.data.result){
                          this.typeList.push({name:item3.name,value:item3.name})
                        }
                      }
                    })
                    .catch(error => {
                      console.log(error)
                    })

       },
       getpersonList(){
         this.$axios.get(`${this.URL_PREFIX}/label/people`)
                    .then(res => {
                      if(res.data.code == '0'){
                        for(let item4 of res.data.result){
                          this.personList.push({name:item4.name,value:item4.name})
                        }
                      }
                    })
                    .catch(error => {
                      console.log(error)
                    })

       },
       getDataList(){
            this.$axios.get(`${this.URL_PREFIX}/supplies/storage?page=1&size=${this.pageSize}`).then( res => {
                if(res.data.code == '0'){
                     this.data1 = res.data.result
                     this.ajaxHistoryData = this.data1
                     this.dataCount =res.data.total
                     this.handleListApproveHistory()
                     this.$Spin.hide()
                 }
               }).catch(error => {
                 this.$Spin.hide()
                 console.log(error)
                })
       },
       Search(){
          this.loading = true
          this.$axios.get(`${this.URL_PREFIX}/supplies/storage?page=1&size=${this.pageSize}&starttime=${this.starttime}&endtime=${this.endtime}&work=${this.station}&type=${this.mode}&model=${this.type}&keyword=${this.keyword}`)
                .then(res => {
                  if(res.data.code == '0'){

                    if(res.data.result.length == 0){
                            this.dataCount = 0
                            this.data1 = []
                            setTimeout(() => {
                                this.loading = false
                              this.$Message.warning('未搜索到匹配信息,请重试!')
                            },1500)
                          }else {
                            this.data1 = res.data.result
                            this.dataCount = res.data.result.length
                            this.ajaxHistoryData = this.data1
                            this.handleListApproveHistory()
                             setTimeout(() => {
                               this.loading = false
                             },1500)
                          }
                  }else {
                    this.loading = false
                    setTimeout(() => {
                      this.$Message.warning('未搜索到匹配信息,请重试!')
                      this.dataCount = 0
                      this.data1 = []
                    },1500)
                  }
                })
                .catch(error => {
                  setTimeout(() => {
                    this.loading = false
                    this.$Message.warning('系统错误,请联系管理员!')
                    this.data1 = []
                    this.dataCount = 0
                  },1500)
                  console.log(error)
                })
       },
       Expor(){
         this.loading1 = true
         this.$axios.get(`${this.URL_PREFIX}/supplies/storage/export?starttime=${this.starttime}&endtime=${this.endtime}&work=${this.station}&type=${this.mode}&model=${this.type}&keyword=${this.keyword}`).then( res => {
             if(res.data.code == '0'){
               this.loading1 = false
               this.$Message.success('导出成功')
               window.location.href=`http://${res.data.url}`
              }
            }).catch(error => {
              this.loading1 = false
              console.log(error)
             })
       },
       CloseModal(){
         this.isCompile = false
         this.Reset()
       },
       //提交编辑操作
       Submit(){

                this.$axios.put(`${this.URL_PREFIX}/supplies/storage`,{
                    work:this.station1,
                    factory:this.vendor,
                    type:this.terminal,
                    model:this.type1,
                    code:this.code,
                    principal:this.stocker,
                    id:this.id
                }).then(res => {
                    if(res.data.code == '0'){
                      setTimeout(() => {
                        this.getDataList()
                        this.isCompile = false
                        this.$Message.success('编辑成功')
                      },1500)
                    }else{
                      setTimeout(() => {
                        this.isCompile = false
                        this.$Message.error('编辑失败')
                      },1500)
                    }
                }).catch(error => {
                    console.log(error)
                })

       },
       //取消编辑操作
       Cancel(){
         this.isCompile = false
         this.Reset()
       },
       Reset(){
         this.station = ''
         this.terminal = ''
         this.vendor = ''
         this.type = ''
         this.code = ''
         this.stocker = ''
       },
       handleListApproveHistory(){
             if(this.data1 < this.pageSize){
                 this.data1 = this.ajaxHistoryData;
             }else{
                 this.data1 = this.ajaxHistoryData.slice(0,this.pageSize);
             }
         },
       changepage(index){
             this.currentpage = index
             this.loading = true
             this.$axios.get(`${this.URL_PREFIX}/supplies/storage?page=${this.currentpage}&size=${this.pageSize}`).then( res => {
                 if(res.data.code == '0'){
                      this.data1 = res.data.result
                      this.loading = false
                  }
                }).catch(error => {
                  console.log(error)
                 })
        },
       handlechanges(datetime){
          this.starttime = datetime
        },
       handlechanges1(datetime){
           this.endtime = datetime
         },
     }

}
</script>

<style lang="scss" scoped>
    .inbound{

    }
    .btn   Button{
        margin-left: 17px;
    }
    .table{
      display: relative;
    }
    .content{
      margin-top: 10px;
    }

    .content li{
      list-style-type:none;
      margin-top: -6px;
    }
    .content li:last-child{
       .line{
         height: 0;
       }
    }
    .content li:first-child .log .circle .minicircle{
          background-color: #90db5a;
    }
    .content li:last-child .log .circle .minicircle{
          background-color: #ee5c53;
    }
    .wrapper{
      display: flex;
    }
    .content .log {
      position: relative;
      left: 33px;
    }
    .content .status{
      position: relative;
      left: 50px;
    }
    .content .log .circle{
      width: 16px;
      height: 16px;
      background-color: #ffffff;
      border-radius: 50%;
      border:1px solid #f0f0f0;
      position: relative;
      left: -7px;
    }
    .content .log .circle .minicircle{
      width: 8px;
      height: 8px;
      border-radius: 50%;
      position: absolute;
      top:50%;
      left: 50%;
      margin-left: -4px;
      margin-top: -4px;
    }
    .content .log .line{
      width: 2px;
      height: 53px;
      background-color:#f0f0f0;
      display: inline-block;
    }
</style>
<style scoped>
.modal-fade-enter,
.modal-fade-leave-active {
    opacity: 0;
}
.modal-fade-enter-active,
.modal-fade-leave-active{
  transition:opacity .5s ease;
}
.stockin{
  position: absolute;
  top: -16px;
  right: 0;
  bottom: 0;
  left:0;
  background-color: rgba(0,0,0,.3);
  justify-content: center;
  align-items: center;
  z-index: 100;
}
.modal{
  width: 390px;
  border-radius: 6px;
  box-shadow: 2px 2px 10px 1px;
  position: absolute;
  top: 130px;
  left: 50%;
  transform: translateX(-50%);
  z-index: 10000;
}
.modal .header{
 height: 45px;
 background-color: #2786d3;
}
.modal .header p{
 text-align: center;
 line-height: 45px;
 color:#ffffff;
 font-size: 14px;
 font-weight: 600;
}
.modal .header .close{
  display: flex;
  justify-content: flex-end;
  font-size: 16px;
  margin-top: -29px;
  margin-right: 14px;
  color:#fff;
  cursor: pointer;
}
.modal .body .lis{
 height: 45px;
 display: flex;
 justify-content: center;
 align-items: center;
 border-bottom: 1px solid #e9e9e9;
 background-color: #ffffff;
}
.modal .footer{
 display: flex;
 justify-content:center;
 align-items: center;
 height: 60px;
 background-color: #ffffff;
}


</style>
<style lang="scss">
.ivu-row{
  background-color: #fff;
}
 .ivu-btn{
  z-index: 1;
}
.ivu-modal .ivu-modal-content {
 width: 560px;
 top: 80px;
 border-radius: 0;
  .ivu-modal-close .ivu-icon-ios-close-empty{
     color: #fff;
     font-weight: 700;
     position: relative;
     top: -7px;
   }
 .ivu-modal-header{
   height: 32px;
   background-color: #2786d3;
  .ivu-modal-header-inner{
     color: #ffffff;
     font-size: 14px;
     margin-top:-7px;
   }
 }
 .ivu-modal-footer{
    display: none;
 }
}
</style>
