import {
  cardGenerateStoreFraud, cardInitStoreFraud,
  durationChooseStoreFraud, durationSetStoreFraud,
  storeGenerateStoreFraud, storeInitStoreFraud,
  userGenerateStoreFraud, userInitStoreFraud,
  storeFraudInit, storeFraudGenerate,
  transferInitStoreFraud, transferGenerateStoreFraud,
  consumeInitStoreFraud, consumeGenerateStoreFraud,
  storeFraudRecreateTable
} from '@/api/storeFraud'

const getDefaultState = () => {
  return {
    storeFraud_user_data: '',
    storeFraud_store_data: '',
    storeFraud_card_data: '',
    storeFraud_date_data: '',
    storeFraud_consume_data: '',
    storeFraud_transfer_data: '',
    storeFraud_data: '',
    storeFraud_recreate_data: '' // 删库
  }
}

const state = getDefaultState()

const mutations = {
  SET_storeFraud_USER: (state, storeFraud_user_data) => {
    state.storeFraud_user_data = storeFraud_user_data
  },
  SET_storeFraud_STORE: (state, storeFraud_store_data) => {
    state.storeFraud_store_data = storeFraud_store_data
  },
  SET_storeFraud_CARD: (state, storeFraud_card_data) => {
    state.storeFraud_card_data = storeFraud_card_data
  },
  SET_storeFraud_DATE: (state, storeFraud_date_data) => {
    state.storeFraud_date_data = storeFraud_date_data
  },
  SET_storeFraud_CONSUME: (state, storeFraud_consume_data) => {
    state.storeFraud_consume_data = storeFraud_consume_data
  },
  SET_storeFraud_TRANSFER: (state, storeFraud_transfer_data) => {
    state.storeFraud_transfer_data = storeFraud_transfer_data
  },
  SET_STOREFRAUD: (state, storeFraud_data) => {
    state.storeFraud_data = storeFraud_data
  },
  SET_storeFraud_RECREATE: (state, storeFraud_recreate_data) => {
    state.storeFraud_recreate_data = storeFraud_recreate_data
  }
}

