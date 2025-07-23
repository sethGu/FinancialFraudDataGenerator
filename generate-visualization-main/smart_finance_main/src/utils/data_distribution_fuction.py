import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta


def binomial(samples=1,pro=0.3,times=100):
    """
    二项分布
    实验样本数 samples,
    发生概率   pro
    实验次数   times
    """
    # example
    example_samples=6
    example_pro = 0.3
    example_times = 100
    result = np.random.binomial(example_samples, example_pro, example_times)

    # https://www.csdn.net/tags/NtjaUg0sNDI3Mi1ibG9n.html
    return result

def binomial_plt(samples=1,pro=0.3,times=100):

    result = binomial(samples, pro, times)

    X = [i for i in range(samples + 1)]
    Y = []
    for i in range(samples + 1):
        Y.append(sum(result == i) / times)
    plt.bar(X, Y, label='graph 1')
    plt.show()

def poisson(lam=0.5, size=100):
    """
    泊松分布
    发生率 lam
    返回数组的形状  size
    # https://www.cjavapy.com/article/1058/
    """
    result = np.random.poisson(lam, size)
    return result

def poisson_plt(lam=0.5, size=100):

    result = poisson(lam, size)
    plt.hist(result)
    plt.show()


def normal(mean=1,sigma=0.3):
    """
    正太分布
    均值 mean
    标准差  sigma

    """

    result = np.random.normal(mean,sigma)
    return result

def normal_plt(mean=1,sigma=0.3):
    result = normal(mean, sigma)
    plt.hist(result, bins=100, density=True, stacked=True)
    plt.show()

'''
def exponential1(start=0,end=15,gap=100000):
    """
    :param start: 起点
    :param end: 终点
    :param gap: 步长
    target:
    :return:
    """
    lambd = 3
    x = np.arange(start, end, gap)
    y = 0.1*lambd*np.exp( 0.1*-lambd * x)
    plt.plot(x, y, label="λ = {:f}".format(0.1 * lambd))
    plt.xlabel('Random Variable', fontsize=12)
    plt.ylabel('Probability', fontsize=12)
    plt.title("Exponential Distribution varying λ")
    plt.legend()
    plt.show()
    #取得target两边的值
    x = list(x)
    pro = 0
    _ = (end-start)/gap
    for i in range(len(x)):
        if target[0]<x[i] and x[i]<target[1]:
            pro += _*y[i]
    print(pro)
'''
def exponential(start=10,end=1500,gap=0.1,target=[5,6]):
    lambd = 0.3
    x = np.arange(start, end, gap)
    y = 0.1 * lambd * np.exp(0.1 * -lambd * x)
    plt.plot(x, y, label="λ = {:f}".format(0.1 * lambd))
    plt.xlabel('Random Variable', fontsize=12)
    plt.ylabel('Probability', fontsize=12)
    plt.title("Exponential Distribution varying λ")
    plt.legend()
    plt.show()
    # 取得target两边的值
    x = list(x)
    pro = 0
    for i in range(len(x)):
        if target[0] < x[i] and x[i] < target[1]:
            pro += gap * y[i]
    result = pro
    return result

def gamma(shape=2., scale=3., size=1000, multi=200):
    """
    gamma分布
    返回偏态随机数
    """
    result = np.random.gamma(shape, scale, size) * multi   # 生成2000个随机数，并进行区间缩放微调。
    # print(s)

    return result

def gamma_plt(shape=2., scale=3., size=1000, multi=200):

    result = gamma(shape, scale, size, multi)
    plt.hist(result, 1000)  # 50：是50个条形图
    plt.show()

def beta_(a=0.5, b=0.5):

    x = np.arange(0.01, 1, 0.01)
    y = beta.pdf(x, a, b)
    plt.plot(x, y)
    plt.title('Beta')
    plt.xlabel('x')
    plt.ylabel('density')
    plt.show()

if __name__ == '__main__':
    # binomial()
    # poisson(3.5, 10000)
    print(gamma_plt(4., 2., 100000, 1))
    # normal()
    # beta_()
    # binomial_plt()
    # poisson_plt()