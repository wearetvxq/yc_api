<template>
    <div class="data">
        <Row>
            <Col span="7" class="data-left">
                <Form :label-width="120" :style="{marginLeft:'-20px'}">
                    <FormItem>
                        <p class="head">导入报表</p>
                    </FormItem>
                    <FormItem label="导入报表类型:" :style="{width:'180px'}">
                      <Select v-model="model1" clearable style="width:200px">
                          <Option v-for="item in typelist1" :value="item.value" :key="item.value">{{ item.label }}</Option>
                      </Select>
                    </FormItem>
                    <FormItem label="Excel表格上传:" :style="{width:'150px'}" id="myform">
                      <Upload
                         :before-upload="handleUpload"
                         action="`${this.URL_PREFIX}/upload/file`">
                         <Button type="ghost" icon="ios-cloud-upload-outline">点击选择本地文件</Button>
                     </Upload>
                     <div v-if="file !== null" class="filename">
                       <p> 文件名: {{ file.name }} </p>
                         <Button type="primary" size="default" @click="upload" :loading="loadingStatus">提交</Button>
                     </div>

                   </FormItem>
                </Form>
            </Col>
            <Col span="17" :style="{padding:'15px'}">
                <Form ref="formCustom">
                    <FormItem>
                        <Row>
                            <Col span="3">
                               <p class="tit">查找导入报表:</p>
                            </Col>
                            <Col span="8">
                                <FormItem label="起始时间:">
                                    <Col span="15">
                                          <DatePicker type="datetime" placeholder="请选择起始时间" :value="startTime" @on-change="handlechange"></DatePicker>
                                    </Col>
                                </FormItem>
                            </Col>
                            <Col span="8">
                                <FormItem label="截止时间:">
                                    <Col span="15">
                                          <DatePicker type="datetime" placeholder="请选择截止时间" :value="endTime" @on-change="handlechange1"></DatePicker>
                                    </Col>
                                </FormItem>
                            </Col>
                            <Col span="4" offset="1">
                                <Button type="ghost" icon="ios-search-strong"  :style="{backgroundColor:'#2786d3',color:'#fff'}" @click="Search">查找</Button>
                            </Col>
                        </Row>
                    </FormItem>
                </Form>
                <div>
                  <Row>
                      <Table stripe border :columns="columns1" :data="data1"></Table>
                  </Row>
                  <Row :style="{marginTop: '15px'}">
                      <Page :style="{float:'right'}" :total="dataCount" size="small" :pageSize="pageSize" show-total show-elevator @on-change="changepage"></Page>
                  </Row>
                </div>
            </Col>
        </Row>
          <Col class="demo-spin-col" span="8" v-show="loading">
            <Spin fix>
                <Icon type="load-c" size=18 class="demo-spin-icon-load"></Icon>
                <div>Loading</div>
            </Spin>
          </Col>
      <Modal v-model="modal2" width="360">
        <p slot="header" style="color:#f60;text-align:center" :style="{marginTop:'-5px'}">
            <Icon type="information-circled"></Icon>
            <span>提示</span>
        </p>
        <div style="text-align:center">
            <p>文件上传中,请勿进行其它操作</p>
            <p>该窗口会在上传完成后自动关闭,请等待</p>
        </div>
        <div slot="footer">
            <Button type="error" size="large">提示</Button>
        </div>
    </Modal>
    <Modal v-model="modal3" width="360">
      <p slot="header" style="color:#f60;text-align:center" :style="{marginTop:'-5px'}">
          <Icon type="information-circled"></Icon>
          <span>提示</span>
      </p>
      <div style="text-align:center">
          <p>文件生成中,请勿进行其它操作</p>
          <p>该窗口会在文件生成完成后自动关闭,请等待</p>
      </div>
      <div slot="footer">
          <Button type="error" size="large" >提示</Button>
      </div>
  </Modal>
    </div>
