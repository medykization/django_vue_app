import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import login from './views/SignIn'
import register from './views/SignUp'
import dashboard from './views/DashBoard'
import logout from './views/Logout'
import about from './views/About'
import board from './views/Board'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/login',
      name: 'login',
      component: login,
      meta: {
        requiresLogged: true
      }
    },
    {
      path: '/register',
      name: 'register',
      component: register,
      meta: {
        requiresLogged: true
      }
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: dashboard,
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/logout',
      name: 'logout',
      component: logout,
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/about',
      name: 'about',
      component: about
    },
    {
      path: '/board/:id/:name',
      name: 'board',
      component: board,
      meta: {
        requiresAuth: true
      }
    }
  ]
})
