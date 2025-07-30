import request from '@/utils/request'

export function userGenerateStoreFraud(data) {
  return request({
    url: '/api_store_fraud/store_fraud/user/',
    method: 'post',
    data
  })
}

export function userInitStoreFraud(data) {
  return request({
    url: '/api_store_fraud/store_fraud/userInit/',
    method: 'get',
    data
  })
}

export function storeGenerateStoreFraud(data) {
  return request({
    url: '/api_store_fraud/store_fraud/store/',
    method: 'post',
    data
  })
}

export function storeInitStoreFraud(data) {
  return request({
    url: '/api_store_fraud/store_fraud/storeInit/',
    method: 'get',
    data
  })
}

export function cardGenerateStoreFraud(data) {
  return request({
    url: '/api_store_fraud/store_fraud/card/',
    method: 'post',
    data
  })
}

export function cardInitStoreFraud(data) {
  return request({
    url: '/api_store_fraud/store_fraud/cardInit/',
    method: 'get',
    data
  })
}

export function durationChooseStoreFraud(data) {
  return request({
    url: '/api_store_fraud/store_fraud/durationChoose/',
    method: 'post',
    data
  })
}

export function durationSetStoreFraud(data) {
  return request({
    url: '/api_store_fraud/store_fraud/durationSet/',
    method: 'get',
    data
  })
}

export function consumeGenerateStoreFraud(data) {
  return request({
    url: '/api_store_fraud/store_fraud/consumption/',
    method: 'post',
    data
  })
}

export function consumeInitStoreFraud(data) {
  return request({
    url: '/api_store_fraud/store_fraud/consumptionInit/',
    method: 'get',
    data
  })
}

export function transferGenerateStoreFraud(data) {
  return request({
    url: '/api_store_fraud/store_fraud/transfer/',
    method: 'post',
    data
  })
}

export function transferInitStoreFraud(data) {
  return request({
    url: '/api_store_fraud/store_fraud/transferInit/',
    method: 'get',
    data
  })
}

export function storeFraudInit(data) {
  return request({
    url: '/api_store_fraud/store_fraud/storeFraudInit/',
    method: 'get',
    data
  })
}

export function storeFraudGenerate(data) {
  return request({
    url: '/api_store_fraud/store_fraud/storeFraud/',
    method: 'post',
    data
  })
}

export function storeFraudRecreateTable(data) {
  return request({
    url: '/api_store_fraud/store_fraud/RecreateTable/',
    method: 'post',
    data
  })
}
