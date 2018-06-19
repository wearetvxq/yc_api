<template lang="html">
      <div class="stockin">
           <div class="modal">
               <div class="header">
                    <p>终端扫码入库</p>
               </div>
               <div class="body">
                  <div class="station lis">
                    <Form :style="{width:'390px',height:'50px',marginLeft:'78px',marginTop:'17px'}">
                        <FormItem label="工作站:">
                          <Select @on-change="handleChange" v-model="station" style="width:180px" clearable>
                              <Option v-for="item in stationList" :value="item.value" :key="item.value">{{ item.value }}</Option>
                          </Select>
                        </FormItem>
                    </Form>
                  </div>
                  <div class="terminal lis">
                    <Form :style="{width:'390px',height:'50px',marginLeft:'65px',marginTop:'17px'}" >
                        <FormItem label="终端类型:">
                          <Select @on-change="handleChange1" v-model="terminal" style="width:180px" clearable>
                              <Option v-for="item in terminalList" :value="item.value" :key="item.value">{{ item.value }}</Option>
                          </Select>
                        </FormItem>
                    </Form>
                  </div>

                  <div class="type lis">
                    <Form :style="{width:'390px',height:'50px',marginLeft:'89px',marginTop:'17px'}" >
                        <FormItem label="型号:">
                          <Select v-model="type" style="width:180px" clearable>
                              <Option v-for="item in typeList" :value="item.value" :key="item.value">{{ item.value }}</Option>
                          </Select>
                        </FormItem>
                    </Form>
                  </div>
                  <div class="outer lis">
                    <Form :style="{width:'390px',height:'50px',marginLeft:'78px',marginTop:'17px'}" >
                        <FormItem label="入库人:">
                          <Select v-model="stocker" style="width:180px" clearable>
                              <Option v-for="item in personList" :value="item.value" :key="item.value">{{ item.value }}</Option>
                          </Select>
                        </FormItem>
                    </Form>
                  </div>
                  <div class="vendor lis">
                    <Form :style="{width:'390px',height:'50px',marginLeft:'89px',marginTop:'17px'}" >
                        <FormItem label="厂家:">
                          <Select v-model="vendor" style="width:180px" clearable>
                              <Option v-for="item in factoryList" :value="item.value" :key="item.value">{{ item.value }}</Option>
                          </Select>
                        </FormItem>
                    </Form>
                  </div>
                  <div class="code lis">
                    <Form :style="{width:'390px',height:'50px',marginLeft:'78px',marginTop:'17px'}" >
                        <FormItem label="条形码:">
                          <Input v-model="code" placeholder="请扫条形码" style="width:180px" clearable></Input>
                        </FormItem>
                    </Form>
                  </div>
               </div>
               <div class="footer">
                  <Button type="primary" icon="arrow-right-c" size="small" :style="{position:'relative',left:'20px'}" @click="inbound">入库</Button>
                  <div class="logo">
                      <img src="../../assets/images/minilogo.gif" alt="">
                  </div>
               </div>
           </div>
      </div>
</template>

