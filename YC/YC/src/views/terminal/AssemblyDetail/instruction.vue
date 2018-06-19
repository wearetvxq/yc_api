<template lang="html">
      <div class="instruction">
           <Row>
             <Row :style="{marginLeft:'15px'}">
                    <h3>装机使用表格下载/数据导入</h3>
                    <Col span="8">
                      <Form :label-width="120" :style="{marginLeft:'-44px',marginTop:'30px'}">
                          <FormItem label="报表模板:" :style="{width:'200px'}" id="myform">
                             <Button type="ghost" icon="ios-cloud-download-outline" @click="downlaod">点击下载</Button>
                         </FormItem>
                      </Form>
                    </Col>
                    <Col span="16" class="data-left">
                      <Form :label-width="120" :style="{marginLeft:'-146px',marginTop:'30px'}">
                          <FormItem label="表格导入:" :style="{width:'200px'}" id="myform"  v-if="file == null">
                            <Upload
                               :before-upload="handleUpload"
                               action="`${this.URL_PREFIX}/supplies/use/upload`">
                               <Button type="ghost" icon="ios-cloud-upload-outline">点击选择本地文件</Button>
                           </Upload>
                         </FormItem>
                         <div v-if="file !== null" class="filename" :style="{display:'inline-block',marginTop:'1px'}">
                           <p :style="{display:'inline-block'}"> 文件名: {{ file.name }} </p>
                           <Button type="error" size="default" @click="upload" :loading="loadingStatus" :style="{display:'inline-block',marginLeft:'15px'}">导入</Button>
                         </div>
                      </Form>
                    </Col>
             </Row>
              <Row>
                  <div :style="{marginLeft:'15px'}">
                    <h3>装机使用明细表</h3>

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
                              <FormItem label="工作站:" :style="{marginLeft:'-30px'}">
                                <Select v-model="station" style="width:180px" clearable>
                                    <Option v-for="item in stationList" :value="item.value" :key="item.value">{{ item.value }}</Option>
                                </Select>
                              </FormItem>
                            </Col>
                          </Row>
                          <Row type="flex" justify="end" :style="{marginRight:'70px',marginTop:'5px'}">
                             <Button type="success" icon="ios-search-strong" :style="{color:'#edf6fb',marginRight:'10px'}" @click="Search">查找</Button>
                             <Button type="ghost" icon="ios-cloud-upload-outline" :style="{backgroundColor:'#2786d3',color:'#edf6fb'}" :loading="loading1" @click="Expor">导出</Button>
                          </Row>
                          <Row :style="{marginTop:'-15px'}">
                            <Col span='6'>
                              <FormItem label="业务类型:">
                                <Select v-model="mode" style="width:180px" clearable>
                                    <Option v-for="item in modeList" :value="item.value" :key="item.value">{{ item.value }}</Option>
                                </Select>
                              </FormItem>
                            </Col>
                            <Col span='7'>
                              <FormItem label="模糊查找:" >
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
                    <Row :style="{marginTop: '15px',marginBottom:'30px'}">
                        <Page :style="{float:'right'}" :total='dataCount' size="small" :page-size="pageSize" show-total show-elevator @on-change="changepage"></Page>
                    </Row>
                  </div>
              </Row>
           </Row>
           <Modal v-model="modal2" width="360">
             <p slot="header" style="color:#f60;text-align:center" :style="{marginTop:'-5px'}">
                 <Icon type="information-circled"></Icon>
                 <span :style="{marginTop:'8px'}">提示</span>
             </p>
             <div style="text-align:center">
                 <p>文件上传中,请勿进行其它操作</p>
                 <p>该窗口会在上传完成后自动关闭,请等待</p>
             </div>
             <div slot="footer">
                 <Button type="error" size="large">提示</Button>
             </div>
          </Modal>
           <Modal v-model="showinfo"
           :title="title"
           width="560">
              <div slot="header">
                  <Select  size="small"  @on-change="handleChange" v-model="modes"  style="width:170px" :style="{marginTop:'-14px',marginLeft:'-5px'}">
                      <Option v-for="item in lists" :value="item.value" :key="item.value">{{ item.value }}</Option>
                  </Select>
                  <span class="tit">终端状态信息</span>
              </div>
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

      </div>
</template>

