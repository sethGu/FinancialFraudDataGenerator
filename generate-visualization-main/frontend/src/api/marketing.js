import request from '@/utils/request'

export function userGenerateMarketing(data) {
  return request({
    url: '/api_marketing/marketing/user/',
    method: 'post',
    data
  })
}

export function userInitMarketing(data) {
  return request({
    url: '/api_marketing/marketing/userInit/',
    method: 'get',
    data
  })
}

export function storeGenerateMarketing(data) {
  return request({
    url: '/api_marketing/marketing/store/',
    method: 'post',
    data
  })
}

export function storeInitMarketing(data) {
  return request({
    url: '/api_marketing/marketing/storeInit/',
    method: 'get',
    data
  })
}

export function cardGenerateMarketing(data) {
  return request({
    url: '/api_marketing/marketing/card/',
    method: 'post',
    data
  })
}

export function cardInitMarketing(data) {
  return request({
    url: '/api_marketing/marketing/cardInit/',
    method: 'get',
    data
  })
}

export function durationChooseMarketing(data) {
  return request({
    url: '/api_marketing/marketing/durationChoose/',
    method: 'post',
    data
  })
}

export function durationSetMarketing(data) {
  return request({
    url: '/api_marketing/marketing/durationSet/',
    method: 'get',
    data
  })
}

export function consumeGenerateMarketing(data) {
  return request({
    url: '/api_marketing/marketing/consumption/',
    method: 'post',
    data
  })
}

export function consumeInitMarketing(data) {
  return request({
    url: '/api_marketing/marketing/consumptionInit/',
    method: 'get',
    data
  })
}

export function transferGenerateMarketing(data) {
  return request({
    url: '/api_marketing/marketing/transfer/',
    method: 'post',
    data
  })
}

export function transferInitMarketing(data) {
  return request({
    url: '/api_marketing/marketing/transferInit/',
    method: 'get',
    data
  })
}

export function marketingInit(data) {
  return request({
    url: '/api_marketing/marketing/MarketingFraudInit/',
    method: 'get',
    data
  })
}

export function marketingGenerate(data) {
  return request({
    url: '/api_marketing/marketing/MarketingFraud/',
    method: 'post',
    data
  })
}

// 删除历史数据并重新建表
export function marketingRecreateTable(data) {
  return request({
    url: '/api_marketing/marketing/RecreateTable/',
    method: 'post',
    data
  })
}
