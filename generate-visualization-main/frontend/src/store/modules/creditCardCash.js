import {
  cardGenerateCredit, cardInitCredit,
  durationChooseCredit, durationSetCredit,
  storeGenerateCredit, storeInitCredit,
  userGenerateCredit, userInitCredit,
  creditInit, creditGenerate,
  transferInitCredit, transferGenerateCredit,
  consumeInitCredit, consumeGenerateCredit,
  creditRecreateTable
} from '@/api/creditCardCash'

const getDefaultState = () => {
  return {
    credit_user_data: '',
    credit_store_data: '',
    credit_card_data: '',
    credit_date_data: '',
    credit_consume_data: '',
    credit_transfer_data: '',
    credit_data: '',
    credit_recreate_data: '' // 删库
  }
}

const state = getDefaultState()

const mutations = {
  SET_credit_USER: (state, credit_user_data) => {
    state.credit_user_data = credit_user_data
  },
  SET_credit_STORE: (state, credit_store_data) => {
    state.credit_store_data = credit_store_data
  },
  SET_credit_CARD: (state, credit_card_data) => {
    state.credit_card_data = credit_card_data
  },
  SET_credit_DATE: (state, credit_date_data) => {
    state.credit_date_data = credit_date_data
  },
  SET_credit_CONSUME: (state, credit_consume_data) => {
    state.credit_consume_data = credit_consume_data
  },
  SET_credit_TRANSFER: (state, credit_transfer_data) => {
    state.credit_transfer_data = credit_transfer_data
  },
  SET_CREDIT: (state, credit_data) => {
    state.credit_data = credit_data
  },
  SET_credit_RECREATE: (state, credit_recreate_data) => {
    state.credit_recreate_data = credit_recreate_data
  }
}

const actions = {
  durationChooseCredit({ commit, state }, date) {
    return new Promise((resolve, reject) => {
      console.log('日期选择')
      const payload = { 'date': date }
      durationChooseCredit(payload).then(response => {
        const { data } = response
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        const credit_date_data = data
        commit('SET_credit_DATE', credit_date_data)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },
  durationSetCredit({ commit }) {
    return new Promise((resolve, reject) => {
      durationSetCredit().then(response => {
        const { data } = response
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        const credit_date_data = data
        commit('SET_credit_DATE', credit_date_data)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },

  userGenerateCredit({ commit, state }, num) {
    return new Promise((resolve, reject) => {
      console.log('用户生成')
      const payload = { 'total': num }
      userGenerateCredit(payload).then(response => {
        const { data } = response
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        const credit_user_data = data
        commit('SET_credit_USER', credit_user_data)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },
  userInitCredit({ commit, state }) {
    return new Promise((resolve, reject) => {
      console.log('用户初始化')
      userInitCredit().then(response => {
        const { data } = response
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        const user_credit_data = data
        commit('SET_credit_USER', user_credit_data)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },

  storeGenerateCredit({ commit, state }, total) {
    return new Promise((resolve, reject) => {
      console.log('商户生成')
      const payload = { 'total': total }
      storeGenerateCredit(payload).then(response => {
        const { data } = response
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        const credit_store_data = data
        commit('SET_credit_STORE', credit_store_data)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },
  storeInitCredit({ commit, state }) {
    return new Promise((resolve, reject) => {
      console.log('商户初始化')
      storeInitCredit().then(response => {
        const { data } = response
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        const credit_store_data = data
        commit('SET_credit_STORE', credit_store_data)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },

  cardGenerateCredit({ commit, state }, is_generate) {
    return new Promise((resolve, reject) => {
      console.log('卡生成')
      const payload = { 'is_generate': is_generate }// 将前端的is_generate数据封装以payload形式发给后端
      cardGenerateCredit(payload).then(response => {
        const { data } = response// 后端返回的数据用data保存
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        const credit_card_data = data
        commit('SET_credit_CARD', credit_card_data)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },
  cardInitCredit({ commit, state }) {
    return new Promise((resolve, reject) => {
      console.log('卡初始化')
      cardInitCredit().then(response => {
        const { data } = response// 后端返回的数据用data保存
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        const credit_card_data = data
        commit('SET_credit_CARD', credit_card_data)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },

  consumeGenerateCredit({ commit }, form) { // 正常消费数据
    const { date, duration } = form
    return new Promise((resolve, reject) => {
      console.log('正常交易生成')
      const payload = {
        'date': date,
        'duration': duration
      }
      consumeGenerateCredit(payload).then(response => {
        const { data } = response
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        const credit_consume_data = data
        commit('SET_credit_CONSUME', credit_consume_data)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },
  consumeInitCredit({ commit }) { // 正常消费数据
    return new Promise((resolve, reject) => {
      console.log('正常交易初始化')
      consumeInitCredit().then(response => {
        const { data } = response
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        const credit_consume_data = data
        commit('SET_credit_CONSUME', credit_consume_data)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },
  transferGenerateCredit({ commit }, form) { // 正常转账数据
    const { date, duration } = form
    return new Promise((resolve, reject) => {
      // console.log('表单信息', form)
      console.log('正常转账生成')
      const payload = {
        'date': date,
        'duration': duration
      }
      transferGenerateCredit(payload).then(response => {
        const { data } = response
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        const credit_transfer_data = data
        commit('SET_credit_TRANSFER', credit_transfer_data)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },
  transferInitCredit({ commit }) { // 正常转账数据
    return new Promise((resolve, reject) => {
      // console.log('表单信息', form)
      console.log('正常转账初始化')
      transferInitCredit().then(response => {
        const { data } = response
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        const credit_transfer_data = data
        commit('SET_credit_TRANSFER', credit_transfer_data)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },
  creditInit({ commit }) { // 信用卡违规套现
    return new Promise((resolve, reject) => {
      console.log('信用卡违规套现初始化')
      creditInit().then(response => {
        const { data } = response
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        const credit_data = data
        commit('SET_CREDIT', credit_data)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },
  creditGenerate({ commit }, form) { // 信用卡违规套现
    const { startDate, shortTime, longTime, user, store, duration, personalRatio, storeRatio, storeMin, storeMax, openTime } = form
    return new Promise((resolve, reject) => {
      // console.log('表单信息', form)
      console.log('信用卡违规套现生成')
      const payload = {
        'small_fraud_gap': shortTime,
        'big_fraud_gap': longTime,
        'date': startDate,
        'user_quantity': user,
        'store_quantity': store,
        'duration': duration,
        'personal_cash_out_ratio': personalRatio,
        'personal_store_ratio': storeRatio,
        'store_group_size_min': storeMin,
        'store_group_size_max': storeMax,
        'is_in_opening_time': openTime
      }
      creditGenerate(payload).then(response => {
        const { data } = response
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        const credit_data = data
        commit('SET_CREDIT', credit_data)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },

  // 删除历史数据并重新建表
  creditRecreateTable({ commit }, is_delete) {
    return new Promise(resolve => {
      console.log('删除历史数据开始')
      const payload = { 'is_recreate': is_delete }
      creditRecreateTable(payload).then(response => {
        const { data } = response// 后端返回的数据用data保存
        if (!data) {
          return false
        }
        const credit_recreate_data = data
        commit('SET_credit_RECREATE', credit_recreate_data)
        resolve(data)
      })
    })
  }
}

export default {
  namespaced: true,
  state,
  mutations,
  actions
}
