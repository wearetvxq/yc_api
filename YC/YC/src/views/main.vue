<template>
    <div class="layout"  style="overflow-y:hidden">
        <Layout :style="{height: '100%'}">
            <Header :style="{background: '#f5f5f5', padding: '0 10px'}">
                <img src="../assets/images/logo.png" class="layout-logo" />
                <div class="layout-quit">
                    <Icon type="person" class="person"></Icon>
                    <span>{{names}}</span>
                    <div @click="logout">
                      <Icon type="power" class="power"></Icon>
                    </div>
                </div>
                <!-- <Modal
                  v-model="modal6"
                  title="提示"
                  :loading="loading"
                  @on-ok="asyncOK"
                  @on-cancel="cancel">
                  <p>你确定要登出该账户吗?</p>
              </Modal> -->
            </Header>
            <Layout :style="{height: '100%'}">
                <Sider hide-trigger :style="{background: '#ffffff', height: '100%' ,borderRight:'1px solid #eeeeee'}">
                    <Menu active-name="/home"   width="auto" :open-names="['1']" @on-select="changeMenu">
                        <MenuItem name="/home/index">
                           <Icon type="home" size='19'></Icon>
                           <span>首页</span>
                       </MenuItem>
                       <Submenu name="2">
                            <template slot="title">
                                <Icon type="ios-list" size='19'></Icon>
                                数据列表
                            </template>
                            <MenuItem name="/datalist/complain">投诉分析列表</MenuItem>
                            <MenuItem name="/datalist/installed">装机分析列表</MenuItem>
                        </Submenu>
                        <MenuItem name="/dataimport/index">
                            <Icon type="ios-upload" size="19"></Icon>
                            <span>数据导入</span>
                        </MenuItem>
                        <Submenu name="/management/index">
                            <template slot="title">
                                <Icon type="person" size='19'></Icon>
                                信息管理
                            </template>
                            <MenuItem name="/management/builders">运维人员信息</MenuItem>
                            <MenuItem name="/management/community">小区信息</MenuItem>
                            <MenuItem name="/management/otherPerson">其他人员信息</MenuItem>
                        </Submenu>
                        <Submenu name="/management/index">
                            <template slot="title">
                                <Icon type="ios-monitor" size='19'></Icon>
                                装维终端管控
                            </template>
                              <MenuItem name="/terminal/stockin">入库操作</MenuItem>
                              <MenuItem name="/terminal/stockout">申领出库操作</MenuItem>
                              <MenuItem name="/terminal/assembly">装维终端明细</MenuItem>
                              <MenuItem name="/terminal/workstation">工作站终端统计表</MenuItem>
                              <MenuItem name="/terminal/maintenancer">装维人员终端统计表</MenuItem>
                        </Submenu>
                    </Menu>

                </Sider>
                <Layout>
                    <Breadcrumb :style="{background: '#fff'}">
                        <BreadcrumbItem>{{$route.meta.title}}</BreadcrumbItem>
                    </Breadcrumb>
                    <Content :style="{padding: '0px', minHeight: '280px', background: '#fff'}">
                        <router-view></router-view>
                    </Content>
                </Layout>
            </Layout>
        </Layout>
    </div>
</template>
<script>
    import { store } from '../store/store'
    export default {
        data() {
          return {
            loading:true,
            modal6: false
          }
        },
        computed: {
            names (){
                return this.$store.state.username;
            }
         },
        methods: {
            changeMenu (to) {
                this.$router.push({path: to});
            },
            logout() {
               //this.modal6 = true
               this.$Modal.confirm({
                            title: '提示',
                            content: '<h3>确定要退出吗?</h3>',
                            onOk: () => {
                                this.asyncOK()
                            },
                            onCancel: () => {
                                //this.$Message.info('Clicked cancel');
                            }
                        });
            },
            asyncOK() {
                setTimeout(()=> {
                    this.model6=false
                    this.$store.commit('LoginOut')
                    this.$router.push('/login')
                    this.$Notice.success({
                      title: '消息提示',
                      render: h => {
                          return h('span', [
                              '用户登出 ',
                              h('a', '成功'),
                          ])
                      }
                    })
                },2000)
            },
            cancel() {
              this.modal6 = false;
            }
        },

    }
</script>
<style lang="scss" scoped>
.layout{
    background: #f5f7f9;
    position: relative;
    height: 100%;
}
.layout-logo{
    width: 167px;
    height: 30.48px;
     margin-top:18px;
    vertical-align: middle;
    float: left;
}
.layout .layout-quit{
    width: 170px;
    height: 35px;
    line-height: 35px;
    color: #258ee9;
    float: right;
    border-radius: 100px;
    margin-top: 15px;
    border: 1px solid #258ee9;
    position: relative;
}
.layout .layout-quit .power{
    font-size: 20px;
    color: #258ee9;
    position: absolute;
    right: 10px;
    top: 7px;
}
.layout .layout-quit .person{
    font-size: 20px;
    color: #258ee9;
    position: absolute;
    left: 10px;
    top: 7px;
}
.layout .layout-quit span{
    padding-left: 30px;
}
</style>
<style>
  .ivu-breadcrumb{
      margin: 0;
      height: 45px;
      line-height: 45px;
      padding: 0 15px;
      border-bottom: 1px solid #e5e9ee;
      background-color: #f3f6fb;
  }
  .ivu-breadcrumb>span:last-child{
      font-size: 12px;
      font-weight: 600;
      color: #495060;
  }
  .ivu-menu-vertical .ivu-menu-item{
      padding: 12px 24px;
  }
  .ivu-menu-light .ivu-menu-vertical .ivu-menu-item-active:not(.ivu-menu-submenu){
    border-right: none;
    color:#447ed9;
  }
  .ivu-menu .ivu-menu-vertical .ivu-menu-light:after{
    background:none;
    width:0;
  }
  .ivu-layout,.ivu-layout-content{
          height: 100%;
  }

</style>
