const getters = {
  sidebar: state => state.app.sidebar,
  device: state => state.app.device,
  token: state => state.user.token,
  avatar: state => state.user.avatar,
  name: state => state.user.name,

  // 伪冒注册
  register_user_data: state => state.register.register_user_data, // 基础数据
  register_store_data: state => state.register.register_store_data,
  register_card_data: state => state.register.register_card_data,
  register_consume_data: state => state.register.register_consume_data, // 正常数据
  register_transfer_data: state => state.register.register_transfer_data,
  register_date_data: state => state.register.register_date_data,
  register_recreate_data: state => state.register.register_recreate_data,
  registerFraud_data: state => state.register.registerFraud_data,

  // 异常转账
  abnormal_user_data: state => state.abnormalTrans.abnormal_user_data, // 基础数据
  abnormal_store_data: state => state.abnormalTrans.abnormal_store_data,
  abnormal_card_data: state => state.abnormalTrans.abnormal_card_data,
  abnormal_consume_data: state => state.abnormalTrans.abnormal_consume_data, // 正常数据
  abnormal_transfer_data: state => state.abnormalTrans.abnormal_transfer_data,
  abnormal_date_data: state => state.abnormalTrans.abnormal_date_data,
  abnormal_recreate_data: state => state.abnormalTrans.abnormal_recreate_data,
  abnormal_data: state => state.abnormalTrans.abnormal_data,

  // 信用卡违规套现
  credit_user_data: state => state.creditCardCash.credit_user_data, // 基础数据
  credit_store_data: state => state.creditCardCash.credit_store_data,
  credit_card_data: state => state.creditCardCash.credit_card_data,
  credit_consume_data: state => state.creditCardCash.credit_consume_data, // 正常数据
  credit_transfer_data: state => state.creditCardCash.credit_transfer_data,
  credit_date_data: state => state.creditCardCash.credit_date_data,
  credit_recreate_data: state => state.creditCardCash.credit_recreate_data,
  credit_data: state => state.creditCardCash.credit_data,

  // 赌博
  gambling_user_data: state => state.gambling.gambling_user_data, // 基础数据
  gambling_store_data: state => state.gambling.gambling_store_data,
  gambling_card_data: state => state.gambling.gambling_card_data,
  gambling_consume_data: state => state.gambling.gambling_consume_data, // 正常数据
  gambling_transfer_data: state => state.gambling.gambling_transfer_data,
  gambling_date_data: state => state.gambling.gambling_date_data,
  gambling_recreate_data: state => state.gambling.gambling_recreate_data,
  gambling_data: state => state.gambling.gambling_data, // 异常数据

  // 黄牛营销
  marketing_user_data: state => state.marketing.marketing_user_data, // 基础数据
  marketing_store_data: state => state.marketing.marketing_store_data,
  marketing_card_data: state => state.marketing.marketing_card_data,
  marketing_consume_data: state => state.marketing.marketing_consume_data, // 正常数据
  marketing_transfer_data: state => state.marketing.marketing_transfer_data,
  marketing_date_data: state => state.marketing.marketing_date_data,
  marketing_recreate_data: state => state.marketing.marketing_recreate_data,
  marketing_data: state => state.marketing.marketing_data,

  // 商户违规
  storeFraud_user_data: state => state.storeFraud.storeFraud_user_data, // 基础数据
  storeFraud_store_data: state => state.storeFraud.storeFraud_store_data,
  storeFraud_card_data: state => state.storeFraud.storeFraud_card_data,
  storeFraud_consume_data: state => state.storeFraud.storeFraud_consume_data, // 正常数据
  storeFraud_transfer_data: state => state.storeFraud.storeFraud_transfer_data,
  storeFraud_date_data: state => state.storeFraud.storeFraud_date_data,
  storeFraud_recreate_data: state => state.storeFraud.storeFraud_recreate_data,
  storeFraud_data: state => state.storeFraud.storeFraud_data
}
export default getters
