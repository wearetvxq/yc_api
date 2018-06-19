<template lang="html">
      <div class="repair">
              <Row :style="{marginLeft:'15px'}">
                     <h3>返修表格导入</h3>
                     <Col span="20" class="data-left">
                       <Form :label-width="120" :style="{marginLeft:'-55px',marginTop:'30px'}">
                           <FormItem label="表格导入:" :style="{width:'200px'}" id="myform"  v-if="file == null">
                             <Upload
                                :before-upload="handleUpload"
                                action="`${this.URL_PREFIX}/supplies/waste/upload?type=2`">
                                <Button type="ghost" icon="ios-cloud-upload-outline">点击选择本地文件</Button>
                            </Upload>
                          </FormItem>
                          <div v-if="file !== null" class="filename" :style="{display:'inline-block',marginTop:'1px',marginLeft:'50px'}">
                            <p :style="{display:'inline-block'}"> 文件名: {{ file.name }} </p>
                            <Button type="error" size="default" @click="upload" :loading="loadingStatus" :style="{display:'inline-block',marginLeft:'15px'}">导入</Button>
                          </div>
                       </Form>
                     </Col>
              </Row>
              <Row>
                  <div :style="{marginLeft:'15px'}">
                    <h3>返修明细表</h3>
                    <Form :style="{marginTop:'20px'}">
                       <FormItem>
                          <Row>
                            <Col span='5'>
                              <FormItem label="起始时间:">
                                      <DatePicker type="datetime" placeholder="请选择" :value="starttime" @on-change="handlechange"></DatePicker>
                              </FormItem>
                            </Col>
                            <Col span='5'>
                              <FormItem label="截止时间:">
                                      <DatePicker type="datetime" placeholder="请选择" :value="endtime" @on-change="handlechange1"></DatePicker>
                              </FormItem>
                            </Col>
                            <Col span='5'>
                              <FormItem label="工作站:">
                                <Select v-model="station" style="width:180px" clearable>
                                    <Option v-for="item in stationList" :value="item.value" :key="item.value">{{ item.value }}</Option>
                                </Select>
                              </FormItem>
                            </Col>
                            <Col span='5'>
                              <FormItem label="模糊查找:">
                                  <Input v-model="keyword" placeholder="请输入关键词进行查找" style="width:180px" clearable></Input>
                              </FormItem>
                            </Col>
                            <Col span="4" class="btn">
                               <Button type="success" icon="ios-search-strong" :style="{color:'#edf6fb'}" @click="Search">查找</Button>
                               <Button type="ghost" icon="ios-cloud-upload-outline" :loading="loading1" @click="Expor" :style="{backgroundColor:'#2786d3',color:'#edf6fb'}" >导出</Button>
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
           loading:false,
           loading1:false,
           loadingStatus:false,
           showinfo:false,
           modal2:false,
           mode:'',
           title:'',
           file: null,
           keyword:'',
           starttime:'',
           endtime:'',
           dataCount:0,
           pageSize:10,
           currentpage:1,
           station:'',
           infos:[],
           stationList:[],
           modeList:[
             {name:'和TV机顶盒,TL-Ep110',value:'和TV机顶盒，TL-Ep110'},
             {name:'光猫,Tl-EP123',value:'光猫,Tl-EP123'},
             {name:'智能网关,Tl-EP000',value:'智能网关,Tl-EP000'},
             {name:'和目,Tl-EP111',value:'和目,Tl-EP111'},
             {name:'固话(移动产权),Tl-EP222',value:'固话(移动产权),Tl-EP222'}
           ],
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
                 title: '返修条形码',
                 key: 'code',
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
                 title: '返修时间',
                 key: 'posttime',
                 align:'center'
             },
             {
                 title: '终端状态',
                 key: 'operating',
                 width: 200,
                 align:'center',
                 render: (h, params) => {
                     return h('div', [
                         h('a', {
                             style: {
                                 color:'#258ee9',

                             },
                             on: {
                                 click: () => {
                                   this.infos = []
                                   this.$axios.get(`${this.URL_PREFIX}/supplies/query/${params.row.code}`)
                                                    .then(res => {
                                                      if(res.data.code == '0'){
                                                        let type = res.data.result[0].type
                                                        let model = res.data.result[0].model
                                                        this.title = `(${type+','+model})`
                                                        this.infos = res.data.result[0].info
                                                      }else{

                                                      }
                                                    }).catch(error => {
                                                        console.log(error)
                                                    })

                                                    setTimeout(() => {
                                                        this.showinfo = true
                                                    },800)
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
                        console.log(this.stationList)
                    })
                    .catch(error => {
                      console.log(error)
                    })
       },
       getDataList() {
         this.$axios.get(`${this.URL_PREFIX}/supplies/waste?page=1&size=${this.pageSize}&type=2`).then( res => {
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
       /*
          搜索
       */
       Search(){
         this.loading = true
         this.$axios.get(`${this.URL_PREFIX}/supplies/waste?page=1&size=${this.pageSize}&type=2&starttime=${this.starttime}&endtime=${this.endtime}&work=${this.station}&keyword=${this.keyword}`)
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
       /*
        导出
       */
       Expor(){
         this.loading1 = true
         this.$axios.get(`${this.URL_PREFIX}/supplies/waste/export?type=2&starttime=${this.starttime}&endtime=${this.endtime}&work=${this.station}&keyword=${this.keyword}`).then( res => {
             if(res.data.code == '0'){
               setTimeout(() => {
                 this.loading1 = false
                 this.$Message.success('导出成功')
                 //打开文件下载链接
                 window.location.href=`http://${res.data.url}`
               },1500)
              }
            }).catch(error => {
              this.loading1 = false
              setTimeout(() => {
                  this.$Message.error('导出失败')
              },1500)
              console.log(error)
             })
       },
       /*发送本地上传file*/
       handleUpload (file) {
           this.file = file;
           this.name = file.name
           return false;
       },
       /*
        上传接口
       */
       upload(){
         this.modal2 = true
         var formData = new FormData(document.getElementById('#myForm'));
         formData.append("files",this.file);
         //添加请求头
         let config = {
           headers: { 'Content-Type': 'multipart/form-data' }
          };
         this.$axios.post(`${this.URL_PREFIX}/supplies/waste/upload?type=2`,formData,config).then( res => {
           if(res.data.code == '0'){
             setTimeout(() => {
               this.$Message.success('导入成功!')
             },2000)
            setTimeout(() => {
              this.modal2 = false
              this.file = null
            },1000)
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
          分页处理
       */
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
               this.$axios.get(`${this.URL_PREFIX}/supplies/waste?page=${this.currentpage}&size=${this.pageSize}&type=2`).then( res => {
                   if(res.data.code == '0'){
                        this.data1 = res.data.result
                        this.loading = false
                    }
                  }).catch(error => {
                    console.log(error)
                   })
          },
       handlechange(datetime){
          this.starttime = datetime
        },
       handlechange1(datetime){
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
</style>
