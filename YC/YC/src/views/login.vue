<template>
    <div class="login">
        <div class="login-banner">
            <img src="../assets/images/banner.jpg" alt="">
        </div>
        <div class="login-content">
            <div class="login-content-comp">
                <div class="login-content-input">
                    <span>用户名</span>
                    <input type="text" v-model="username" placeholder="请输入登录用户名" />
                </div>
                <div class="login-content-input">
                    <span>密码</span>
                    <input type="password" v-model="password" placeholder="请输入登录密码" />
                </div>
                <div class="login-content-input">
                    <button :loading="loading1" type="button" @click="login">登录</button>
                    <button type="button" @click="reset">重置</button>
                </div>
                <div class="login-content-input" style="width:160px;">
                    <CheckboxGroup v-model="checked">
                        <Checkbox label="记住密码"></Checkbox>
                        <Checkbox label="自动登录"></Checkbox>
                    </CheckboxGroup>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
    import { store } from '../store/store'
    import Cookies from 'js-cookie';
    export default {
        data () {
            return {
                username: '',
                password: '',
                loading1:false,
                checked: ['记住密码']

            }
        },
        methods: {
            login () {
                     if(this.username ==''||this.username == null){
                        this.$Message.warning('用户名不能为空!');
                     }else if(this.password ==''||this.password == null){
                       this.$Message.warning('密码不能为空!');
                     }else{
                       this.$axios.post(`${this.URL_PREFIX}/login`,{
                         username:this.username,
                         password:this.password
                       }).then(res => {
                           this.loading1 =  true
                           if (res.data.code == '0'){
                             this.loading1 =  false
                             Cookies.set('username',this.username)
                             var name = Cookies.get('username')
                             Cookies.set('password',this.password)
                             var pwd = Cookies.get('password')
                              setTimeout(()=> {
                                this.$Notice.success({
                                  title: '消息提示',
                                  render: h => {
                                      return h('span', [
                                          '用户登录 ',
                                          h('a', '成功'),
                                      ])
                                  }
                                })
                              },1500)
                              let name = ''
                              name = this.username
                               setTimeout(() => {
                                 //Cookies.set('password', this.password);
                                 this.$store.commit('setLogin',{data:'test'})
                                 this.$store.commit('saveUser',name)
                                 this.$router.push({ path:'/home'})
                               },1000)
                           }else{
                             this.loading1 =  false
                             setTimeout(() => {
                               this.$Notice.error({
                                 title: '登录提示',
                                 render: h => {
                                     return h('span', [
                                         '登录失败!',
                                         h('a', '请核对您的用户名和密码是否输入有误'),
                                     ])
                                 }
                               })
                             },1500)
                           }
                       }).catch(error => {
                           console.log(error)
                       });

                     }


            },
            reset () {
              this.username = ''
              this.password = ''
              Cookies.remove('username')
              Cookies.remove('password')
            }
        }
    };
</script>
<style lang="scss" scoped>
    input::-webkit-input-placeholder, textarea::-webkit-input-placeholder { /* WebKit*/
       color: #c4c4c4;
    }
    input:-moz-placeholder, textarea:-moz-placeholder { /* Mozilla Firefox 4 to 18 */
        color: #c4c4c4;
    }
    input::-moz-placeholder, textarea::-moz-placeholder { /* Mozilla Firefox 19+ */
        color: #c4c4c4;
    }
    input:-ms-input-placeholder, textarea:-ms-input-placeholder { /* IE 10+ */
        color: #c4c4c4;
    }
    input{
      outline: none;
    }
    .login{
        margin: 0;
        padding: 0;
    }
    button{
      outline: none
    }
   .login-banner{
      width: 100%;
      img{
        height: 460px;
        width: 100%;
      }
    }
    .login .login-content{
        width: 72.5%;
        height: auto;
        margin: 0 auto;
        padding: 20px 0 30px 0;
        position: relative;
    }
     .login .login-content .login-content-sxt{
        width: 200px;
        height: 200px;
        position: absolute;
        top: -100px;
        left: 0;
     }
    .login .login-content .login-content-comp{
        width: 81.4%;
        float: right;
    }
    .login .login-content-comp .login-content-input{
        width: 200px;
        height: auto;
        position: relative;
        float: left;
        margin-left: 20px;
    }
    .login .login-content-comp .login-content-input input{
        border: 1px dashed #bbb;
        border-radius: 100px;
        width: 100%;
        height: 35px;
        padding: 0 10px;
    }
    .login .login-content-comp .login-content-input span{
        position: absolute;
        left: 18px;
        top: -10px;
        font-size: 14px;
        color: #999;
        background-color: #FFF;
    }
    .login .login-content-comp .login-content-input button{
        width: 90px;
        height: 35px;
        border-radius: 100px;
        font-size: 14px;
    }
    .login .login-content-comp .login-content-input button:nth-child(1){
        background-color: #3f8d76;
        border: none;
        color: #FFF;
    }
    .login .login-content-comp .login-content-input button:nth-child(2){
        margin-left: 15px;
        border: 1px dashed #bbb;
        color: #999;
    }
    .login .login-content-input .ivu-checkbox-group{
        color: #3f8d76 !important;
        margin-top: 6px;
    }

    .login-content-comp{
      margin-top: 20px;
    }
</style>
