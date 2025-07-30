import {
  cardGenerateAbnormal, cardInitAbnormal,
  durationChooseAbnormal, durationSetAbnormal,
  storeGenerateAbnormal, storeInitAbnormal,
  userGenerateAbnormal, userInitAbnormal,
  abnormalGenerate, abnormalInit,
  transferGenerateAbnormal, transferInitAbnormal,
  consumeGenerateAbnormal, consumeInitAbnormal,
  abnormalRecreateTable
} from '@/api/abnormalTrans'

const getDefaultState = () => {
  return {
    abnormal_user_data: '',
    abnormal_store_data: '',
    abnormal_card_data: '',
    abnormal_date_data: '',
    abnormal_consume_data: '',
    abnormal_transfer_data: '',
    abnormal_data: '',
    abnormal_recreate_data: ''
  }
}

const state = getDefaultState()

const mutations = {
  SET_abnormal_USER: (state, abnormal_user_data) => {
    state.abnormal_user_data = abnormal_user_data
  },
  SET_abnormal_STORE: (state, abnormal_store_data) => {
    state.abnormal_store_data = abnormal_store_data
  },
  SET_abnormal_CARD: (state, abnormal_card_data) => {
    state.abnormal_card_data = abnormal_card_data
  },
  SET_abnormal_DATE: (state, abnormal_date_data) => {
    state.abnormal_date_data = abnormal_date_data
  },
  SET_abnormal_CONSUME: (state, abnormal_consume_data) => {
    state.abnormal_consume_data = abnormal_consume_data
  },
  SET_abnormal_TRANSFER: (state, abnormal_transfer_data) => {
    state.abnormal_transfer_data = abnormal_transfer_data
  },
  SET_ABNORMAL: (state, abnormal_data) => {
    state.abnormal_data = abnormal_data
  },
  SET_abnormal_RECREATE: (state, abnormal_recreate_data) => {
    state.abnormal_recreate_data = abnormal_recreate_data
  }
}

const actions = {
  durationChooseAbnormal({ commit, state }, date) {
    return new Promise((resolve, reject) => {
      console.log('Date selection')
      const payload = { 'date': date }
      durationChooseAbnormal(payload).then(response => {
        const { data } = response
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        const abnormal_date_data = data
        commit('SET_abnormal_DATE', abnormal_date_data)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },
  durationSetAbnormal({ commit }) {
    return new Promise((resolve, reject) => {
      durationSetAbnormal().then(response => {
        const { data } = response
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        const abnormal_date_data = data
        commit('SET_abnormal_DATE', abnormal_date_data)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },

  userGenerateAbnormal({ commit, state }, num) {
    return new Promise((resolve, reject) => {
      console.log('User generation')
      const payload = { 'total': num }
      userGenerateAbnormal(payload).then(response => {
        const { data } = response
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        const abnormal_user_data = data
        commit('SET_abnormal_USER', abnormal_user_data)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },
  userInitAbnormal({ commit, state }) {
    return new Promise((resolve, reject) => {
      console.log('User initialization')
      userInitAbnormal().then(response => {
        const { data } = response
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        const user_abnormal_data = data
        commit('SET_abnormal_USER', user_abnormal_data)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },

  storeGenerateAbnormal({ commit, state }, total) {
    return new Promise((resolve, reject) => {
      console.log('Merchant generation')
      const payload = { 'total': total }
      storeGenerateAbnormal(payload).then(response => {
        const { data } = response
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        const abnormal_store_data = data
        commit('SET_abnormal_STORE', abnormal_store_data)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },
  storeInitAbnormal({ commit, state }) {
    return new Promise((resolve, reject) => {
      console.log('Merchant initialization')
      storeInitAbnormal().then(response => {
        const { data } = response
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        const abnormal_store_data = data
        commit('SET_abnormal_STORE', abnormal_store_data)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },

  cardGenerateAbnormal({ commit, state }, is_generate) {
    return new Promise((resolve, reject) => {
      console.log('Card generation')
      const payload = { 'is_generate': is_generate }
      cardGenerateAbnormal(payload).then(response => {
        const { data } = response
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        const abnormal_card_data = data
        commit('SET_abnormal_CARD', abnormal_card_data)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },
  cardInitAbnormal({ commit, state }) {
    return new Promise((resolve, reject) => {
      console.log('Card initialization')
      cardInitAbnormal().then(response => {
        const { data } = response
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        const abnormal_card_data = data
        commit('SET_abnormal_CARD', abnormal_card_data)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },

  consumeGenerateAbnormal({ commit }, form) {
    const { date, duration } = form
    return new Promise((resolve, reject) => {
      console.log('Normal transaction generation')
      const payload = {
        'date': date,
        'duration': duration
      }
      consumeGenerateAbnormal(payload).then(response => {
        const { data } = response
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        const abnormal_consume_data = data
        commit('SET_abnormal_CONSUME', abnormal_consume_data)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },
  consumeInitAbnormal({ commit }) {
    return new Promise((resolve, reject) => {
      console.log('Normal transaction initialization')
      consumeInitAbnormal().then(response => {
        const { data } = response
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        const abnormal_consume_data = data
        commit('SET_abnormal_CONSUME', abnormal_consume_data)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },
  transferGenerateAbnormal({ commit }, form) {
    const { date, duration } = form
    return new Promise((resolve, reject) => {
      console.log('Normal transfer generation')
      const payload = {
        'date': date,
        'duration': duration
      }
      transferGenerateAbnormal(payload).then(response => {
        const { data } = response
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        const abnormal_transfer_data = data
        commit('SET_abnormal_TRANSFER', abnormal_transfer_data)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },
  transferInitAbnormal({ commit }) {
    return new Promise((resolve, reject) => {
      console.log('Normal transfer initialization')
      transferInitAbnormal().then(response => {
        const { data } = response
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        const abnormal_transfer_data = data
        commit('SET_abnormal_TRANSFER', abnormal_transfer_data)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },

  abnormalInit({ commit }) {
    return new Promise((resolve, reject) => {
      console.log('Abnormal transfer transaction initialization')
      abnormalInit().then(response => {
        const { data } = response
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        const abnormal_data = data
        commit('SET_ABNORMAL', abnormal_data)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },
  abnormalGenerate({ commit }, form) {
    const { gang, startDate, duration } = form
    return new Promise((resolve, reject) => {
      console.log('Abnormal transfer transaction generation')
      const payload = {
        'gang_num': gang,
        'start_date': startDate,
        'duration': duration
      }
      abnormalGenerate(payload).then(response => {
        const { data } = response
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        const abnormal_data = data
        commit('SET_ABNORMAL', abnormal_data)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },
  abnormalRecreateTable({ commit }, is_delete) {
    return new Promise(resolve => {
      console.log('Delete historical data start')
      const payload = { 'is_recreate': is_delete }
      abnormalRecreateTable(payload).then(response => {
        const { data } = response
        if (!data) {
          return false
        }
        const abnormal_recreate_data = data
        commit('SET_abnormal_RECREATE', abnormal_recreate_data)
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