<script>
export default {
     data(){
       return {
           id:null,
           modal2:false,
           isModalVisible:false,
           loading:false,
           loading1:false,
           loadingStatus:false,
           showinfo:false,
           mode:'',
           modes:'',
           title:'',
           keyword:'',
           file:null,
           filepath:'',
           starttime:'',
           endtime:'',
           dataCount:10,
           pageSize:10,
           currentpage:1,
           station:'',
           infos:[],
           lists:[],
           stationList:[],
           modeList:[
               {name:'宽带单独安装',value:'宽带单独安装'},
               {name:'N业务加装',value:'N业务加装'},
               {name:'宽带+N业务同时报装',value:'宽带+N业务同时报装'},
               {name:'正常装机',value:'正常装机'},
               {name:'B改H装机',value:'B改H装机'}
           ],
           typeList:[],
           lists:[],
           data1:[],
           columns1:[
             {
                 title: '工作站',
                 key: 'work',
                 width:100,
                 align:'center'
             },
             {
                 title: '业务类型',
                 key: 'business',
                 width:100,
                 align:'center'
             },
             {
                 title: '装机工单业务账号',
                 key: 'order',
                 align:'center'
             },
             {
                 title: '光猫条码',
                 key: 'modem',
                 align:'center'
             },
             {
                 title: '智能网关条码',
                 key: 'gateway',
                 align:'center'
             },
             {
                 title: '机顶盒条码',
                 key: 'box',
                 align:'center'
             },
             {
                 title: '和目条码',
                 key: 'hemu',
                 align:'center'
             },
             {
                 title: '固话(移动产权)条码',
                 key: 'phone',
                 width:145,
                 align:'center'
             },
             {
                 title: '装维人员',
                 key: 'principal',
                 width:100,
                 align:'center'
             },
             {
                 title: '装机使用时间',
                 key: 'posttime',
                 align:'center'
             },
             {
                 title: '终端状态',
                 key: 'operating',
                 width: 120,
                 align:'center',
                 render: (h, params) => {
                     return h('div', [
                         h('a', {
                             style: {
                                 color:'#258ee9',

                             },
                             on: {
                                 click: () => {
                                   setTimeout(() => {
                                      this.showinfo = true
                                   },500)
                                   this.lists = []
                                   this.id = params.row.id
                                   this.$axios.get(`${this.URL_PREFIX}/supplies/use/code/${params.row.id}`)
                                              .then(res => {
                                                if(res.data.code == '0'){
                                                  let code = res.data.result[0].code
                                                   for (let item of res.data.result){
                                                     let all = ''
                                                     all = item.type+','  +item.model
                                                     this.lists.push({name:all,value:all})
                                                  }
                                                  this.modes = this.lists[0].value

                                                }
                                              })
                                              .catch(error => {
                                                  console.log(error)
                                              })

                             }
                          }
                         }, '查看'),
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
       getDataList() {
         this.$axios.get(`${this.URL_PREFIX}/supplies/use?page=1&size=${this.pageSize}`).then( res => {
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
         this.$axios.get(`${this.URL_PREFIX}/supplies/use?page=1&size=${this.pageSize}&starttime=${this.starttime}&endtime=${this.endtime}&work=${this.station}&type=${this.mode}&model=${this.type}&keyword=${this.keyword}`)
               .then(res => {
                 if(res.data.code == '0'){
                   if(res.data.result.length == 0){
                           this.data1 = []
                           this.dataCount = 0
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
                     this.data1 = []
                     this.dataCount = 0
                   },1500)
                 }
               })
               .catch(error => {
                 setTimeout(() => {
                   this.loading = false
                   this.$Message.warning('未搜索到匹配信息,请重试!')
                   this.data1 = []
                   this.dataCount = 0
                 },1500)
                 console.log(error)
               })
       },
       Expor(){
         this.loading1 = true
         this.$axios.get(`${this.URL_PREFIX}/supplies/use/export?starttime=${this.starttime}&endtime=${this.endtime}&work=${this.station}&type=${this.mode}&model=${this.type}&keyword=${this.keyword}`).then( res => {
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
        /*发送本地上传file*/
       handleUpload (file) {
           this.file = file;
           this.name = file.name

           //this.upload();
           return false;
       },
       upload() {
         this.modal2 = true
         var formData = new FormData(document.getElementById('#myForm'));
         formData.append("files",this.file);
         //添加请求头
         let config = {
           headers: { 'Content-Type': 'multipart/form-data' }
          };
         this.$axios.post(`${this.URL_PREFIX}/supplies/use/upload`,formData,config).then( res => {
           if(res.data.code == '0'){
             setTimeout(() => {
               this.$Message.success('导入成功!')
             },2000)
            setTimeout(() => {
              this.modal2 = false
              this.file = null
            },1000)
           }else if (res.data.code == '10003'){
             setTimeout(() => {
                     this.modal2 = false
                     this.file = null
                     this.$Message.success('上传文件已存在!')
             },1500)
           }
         }).catch(error => {
           console.log(error)
           setTimeout(() => {
                   this.modal2 = false
                   this.file = null
                   this.$Message.success('上传失败!')
           },1500)
         })
       },
       /*
        模板下载
       */
       downlaod() {
          setTimeout(() => {
              window.location.href='http://127.0.0.1:86/zj_model.xlsx    '
              this.$Message.success('下载成功')
          },1000)
       },
       handleChange(value){
          let Selects = []
          for(let items of this.lists){
            Selects.push(items.name)
          }
           let index = Selects.indexOf(value)
           this.infos = []
           this.$axios.get(`${this.URL_PREFIX}/supplies/use/code/${this.id}`)
                      .then(res => {
                        if(res.data.code == '0'){
                           let code = res.data.result[index].code

                             this.$axios.get(`${this.URL_PREFIX}/supplies/query/${code}`)
                                        .then(res => {
                                          if(res.data.code == '0'){
                                            this.infos = res.data.result[0].info
                                          }
                                        })


                        }
                      })

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
               this.$axios.get(`${this.URL_PREFIX}/supplies/use?page=${this.currentpage}&size=${this.pageSize}`).then( res => {
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
.filename{
  width: 400px;
  height: 60px;
  margin-top: 10px;
  padding: 0 5px;
}
.tit{
  position: relative;
  top: -4px;
  left: 60px;
  color:#fff;
  font-size: 14px;
  font-weight: 700;
}
</style>
