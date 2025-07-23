import Vue from 'vue'
import Vuex from 'vuex'
import getters from './getters'
import app from './modules/app'
import settings from './modules/settings'
import user from './modules/user'
import register from '@/store/modules/register'
import gambling from '@/store/modules/gambling'
import storeFraud from '@/store/modules/storeFraud'
import marketing from '@/store/modules/marketing'
import abnormalTrans from '@/store/modules/abnormalTrans'
import creditCardCash from '@/store/modules/creditCardCash'

Vue.use(Vuex)

const store = new Vuex.Store({
  modules: {
    app,
    settings,
    user,
    register,
    abnormalTrans,
    creditCardCash,
    gambling,
    marketing,
    storeFraud
  },
  getters
})

export default store
