import Vue from 'vue'
import Router from 'vue-router'
import Register from "../components/Register";
import Login from "../components/Login";
import Index from "../components/Index"
import Add_emp from "../components/Add_emp";
import Update from "../components/Update";


Vue.use(Router)

export default new Router({
  routes: [
      {path:'/register',component:Register},
      {path:'/login',component:Login},
      {path:'/index',component:Index},
      {path:'/add',component:Add_emp},
      {path:'/update/:id/',component:Update},
      {path:'/',component:Login},
      {path:'/*',component:Login},
  ]

})
