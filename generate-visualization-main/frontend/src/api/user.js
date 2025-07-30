import request from '@/utils/request'
// import axiosInstance from './index'
// const axios = axiosInstance

export function login(data) {
  return request({
    // baseURL: 'http://127.0.0.1:8000/',
    url: '/api/user_login/',
    method: 'post',
    data
  })
}

export function getInfo(token) {
  return request({
    url: 'api/user_info/',
    method: 'get',
    params: { token }
    // headers: { 'Authentication': [token] }
  })
}

export function logout() {
  return request({
    url: 'api/user_logout/',
    method: 'post'
  })
}

export function updatePassword(data) {
  return request({
    url: 'api/user_update_password/',
    method: 'post',
    data
  })
}
