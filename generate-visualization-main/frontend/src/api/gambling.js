import request from '@/utils/request'

export function userGenerateGambling(data) {
  return request({
    url: '/api_gambling/gambling/user/',
    method: 'post',
    data
  })
}

export function userInitGambling(data) {
  return request({
    url: '/api_gambling/gambling/userInit/',
    method: 'get',
    data
  })
}

export function storeGenerateGambling(data) {
  return request({
    url: '/api_gambling/gambling/store/',
    method: 'post',
    data
  })
}

export function storeInitGambling(data) {
  return request({
    url: '/api_gambling/gambling/storeInit/',
    method: 'get',
    data
  })
}

export function cardGenerateGambling(data) {
  return request({
    url: '/api_gambling/gambling/card/',
    method: 'post',
    data
  })
}

export function cardInitGambling(data) {
  return request({
    url: '/api_gambling/gambling/cardInit/',
    method: 'get',
    data
  })
}

export function durationChooseGambling(data) {
  return request({
    url: '/api_gambling/gambling/durationChoose/',
    method: 'post',
    data
  })
}

export function durationSetGambling(data) {
  return request({
    url: '/api_gambling/gambling/durationSet/',
    method: 'get',
    data
  })
}

export function consumeGenerateGambling(data) {
  return request({
    url: '/api_gambling/gambling/consumption/',
    method: 'post',
    data
  })
}

export function consumeInitGambling(data) {
  return request({
    url: '/api_gambling/gambling/consumptionInit/',
    method: 'get',
    data
  })
}

export function transferGenerateGambling(data) {
  return request({
    url: '/api_gambling/gambling/transfer/',
    method: 'post',
    data
  })
}

export function transferInitGambling(data) {
  return request({
    url: '/api_gambling/gambling/transferInit/',
    method: 'get',
    data
  })
}

export function gamblingInit(data) {
  return request({
    url: '/api_gambling/gambling/GamblingTransInit/',
    method: 'get',
    data
  })
}

export function gamblingGenerate(data) {
  return request({
    url: '/api_gambling/gambling/GamblingTrans/',
    method: 'post',
    data
  })
}

// 删除历史数据并重新建表
export function gamblingRecreateTable(data) {
  return request({
    url: '/api_gambling/gambling/RecreateTable/',
    method: 'post',
    data
  })
}
