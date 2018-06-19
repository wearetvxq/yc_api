import Vue from 'vue';
import BaiduMap from 'vue-baidu-map'
import VueRouter from 'vue-router';
import { routers } from './router';
import Axios from 'axios'
import { store } from './store/store'
import Util from './libs/util';
import moment from 'moment/moment'
import iView from 'iview';
import 'iview/dist/styles/iview.css';
import './assets/Style/global.css'
import App from './app.vue';

import VueI18n from 'vue-i18n';
import Locales from './locale';
import zhLocale from 'iview/src/locale/lang/zh-CN';
import enLocale from 'iview/src/locale/lang/en-US';
import '../theme/index.less';
Vue.use(iView);
//按需引入 减少文件体积
import { Button, Table, FormItem, Page, Select, Upload, CheckboxGroup, Modal} from 'iview';
Vue.component('Button', Button);
Vue.component('Table', Table);
Vue.component('FormItem', FormItem);
Vue.component('Page', Page);
Vue.component('Select', Select);
Vue.component('Upload', Upload);
Vue.component('CheckboxGroup', CheckboxGroup);
Vue.component('Modal', Modal);

// 引入样式
import 'vue-easytable/libs/themes-base/index.css'
// 导入 table 和 分页组件
import {VTable,VPagination} from 'vue-easytable'
Vue.component(VTable.name, VTable)
Vue.component(VPagination.name, VPagination)

//引入百度地图
Vue.use(BaiduMap, {
  ak: 'wUYDdHvNZ2b3iOtLcbRczL9VDFpPhXx0'   //ak 是在百度地图开发者平台申请的密钥
})



//Mock假数据
require('./mock')

//axios全局引用
Vue.prototype.$axios = Axios

//本地测试API接口地址  //http://192.168.188.201:81/v1
//线上地址  http://39.108.165.149:7005
if (process.env.NODE_ENV !== 'development') {
   Vue.prototype.URL_PREFIX = 'http://127.0.0.1:89/v1'
 } else {
   Vue.prototype.URL_PREFIX = 'http://127.0.0.1:89/v1'
 }

Vue.use(VueRouter);
Vue.use(VueI18n);

// 自动设置语言
const navLang = navigator.language;
const localLang = (navLang === 'zh-CN' || navLang === 'en-US') ? navLang : false;
const lang = window.localStorage.getItem('language') || localLang || 'zh-CN';

Vue.config.lang = lang;

// 多语言配置
const locales = Locales;
const mergeZH = Object.assign(zhLocale, locales['zh-CN']);
const mergeEN = Object.assign(enLocale, locales['en-US']);
Vue.locale('zh-CN', mergeZH);
Vue.locale('en-US', mergeEN);


// 路由配置
const RouterConfig = {
    mode: 'history',
    routes: routers
};
const router = new VueRouter(RouterConfig);



//页面刷新时store.token会被清空,需重新赋值token

if(window.localStorage.getItem('token')){
    store.commit('setLogin', window.localStorage.getItem('token'))
    store.commit('saveUser', window.localStorage.getItem('username'))
}

//路由拦截 实现用户登录权限控制

router.beforeEach((to, from, next) => {
    iView.LoadingBar.start();
    Util.title(to.meta.title);
    if (to.matched.some(res => res.meta.requireAuth)) {// 判断是否需要登录权限
      if (store.state.token) {// 判断是否登录
        next();
      }else {
        // 没登录则跳转到登录界面
          next({
          path: '/login',
          query: {redirect: to.fullPath}
        })

      }
  }else{
    next()
  }
});

//路由导航钩子函数
router.afterEach(() => {
    iView.LoadingBar.finish();
    window.scrollTo(0, 0);
});
//全局过滤器
 Vue.filter('moment',function(value,formatString) {
    formatString = formatString || 'YYYY-MM-DD HH:mm:ss'
    return moment.unix(value).format(formatString)
})
new Vue({
    el: '#app',
    router:router,
    store:store,
    render: h => h(App)
});
