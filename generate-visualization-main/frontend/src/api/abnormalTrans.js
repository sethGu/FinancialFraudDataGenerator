import request from '@/utils/request'

export function userGenerateAbnormal(data) {
  return request({
    url: '/api_abnormal/abnormal/user/',
    method: 'post',
    data
  })
}

export function userInitAbnormal(data) {
  return request({
    url: '/api_abnormal/abnormal/userInit/',
    method: 'get',
    data
  })
}

export function storeGenerateAbnormal(data) {
  return request({
    url: '/api_abnormal/abnormal/store/',
    method: 'post',
    data
  })
}

export function storeInitAbnormal(data) {
  return request({
    url: '/api_abnormal/abnormal/storeInit/',
    method: 'get',
    data
  })
}

export function cardGenerateAbnormal(data) {
  return request({
    url: '/api_abnormal/abnormal/card/',
    method: 'post',
    data
  })
}

export function cardInitAbnormal(data) {
  return request({
    url: '/api_abnormal/abnormal/cardInit/',
    method: 'get',
    data
  })
}

export function durationChooseAbnormal(data) {
  return request({
    url: '/api_abnormal/abnormal/durationChoose/',
    method: 'post',
    data
  })
}

export function durationSetAbnormal(data) {
  return request({
    url: '/api_abnormal/abnormal/durationSet/',
    method: 'get',
    data
  })
}

export function consumeGenerateAbnormal(data) {
  return request({
    url: '/api_abnormal/abnormal/consumption/',
    method: 'post',
    data
  })
}

export function consumeInitAbnormal(data) {
  return request({
    url: '/api_abnormal/abnormal/consumptionInit/',
    method: 'get',
    data
  })
}

export function transferGenerateAbnormal(data) {
  return request({
    url: '/api_abnormal/abnormal/transfer/',
    method: 'post',
    data
  })
}

export function transferInitAbnormal(data) {
  return request({
    url: '/api_abnormal/abnormal/transferInit/',
    method: 'get',
    data
  })
}

export function abnormalInit(data) {
  return request({
    url: '/api_abnormal/abnormal/AbnormalTransInit/',
    method: 'get',
    data
  })
}

export function abnormalGenerate(data) {
  return request({
    url: '/api_abnormal/abnormal/AbnormalTrans/',
    method: 'post',
    data
  })
}

// 删除历史数据并重新建表
export function abnormalRecreateTable(data) {
  return request({
    url: '/api_abnormal/abnormal/RecreateTable/',
    method: 'post',
    data
  })
}
