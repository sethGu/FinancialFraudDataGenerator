import request from '@/utils/request'

export function userGenerateRegister(data) {
  return request({
    url: '/api_register/register/user/',
    method: 'post',
    data
  })
}

export function userInitRegister(data) {
  return request({
    url: '/api_register/register/userInit/',
    method: 'get',
    data
  })
}

export function storeGenerateRegister(data) {
  return request({
    url: '/api_register/register/store/',
    method: 'post',
    data
  })
}

export function storeInitRegister(data) {
  return request({
    url: '/api_register/register/storeInit/',
    method: 'get',
    data
  })
}

export function cardGenerateRegister(data) {
  return request({
    url: '/api_register/register/card/',
    method: 'post',
    data
  })
}

export function cardInitRegister(data) {
  return request({
    url: '/api_register/register/cardInit/',
    method: 'get',
    data
  })
}

export function durationChooseRegister(data) {
  return request({
    url: '/api_register/register/durationChoose/',
    method: 'post',
    data
  })
}

export function durationSetRegister(data) {
  return request({
    url: '/api_register/register/durationSet/',
    method: 'get',
    data
  })
}

export function consumeGenerateRegister(data) {
  return request({
    url: '/api_register/register/consumption/',
    method: 'post',
    data
  })
}

export function consumeInitRegister(data) {
  return request({
    url: '/api_register/register/consumptionInit/',
    method: 'get',
    data
  })
}

export function transferGenerateRegister(data) {
  return request({
    url: '/api_register/register/transfer/',
    method: 'post',
    data
  })
}

export function transferInitRegister(data) {
  return request({
    url: '/api_register/register/transferInit/',
    method: 'get',
    data
  })
}

export function registerFraudInit(data) {
  return request({
    url: '/api_register/register/registerFraudInit/',
    method: 'get',
    data
  })
}

export function registerFraudGenerate(data) {
  return request({
    url: '/api_register/register/registerFraud/',
    method: 'post',
    data
  })
}

// 删除历史数据并重新建表
export function registerRecreateTable(data) {
  return request({
    url: '/api_register/register/RecreateTable/',
    method: 'post',
    data
  })
}
