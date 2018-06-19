<template lang="html">
     <div class="community">
        <Row>
            <h3 class="info">其他人员信息</h3>
            <Form :style="{marginTop:'20px',marginLeft:'15px'}">
               <FormItem>
                   <Row>
                      <Col span="5">
                        <FormItem label="选择部门:">
                          <Select v-model="net" style="width:180px" clearable>
                              <Option v-for="item in netList" :value="item.value" :key="item.value">{{ item.value }}</Option>
                          </Select>
                        </FormItem>
                      </Col>
                      <Col span="5">
                        <FormItem label="工号:" :style="{marginLeft:'10px'}">
                            <Input v-model="jobNumber" placeholder="请输入工号查找"style="width:180px" clearable></Input>
                        </FormItem>
                      </Col>
                      <Col span="5">
                        <FormItem label="姓名:" >
                            <Input v-model='name' placeholder="请输入姓名查找"style="width:180px" clearable></Input>
                        </FormItem>
                      </Col>
                      <Col span="5">
                        <FormItem label="电话:" >
                            <Input v-model='phone' placeholder="请输入电话查找"style="width:180px" clearable></Input>
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
       jobNumber:'',
       phone:'',
       installer:'',
       dataCount:3,
       pageSize:10,
       ajaxHistoryData:[],
       netList:[
         {name:'宜昌城区云集路网格',value:'宜昌城区云集路网格'}
       ],
       data1:[
         {number:'13997672526',role:'客服中心主任',name:'易勋伟',contact:'18372370014'},
         {number:'16597618027',role:'客服中心主任',name:'李华',contact:'18062055491'},
         {number:'14697672501',role:'客服中心主任',name:'张国明',contact:'13597648649'},
       ],
       columns1:[
         {
             title: '工号',
             key: 'number',
             align:'center'
         },
         {
             title: '姓名',
             key: 'name',
             align:'center'
         },
         {
             title: '联系电话',
             key: 'contact',
             align:'center'
         },
         {
             title: '对应角色',
             key: 'role',
             align:'center'
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