<script>
export default {
    data(){
      return{
        terminal:'',
        type:'',
        vendor:'',
        stocker:'',
        code:'',
        station:'',
        factoryList:[
          {name:'中兴',value:'中兴'},
          {name:'华为',value:'华为'},
          {name:'贝尔',value:'贝尔'},
          {name:'杭研',value:'杭研'}
        ],
        terminalList:[],
        typeList:[],
        personList:[],
        stationList:[]
      }
    },
    watch: {
      code(){
         if(this.code ==''||this.code ==null){
           return
         }else{
           this.$axios.post(`${this.URL_PREFIX}/supplies/storage`,{
             work:this.station,
             type:this.terminal,
             factory:this.vendor,
             model:this.type,
             principal:this.stocker,
             code:this.code
           })
          .then(res => {
            if(res.data.code == '0'){
              setTimeout(() => {
                this.reset()
                this.$Notice.success({
                  title: '消息提示',
                  render: h => {
                      return h('span', [
                          '扫码入库 ',
                          h('a', '成功'),
                      ])
                  }
                })
              },1000)
            }else if(res.data.code == '10003'){
              setTimeout(() => {
                this.reset()
                this.$Notice.error({
                  title: '消息提示',
                  render: h => {
                      return h('span', [
                          '该条形码已存在',
                          h('a', '请重试!'),
                      ])
                  }
                })
              },1000)
            }
          })
          .catch(error => {

          })
         }
      }
    },
    created(){
           this.$nextTick(function () {
                this.Getworkstation()
                this.GetterminalList()
                this.gettypeList()
                this.getpersonList()
           })
     },
    methods:{
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
         /*
             入库操作
         */
         inbound(){
           if(this.code ==''||this.code == null){
              this.$Message.warning('请扫码!');
           }else{
             this.$axios.post(`${this.URL_PREFIX}/supplies/storage`,{
               work:this.station,
               type:this.terminal,
               factory:this.vendor,
               model:this.type,
               principal:this.stocker,
               code:this.code
             })
                .then(res => {
                    if(res.data.code == '0'){
                      setTimeout(() => {
                        this.reset()
                        this.$Notice.success({
                          title: '消息提示',
                          render: h => {
                              return h('span', [
                                  '扫码入库 ',
                                  h('a', '成功'),
                              ])
                          }
                        })
                      },1000)
                    }else if(res.data.code == '10003'){
                      setTimeout(() => {
                        this.reset()
                        this.$Notice.error({
                          title: '消息提示',
                          render: h => {
                              return h('span', [
                                  '该条形码已存在',
                                  h('a', '请重试!'),
                              ])
                          }
                        })
                      },1000)
                    }else {
                      setTimeout(() => {
                        this.reset()
                        this.$Notice.error({
                          title: '消息提示',
                          render: h => {
                              return h('span', [
                                  '扫码入库 ',
                                  h('a', '失败'),
                              ])
                          }
                        })
                      },1000)
                    }
                })
                .catch(error => {
                  setTimeout(() => {
                    this.reset()
                    this.$Notice.success({
                      title: '消息提示',
                      render: h => {
                          return h('span', [
                              '系统 ',
                              h('a', '错误'),
                          ])
                      }
                    })
                  },1000)
                  console.log(error)
                })
           }
         },
         reset(){
           this.station = ''
           this.terminal = ''
           this.vendor = ''
           this.type = ''
           this.stocker = ''
           this.code = ''
         },
         /*
            工作站联动工作人员
         */
        handleChange(value){
         //     let Selects = []
         //     for(let items of this.stationList){
         //       Selects.push(items.name)
         //     }
         //     let index = Selects.indexOf(value)
         //     let id = index + 1
         //     this.$axios.get(`${this.URL_PREFIX}/label/people?id=${id}`)
         //                .then(res => {
         //                  if(res.data.code == '0'){
         //                    this.personList = []
         //                    for(let item of res.data.result){
         //                      this.personList.push({name:item.name,value:item.name})
         //                    }
         //                     this.stocker = this.personList[0].name
         //                  }
         //                })
         //                .catch(error => {
         //                  console.log(error)
         //                })
          },
         /*
          终端类型联动型号
         */
         handleChange1(value){
           let Selects1 = []
           for(let items of this.terminalList){
             Selects1.push(items.name)
           }
           let index = Selects1.indexOf(value)
           let id = index + 1
           this.$axios.get(`${this.URL_PREFIX}/label/terminal/model?id=${id}`)
                      .then(res => {
                        if(res.data.code == '0'){
                          this.typeList = []
                          for(let item of res.data.result){
                            this.typeList.push({name:item.name,value:item.name})
                          }
                           this.type = this.typeList[0].name
                        }
                      })
                      .catch(error => {
                        console.log(error)
                      })
         }
    }
}
</script>

<style lang="scss" scoped>
   .stockin{
     position: relative;
     width: 100;
     height: 100%;
   }
   .modal{
     width: 390px;
     position: absolute;
     top:40px;
     left:50%;
     margin-left: -195px;
     border: 1px solid #e5e9ef;
     border-radius: 6px;
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
    justify-content: center;
    align-items: center;
    height: 60px;
    background-color: #ffffff;
  }
  .modal .footer .logo{

    img{
      width: 55.06px;
      height: 41.87px;
      position: relative;
      left: 120px;

    }
  }
</style>