</template>
<script>
    export default {
        data() {
            return {
                modal2: false,
                modal3: false,
                loading:false,
                file: null,
                filepath:'',
                listpath:'',
                name:'',
                loadingStatus: false,
                ajaxHistoryData:[],
                pageSize:10,
                dataCount:0,
                startTime:'',
                endTime:'',
                columns1:[
                    {
                        title: '导入报表名称',
                        key: 'name',
                        align:'center'
                    },

                    {
                        title: '导入时间',
                        width: 250,
                        key: 'time',
                        align:'center'
                    },
                    {
                        title: '操作',
                        key: 'operating',
                        width: 200,
                        align:'center',
                        render: (h, params) => {
                            return h('div', [
                                h('Button', {
                                    props: {
                                        type: 'info',
                                        size: 'small'
                                    },
                                    style: {
                                        marginRight: '25px'
                                    },
                                    on: {
                                        click: () => {
                                            window.location.href=`http://${params.row.url}`
                                        }
                                    }
                                }, '下载'),
                                h('Button', {
                                    props: {
                                        type: 'error',
                                        size: 'small'
                                    },
                                    style: {
                                        marginRight: '5px'
                                    },
                                    on: {
                                        click: () => {
                                          console.log(params.row.id)
                                          this.$axios.delete(`${this.URL_PREFIX}/upload/delete?id=${params.row.id}`,{
                                             headers: { 'Content-Type': 'application/json' }
                                         }).then(res => {
                                           if(res.data.code == '0'){
                                                     setTimeout(() => {
                                                      this.Getimportlist()
                                                      this.$Message.success('删除成功')
                                                     },1500)
                                                 }else if(res.data.code == '10003'){
                                                   setTimeout(() => {
                                                     this.$Message.warning('删除的用户不存在')
                                                   },1500)
                                                 }else{
                                                   setTimeout(() => {
                                                    this.$Message.error('删除失败')
                                                   },1500)
                                                }
                                         }).catch(error => {
                                           console.log(error)
                                         })
                                        }
                                    }
                                }, '删除')
                            ]);
                        }
                    }
                ],
                data1: [],
                historyData: [],
                model1:'',
                model2:'',
                typelist1: [
                  { value:'家宽投诉列表类',label:'家宽投诉列表类'},
                  { value:'家宽新装/移机列表类',label:'家宽新装/移机列表类'},
                  { value:'回访不满意工单类',label:'回访不满意工单类'},
                  { value:'用户基础信息类',label:'用户基础信息类'}
                ]
            }
        },
        mounted() {
          this.Getimportlist()
        },
        methods: {
          Transform() {
             if(this.model1 == '家宽投诉列表类'){
               this.model1 = 1
             }else if (this.model1 == '家宽新装/移机列表类'){
               this.model1 = 2
             }else if (this.model1 == '回访不满意工单类'){
               this.model1 = 3
             }else {
              this.model1 = 4
             }
          },
          /*获取历史导入数据*/
          Getimportlist() {
             this.$axios.get(`${this.URL_PREFIX}/upload/filelist?starttime=${this.startTime}&endtime=${this.endTime}`)
                  .then(res => {
                    if(res.data.code = '0'){
                      this.data1 = res.data.result
                      this.ajaxHistoryData = this.data1
                      this.dataCount = res.data.result.length
                      this.handleListApproveHistory()
                    }
                  })
                  .catch(error => {
                    console.log(error)
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
                var _start = ( index - 1 ) * this.pageSize;
                var _end = index * this.pageSize;
                this.data1 = this.ajaxHistoryData.slice(_start,_end);
            },
            importfile() {
              var formData = new FormData(document.getElementById('#myForm'));
              formData.append("files",this.file);
              //添加请求头
              let config = {
                headers: { 'Content-Type': 'multipart/form-data' }
               };
              this.$axios.post(`${this.URL_PREFIX}/upload/file`,formData,config).then( res => {
                if(res.data.code == '0'){
                  this.loadingStatus = false;
                  this.filepath = res.data.msg;
                  setTimeout(() => {
                          this.modal2 = false
                  },2000)
                }
              }).catch(error => {
                console.log(error)
              })
            },
            /*发送本地上传file*/
            handleUpload (file) {
                this.file = file;
                this.name = file.name
                setTimeout(()=> {
                  this.modal2 = true
                },1000)
                this.importfile();
                return false;
            },
            /*upload file*/
            UpFile() {
              this.Transform()
              this.$axios.post(`${this.URL_PREFIX}/upload`,{
                name:this.name,
                type:this.model1,
                url:this.filepath
              }).then(res => {
                  if(res.data.code == '0'){
                    this.modal3 = false
                    //this.listpath = res.data.msg
                    this.$Message.success('文件上传成功')
                    setTimeout(() => {
                         this.Getimportlist()
                    },1500)

                   } else{
                    this.modal3 = false
                    this.$Message.warning('文件上传失败')
                    }
              }).catch( error => {
                console.log(error)
              })
            },
            /*文件上传*/
            upload() {
              if(this.model1 ==''||this.model1 == null){
                setTimeout(() => {
                     this.$Message.warning({content:'上传报表类型不能为空',duraction:3})
                     this.loadingStatus = false
                },1500)
              }else{
                setTimeout(() => {
                  this.modal3 = true
                  this.file=null
                },1000)
                setTimeout(() => {
                  this.UpFile()
                },2000)
              }
              this.loadingStatus = true;

            },

            /*
              查找功能
            */
            Search() {
                // this.loading = true
                 this.$axios.get(`${this.URL_PREFIX}/upload/filelist?starttime=${this.startTime}&endtime=${this.endTime}`)
                     .then( res=> {
                       if(res.data.code == '0'){
                         //console.log(res)
                         //console.log(res.data.result)
                         if(res.data.result.length == 0){
                          setTimeout(() => {
                            this.loading = false
                            this.$Message.warning('未搜索到匹配信息,请重试!')
                            this.data1 = ''
                          },1500)
                        }else {
                           setTimeout(() => {
                             this.loading = false
                             this.data1 = res.data.result
                             this.dataCount = res.data.result.length
                             this.ajaxHistoryData = this.data1
                             this.handleListApproveHistory()
                           },1500)
                        }
                      }
                    }).catch( error => {
                      console.log(error)
                    })
            },
            handlechange(datetime){
            this.startTime = datetime
            },
            handlechange1(datetime){
              this.endTime = datetime
            },
        }
    }
</script>
<style lang="scss" scoped>
    .data,.ivu-row{
        height: 100%;
    }
    .data .data-left{
        height: 100%;
        padding: 15px;
        border-right: 1px solid #e5e9ee;
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
    .head{
      margin-left: -87px;
      font-size: 14px;
      font-weight: 700;
    }
    .filename{
      width: 400px;
      height: 60px;
      margin-top: 10px;
      padding: 0 5px;
    }
    .tit{
       color:#101010;
       font-size: 13px;
    }
</style>
