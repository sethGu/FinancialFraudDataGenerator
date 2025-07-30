import {
  cardGenerateGambling, cardInitGambling,
  durationChooseGambling, durationSetGambling,
  storeGenerateGambling, storeInitGambling,
  userGenerateGambling, userInitGambling,
  gamblingInit, gamblingGenerate,
  transferInitGambling, transferGenerateGambling,
  consumeInitGambling, consumeGenerateGambling,
  gamblingRecreateTable
} from '@/api/gambling'

const getDefaultState = () => {
  return {
    gambling_user_data: '',
    gambling_store_data: '',
    gambling_card_data: '',
    gambling_date_data: '',
    gambling_consume_data: '',
    gambling_transfer_data: '',
    gambling_data: '',
    gambling_recreate_data: '',
    gambleModel_data: '',
    gambleTest_data: ''
  }
}

const state = getDefaultState()

const mutations = {
  SET_gambling_USER: (state, gambling_user_data) => {
    state.gambling_user_data = gambling_user_data
  },
  SET_gambling_STORE: (state, gambling_store_data) => {
    state.gambling_store_data = gambling_store_data
  },
  SET_gambling_CARD: (state, gambling_card_data) => {
    state.gambling_card_data = gambling_card_data
  },
  SET_gambling_DATE: (state, gambling_date_data) => {
    state.gambling_date_data = gambling_date_data
  },
  SET_gambling_CONSUME: (state, gambling_consume_data) => {
    state.gambling_consume_data = gambling_consume_data
  },
  SET_gambling_TRANSFER: (state, gambling_transfer_data) => {
    state.gambling_transfer_data = gambling_transfer_data
  },
  SET_GAMBLING: (state, gambling_data) => {
    state.gambling_data = gambling_data
  },
  SET_gambling_RECREATE: (state, gambling_recreate_data) => {
    state.gambling_recreate_data = gambling_recreate_data
  }
}

const actions = {
  durationChooseGambling({ commit, state }, date) {
    return new Promise((resolve, reject) => {
      console.log('Date selection')
      const payload = { 'date': date }
      durationChooseGambling(payload).then(response => {
        const { data } = response
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        const gambling_date_data = data
        commit('SET_gambling_DATE', gambling_date_data)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },
  durationSetGambling({ commit }) {
    return new Promise((resolve, reject) => {
      durationSetGambling().then(response => {
        const { data } = response
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        const gambling_date_data = data
        commit('SET_gambling_DATE', gambling_date_data)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },

  userGenerateGambling({ commit, state }, num) {
    return new Promise((resolve, reject) => {
      console.log('User generation')
      const payload = { 'total': num }
      userGenerateGambling(payload).then(response => {
        const { data } = response
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        const gambling_user_data = data
        commit('SET_gambling_USER', gambling_user_data)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },
  userInitGambling({ commit, state }) {
    return new Promise((resolve, reject) => {
      console.log('User initialization')
      userInitGambling().then(response => {
        const { data } = response
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        const user_gambling_data = data
        commit('SET_gambling_USER', user_gambling_data)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },

  storeGenerateGambling({ commit, state }, total) {
    return new Promise((resolve, reject) => {
      console.log('Merchant generation')
      const payload = { 'total': total }
      storeGenerateGambling(payload).then(response => {
        const { data } = response
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        const gambling_store_data = data
        commit('SET_gambling_STORE', gambling_store_data)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },
  storeInitGambling({ commit, state }) {
    return new Promise((resolve, reject) => {
      console.log('Merchant initialization')
      storeInitGambling().then(response => {
        const { data } = response
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        const gambling_store_data = data
        commit('SET_gambling_STORE', gambling_store_data)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },

  cardGenerateGambling({ commit, state }, is_generate) {
    return new Promise((resolve, reject) => {
      console.log('Card generation')
      const payload = { 'is_generate': is_generate }
      cardGenerateGambling(payload).then(response => {
        const { data } = response
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        const gambling_card_data = data
        commit('SET_gambling_CARD', gambling_card_data)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },
  cardInitGambling({ commit, state }) {
    return new Promise((resolve, reject) => {
      console.log('Card initialization')
      cardInitGambling().then(response => {
        const { data } = response
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        const gambling_card_data = data
        commit('SET_gambling_CARD', gambling_card_data)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },

  consumeGenerateGambling({ commit }, form) {
    const { date, duration } = form
    return new Promise((resolve, reject) => {
      console.log('Normal transaction generation')
      const payload = {
        'date': date,
        'duration': duration
      }
      consumeGenerateGambling(payload).then(response => {
        const { data } = response
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        const gambling_consume_data = data
        commit('SET_gambling_CONSUME', gambling_consume_data)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },
  consumeInitGambling({ commit }) {
    return new Promise((resolve, reject) => {
      console.log('Normal transaction initialization')
      consumeInitGambling().then(response => {
        const { data } = response
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        const gambling_consume_data = data
        commit('SET_gambling_CONSUME', gambling_consume_data)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },
  transferGenerateGambling({ commit }, form) {
    const { date, duration } = form
    return new Promise((resolve, reject) => {
      console.log('Normal transfer generation')
      const payload = {
        'date': date,
        'duration': duration
      }
      transferGenerateGambling(payload).then(response => {
        const { data } = response
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        const gambling_transfer_data = data
        commit('SET_gambling_TRANSFER', gambling_transfer_data)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },
  transferInitGambling({ commit }) {
    return new Promise((resolve, reject) => {
      console.log('Normal transfer initialization')
      transferInitGambling().then(response => {
        const { data } = response
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        const gambling_transfer_data = data
        commit('SET_gambling_TRANSFER', gambling_transfer_data)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },
  gamblingInit({ commit }) {
    return new Promise((resolve, reject) => {
      console.log('Gambling transaction initialization')
      gamblingInit().then(response => {
        const { data } = response
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        const gambling_data = data
        commit('SET_GAMBLING', gambling_data)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },
  gamblingGenerate({ commit }, form) {
    const { startDate, duration, store, user, isOpenTime, personalTrans, storeLow, storeMiddle, storeHigh, gambleUser } = form
    return new Promise((resolve, reject) => {
      console.log('Gambling transaction generation')
      const payload = {
        'date': startDate,
        'duration': duration,
        'store_quantity': store,
        'user_quantity': user,
        'is_in_opening_time': isOpenTime,
        'personal_trans_time_ratio': personalTrans,
        'low_rank_store_ratio': storeLow,
        'middle_rank_store_ratio': storeMiddle,
        'high_rank_store_ratio': storeHigh,
        'gambling_user_ratio': gambleUser
      }
      gamblingGenerate(payload).then(response => {
        const { data } = response
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        const gambling_data = data
        commit('SET_GAMBLING', gambling_data)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },
  // 删除历史数据并重新建表
  gamblingRecreateTable({ commit }, is_delete) {
    return new Promise(resolve => {
      console.log('Delete historical data start')
      const payload = { 'is_recreate': is_delete }
      gamblingRecreateTable(payload).then(response => {
        const { data } = response
        if (!data) {
          return false
        }
        const gambling_recreate_data = data
        commit('SET_gambling_RECREATE', gambling_recreate_data)
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
