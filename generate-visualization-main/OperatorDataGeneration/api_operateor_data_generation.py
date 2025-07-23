# @Time    : 2023/5/17 22:32
# @Author  : SuperRich Liu

from OperatorDataGeneration.utils import data_delete, data_export, data_genetation


def api_data_delete():
    """清空数据库表"""
    data_delete.delete()


def api_data_genetation(total=5):
    """数据生成，追加数据"""
    data_genetation.generation(total=total)


def api_data_export(path='result_datas'):
    """数据导出"""
    data_export.export(path=path)


if __name__ == '__main__':
    # api_data_delete()
    api_data_genetation(5)
    api_data_export()
