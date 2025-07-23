from src.dataGen20220414.service.TransService import TransService
from src.utils.config import get_mysql_connection
import sys

from src.dataGen20220414.entity.Trans import Trans


class TransFactory():
    def __init__(self, scene):
        self.transService = TransService(scene)

    def createTransTable(self):
        self.transService.createTransTable()

    def createFraudTransTable(self):
        self.transService.createFraudTransTable()

#
#
# if __name__ == '__main__':
#     tt = TransTactory()
#     tt.createTransTable()