<template lang="html">
     <div class="twentyfour">
       <Row>
         <Row>
             <h3>家宽高频投诉小区通报</h3>
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
                               <Radio label="高频小区"></Radio>
                           </RadioGroup>
                       </FormItem>
                   </Row>
                </FormItem>
             </Form>
         </Row>
         <Row :style="{marginBottom:'50px'}">
            <div class="linelist">
                <!-- <span>{{this.category}}</span> -->
                <Row>
                    <Col span="12">
                      <div class="map">
                        <baidu-map :center="center" :zoom="zoom"  @ready="handler" class="bm_view">
                          <bm-navigation anchor="BMAP_ANCHOR_TOP_RIGHT"></bm-navigation>
                          <bm-marker  v-for="(item,index) in this.master" :position="item[0]" :dragging="true" @click="clickHandler">
                          </bm-marker>
                        </baidu-map>
                      </div>
                    </Col>
                    <Col span="12">
                      <div class="area" v-if="this.barData.length>0">
                        <!-- <p :style="{marginLeft:'15px'}">高频小区详情</p> -->
                        <bar-area :barData="this.barData" :starttime="this.starttimes" :endtime="this.endtimes" :types="this.model1" :lngs="this.lngs" :lats="this.lats"></bar-area>
                      </div>
                    </Col>
                </Row>
            </div>
         </Row>
         <Row class="table">
           <Form ref="formCustom" :style="{marginTop:'80px'}">
               <FormItem>
                   <Row >
                       <Col span="4">
                           <FormItem label="起始时间:">
                               <Col span="13">
                                   <DatePicker type="datetime" placeholder="请选择" :value="starttimes" @on-change="handlechanges"></DatePicker>
                               </Col>

                           </FormItem>
                       </Col>
                       <Col span="4">
                           <FormItem label="截止时间:">
                               <Col span="13">
                                   <DatePicker type="datetime" placeholder="请选择" :value="endtimes" @on-change="handlechanges1"></DatePicker>
                               </Col>
                           </FormItem>
                       </Col>
                       <Col span="4">
                           <FormItem label="地区">
                             <Col span="12">
                               <Select v-model="cityarea" style="width:110px" clearable>
                                   <Option placeholder="请选择" v-for="item in arealist" :value="item.value" :key="item.value">{{ item.label }}</Option>
                               </Select>
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
                            <Button :loading='loading1' type="ghost" icon="ios-cloud-upload-outline" :style="{backgroundColor:'#2786d3',color:'#edf6fb'}" @click="Expor">导出</Button>
                      </Col>
                   </Row>
               </FormItem>
           </Form>
           <div :style="{marginTop: '40px'}">
             <Row>
                 <Table :columns="columns1" :data="datas" border ></Table>
             </Row>
             <Row :style="{marginTop: '30px'}">
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
import barArea from '../components/bar_area.vue'
import {BmMarker} from 'vue-baidu-map'
export default {
  components:{
    BmMarker:'bm-marker'
  },
  data () {
      return {
          center: {lng: 0, lat: 0},
          Obj:{lng:'',lat:''},
          lngs:'',
          lats:'',
          zoom: 3,
          datas:[],
          master:[],
          cityarea:'',
          category:'高频小区',
          Types:'',
          loadings: false,
          loading1:false,
          barData:[],
          barData1:[],
          ajaxHistoryData:[],
          pageSize:11,
          dataCount:0,
          data3:[],
          data4:[],
          starttime:'',
          endtime:'',
          starttimes:'',
          endtimes:'',
          communitys:{},
          Obj:{},
          city:[],
          All:'',
          options:['投诉工单量'],
          options1:[],
          options3:[],
          typelist1:[
            { value:'EMOS',label:'EMOS'},
            { value:'微信一键报障',label:'微信一键报障'}
          ],
          arealist:[
            {label:'秭归',value:'秭归'},
            {label:'枝江',value:'枝江'},
            {label:'长阳',value:'长阳'},
            {label:'远安',value:'远安'},
            {label:'宜都',value:'宜都'},
            {label:'夷陵',value:'夷陵'},
            {label:'兴山',value:'兴山'},
            {label:'五峰',value:'五峰'},
            {label:'开发区',value:'开发区'},
            {label:'当阳',value:'当阳'},
            {label:'城区',value:'城区'}
          ],
          model1:'EMOS',
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
                  key:'area',
                  width: 150,
                  align:'center'
                  // filters:[
                  //   {label:'秭归',value:'秭归'},
                  //   {label:'枝江',value:'枝江'},
                  //   {label:'长阳',value:'长阳'},
                  //   {label:'远安',value:'远安'},
                  //   {label:'宜都',value:'宜都'},
                  //   {label:'夷陵',value:'夷陵'},
                  //   {label:'兴山',value:'兴山'},
                  //   {label:'五峰',value:'五峰'},
                  //   {label:'开发区',value:'开发区'},
                  //   {label:'当阳',value:'当阳'},
                  //   {label:'城区',value:'城区'}
                  // ],
                  //filterMultiple: false,
                  // filterRemote(value){
                  //   if(value === '枝江'){
                  //     let list = this.filters.map(item => {
                  //       return {
                  //         value: item,
                  //         label:item
                  //       };
                  //       this.datas = list.filter(item => item.label.indexOf(value) > -1)
                  //     })
                  //   }
                  // }
                  // filterMethod(value,row) {
                  //   return row.area.indexOf(value)>-1
                  // }
              },
              {
                  title: '高频小区名',
                  key:'community',
                  align:'center'
                  // render: (h, params) => {
                  // //  return h('div', [
                  //       return  h('Select', {
                  //                   props:{
                  //                       placeholder:'请选择',
                  //                       clearable: true
                  //                   },
                  //                   style: {
                  //                       width:'400px',
                  //                       height:'32px',
                  //                       display: 'inline-block',
                  //                       borderRadius:'20px',
                  //                       marginRight:'15px'
                  //                   },
                  //                   on: {
                  //                       'on-change':(event) => {
                  //                             this.data4[params.index].value= event;
                  //                       }
                  //
                  //                   },
                  //               },
                  //               this.options1.map(function(option){
                  //
                  //                     // return h('Option', {
                  //                     //     props: {value: item}
                  //                     // }, option);
                  //
                  //               })
                  //
                  //
                  //
                  //           )
                     //]);
                //  }
              },
              {
                  title: '投诉工单量',
                  key:'total',
                  width:200,
                  align:'center'
              },
              {
                  title: '详单',
                  key: 'operating',
                  width:250,
                  align:'center',
                  render: (h, params) => {
                      return h('div', [
                          h('Select', {
                                    props:{
                                        placeholder:'请选择',
                                        clearable: true,
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
                                    //let area = params.row.area
                                    let time = this.starttimes
                                    let time2 = this.endtimes
                                    let category = this.model1
                                    let types = this.data3[params.index].value
                                    let types1 = params.row.community
                                    this.All = time+'_'+time2+'_'+types1+'_'+category+'_'+types
                                    if(Number.isInteger(this.data3[params.index].value)){
                                       this.$Message.error('请选择导出报表类型')
                                    }else{
                                      this.$axios.get(`${this.URL_PREFIX}/complain/high/info/export?type=${this.All}`)
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
          datas: [],
          historyData: []
      }
  },
  created (){
    //  this.handleSpinCustom()
  },
  mounted (){
      // this.getDatalist()
      // this.Mapdata()
      // this.getBar()
      this.handleSpinCustom()
      this.Mapdata()
      this.getBar()
  },
  methods: {
    /*
      map地图函数
    */
    handler ({BMap, map}) {
      this.center.lng = 111.28
      this.center.lat = 30.70
      this.zoom = 10
    },
    /*
      点击地图点 联动Echart表
    */
    clickHandler(e){
    //  alert(`单击点的坐标为：${e.point.lng}, ${e.point.lat}`);
      this.barData = []
      this.$axios.get(`${this.URL_PREFIX}/complain/high/column?lat=${e.point.lng}_${this.starttime}_${this.starttime}_${this.model1}&lon=${e.point.lat}`)
      .then(res => {
         if(res.data.code == '0'){
            this.barData = res.data.result
         }
      })
    },
    getBar(){
      this.$axios.get(`${this.URL_PREFIX}/complain/high/column?lat=${this.lngs}_${this.starttime}_${this.starttime}_${this.model1}&lon=${this.lats}`)
      .then(res => {
         if(res.data.code == '0'){
            this.barData = res.data.result
         }
      })
    },
    /*
      Map数据接口
    */
    Mapdata() {
      this.$axios.get(`${this.URL_PREFIX}/complain/high/chart?starttime=${this.starttimes}&endtime=${this.endtimes}&type=${this.model1}`)
            .then(res => {
              if(res.data.code == '0'){
                this.datas = res.data.result
                for(let item of this.datas){
                  let obj = {lng:'',lat:''}
                  let Rank = {rank:''}
                  obj.lng = item.geo[0]
                  obj.lat = item.geo[1]
                  Rank.rank= item.rank
                  let objs = []
                  objs.push(obj)
                  objs.push(Rank)
                  this.master.push(objs)
                }
              }
            })
            .catch(error => {
              console.log(error)
            })
    },
    /*获取数据列表*/
    getDatalist(){
      this.Types = this.cityarea+'_'+this.model1
      this.$axios.get(`${this.URL_PREFIX}/complain/high/list?starttime=${this.starttimes}&endtime=${this.endtimes}&type=${this.Types}`)
            .then(res => {
              if(res.data.code == '0'){
                   this.datas = res.data.result
                   this.dataCount = res.data.result.length
                   this.ajaxHistoryData = this.datas
                   this.handleListApproveHistory()
                   // for(let item of res.data.result){
                   //   //for(let items of item.community){
                   //     this.options1.push(item.community)
                   //   //}
                   // }
                  //console.log(this.options1)

                let len = this.datas.length
                for(let i=0;i<len; i++){
                  this.data3.push({'value': i })
                  this.data4.push({'value': i })
                }

              }
            })
            .catch(error => {
              console.log(error)
            })
    },

    Search() {
      this.loadings = true
      //alert(this.cityarea)
      this.Types = this.cityarea+'_'+this.model1
      this.$axios.get(`${this.URL_PREFIX}/complain/high/list?starttime=${this.starttimes}&endtime=${this.endtimes}&type=${this.Types}`)
            .then(res => {
              if(res.data.code == '0'){
                this.loadings = false
                if(res.data.result.length == 0){
                        setTimeout(() => {
                          this.loadings = false
                          this.$Message.warning('未搜索到匹配信息,请重试!')
                          this.datas = ''
                        },1500)
                      }else {
                        this.loadings = false
                       this.datas = res.data.result
                       let len = this.datas.length
                        for(let i=0;i<len; i++){
                          this.data3.push({'value': i })
                        }
                       this.datas = res.data.result
                       this.dataCount = res.data.result.length
                       this.ajaxHistoryData = this.datas
                       this.handleListApproveHistory()
                      }
              }else {
                this.loadings = false
                setTimeout(() => {
                  this.$Message.warning('未搜索到匹配信息,请重试!')
                  this.datas = ''
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
        this.$axios.get(`${this.URL_PREFIX}/complain/high/list/export?starttime=${this.starttimes}&endtime=${this.endtimes}&type=${this.model1}`).then(res => {
          if(res.data.code == '0'){
            this.loading1 = false
            setTimeout(() => {
              this.$Message.success('导出成功')
              //打开文件下载链接
              window.location.href=`http://${res.data.url}`
            },1500)
          }else{
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
                    h('div', '页面数据加载中...')
                ])
            }
        });
        this.getDatalist()
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
  },
  components: {
      barArea
  }

}
</script>
<style scoped lang="scss">
    .twentyfour{
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
     margin-top: -58px;
     margin-bottom: 12px;
     padding-right: 17px;
   }
   .bm_view{
     width: 100%;
     height: 430px;
     padding-right: 18px;
   }
   .area{
     width: 100%;
     height: 480px;
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