const actions = {
  durationChooseStoreFraud({ commit, state }, date) {
    return new Promise((resolve, reject) => {
      console.log('日期选择')
      const payload = { 'date': date }
      durationChooseStoreFraud(payload).then(response => {
        const { data } = response
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        const storeFraud_date_data = data
        commit('SET_storeFraud_DATE', storeFraud_date_data)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },
  durationSetStoreFraud({ commit }) {
    return new Promise((resolve, reject) => {
      durationSetStoreFraud().then(response => {
        const { data } = response
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        const storeFraud_date_data = data
        commit('SET_storeFraud_DATE', storeFraud_date_data)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },

  userGenerateStoreFraud({ commit, state }, num) {
    return new Promise((resolve, reject) => {
      console.log('用户生成')
      const payload = { 'total': num }
      userGenerateStoreFraud(payload).then(response => {
        const { data } = response
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        const storeFraud_user_data = data
        commit('SET_storeFraud_USER', storeFraud_user_data)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },
  userInitStoreFraud({ commit, state }) {
    return new Promise((resolve, reject) => {
      console.log('用户初始化')
      userInitStoreFraud().then(response => {
        const { data } = response
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        const user_storeFraud_data = data
        commit('SET_storeFraud_USER', user_storeFraud_data)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },

  storeGenerateStoreFraud({ commit, state }, total) {
    return new Promise((resolve, reject) => {
      console.log('商户生成')
      const payload = { 'total': total }
      storeGenerateStoreFraud(payload).then(response => {
        const { data } = response
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        const storeFraud_store_data = data
        commit('SET_storeFraud_STORE', storeFraud_store_data)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },
  storeInitStoreFraud({ commit, state }) {
    return new Promise((resolve, reject) => {
      console.log('商户初始化')
      storeInitStoreFraud().then(response => {
        const { data } = response
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        const storeFraud_store_data = data
        commit('SET_storeFraud_STORE', storeFraud_store_data)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },

  cardGenerateStoreFraud({ commit, state }, is_generate) {
    return new Promise((resolve, reject) => {
      console.log('卡生成')
      const payload = { 'is_generate': is_generate }// 将前端的is_generate数据封装以payload形式发给后端
      cardGenerateStoreFraud(payload).then(response => {
        const { data } = response// 后端返回的数据用data保存
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        const storeFraud_card_data = data
        commit('SET_storeFraud_CARD', storeFraud_card_data)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },
  cardInitStoreFraud({ commit, state }) {
    return new Promise((resolve, reject) => {
      console.log('卡初始化')
      cardInitStoreFraud().then(response => {
        const { data } = response// 后端返回的数据用data保存
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        const storeFraud_card_data = data
        commit('SET_storeFraud_CARD', storeFraud_card_data)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },

  consumeGenerateStoreFraud({ commit }, form) { // 正常消费数据
    const { date, duration } = form
    return new Promise((resolve, reject) => {
      console.log('正常交易生成')
      const payload = {
        'date': date,
        'duration': duration
      }
      consumeGenerateStoreFraud(payload).then(response => {
        const { data } = response
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        const storeFraud_consume_data = data
        commit('SET_storeFraud_CONSUME', storeFraud_consume_data)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },
  consumeInitStoreFraud({ commit }) { // 正常消费数据
    return new Promise((resolve, reject) => {
      console.log('正常交易初始化')
      consumeInitStoreFraud().then(response => {
        const { data } = response
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        const storeFraud_consume_data = data
        commit('SET_storeFraud_CONSUME', storeFraud_consume_data)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },
  transferGenerateStoreFraud({ commit }, form) { // 正常转账数据
    const { date, duration } = form
    return new Promise((resolve, reject) => {
      // console.log('表单信息', form)
      console.log('正常转账生成')
      const payload = {
        'date': date,
        'duration': duration
      }
      transferGenerateStoreFraud(payload).then(response => {
        const { data } = response
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        const storeFraud_transfer_data = data
        commit('SET_storeFraud_TRANSFER', storeFraud_transfer_data)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },
  transferInitStoreFraud({ commit }) { // 正常转账数据
    return new Promise((resolve, reject) => {
      // console.log('表单信息', form)
      console.log('正常转账初始化')
      transferInitStoreFraud().then(response => {
        const { data } = response
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        const storeFraud_transfer_data = data
        commit('SET_storeFraud_TRANSFER', storeFraud_transfer_data)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },
  storeFraudInit({ commit }) { // 商户违规
    return new Promise((resolve, reject) => {
      console.log('商户违规生成')
      storeFraudInit().then(response => {
        const { data } = response
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        const storeFraud_data = data
        commit('SET_STOREFRAUD', storeFraud_data)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },
  storeFraudGenerate({ commit }, form) { // 商户违规
    const { store, startDate } = form
    return new Promise((resolve, reject) => {
      // console.log('表单信息', form)
      console.log('商户违规生成')
      const payload = {
        'ymd': startDate,
        'number_of_stores': store
      }
      storeFraudGenerate(payload).then(response => {
        const { data } = response
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        const storeFraud_data = data
        commit('SET_STOREFRAUD', storeFraud_data)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },
  // 删除历史数据并重新建表
  storeFraudRecreateTable({ commit }, is_delete) {
    return new Promise(resolve => {
      console.log('删除历史数据开始')
      const payload = { 'is_recreate': is_delete }
      storeFraudRecreateTable(payload).then(response => {
        const { data } = response// 后端返回的数据用data保存
        if (!data) {
          return false
        }
        const storeFraud_recreate_data = data
        commit('SET_storeFraud_RECREATE', storeFraud_recreate_data)
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
