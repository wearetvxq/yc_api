import main from './views/main.vue';

export const normal = {
    path: '/',
    redirect:'/login'
}

export const login = {
    path: '/login',
    name: 'login',
    meta: {
        title: '登录'
    },
    component: (resolve) => require(['./views/login.vue'], resolve)
}

export const homeRouter = {
  path: '/home',
  name: 'homeRouter',
  redirect:'home/index',
  component: main,
  children: [
      { path: 'index', title: {i18n: 'list'}, name: 'home_index', meta:{title:'首页',requireAuth:true},component: resolve => { require(['./views/home/home.vue'], resolve); } },
  ]
};

export const datalistRouter = {
    path: '/datalist',
    name: 'otherRouter',
    meta:{requireAuth:true},
    // redirect: '/home',
    component: main,
    children: [
        { path: 'complain', title: {i18n: 'list'}, name: 'datalist_complain', meta:{title:'投诉分析列表',requireAuth:true},component: resolve => { require(['./views/datalist/complain.vue'], resolve); } },
        { path: 'installed', title: {i18n: 'list'}, name: 'datalist_installed', meta:{title:'装机分析列表',requireAuth:true},component: resolve => { require(['./views/datalist/installed.vue'], resolve); } }
    ]
};

export const dataimportRouter = {
    path: '/dataimport',
    name: 'dataimportRouter',
    component: main,
    children: [
        { path: 'index', title: {i18n: 'dataimport'}, name: 'dataimport_index',meta:{title:'数据导入',requireAuth:true}, component: resolve => { require(['./views/dataimport/index.vue'], resolve); } },
    ]
};

export const ManagementRouter = {
  path: '/management',
  name: 'ManagementRouter',
  meta:{requireAuth:true},
  redirect: 'management/builders',
  component: main,
  children: [
      { path: 'builders', title: {i18n: 'management'}, name: 'message_builders', meta:{title:'运维人员信息管理',requireAuth:true},component: resolve => { require(['./views/userMessage/builders.vue'], resolve); } },
      { path: 'community', title: {i18n: 'management'}, name: 'message_community', meta:{title:'运维人员信息管理',requireAuth:true},component: resolve => { require(['./views/userMessage/community.vue'], resolve); } },
      { path: 'otherPerson', title: {i18n: 'management'}, name: 'message_other', meta:{title:'运维人员信息管理',requireAuth:true},component: resolve => { require(['./views/userMessage/otherPerson.vue'], resolve); } }
  ]
};
export const TerminalRouter = {
  path:'/terminal',
  name:'TerminalRouter',
  meta:{requireAuth:true},
  component:main,
  children:[
      { path: 'assembly', title: {i18n: 'terminal'}, name: 'terminal_assembly', meta:{title:'装维终端明细',requireAuth:true},component: resolve => { require(['./views/terminal/assembly.vue'], resolve); } },
      { path: 'workstation', title: {i18n: 'terminal'}, name: 'terminal_workstation', meta:{title:'工作站终端统计表',requireAuth:true},component: resolve => { require(['./views/terminal/workstation.vue'], resolve); } },
      { path: 'maintenancer', title: {i18n: 'terminal'}, name: 'terminal_maintenancer', meta:{title:'装维人员终端统计表',requireAuth:true},component: resolve => { require(['./views/terminal/maintenancer.vue'], resolve); } },
      { path: 'stockin', title: {i18n: 'terminal'}, name: 'terminal_in', meta:{title:'扫码入库',requireAuth:true},component: resolve => { require(['./views/terminal/stockin.vue'], resolve); } },
      { path: 'stockout', title: {i18n: 'terminal'}, name: 'terminal_out', meta:{title:'申领出库',requireAuth:true},component: resolve => { require(['./views/terminal/stockout.vue'], resolve); } }
  ]
};

export const routers = [
    normal,
    login,
    homeRouter,
    datalistRouter,
    dataimportRouter,
    ManagementRouter,
    TerminalRouter
];
