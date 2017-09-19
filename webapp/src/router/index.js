import Vue from 'vue'
import Router from 'vue-router'
import Hello from '@/components/Hello'
import Monitor from '@/components/Monitor'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Monitor',
      component: Monitor
    },
    {
      path: '/hello',
      name: 'Hello',
      component: Hello
    }
  ]
})
