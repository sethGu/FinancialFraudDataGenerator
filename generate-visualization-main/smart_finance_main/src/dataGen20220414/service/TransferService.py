import random

class TransferService:
    def from_distributin_to_one_anser(self,kx, glfb):
        sum = [0 for i in range(len(glfb))]
        sum[0] = glfb[0]
        for i in range(1, len(glfb)):
            sum[i] = sum[i - 1] + glfb[i]
        a = random.random()
        for i in range(len(sum)):
            if a <= sum[i]:
                return kx[i]

    def from_human_age_to_tras_pat(self,age):
        transfer_pattern = ["student", "adult", "old"]
        if age <= 22:
            return transfer_pattern[0]
        elif age > 22 and age < 55:
            return transfer_pattern[1]
        else:
            return transfer_pattern[3]

    def from_wage_to_total_trans_num(self,wage):
        wage_total_num_dict = {"0-100000": "10-200",
                               "100000-200000": "200-400",
                               "200000-1000000": "400-600",
                               "> 1000000": "600-1000"}
        for key, value in wage_total_num_dict.items():
            if key != "> 1000000":
                wg_st = int(key.strip("\"").split("-")[0])
                wg_ed = int(key.strip("\"").split("-")[1])
                if wage >= wg_st and wage <= wg_ed:
                    st = int(value.strip("\"").split("-")[0])
                    ed = int(value.strip("\"").split("-")[1])
                    return random.randint(st, ed)
            else:
                return random.randint(600, 1000)

    def per_ji_tras_time(self, total_trans_num):
        ratio = [0.0, 0.0, 0.0]
        jtcs = [0, 0, 0]
        ratio[0] = random.uniform(0.5, 0.85)
        rest = 1 - ratio[0]
        ratio[1] = random.uniform(ratio[0] + rest / 2.0, 0.99) - ratio[0]

        jtcs[0] = int(total_trans_num * ratio[0])
        jtcs[1] = int(total_trans_num * ratio[1])
        jtcs[2] = max(0, total_trans_num - jtcs[0] - jtcs[1])
        return jtcs

    def from_wage_to_xflx(self,wage):
        wage_rank_dict = {"0-100000": {"Small": 0.6, "Medium": 0.3, "Large": 0.1},
                          "100000-200000": {"Small": 0.6, "Medium": 0.3, "Large": 0.1},
                          "200000-1000000": {"Small": 0.5, "Medium": 0.3, "Large": 0.2},
                          "> 1000000": {"Small": 0.35, "Medium": 0.35, "Large": 0.3}}
        for key, value in wage_rank_dict.items():
            if key != "> 1000000":
                wg_st = int(key.strip("\"").split("-")[0])
                wg_ed = int(key.strip("\"").split("-")[1])
                if wage >= wg_st and wage <= wg_ed:
                    lx_ls = []
                    lx_atribute = []
                    for lx, atr in value.items():
                        lx_ls.append(lx)
                        lx_atribute.append(atr)
                    return self.from_distributin_to_one_anser(lx_ls, lx_atribute)
            else:
                lx_ls = ["Small", "Medium", "Large"]
                lx_atribute = [0.35, 0.35, 0.3]
                return self.from_distributin_to_one_anser(lx_ls, lx_atribute)


    def get_trans_time_duration(self,xflx):
        xflx_je_dict = {"Small": "1-365", "Medium": "30-365", "Large": "90-365"}
        jefw = xflx_je_dict[xflx]
        je_st = int(jefw.strip("\"").split("-")[0])
        je_ed = int(jefw.strip("\"").split("-")[1])
        return random.randint(je_st, je_ed)