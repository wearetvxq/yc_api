<template lang="html">
      <div class="workstation">
           <Row>
                <h3 class="info">工作站装维人员终端进销存统计表</h3>
                <Form :style="{marginTop:'20px',marginLeft:'15px'}">
                   <FormItem>
                      <Row>
                          <Col span='20'>
                              <Row>
                                <Row>
                                  <Col span='6'>
                                    <FormItem label="起始时间:">
                                            <DatePicker type="datetime" placeholder="请选择" :value="starttime" @on-change="handlechanges" style="width:138px"></DatePicker>
                                    </FormItem>
                                  </Col>
                                  <Col span='6'>
                                    <FormItem label="截止时间:">
                                            <DatePicker type="datetime" placeholder="请选择" :value="endtime" @on-change="handlechanges1" style="width:138px"></DatePicker>
                                    </FormItem>
                                  </Col>
                                  <Col span='6'>
                                    <FormItem label="工作站:">
                                      <Select v-model="station" style="width:130px" clearable>
                                          <Option v-for="item in stationList" :value="item.value" :key="item.value">{{ item.value }}</Option>
                                      </Select>
                                    </FormItem>
                                  </Col>
                                  <Col span='6'>
                                      <FormItem label="终端类型:">
                                        <Select v-model="type" style="width:130px" clearable>
                                            <Option v-for="item in modeList" :value="item.value" :key="item.value">{{ item.value }}</Option>
                                        </Select>
                                      </FormItem>
                                  </Col>

                                </Row>
                              </Row>
                              <Row :style="{marginTop:'38px'}">
                                <Row :style="{marginTop:'-15px'}">
                                  <Col span="6" :style="{marginRight:'24px'}">
                                    <FormItem label="生产厂家:">
                                      <Select v-model="mode" style="width:138px" clearable>
                                          <Option v-for="item in typeList" :value="item.value" :key="item.value">{{ item.value }}</Option>
                                      </Select>
                                    </FormItem>
                                  </Col>
                                  <Col span='6'>
                                    <FormItem label="装维人员:" :style="{marginLeft:'-24px'}">
                                          <Input v-model="installer" placeholder="请输入装维人员姓名" style="width:138px" clearable></Input>
                                    </FormItem>
                                  </Col>
                                  <Col span='6'>
                                    <FormItem label="模糊查找:" :style="{marginLeft:'-32px'}">
                                        <Input v-model="keyword" placeholder="请输入关键词查找" style="width:130px" clearable></Input>
                                    </FormItem>
                                  </Col>
                                </Row>
                              </Row>
                          </Col>
                          <Col span="4">
                            <Row type="flex" justify="end" :style="{marginRight:'30px',marginTop:'28px'}">
                               <Button type="success" icon="ios-search-strong" :style="{color:'#edf6fb',marginRight:'10px'}" @click="Search" class="btn">查找</Button>
                               <Button type="ghost" icon="ios-cloud-upload-outline" :style="{backgroundColor:'#2786d3',color:'#edf6fb'}" @click="Expor" :loading="loading1" class="btn">导出</Button>
                            </Row>
                          </Col>
                      </Row>
                   </FormItem>
                </Form>
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
      </div>
</template>

<script>
export default {
   data(){
     return{
       mode:'',
       type:'',
       loading:false,
       loading1:false,
       dataCount:10,
       pageSize:10,
       starttime:'',
       endtime:'',
       keyword:'',
       installer:'',
       station:'',
       stationList:[],
       modeList:[
           {name:'光猫',value:'光猫'},
           {name:'智能网关',value:'智能网关'}
       ],
       typeList:[
         {name:'中兴',value:'中兴'},
         {name:'华为',value:'华为'},
         {name:'贝尔',value:'贝尔'},
         {name:'杭研',value:'杭研'}
       ],
       data1:[

       ],
       columns1:[
         {
             title: '工作站',
             key: 'work',
             align:'center'
         },
         {
             title: '装维人员',
             key: 'people',
             align:'center'
         },
         {
           title:'终端类型',
           key: 'type',
           align:'center'
         },
         {
             title: '厂家',
             key: 'produce',
             align:'center'
         },
         {
             title: '型号',
             key: 'model',
             align:'center'
         },
         {
             title: '上期储存',
             key: 'last',
             align:'center'
         },
         {
             title: '本期中领数量',
             key: 'now',
             align:'center'
         },
         {
             title: '装机使用数量',
             key: 'use',
             align:'center'
         },
         {
             title: '维护使用数量',
             key: 'maintain',
             align:'center'
         },
         {
             title: '结余好件数量',
             key: 'good',
             align:'center'
         },
         {
             title: '结余坏件数量',
             key: 'bad',
             align:'center'
         }
       ]
     }
   },
   created(){
          this.$nextTick(function () {
             //this.getDataList()
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
     getDataList(){
          this.$axios.get(`http://127.0.0.1:81/v1/supplies/statistics/install?page=1&size=${this.pageSize}&starttime=${this.starttime}&endtime=${this.endtime}&work=${this.station}&type=${this.type}&modle=${this.mode}&workman=${this.installer}&keyword=${this.keyword}`).then( res => {
              if(res.data.code == '0'){
                   this.data1 = res.data.result
                   this.ajaxHistoryData = this.data1
                   this.dataCount =res.data.result.length
                   this.handleListApproveHistory()
                   this.$Spin.hide()
               }
             }).catch(error => {
               console.log(error)
               this.$Spin.hide()
              })
     },
     Search(){
       this.loading = true
       this.$axios.get(`http://127.0.0.1:81/v1/supplies/statistics/install?page=1&size=${this.pageSize}&starttime=${this.starttime}&endtime=${this.endtime}&work=${this.station}&type=${this.type}&modle=${this.mode}&workman=${this.installer}&keyword=${this.keyword}`)
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
                         setTimeout(() => {
                           this.data1 = res.data.result
                           this.dataCount = res.data.result.length
                           this.ajaxHistoryData = this.data1
                           this.handleListApproveHistory()
                           this.loading = false
                         },1500)
                       }
               }else {
                 this.$Message.warning('未搜索到匹配信息,请重试!')
                 this.dataCount = 0
                 this.data1 = []
                 setTimeout(() => {
                   this.loading = false
                 },1000)
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
       this.$axios.get(`http://127.0.0.1:81/v1/supplies/statistics/install/export?page=1&size=${this.pageSize}&starttime=${this.starttime}&endtime=${this.endtime}&work=${this.station}&type=${this.type}&modle=${this.mode}&workman=${this.installer}&keyword=${this.keyword}`).then( res => {
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
     handlechanges(datetime){
        this.starttime = datetime
      },
     handlechanges1(datetime){
         this.endtime = datetime
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
       }
   }
}
</script>

<style lang="scss" scoped>
   .workstation .info{
       margin-top: 15px;
       margin-left: 15px;
   }
</style>
