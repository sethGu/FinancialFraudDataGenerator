import request from '@/utils/request'

export function userGenerateCredit(data) {
  return request({
    url: '/api_credit_card/credit_card/user/',
    method: 'post',
    data
  })
}

export function userInitCredit(data) {
  return request({
    url: '/api_credit_card/credit_card/userInit/',
    method: 'get',
    data
  })
}

export function storeGenerateCredit(data) {
  return request({
    url: '/api_credit_card/credit_card/store/',
    method: 'post',
    data
  })
}

export function storeInitCredit(data) {
  return request({
    url: '/api_credit_card/credit_card/storeInit/',
    method: 'get',
    data
  })
}

export function cardGenerateCredit(data) {
  return request({
    url: '/api_credit_card/credit_card/card/',
    method: 'post',
    data
  })
}

export function cardInitCredit(data) {
  return request({
    url: '/api_credit_card/credit_card/cardInit/',
    method: 'get',
    data
  })
}

export function durationChooseCredit(data) {
  return request({
    url: '/api_credit_card/credit_card/durationChoose/',
    method: 'post',
    data
  })
}

export function durationSetCredit(data) {
  return request({
    url: '/api_credit_card/credit_card/durationSet/',
    method: 'get',
    data
  })
}

export function consumeGenerateCredit(data) {
  return request({
    url: '/api_credit_card/credit_card/consumption/',
    method: 'post',
    data
  })
}

export function consumeInitCredit(data) {
  return request({
    url: '/api_credit_card/credit_card/consumptionInit/',
    method: 'get',
    data
  })
}

export function transferGenerateCredit(data) {
  return request({
    url: '/api_credit_card/credit_card/transfer/',
    method: 'post',
    data
  })
}

export function transferInitCredit(data) {
  return request({
    url: '/api_credit_card/credit_card/transferInit/',
    method: 'get',
    data
  })
}

export function creditInit(data) {
  return request({
    url: '/api_credit_card/credit_card/CreditCardCashOutInit/',
    method: 'get',
    data
  })
}

export function creditGenerate(data) {
  return request({
    url: '/api_credit_card/credit_card/CreditCardCashOut/',
    method: 'post',
    data
  })
}

// 删除历史数据并重新建表
export function creditRecreateTable(data) {
  return request({
    url: '/api_credit_card/credit_card/RecreateTable/',
    method: 'post',
    data
  })
}
