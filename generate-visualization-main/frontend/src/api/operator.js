import request from '@/utils/request'

export function generateOperator(num) {
  return request({
    url: '/api_operator/operator/operatorGenerate/',
    method: 'post',
    data: { 'number_of_operators': num }
  })
}

export function fetchList(query) {
  return request({
    url: '/api_operator/operator/fetchList/',
    method: 'get',
    params: query
  })
}

export function operatorDataInit(data) {
  return request({
    url: '/api_operator/operator/operatorInit/',
    method: 'get',
    data
  })
}

// 删除历史数据并重新建表
export function operatorRecreateTable(data) {
  return request({
    url: '/api_operator/operator/RecreateTable/',
    method: 'post',
    data
  })
}
