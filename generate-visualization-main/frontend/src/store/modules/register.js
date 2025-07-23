import {
  cardGenerateRegister, cardInitRegister,
  durationChooseRegister, durationSetRegister,
  storeGenerateRegister, storeInitRegister,
  userGenerateRegister, userInitRegister,
  registerFraudGenerate, registerFraudInit,
  transferInitRegister, transferGenerateRegister,
  consumeInitRegister, consumeGenerateRegister,
  registerRecreateTable
} from '@/api/register'

const getDefaultState = () => {
  return {
    register_user_data: '',
    register_store_data: '',
    register_card_data: '',
    register_date_data: '',
    register_consume_data: '',
    register_transfer_data: '',
    registerFraud_data: '',
    register_recreate_data: ''
  }
}

const state = getDefaultState()

const mutations = {
  SET_register_USER: (state, register_user_data) => {
    state.register_user_data = register_user_data
  },
  SET_register_STORE: (state, register_store_data) => {
    state.register_store_data = register_store_data
  },
  SET_register_CARD: (state, register_card_data) => {
    state.register_card_data = register_card_data
  },
  SET_register_DATE: (state, register_date_data) => {
    state.register_date_data = register_date_data
  },
  SET_register_CONSUME: (state, register_consume_data) => {
    state.register_consume_data = register_consume_data
  },
  SET_register_TRANSFER: (state, register_transfer_data) => {
    state.register_transfer_data = register_transfer_data
  },
  SET_register_RECREATE: (state, register_recreate_data) => {
    state.register_recreate_data = register_recreate_data
  },
  SET_REGISTERFRAUD: (state, registerFraud_data) => {
    state.registerFraud_data = registerFraud_data
  }
}

const actions = {
  durationChooseRegister({ commit, state }, date) {
    return new Promise((resolve, reject) => {
      console.log('日期选择')
      const payload = { 'date': date }
      durationChooseRegister(payload).then(response => {
        const { data } = response
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        const register_date_data = data
        commit('SET_register_DATE', register_date_data)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },
  durationSetRegister({ commit }) {
    return new Promise((resolve, reject) => {
      durationSetRegister().then(response => {
        const { data } = response
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        const register_date_data = data
        commit('SET_register_DATE', register_date_data)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },

  userGenerateRegister({ commit, state }, num) {
    return new Promise((resolve, reject) => {
      console.log('用户生成')
      const payload = { 'total': num }
      userGenerateRegister(payload).then(response => {
        const { data } = response
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        const register_user_data = data
        commit('SET_register_USER', register_user_data)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },
  userInitRegister({ commit, state }) {
    return new Promise((resolve, reject) => {
      console.log('用户初始化')
      userInitRegister().then(response => {
        const { data } = response
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        const user_register_data = data
        commit('SET_register_USER', user_register_data)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },

  storeGenerateRegister({ commit, state }, total) {
    return new Promise((resolve, reject) => {
      console.log('商户生成')
      const payload = { 'total': total }
      storeGenerateRegister(payload).then(response => {
        const { data } = response
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        const register_store_data = data
        commit('SET_register_STORE', register_store_data)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },
  storeInitRegister({ commit, state }) {
    return new Promise((resolve, reject) => {
      console.log('商户初始化')
      storeInitRegister().then(response => {
        const { data } = response
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        const register_store_data = data
        commit('SET_register_STORE', register_store_data)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },

  cardGenerateRegister({ commit, state }, is_generate) {
    return new Promise((resolve, reject) => {
      console.log('卡生成')
      const payload = { 'is_generate': is_generate }// 将前端的is_generate数据封装以payload形式发给后端
      cardGenerateRegister(payload).then(response => {
        const { data } = response// 后端返回的数据用data保存
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        const register_card_data = data
        commit('SET_register_CARD', register_card_data)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },
  cardInitRegister({ commit, state }) {
    return new Promise((resolve, reject) => {
      console.log('卡初始化')
      cardInitRegister().then(response => {
        const { data } = response// 后端返回的数据用data保存
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        const register_card_data = data
        commit('SET_register_CARD', register_card_data)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },

  consumeGenerateRegister({ commit }, form) { // 正常消费数据
    const { date, duration } = form
    return new Promise((resolve, reject) => {
      console.log('正常交易生成')
      const payload = {
        'date': date,
        'duration': duration
      }
      consumeGenerateRegister(payload).then(response => {
        const { data } = response
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        const register_consume_data = data
        commit('SET_register_CONSUME', register_consume_data)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },
  consumeInitRegister({ commit }) { // 正常消费数据
    return new Promise((resolve, reject) => {
      console.log('正常交易初始化')
      consumeInitRegister().then(response => {
        const { data } = response
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        const register_consume_data = data
        commit('SET_register_CONSUME', register_consume_data)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },
  transferGenerateRegister({ commit }, form) { // 正常转账数据
    const { date, duration } = form
    return new Promise((resolve, reject) => {
      // console.log('表单信息', form)
      console.log('正常转账生成')
      const payload = {
        'date': date,
        'duration': duration
      }
      transferGenerateRegister(payload).then(response => {
        const { data } = response
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        const register_transfer_data = data
        commit('SET_register_TRANSFER', register_transfer_data)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },
  transferInitRegister({ commit }) { // 正常转账数据
    return new Promise((resolve, reject) => {
      // console.log('表单信息', form)
      console.log('正常转账初始化')
      transferInitRegister().then(response => {
        const { data } = response
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        const register_transfer_data = data
        commit('SET_register_TRANSFER', register_transfer_data)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },

  registerFraudInit({ commit }) { // 伪冒注册
    return new Promise((resolve, reject) => {
      console.log('伪冒注册初始化')
      registerFraudInit().then(response => {
        const { data } = response
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        const registerFraud_data = data
        commit('SET_REGISTERFRAUD', registerFraud_data)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },
  registerFraudGenerate({ commit }, form) { // 伪冒注册
    const { startDate, number_of_victims } = form
    return new Promise((resolve, reject) => {
      // console.log('表单信息', form)
      console.log('伪冒注册生成')
      const payload = {
        'date': startDate,
        'number_of_victims': number_of_victims
      }
      registerFraudGenerate(payload).then(response => {
        const { data } = response
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        const registerFraud_data = data
        commit('SET_REGISTERFRAUD', registerFraud_data)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },
  // 删除历史数据并重新建表
  registerRecreateTable({ commit }, is_delete) {
    return new Promise(resolve => {
      console.log('删除历史数据开始')
      const payload = { 'is_recreate': is_delete }
      registerRecreateTable(payload).then(response => {
        const { data } = response// 后端返回的数据用data保存
        if (!data) {
          return false
        }
        const register_recreate_data = data
        commit('SET_register_RECREATE', register_recreate_data)
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
