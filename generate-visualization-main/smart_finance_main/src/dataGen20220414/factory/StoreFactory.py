import random

import sys
import json

from src.dataGen20220414.service.StoreService import StoreService
from src.utils.config import get_mysql_connection
from src.utils.functions import id_generator
from src.dataGen20220414.entity.Store import Store

class StoreFactory:

    def __init__(self, scene):
        self.storeService = StoreService(scene)

    def createStoreTable(self):
        self.storeService.createStoreTable()

    def createStores(self,n):
        storeList = []
        for i in range(n):
            store = self.storeService.createStore()
            storeList.extend(store)
        self.storeService.insertStores(storeList)