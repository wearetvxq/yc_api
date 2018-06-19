<template lang="html">
     <div class="community">
        <Row>
            <h3 class="info">小区信息</h3>
            <Form :style="{marginTop:'20px',marginLeft:'15px'}">
               <FormItem>
                   <Row>
                      <Col span="5">
                        <FormItem label="选择网格:">
                          <Select v-model="net" style="width:180px" clearable>
                              <Option v-for="item in netList" :value="item.value" :key="item.value">{{ item.value }}</Option>
                          </Select>
                        </FormItem>
                      </Col>
                      <Col span="5">
                        <FormItem label="小区名称:">
                          <Select v-model="communityname" style="width:180px" clearable>
                              <Option v-for="item in communityList" :value="item.value" :key="item.value">{{ item.value }}</Option>
                          </Select>
                        </FormItem>
                      </Col>
                      <Col span="5">
                        <FormItem label="名称:" :style="{marginLeft:'10px'}">
                            <Input v-model="name" placeholder="请输入名称查找"style="width:180px" clearable></Input>
                        </FormItem>
                      </Col>
                      <Col span="5">
                        <FormItem label="装维人员:" >
                            <Input v-model='installer' placeholder="请输入装维人员名字查找"style="width:180px" clearable></Input>
                        </FormItem>
                      </Col>
                      <Col span="4">
                          <Button type="ghost" icon="ios-search-strong" :style="{backgroundColor:'#2786d3',color:'#edf6fb',marginLeft:'30px'}" @click="Search" >查找</Button>
                      </Col>
                   </Row>
               </FormItem>
            </Form>
            <div :style="{padding:'0 15px',marginTop:'30px'}" class="table">
              <Row :style="{marginBottom:'30px'}">
                  <Table :loading="loading" :columns="columns1" :data="data1" border></Table>
              </Row>
              <Row :style="{marginTop: '15px'}">
                  <Page :style="{float:'right'}" :total='dataCount' size="small" :page-size="pageSize" show-total show-elevator @on-change="changepage"></Page>
              </Row>
            </div>
            <Col class="demo-spin-cols" span="8" v-show="loadings">
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
  data(){
    return{
      loading:false,
      loadings:false,
       net:'',
       name:'',
       installer:'',
       dataCount:4,
       pageSize:10,
       ajaxHistoryData:[],
       communityname:'',
       communityList:[
         {name:'北门正外街99号',value:'北门正外街99号'},
         {name:'北门正外街社区',value:'北门正外街社区'}
       ],
       netList:[
         {name:'宜昌城区云集路网格',value:'宜昌城区云集路网格'}
       ],
       data1:[
         {community:'北门外正街99号',net:'宜昌城区环城路点军网络',builder:'邓建国',contact:'18372370014'},
         {community:'北门外正街商铺增补',net:'宜昌城区环城路点军网络',builder:'王明',contact:'15505253982'},
         {community:'北门外正街社区',net:'宜昌城区环城路点军网络',builder:'赵旭',contact:'13597828449'},
         {community:'城区国土资源局',net:'宜昌城区环城路点军网络',builder:'张东阳',contact:'18062045237'}
       ],
       columns1:[
         {
             title: '小区名称',
             key: 'community',
             align:'center'
         },
         {
             title: '所属网格',
             key: 'net',
             align:'center'
         },
         {
             title: '对应装修人员',
             key: 'builder',
             align:'center'
         },
         {
             title: '装修人员联系电话',
             key: 'contact',
             align:'center'
         },
         // {
         //     title: '操作',
         //     key: 'operating',
         //     width: 200,
         //     align:'center',
         //     render: (h, params) => {
         //         return h('div', [
         //             h('Button', {
         //                 props: {
         //                     type: 'primary',
         //                     size: 'small'
         //                 },
         //                 style: {
         //                     marginRight: '25px'
         //                 },
         //                 on: {
         //                     click: () => {
         //
         //                     }
         //                 }
         //             }, '查看'),
         //         ]);
         //     }
         // }
       ]
    }
  },
  mounted(){

  },
  methods:{
    Search(){
       //this.loading = true
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
    .community{
      .info{
        margin-top: 15px;
        margin-left: 15px;
      }
    }
</style>
