<template lang="html">
    <div class="builders">
        <Row>
            <h3 class="info">查找施工人员信息</h3>
            <Form :style="{marginTop:'20px',marginLeft:'15px'}">
               <FormItem>
                  <Row>
                    <Col span='6'>
                      <FormItem label="单位:">
                        <Select v-model="unit" style="width:180px" clearable>
                            <Option v-for="item in unitList" :value="item.value" :key="item.value">{{ item.value }}</Option>
                        </Select>
                      </FormItem>
                    </Col>
                    <Col span='7'>
                      <FormItem label="网格:">
                        <Select v-model="net" style="width:180px" clearable>
                            <Option v-for="item in netList" :value="item.value" :key="item.value">{{ item.value }}</Option>
                        </Select>
                      </FormItem>
                    </Col>
                    <Col span='8'>
                      <FormItem label="人员:">
                          <Cascader :data="userInfo" trigger="hover"  @on-change="handleChange" :style="{width:'180px',marginLeft:'40px'}"></Cascader>
                      </FormItem>
                    </Col>
                  </Row>
                  <Row type="flex" justify="end" :style="{marginRight:'150px',marginTop:'5px'}">
                     <Button type="ghost" icon="ios-search-strong" :style="{backgroundColor:'#2786d3',color:'#edf6fb'}" @click="Search">查找</Button>
                  </Row>
                  <Row :style="{marginTop:'-15px'}">
                    <Col span='6'>
                      <FormItem label="工号:" >
                          <Input v-model="jobNumber" placeholder="输入工号查找" style="width:180px" clearable></Input>
                      </FormItem>
                    </Col>
                    <Col span='7'>
                      <FormItem label="姓名:" >
                          <Input v-model="name" placeholder="输入姓名查找"style="width:180px" clearable></Input>
                      </FormItem>
                    </Col>
                    <Col span='8'>
                      <FormItem label="电话:" >
                          <Input v-model="jobNumber" placeholder="输入电话查找" style="width:180px" clearable></Input>
                      </FormItem>
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
              <Col class="demo-spin-cols" span="8" v-show="loadings">
                <Spin fix>
                    <Icon type="load-c" size=18 class="demo-spin-icon-load"></Icon>
                    <div>数据查询中...</div>
                </Spin>
              </Col>
            </div>
        </Row>
        <Modal
                v-model="modal"
                title="人员信息"
                width="560"
                @on-ok="confirm"
                >
                  <div class="modal">
                    <div class="left">
                      <table border="1" :style="{width:'393px',height:'195px',borderCollapse:'collapse'}">
                           <tr>
                               <td colspan="2">基本信息</td>
                           </tr>
                           <tr>
                               <td>姓名: 张三</td>
                               <td>人员角色: 施工人员</td>
                           </tr>
                           <tr>
                             <td>工号: 18271370009</td>
                             <td>所属网格网格长: 王强</td>
                           </tr>
                           <tr>
                             <td>联系电话: 1827230019</td>
                             <td>所属网络: 宜昌城区体育场胜利四路网格</td>
                           </tr>
                           <tr>
                             <td colspan="2">辅助考核成绩</td>
                           </tr>
                           <tr>
                             <td>装/维单数 : 100</td>
                             <td>
                               用户满意度评级:
                               <Rate show-text disabled v-model="valueDisabled" allow-half>
                                  <span style="color: #f5a623" :style="{marginLeft:'-10px'}">{{ valueDisabled }}</span>
                               </Rate>
                             </td>
                           </tr>
                      </table>
                    </div>
                    <div class="right">
                        <div class="avatar">
                           <img src="http://img3.imgtn.bdimg.com/it/u=681361398,3689351797&fm=27&gp=0.jpg">
                           <p>查看所有图片</p>
                        </div>
                        <div class="btn">
                           <Button type="primary" icon="ios-cloud-upload-outline" size="small">导出</Button>
                        </div>
                    </div>
                  </div>
                </Modal>
    </div>
</template>

