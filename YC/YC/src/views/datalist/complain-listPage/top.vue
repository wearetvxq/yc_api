<template lang="html">
     <div class="TopTwenty">
       <Row>
         <Row>
             <h3>投诉处理时长TOP20</h3>
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
                     <Col span='10'>
                          <Button type="ghost" icon="ios-search-strong" :style="{backgroundColor:'#2786d3',color:'#edf6fb'}">查看</Button>
                     </Col>
                   </Row>
                   <Row :style="{marginTop:'15px'}">
                       <FormItem label="图形展示:">
                            <RadioGroup v-model="category">
                               <Radio label="投诉处理时长TOP20"></Radio>
                           </RadioGroup>
                       </FormItem>
                   </Row>
                </FormItem>
             </Form>
         </Row>
         <Row>
            <div class="linelist">
               <!-- <span>{{this.category}}</span> -->
               <div class="map">
                 <baidu-map :center="center" :zoom="zoom"  @ready="handler" class="bm_view">
                   <bm-navigation anchor="BMAP_ANCHOR_TOP_RIGHT"></bm-navigation>
                   <bm-marker  v-for="(item,index) in this.master" :position="item[0]" :dragging="true" @click="clickHandler">
                      <bm-label :content='item[1].rank' :labelStyle="{color: 'red', fontSize : '14px',border:'none'}" :offset="{width: -25, height: 20}"/>
                   </bm-marker>
                 </baidu-map>
               </div>
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
                                   <DatePicker type="datetime" placeholder="请选择"  :value="endtimes" @on-change="handlechanges1"></DatePicker>
                               </Col>
                           </FormItem>
                       </Col>
                       <Col span="6" class="btn">
                          <Button type="ghost" icon="ios-search-strong" :style="{backgroundColor:'#2786d3',color:'#edf6fb'}" @click="Search">查看</Button>
                          <Button :loading="loading1" type="ghost" icon="ios-cloud-upload-outline"  @click="Expor" :style="{backgroundColor:'#2786d3',color:'#edf6fb'}" >导出</Button>
                      </Col>
                   </Row>
               </FormItem>
           </Form>
           <div>
             <Row>
                 <Table  :columns="columns" :data="data1" border ref="table"></Table>
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
import excel from '../../../libs/tableToExcel.js'
import {BmMarker} from 'vue-baidu-map'
export default {
  components:{
    BmMarker:'bm-marker'
  },
  data () {
      return {
          center: {lng: 0, lat: 0},
          Tops:[],
          Obj:{lng:'',lat:''},
          zoom: 3,
          position:[],
          datas:[],
          master:[

          ],
          loading1:false,
          category:'投诉处理时长TOP20',
          loading: false,
          loadings:false,
          ajaxHistoryData:[],
          pageSize:10,
          dataCount:0,
          starttime:'',
          endtime:'',
          starttimes:'',
          endtimes:'',
          model2:'',
          model3:'',
          model7:'',
          delystate:'',
          dely:[
            { value:'是',label:'是'},
            { value:'否',label:'否'},
          ],
          columns: [
              {
                  title: 'TOP',
                  key: 'id',
                  width: 120,
                  align:'center'
              },
              {
                  title: '区县',
                  key: 'area',
                  align:'center'
              },
              {
                  title: '工单流水号',
                  key: 'number',
                  align:'center'
              },
              {
                  title: '联系人',
                  key: 'contacts',
                  align:'center'
              },
              {
                  title: '用户电话',
                  key: 'phone',
                  align:'center'
              },
              {
                  title: 'T2操作时间',
                  key: 't2',
                  align:'center'
              },
              {
                  title: '处理时长(h)',
                  key: 'times',
                  align:'center'
              }
          ],
          data1: [],
          historyData: []
      }
  },
  created (){
    //  this.handleSpinCustom()
  },
  mounted (){
      this.getDatalist()
      this.Mapdata()
  },
  methods: {
    /*
      map地图
    */
    handler ({BMap, map}) {
        this.center.lng = 111.28
        this.center.lat = 30.70
        this.zoom = 11

    },
    clickHandler(e){
      //alert(`单击点的坐标为：${e.point.lng}, ${e.point.lat}`);
    },
    Mapdata() {
      this.$axios.get(`${this.URL_PREFIX}/complain/top/chart?starttime=${this.starttimes}&endtime=${this.endtimes}&type=`)
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
        this.$axios.get(`${this.URL_PREFIX}/complain/top/list?starttime=${this.starttimes}&endtime=${this.endtimes}&type=${this.model1}`)
              .then(res => {
                if(res.data.code == '0'){
                  //将获取的数据保存到data1空数组中
                  this.data1 = res.data.result
                  this.dataCount = res.data.result.length
                  this.ajaxHistoryData = this.data1
                  this.handleListApproveHistory()
                }
              })
              .catch(error => {
                console.log(error)
              })
      },
      Search() {
        this.loadings = true
        this.$axios.get(`${this.URL_PREFIX}/complain/top/list?starttime=${this.starttimes}&endtime=${this.endtimes}`)
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
          this.$axios.get(`${this.URL_PREFIX}/complain/top/list/export?starttime=${this.starttimes}&endtime=${this.endtimes}`).then(res => {
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
          //         excel(this.columns, this.$refs.table, '处理时长Top20.Xls ');
          //         this.$Message.success('导出成功!')
          // },1500)
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

  }

}
</script>
<style scoped lang="scss">
    .TopTwenty{
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
     margin-top: 170px;
     margin-bottom: 12px;
     padding-right: 17px;
   }
   .bm_view{
     width: 100%;
     height: 480px;
     padding-right: 18px;
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
