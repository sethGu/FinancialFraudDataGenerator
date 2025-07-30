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
      console.log('Date selection')
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
      console.log('User generation')
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
      console.log('User initialization')
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
      console.log('Merchant generation')
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
      console.log('Merchant initialization')
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
      console.log('Card generation')
      const payload = { 'is_generate': is_generate }
      cardGenerateRegister(payload).then(response => {
        const { data } = response
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
      console.log('Card initialization')
      cardInitRegister().then(response => {
        const { data } = response
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

  consumeGenerateRegister({ commit }, form) {
    const { date, duration } = form
    return new Promise((resolve, reject) => {
      console.log('Normal transaction generation')
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
  consumeInitRegister({ commit }) {
    return new Promise((resolve, reject) => {
      console.log('Normal transaction initialization')
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
  transferGenerateRegister({ commit }, form) {
    const { date, duration } = form
    return new Promise((resolve, reject) => {
      console.log('Normal transfer generation')
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
  transferInitRegister({ commit }) {
    return new Promise((resolve, reject) => {
      console.log('Normal transfer initialization')
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

  registerFraudInit({ commit }) {
    return new Promise((resolve, reject) => {
      console.log('Fake registration initialization')
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
  registerFraudGenerate({ commit }, form) {
    const { startDate, number_of_victims } = form
    return new Promise((resolve, reject) => {
      console.log('Fake registration generation')
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
  registerRecreateTable({ commit }, is_delete) {
    return new Promise(resolve => {
      console.log('Delete historical data start')
      const payload = { 'is_recreate': is_delete }
      registerRecreateTable(payload).then(response => {
        const { data } = response
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
