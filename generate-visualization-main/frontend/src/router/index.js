import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

/* Layout */
import Layout from '@/layout'

/**
 * Note: sub-menu only appear when route children.length >= 1
 * Detail see: https://panjiachen.github.io/vue-element-admin-site/guide/essentials/router-and-nav.html
 *
 * hidden: true                   if set true, item will not show in the sidebar(default is false)
 * alwaysShow: true               if set true, will always show the root menu
 *                                if not set alwaysShow, when item has more than one children route,
 *                                it will becomes nested mode, otherwise not show the root menu
 * redirect: noRedirect           if set noRedirect will no redirect in the breadcrumb
 * name:'router-name'             the name is used by <keep-alive> (must set!!!)
 * meta : {
    roles: ['admin','editor']    control the page roles (you can set multiple roles)
    title: 'title'               the name show in sidebar and breadcrumb (recommend set)
    icon: 'svg-name'/'el-icon-x' the icon show in the sidebar
    breadcrumb: false            if set false, the item will hidden in breadcrumb(default is true)
    activeMenu: '/example/list'  if set path, the sidebar will highlight the path you set
  }
 */

/**
 * constantRoutes
 * a base page that does not have permission requirements
 * all roles can be accessed
 */
export const constantRoutes = [
  {
    path: '/login',
    component: () => import('@/views/login/index'),
    hidden: true
  },

  {
    path: '/404',
    component: () => import('@/views/404'),
    hidden: true
  },

  // dashboard
  {
    path: '/',
    component: Layout,
    hidden: true,
    redirect: '/dashboard',
    children: [{
      path: 'dashboard',
      name: 'Dashboard',
      component: () => import('@/views/dashboard/index'),
      meta: { title: 'Home', icon: 'dashboard' }
    }]
  },
  // {
  //   path: '/windex',
  //   name: 'windex',
  //   component: () => import('@/views/factory/creditCardCash')
  //   //  hidden: true
  // },
  {
    path: '/sceneDataGenerate',
    component: Layout,
    redirect: 'noRedirect',
    name: 'Scenario module',
    meta: { title: 'Scenario module', icon: 'el-icon-s-data' },
    children: [
      {
        path: 'cash',
        name: 'Credit card cash-out',
        component: () => import('@/views/factory/creditCardCash'),
        meta: { title: 'Credit card cash-out', icon: 'cash' }
      },
      {
        path: 'gamble',
        name: 'Gambling violation',
        component: () => import('@/views/factory/gamblingTrans'),
        meta: { title: 'Gambling violation', icon: 'gamble' }
      },
      {
        path: 'scalper',
        name: 'Scalper marketing',
        component: () => import('@/views/factory/marketingFraud'),
        meta: { title: 'Scalper marketing', icon: 'scalper' }
      },
      {
        path: 'fake',
        name: 'Fake registration',
        component: () => import('@/views/factory/registerFraud'),
        meta: { title: 'Fake registration', icon: 'fake' }
      },
      {
        path: 'illegal',
        name: 'Merchant violation',
        component: () => import('@/views/factory/storeFraud'),
        meta: { title: 'Merchant violation', icon: 'illegal' }
      },
      {
        path: 'transfer',
        name: 'Abnormal transfer',
        component: () => import('@/views/factory/abnormalTrans'),
        meta: { title: 'Abnormal transfer', icon: 'transfer' }
      }
    ]
  },
  // {
  //   path: '/enterpriseDataGenerate',
  //   component: Layout,
  //   redirect: 'noRedirect',
  //   name: '工商企业数据',
  //   meta: { title: '工商企业数据', icon: 'el-icon-s-data' },
  //   children: [
  //     {
  //       path: 'enterprise',
  //       name: '工商企业数据',
  //       component: () => import('@/views/enterprise/index'),
  //       meta: { title: '工商企业数据', icon: 'el-icon-tickets' }
  //     }
  //   ]
  // },
  // {
  //   path: '/operatorDataGenerate',
  //   component: Layout,
  //   redirect: 'noRedirect',
  //   name: '运营商数据',
  //   meta: { title: '运营商数据', icon: 'el-icon-s-claim' },
  //   children: [
  //     {
  //       path: 'operator',
  //       name: '运营商数据',
  //       component: () => import('@/views/operator/index'),
  //       meta: { title: '运营商数据', icon: 'el-icon-data-analysis' }
  //     }
  //   ]
  // },

  // 404 page must be placed at the end !!!
  { path: '*', redirect: '/404', hidden: true }
]

const createRouter = () => new Router({
  // mode: 'history', // require service support
  scrollBehavior: () => ({ y: 0 }),
  routes: constantRoutes
})

const router = createRouter()

// Detail see: https://github.com/vuejs/vue-router/issues/1234#issuecomment-357941465
export function resetRouter() {
  const newRouter = createRouter()
  router.matcher = newRouter.matcher // reset router
}

export default router
