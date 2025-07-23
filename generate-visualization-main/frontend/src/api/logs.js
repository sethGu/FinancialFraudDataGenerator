import request from '@/utils/request'

// 新增日志记录的 API
export function logChange(data) {
  return request({
    url: '/api/logs/',
    method: 'post',
    data// 传递日志内容
  })
}