<script>
export default {
  data() {
    return {
       valueDisabled:4.5,
       loadings:false,
       loading:false,
       builders:'',
       modal:false,
       dataCount:10,
       pageSize:10,
       star:3,
       ajaxHistoryData:[],
       unit:'',
       net:'',
       name:'',
       jobNumber:'',
       personInfo:{},
       userInfo:[
                {
                    value: '网格长',
                    label: '网格长',
                    children: [
                        {
                            value: 'gugong',
                            label: '赵旭'
                        }
                    ]
                },
                {
                    value: '装修人员',
                    label: '装修人员',
                    children: [
                        {
                            value: 'nanjing',
                            label: '周晨',
                        },
                        {
                            value: 'tiantan',
                            label: '王明'
                        },
                        {
                            value: 'wangfujing',
                            label: '邓建国'
                        }
                    ]
                }
       ],
       unitList:[
         {name:'城区支撑服务中心',value:'城区支撑服务中心'}
       ],
       netList:[
         {name:'宜昌城区云集路网格',value:'宜昌城区云集路网格'}
       ],
       data1:[
         {name:'张凯',role:'施工人员',phone:'15728292612',net:'夷陵大道网络',order:'200',rate:5},
         {name:'李强',role:'施工人员',phone:'18062344512',net:'宜昌城区网络',order:'150',rate:2.5},
         {name:'王伟',role:'施工人员',phone:'15507257063',net:'夷陵大道网络',order:'110',rate:3},
         {name:'石康',role:'施工人员',phone:'13597618546',net:'宜昌城区网络',order:'190',rate:4},
         {name:'周琦',role:'施工人员',phone:'18607843615',net:'夷陵大道网络',order:'230',rate:3.5},
         {name:'赵大千',role:'施工人员',phone:'15002370571',net:'宜昌城区网络',order:'350',rate:2},
         {name:'王明',role:'施工人员',phone:'18696147114',net:'夷陵大道网络',order:'80',rate:5},
         {name:'邓建国',role:'施工人员',phone:'1808292509',net:'宜昌城区网络',order:'176',rate:4.5},
         {name:'张东阳',role:'施工人员',phone:'13858294801',net:'夷陵大道网络',order:'150',rate:1.5},
         {name:'赵旭',role:'施工人员',phone:'13328297216',net:'宜昌城区网络',order:'168',rate:0.5}
       ],
       columns1:[
         {
             title: '姓名',
             key: 'name',
             align:'center'
         },
         {
             title: '人员角色',
             key: 'role',
             align:'center'
         },
         {
             title: '电话',
             key: 'phone',
             align:'center'
         },
         {
             title: '所属网络',
             key: 'net',
             align:'center'
         },
         {
             title: '装维单数',
             key: 'order',
             align:'center'
         },
         {
             title: '用户满意度评级',
             key: 'rate',
             align:'center',
             render:function(h,params){
               return h('div',[
                 h('rate',{
                   props: {
                        count:5,
                        value:params.row.rate,
                        allowHalf:true,
                        disabled:true,
                    }
                 })
               ])
             }
         },
         {
             title: '操作',
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
                                this.modal = true
                                //根据id数据
                             }
                         }
                     }, '查看'),
                 ]);
             }
         }
       ]
    }
  },
  mounted(){

  },
  methods:{
     getDataList(){

     },
     Search(){
        //this.loading = true
     },
     confirm(){

     },
     handleChange(value,selectedData){
         this.builders = selectedData.map( o => o.label).join('/')
         //console.log(this.builders)
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
     .builders{
       .info{
         margin-top: 15px;
         margin-left: 15px;
       }
     }
     .table{
       display: relative;
       @keyframes ani-demo-spin{
            from { transform: rotate(0deg);}
            50%  { transform: rotate(180deg);}
            to   { transform: rotate(360deg);}
        }
        .demo-spin-icon-loads{
            animation: ani-demo-spin 1s linear infinite;
        }
       .demo-spin-icon-load{
            animation: ani-demo-spin 1s linear infinite;
        }
       .demo-spin-cols{
           position: absolute;
           left: 30%;
           top:50%;
           z-index: 100;
           transform: translate3d(-30%,-50%);
       }
     }
     .modal{
       display: flex;
     }
     .left table{
       border:1px solid #cfcfcf;
       tr{
         td{
          padding-left: 12px;
          height: 32.5px;
          color:#101010;
         }
       }
     }
     .right{
       height: 194px;
       width: 100%;
       .avatar{
         img{
           width: 85px;
           height: 120px;
           margin-left: 33px;
         }
         p{
           font-size: 12px;
           margin-left: 40px;
           margin-top: 10px;
           color:#101010;
         }
       }
       .btn{
         Button{
           margin-left: 45px;
           margin-top: 22px;
         }
       }
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
<style lang="scss">
  .builders{
    .ivu-table {
      .ivu-table-header{
        background-color: red;
      }
    }
  }


<style>
