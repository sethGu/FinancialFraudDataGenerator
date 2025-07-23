import request from '@/utils/request'

export function generateEnterprise(num) {
  return request({
    url: '/api_enterprise/enterprise/enterpriseGenerate/',
    method: 'post',
    data: { 'number_of_enterprises': num }
  })
}

export function enterpriseDataInit(data) {
  return request({
    url: '/api_enterprise/enterprise/enterpriseInit/',
    method: 'get',
    data
  })
}

export function fetchList(query) {
  return request({
    url: '/api_enterprise/enterprise/fetchList/',
    method: 'get',
    params: query
  })
}

// 删除历史数据并重新建表
export function enterpriseRecreateTable(data) {
  return request({
    url: '/api_enterprise/enterprise/RecreateTable/',
    method: 'post',
    data
  })
}
