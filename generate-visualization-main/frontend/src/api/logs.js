import request from '@/utils/request'

export function logChange(data) {
  return request({
    url: '/api/logs/',
    method: 'post',
    data
  })
}
