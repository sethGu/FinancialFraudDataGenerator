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
    gambling_recreate_data: '', // 删库
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
  },
}

const actions = {
  durationChooseGambling({ commit, state }, date) {
    return new Promise((resolve, reject) => {
      console.log('日期选择')
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
      console.log('用户生成')
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
      console.log('用户初始化')
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
      console.log('商户生成')
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
      console.log('商户初始化')
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
      console.log('卡生成')
      const payload = { 'is_generate': is_generate }// 将前端的is_generate数据封装以payload形式发给后端
      cardGenerateGambling(payload).then(response => {
        const { data } = response// 后端返回的数据用data保存
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
      console.log('卡初始化')
      cardInitGambling().then(response => {
        const { data } = response// 后端返回的数据用data保存
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

  consumeGenerateGambling({ commit }, form) { // 正常消费数据
    const { date, duration } = form
    return new Promise((resolve, reject) => {
      console.log('正常交易生成')
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
  consumeInitGambling({ commit }) { // 正常消费数据
    return new Promise((resolve, reject) => {
      console.log('正常交易初始化')
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
  transferGenerateGambling({ commit }, form) { // 正常转账数据
    const { date, duration } = form
    return new Promise((resolve, reject) => {
      // console.log('表单信息', form)
      console.log('正常转账生成')
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
  transferInitGambling({ commit }) { // 正常转账数据
    return new Promise((resolve, reject) => {
      // console.log('表单信息', form)
      console.log('正常转账初始化')
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
  gamblingInit({ commit }) { // 赌博交易
    return new Promise((resolve, reject) => {
      console.log('赌博交易初始化')
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
  gamblingGenerate({ commit }, form) { // 赌博交易
    const { startDate, duration, store, user, isOpenTime, personalTrans, storeLow, storeMiddle, storeHigh, gambleUser } = form
    return new Promise((resolve, reject) => {
      console.log('赌博交易生成')
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
      console.log('删除历史数据开始')
      const payload = { 'is_recreate': is_delete }
      gamblingRecreateTable(payload).then(response => {
        const { data } = response// 后端返回的数据用data保存
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
