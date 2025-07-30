import {
  cardGenerateMarketing, cardInitMarketing,
  durationChooseMarketing, durationSetMarketing,
  storeGenerateMarketing, storeInitMarketing,
  userGenerateMarketing, userInitMarketing,
  marketingInit, marketingGenerate,
  transferInitMarketing, transferGenerateMarketing,
  consumeInitMarketing, consumeGenerateMarketing,
  marketingRecreateTable
} from '@/api/marketing'

const getDefaultState = () => {
  return {
    marketing_user_data: '',
    marketing_store_data: '',
    marketing_card_data: '',
    marketing_date_data: '',
    marketing_consume_data: '',
    marketing_transfer_data: '',
    marketing_data: '',
    marketing_recreate_data: ''
  }
}

const state = getDefaultState()

const mutations = {
  SET_marketing_USER: (state, marketing_user_data) => {
    state.marketing_user_data = marketing_user_data
  },
  SET_marketing_STORE: (state, marketing_store_data) => {
    state.marketing_store_data = marketing_store_data
  },
  SET_marketing_CARD: (state, marketing_card_data) => {
    state.marketing_card_data = marketing_card_data
  },
  SET_marketing_DATE: (state, marketing_date_data) => {
    state.marketing_date_data = marketing_date_data
  },
  SET_marketing_CONSUME: (state, marketing_consume_data) => {
    state.marketing_consume_data = marketing_consume_data
  },
  SET_marketing_TRANSFER: (state, marketing_transfer_data) => {
    state.marketing_transfer_data = marketing_transfer_data
  },
  SET_MARKETING: (state, marketing_data) => {
    state.marketing_data = marketing_data
  },
  SET_marketing_RECREATE: (state, marketing_recreate_data) => {
    state.marketing_recreate_data = marketing_recreate_data
  }
}

const actions = {
  durationChooseMarketing({ commit, state }, date) {
    return new Promise((resolve, reject) => {
      console.log('Date selection')
      const payload = { 'date': date }
      durationChooseMarketing(payload).then(response => {
        const { data } = response
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        const marketing_date_data = data
        commit('SET_marketing_DATE', marketing_date_data)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },
  durationSetMarketing({ commit }) {
    return new Promise((resolve, reject) => {
      durationSetMarketing().then(response => {
        const { data } = response
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        const marketing_date_data = data
        commit('SET_marketing_DATE', marketing_date_data)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },

  userGenerateMarketing({ commit, state }, num) {
    return new Promise((resolve, reject) => {
      console.log('User generation')
      const payload = { 'total': num }
      userGenerateMarketing(payload).then(response => {
        const { data } = response
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        const marketing_user_data = data
        commit('SET_marketing_USER', marketing_user_data)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },
  userInitMarketing({ commit, state }) {
    return new Promise((resolve, reject) => {
      console.log('User initialization')
      userInitMarketing().then(response => {
        const { data } = response
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        const user_marketing_data = data
        commit('SET_marketing_USER', user_marketing_data)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },

  storeGenerateMarketing({ commit, state }, total) {
    return new Promise((resolve, reject) => {
      console.log('Merchant generation')
      const payload = { 'total': total }
      storeGenerateMarketing(payload).then(response => {
        const { data } = response
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        const marketing_store_data = data
        commit('SET_marketing_STORE', marketing_store_data)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },
  storeInitMarketing({ commit, state }) {
    return new Promise((resolve, reject) => {
      console.log('Merchant initialization')
      storeInitMarketing().then(response => {
        const { data } = response
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        const marketing_store_data = data
        commit('SET_marketing_STORE', marketing_store_data)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },

  cardGenerateMarketing({ commit, state }, is_generate) {
    return new Promise((resolve, reject) => {
      console.log('Card generation')
      const payload = { 'is_generate': is_generate }
      cardGenerateMarketing(payload).then(response => {
        const { data } = response
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        const marketing_card_data = data
        commit('SET_marketing_CARD', marketing_card_data)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },
  cardInitMarketing({ commit, state }) {
    return new Promise((resolve, reject) => {
      console.log('Card initialization')
      cardInitMarketing().then(response => {
        const { data } = response
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        const marketing_card_data = data
        commit('SET_marketing_CARD', marketing_card_data)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },

  consumeGenerateMarketing({ commit }, form) {
    const { date, duration } = form
    return new Promise((resolve, reject) => {
      console.log('Normal transaction generation')
      const payload = {
        'date': date,
        'duration': duration
      }
      consumeGenerateMarketing(payload).then(response => {
        const { data } = response
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        const marketing_consume_data = data
        commit('SET_marketing_CONSUME', marketing_consume_data)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },
  consumeInitMarketing({ commit }) {
    return new Promise((resolve, reject) => {
      console.log('Normal transaction initialization')
      consumeInitMarketing().then(response => {
        const { data } = response
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        const marketing_consume_data = data
        commit('SET_marketing_CONSUME', marketing_consume_data)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },
  transferGenerateMarketing({ commit }, form) {
    const { date, duration } = form
    return new Promise((resolve, reject) => {
      console.log('Normal transfer generation')
      const payload = {
        'date': date,
        'duration': duration
      }
      transferGenerateMarketing(payload).then(response => {
        const { data } = response
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        const marketing_transfer_data = data
        commit('SET_marketing_TRANSFER', marketing_transfer_data)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },
  transferInitMarketing({ commit }) {
    return new Promise((resolve, reject) => {
      console.log('Normal transfer initialization')
      transferInitMarketing().then(response => {
        const { data } = response
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        const marketing_transfer_data = data
        commit('SET_marketing_TRANSFER', marketing_transfer_data)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },
  marketingInit({ commit }) {
    return new Promise((resolve, reject) => {
      console.log('Scalper marketing fraud initialization')
      marketingInit().then(response => {
        const { data } = response
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        const marketing_data = data
        commit('SET_MARKETING', marketing_data)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },
  marketingGenerate({ commit }, form) {
    const { startDate, duration, store, user, openTime, clothRatio, serviceRatio } = form
    return new Promise((resolve, reject) => {
      console.log('Scalper marketing fraud generation')
      const payload = {
        'date': startDate,
        'duration': duration,
        'store_quantity': store,
        'fraud_user_quantity': user,
        'is_in_opening_time': openTime,
        'cloth_ratio': clothRatio,
        'life_service_ratio': serviceRatio
      }
      marketingGenerate(payload).then(response => {
        const { data } = response
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        const marketing_data = data
        commit('SET_MARKETING', marketing_data)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },
  marketingRecreateTable({ commit }, is_delete) {
    return new Promise(resolve => {
      console.log('Delete historical data start')
      const payload = { 'is_recreate': is_delete }
      marketingRecreateTable(payload).then(response => {
        const { data } = response
        if (!data) {
          return false
        }
        const marketing_recreate_data = data
        commit('SET_marketing_RECREATE', marketing_recreate_data)
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
