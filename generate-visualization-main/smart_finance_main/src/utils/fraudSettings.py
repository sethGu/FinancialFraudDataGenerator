from src.utils.data_distribution_fuction import *

class FraudSettings:

    def __init__(self, basic_fraud_amount, basic_sigma_2=None, basic_miu=None, basic_sigma=None, multiply_base=2,
                 age_division=None, age_basic_fraud_multiply=None):
        if age_division is None:
            age_division = {"Youth": "17-30", "Young_and_middle_aged": "31-40", "Middle_aged": "41-60", "Middle_aged_and_elderly": "61-70", "Elderly": "71-150"}
        if age_basic_fraud_multiply is None:
            age_basic_fraud_multiply = {"Youth": 2, "Young_and_middle_aged": 0.75, "Middle_aged": 0.5, "Middle_aged_and_elderly": 1.5, "Elderly": 5}
        if basic_miu is None:
            basic_miu = basic_fraud_amount / 100
        if basic_sigma is None:
            basic_sigma = basic_fraud_amount / 1000
        if basic_sigma_2 is None:
            basic_sigma_2 = 3

        self.basic_fraud_amount = basic_fraud_amount
        self.basic_miu = basic_miu
        self.basic_sigma = basic_sigma
        self.age_division = age_division
        self.basic_sigma_2 = basic_sigma_2
        self.age_basic_fraud_multiply = age_basic_fraud_multiply
        self.multiply_base = multiply_base

    def generate_basic_fraud_amount(self, fraud_scene_multi, age_lvl, age_basic_fraud_multiply=None):
        if age_basic_fraud_multiply is None:
            age_basic_fraud_multiply = self.age_basic_fraud_multiply
        lvl_2_normal = normal(mean=self.basic_miu, sigma=self.basic_sigma_2)
        lvl_1_normal = normal(mean=lvl_2_normal, sigma=self.basic_sigma)

        if age_lvl not in age_basic_fraud_multiply.keys():
            raise Exception('The entered age group is incorrect.')
        fraud_multiply = self.multiply_base ** age_basic_fraud_multiply[age_lvl]

        fraud_amount = lvl_1_normal * fraud_multiply * fraud_scene_multi
        return fraud_amount

    def get_age_lvl_from_age(self, age):
        if age > 149 or age < 18:
            raise Exception('The age must be an integer between 18 and 149.')
        for key, val in self.age_division.items():
            start_age = int(val[:2])
            end_age = int(val[3:])
            if start_age <= age <= end_age:
                return key


def main():
    fs = FraudSettings(80000, 3)
    val = fs.generate_basic_fraud_amount(0.1, 'Youth')
    print(val)

if __name__ == '__main__':
    for _ in range(50):
        main()
