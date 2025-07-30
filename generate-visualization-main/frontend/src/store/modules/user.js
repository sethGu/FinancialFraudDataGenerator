import {logout, getInfo, recreateTable, download, updatePassword} from '@/api/user'
import { getToken, setToken, removeToken } from '@/utils/auth'
import { resetRouter } from '@/router'
import * as user from '@/api/user'

const getDefaultState = () => {
  return {
    token: getToken(),
    name: '',
    avatar: '',
    reCreate_data: ''
  }
}

const state = getDefaultState()

const mutations = {
  RESET_STATE: (state) => {
    Object.assign(state, getDefaultState())
  },
  SET_TOKEN: (state, token) => {
    state.token = token
  },
  SET_NAME: (state, name) => {
    state.name = name
  },
  SET_AVATAR: (state, avatar) => {
    state.avatar = avatar
  },
  SET_RECREATE: (state, reCreate_data) => {
    state.reCreate_data = reCreate_data
  }
}
const actions = {
  // user login
  login({ commit }, userInfo) {
    const { username, password } = userInfo

    return new Promise((resolve, reject) => {
      console.log('userInfo', userInfo)
      const payload = {
        username: username,
        password: password
      }
      user.login(payload).then(response => {
        const { data } = response
        console.log('response', response)
        commit('SET_TOKEN', data.token)
        setToken(data.token)
        resolve()
      }).catch(error => {
        reject(error)
      })
    })
  },

  // update password
  updatePassword({ commit }, userInfo) {
    const { username, oldPassword, newPassword } = userInfo

    return new Promise((resolve, reject) => {
      console.log('userInfo', userInfo)
      const payload = {
        username: username,
        oldPassword: oldPassword,
        newPassword: newPassword
      }
      updatePassword(payload).then(response => {
        const { data } = response
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        if (data.state === false) {
          reject('Incorrect password')
        }
        resolve()
      }).catch(error => {
        reject(error)
      })
    })
  },

  // get user info
  getInfo({ commit, state }) {
    return new Promise((resolve, reject) => {
      getInfo(state.token).then(response => {
        const { data } = response

        if (!data) {
          return reject('Verification failed, please Login again.')
        }

        const {
          // roles,
          name,
          avatar,
          // introduction,
          token } = data

        // commit('SET_ROLES', roles)
        commit('SET_NAME', name)
        commit('SET_AVATAR', avatar)
        // commit('SET_INTRODUCTION', introduction)
        commit('SET_TOKEN', token)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },

  // user logout
  logout({ commit, state }) {
    return new Promise((resolve, reject) => {
      logout(state.token).then(() => {
        removeToken() // must remove  token  first
        resetRouter()
        commit('RESET_STATE')
        resolve()
      }).catch(error => {
        reject(error)
      })
    })
  },

  // remove token
  resetToken({ commit }) {
    return new Promise(resolve => {
      removeToken() // must remove  token  first
      commit('RESET_STATE')
      resolve()
    })
  },
  recreateTable({ commit }, is_delete) {
    return new Promise(resolve => {
      console.log('Delete historical data start')
      const payload = { 'is_recreate': is_delete }
      recreateTable(payload).then(response => {
        const { data } = response
        if (!data) {
          return false
        }
        const reCreate_data = data
        commit('SET_RECREATE', reCreate_data)
        resolve(data)
      })
    })
  },
  download({ state }) {
    return new Promise((resolve, reject) => {
      download(state.token).then(response => {
        const { data } = response
        if (!data) {
          return reject('Verification failed, please Login again.')
        }
      }).catch(error => {
        reject(error)
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
