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
    storeFraud_recreate_data: ''
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
      console.log('Date selection')
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
      console.log('User generation')
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
      console.log('User initialization')
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
      console.log('Merchant generation')
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
      console.log('Merchant initialization')
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
      console.log('Card generation')
      const payload = { 'is_generate': is_generate }
      cardGenerateStoreFraud(payload).then(response => {
        const { data } = response
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
      console.log('Card initialization')
      cardInitStoreFraud().then(response => {
        const { data } = response
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

  consumeGenerateStoreFraud({ commit }, form) {
    const { date, duration } = form
    return new Promise((resolve, reject) => {
      console.log('Normal transaction generation')
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
  consumeInitStoreFraud({ commit }) {
    return new Promise((resolve, reject) => {
      console.log('Normal transaction initialization')
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
  transferGenerateStoreFraud({ commit }, form) {
    const { date, duration } = form
    return new Promise((resolve, reject) => {
      console.log('Normal transfer generation')
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
  transferInitStoreFraud({ commit }) {
    return new Promise((resolve, reject) => {
      console.log('Normal transfer initialization')
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
  storeFraudInit({ commit }) {
    return new Promise((resolve, reject) => {
      console.log('Merchant violation generation')
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
  storeFraudGenerate({ commit }, form) {
    const { store, startDate } = form
    return new Promise((resolve, reject) => {
      console.log('Merchant violation generation')
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
  storeFraudRecreateTable({ commit }, is_delete) {
    return new Promise(resolve => {
      console.log('Delete historical data start')
      const payload = { 'is_recreate': is_delete }
      storeFraudRecreateTable(payload).then(response => {
        const { data } = response
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
