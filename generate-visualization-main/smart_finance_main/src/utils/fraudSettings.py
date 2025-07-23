from src.utils.data_distribution_fuction import *

__author__ = '顾峻铨'


class FraudSettings:

    def __init__(self, basic_fraud_amount, basic_sigma_2=None, basic_miu=None, basic_sigma=None, multiply_base=2,
                 age_division=None, age_basic_fraud_multiply=None):
        if age_division is None:
            age_division = {"青年": "17-30", "中青年": "31-40", "中年": "41-60", "中老年": "61-70", "老年": "71-150"}
        if age_basic_fraud_multiply is None:
            age_basic_fraud_multiply = {"青年": 2, "中青年": 0.75, "中年": 0.5, "中老年": 1.5, "老年": 5}
        if basic_miu is None:
            basic_miu = basic_fraud_amount / 100
        if basic_sigma is None:
            basic_sigma = basic_fraud_amount / 1000
        if basic_sigma_2 is None:
            basic_sigma_2 = 3

        self.basic_fraud_amount = basic_fraud_amount  # 基础诈骗值（工资）
        self.basic_miu = basic_miu  # 基础均值
        self.basic_sigma = basic_sigma  # 基础标准差
        self.age_division = age_division  # 年龄分层，暂不具备通过外部修改
        self.basic_sigma_2 = basic_sigma_2  # 基础标准差（第二层）
        self.age_basic_fraud_multiply = age_basic_fraud_multiply  # 年龄层的诈骗倍率
        self.multiply_base = multiply_base  # 年龄层的诈骗倍率的底数

    def generate_basic_fraud_amount(self, fraud_scene_multi, age_lvl, age_basic_fraud_multiply=None):
        '''

        :param fraud_scene_multi: 欺诈金额的场景倍率
        :param age_lvl: 年龄层（如青年）
        :param age_basic_fraud_multiply: 年龄层的诈骗倍率，默认为{"青年": 2, "中青年": 0.75, "中年": 0.5, "中老年": 1.5, "老年": 5}
        :return:
        '''
        if age_basic_fraud_multiply is None:
            age_basic_fraud_multiply = self.age_basic_fraud_multiply
        lvl_2_normal = normal(mean=self.basic_miu, sigma=self.basic_sigma_2)
        lvl_1_normal = normal(mean=lvl_2_normal, sigma=self.basic_sigma)

        if age_lvl not in age_basic_fraud_multiply.keys():
            raise Exception('传入的年龄层不正确')
        fraud_multiply = self.multiply_base ** age_basic_fraud_multiply[age_lvl]

        fraud_amount = lvl_1_normal * fraud_multiply * fraud_scene_multi
        return fraud_amount

    def get_age_lvl_from_age(self, age):
        '''
        此处对于中间数值，如传入年龄为30岁将定义为“青年”，传入年龄为31岁则会定义为“中青年”
        :param age: 传入的用户年龄，可由user['age']、user.get_age()等表示
        :return:
        '''
        if age > 149 or age < 18:
            raise Exception('年龄需要是18-149之间的整数')
        for key, val in self.age_division.items():
            start_age = int(val[:2])
            end_age = int(val[3:])
            if start_age <= age <= end_age:
                return key


def main():
    fs = FraudSettings(80000, 3)
    val = fs.generate_basic_fraud_amount(0.1, '青年')
    print(val)

if __name__ == '__main__':
    for _ in range(50):
        main()
