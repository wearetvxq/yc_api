import Vue from 'vue'
import Vuex from 'vuex'
Vue.use(Vuex)

export const store = new Vuex.Store({
  state:{
      // admininfo : {
      //   avatar: ''
      // }
      user:{},
      username:null,
      token:null,
      title:''
  },
  getters:{
    name: (state) => {
          return state.username
      }
  },
  mutations:{
    // saveAdminInfo(state, adminInfo){
  	// 	state.adminInfo = adminInfo;
  	// },
    setLogin: (state,data) => {
       localStorage.token = data;
       state.token = data
    },
    saveUser: (state,data) => {
      localStorage.username = data;
      state.username = data
    },
    LoginOut: (state) => {
      localStorage.removeItem('token');
      state.token = null
      state.username = null
    }
  },
  actions:{

  }

})
