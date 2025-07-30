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
    credit_recreate_data: ''
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
      console.log('Date selection')
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
      console.log('User generation')
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
      console.log('User initialization')
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
      console.log('Merchant generation')
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
      console.log('Merchant initialization')
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
      console.log('Card generation')
      const payload = { 'is_generate': is_generate }
      cardGenerateCredit(payload).then(response => {
        const { data } = response
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
      console.log('Card initialization')
      cardInitCredit().then(response => {
        const { data } = response
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

  consumeGenerateCredit({ commit }, form) {
    const { date, duration } = form
    return new Promise((resolve, reject) => {
      console.log('Normal transaction generation')
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
  consumeInitCredit({ commit }) {
    return new Promise((resolve, reject) => {
      console.log('Normal transaction initialization')
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
  transferGenerateCredit({ commit }, form) {
    const { date, duration } = form
    return new Promise((resolve, reject) => {
      console.log('Normal transfer generation')
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
  transferInitCredit({ commit }) {
    return new Promise((resolve, reject) => {
      console.log('Normal transfer initialization')
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
  creditInit({ commit }) {
    return new Promise((resolve, reject) => {
      console.log('Credit card fraudulent cash withdrawal initialization')
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
  creditGenerate({ commit }, form) {
    const { startDate, shortTime, longTime, user, store, duration, personalRatio, storeRatio, storeMin, storeMax, openTime } = form
    return new Promise((resolve, reject) => {
      console.log('Credit card fraudulent cash withdrawal generation')
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
  creditRecreateTable({ commit }, is_delete) {
    return new Promise(resolve => {
      console.log('Delete historical data start')
      const payload = { 'is_recreate': is_delete }
      creditRecreateTable(payload).then(response => {
        const { data } = response
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
