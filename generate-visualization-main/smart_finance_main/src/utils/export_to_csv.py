# -*- coding: utf-8 -*-
# @Time     : 2022/9/9 11:24
# @Author   : Guo Jiayu
import csv

from src.dataGen20220414.service.StoreService import StoreService
from src.dataGen20220414.service.TransService import TransService
from pandas import DataFrame

def get_trans(scene, path, filename="t.csv"):
    DataFrame().to_csv(path + filename, index=False, encoding='gb18030') #lcf
    transService = TransService(scene)
    transList = transService.selectAllTransByTime()
    first = True
    for trans in transList:
        data = {
            'T1': [str(trans.T1)+'\t'],
            'T2': [str(trans.T2)+'\t'],
            'T3': [str(trans.T3)+'\t'],
            'T4': [str(trans.T4)+'\t'],
            'T5': [str(trans.T5)+'\t'],
            'T6': [str(trans.T6)+'\t'],
            'T7': [str(trans.T7)+'\t'],
            'T8': [str(trans.T8)+'\t'],
            'T9': [str(trans.T9)+'\t'],
            'T10': [str(trans.T10)+'\t'],
            'T11': [str(trans.T11) + '\t'],
            'T12': [str(trans.T12) + '\t'],
            'T13': [str(trans.T13) + '\t'],
            'T14': [str(trans.T14) + '\t'],
            'T15': [str(trans.T15) + '\t'],
            'T16': [str(trans.T16) + '\t'],
            'T17': [str(trans.T17) + '\t'],
            'T18': [str(trans.T18) + '\t'],
            'T19': [str(trans.T19) + '\t'],
            'T20': [str(trans.T20) + '\t'],
            'T21': [str(trans.T21) + '\t'],
            'T22': [str(trans.T22) + '\t'],
            'T23': [str(trans.T23) + '\t'],
            'T24': [str(trans.T24) + '\t'],
            'T25': [str(trans.T25) + '\t'],
            'T26': [str(trans.T26) + '\t'],
            'T27': [str(trans.T27) + '\t'],
            'T28': [str(trans.T28) + '\t'],
            'T29': [str(trans.T29) + '\t'],
            'T30': [str(trans.T30) + '\t' if len(str(trans.T30)) > 0 else '0000' + '\t'],
            'T31': [str(trans.T31) + '\t' if len(str(trans.T31)) > 0 else '00000000' + '\t'],
            'T32': [str(trans.T32) + '\t'],
            'T33': [str(trans.T33) + '\t'],
            'T34': [str(trans.T34) + '\t'],
            'T35': [str(trans.T35) + '\t'],
            'T36': [str(trans.T36) + '\t'],
            'T37': [str(trans.T37) + '\t'],
            'T38': [str(trans.T38) + '\t'],
            'T39': [str(trans.T39) + '\t']
        }
        df = DataFrame(data, columns=["T1", "T2", "T3", "T4", "T5", "T6", "T7", "T8", "T9", "T10",
                             "T11", "T12", "T13", "T14", "T15", "T16", "T17", "T18", "T19", "T20",
                            "T21", "T22", "T23", "T24", "T25", "T26", "T27", "T28", "T29", "T30",
                            "T31", "T32", "T33", "T34", "T35", "T36", "T37", "T38", "T39"])
        df.to_csv (path + filename, mode="a" ,index = False, header=first,encoding='gb18030')
        first = False

def get_stores(scene, path, filename="s.csv"):
    DataFrame().to_csv(path + filename, index=False, encoding='gb18030') #lcf
    storeService = StoreService(scene)
    storeList = storeService.selectStores()
    first = True
    for store in storeList:
        data = {
            'S1': [str(store.S1)+'\t'],
            'S2': [str(store.S2)+'\t'],
            'S3': [str(store.S3)+'\t'],
            'S4': [str(store.S4)+'\t'],
            'S5': [str(store.S5)+'\t'],
            'S6': [str(store.S6)+'\t'],
            'S7': [str(store.S7)+'\t'],
            'S8': [str(store.S8)+'\t'],
            'S9': [str(store.S9)+'\t'],
            'S10': [str(store.S10)+'\t'],
            'S11': [str(store.S11) + '\t'],
            'S12': [str(store.S12) + '\t'],
            'S13': [str(store.S13) + '\t'],
            'S14': [str(store.S14) + '\t'],
            'S15': [str(store.S15) + '\t'],
            'S16': [str(store.S16) + '\t'],
            'S17': [str(store.S17) + '\t'],
            'S18': [str(store.S18) + '\t'],
            'S19': [str(store.S19) + '\t'],
            'S20': [str(store.S20) + '\t'],
            'S21': [str(store.S21) + '\t'],
            'S22': [str(store.S22) + '\t'],
            'S23': [str(store.S23) + '\t'],
            'S24': [str(store.S24) + '\t'],
            'S25': [str(store.S25) + '\t'],
            'S26': [str(store.S26) + '\t'],
            'S27': [str(store.S27) + '\t'],
            'S28': [str(store.S28) + '\t'],
            'S29': [str(store.S29) + '\t']
        }
        df = DataFrame(data, columns=["S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", "S10",
                             "S11", "S12", "S13", "S14", "S15", "S16", "S17", "S18", "S19", "S20",
                            "S21", "S22", "S23", "S24", "S25", "S26", "S27", "S28", "S29"])
        df.to_csv (path + filename, mode="a" ,index = False, header=first,encoding='gb18030')
        first = False

def get_f_t(scene, path, filename="f_t.csv"):
    DataFrame().to_csv(path + filename, index=False, encoding='gb18030') #lcf
    transService = TransService(scene)
    transList = transService.selectAllFraudTrans()
    first = True
    for trans in transList:
        data = {
            'F1': [str(trans.F1)+'\t'],
            'F2': [str(trans.F2)+'\t'],
            'F3': [str(trans.F3)+'\t'],
            'F4': [str(trans.F4)+'\t'],
            'F5': [str(trans.F5)+'\t'],
            'F6': [str(trans.F6)+'\t'],
            'F7': [str(trans.F7)+'\t'],
            'F8': [str(trans.F8)+'\t'],
            'F9': [str(trans.F9)+'\t'],
            'F10': [str(trans.F10)+'\t'],
            'F11': [str(trans.F11) + '\t'],
            'F12': [str(trans.F12) + '\t'],
            'F13': [str(trans.F13) + '\t'],
            'F14': [str(trans.F14) + '\t'],
            'F15': [str(trans.F15) + '\t'],
            'F16': [str(trans.F16) + '\t'],
            'F17': [str(trans.F17) + '\t'],
            'F18': [str(trans.F18) + '\t'],
            'F19': [str(trans.F19) + '\t'],
            'F20': [str(trans.F20) + '\t'],
            'F21': [str(trans.F21) + '\t'],
            'F22': [str(trans.F22) + '\t'],
            'F23': [str(trans.F23) + '\t'],
            'F24': [str(trans.F24) + '\t'],
            'F25': [str(trans.F25) + '\t'],
            'F26': [str(trans.F26) + '\t'],
            'F27': [str(trans.F27) + '\t'],
            'F28': [str(trans.F28) + '\t'],
            'F29': [str(trans.F29) + '\t'],
            'F30': [str(trans.F30) + '\t'],
            'F31': [str(trans.F31) + '\t'],
            'F32': [str(trans.F32) + '\t'],
            'F33': [str(trans.F33) + '\t'],
            'F34': [str(trans.F34) + '\t'],
            'F35': [str(trans.F35) + '\t'],
            'F36': [str(trans.F36) + '\t'],
            'F37': [str(trans.F37) + '\t'],
            'F38': [str(trans.F38) + '\t'],
            'F39': [str(trans.F39) + '\t'],
            'F40': [str(trans.F40) + '\t'],
            'F41': [str(trans.F41) + '\t'],
            'F42': [str(trans.F42) + '\t'],
            'F43': [str(trans.F43) + '\t'],
            'F44': [str(trans.F44) + '\t'],
            'F45': [str(trans.F45) + '\t']
        }
        df = DataFrame(data, columns=["F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "F10",
                             "F11", "F12", "F13", "F14", "F15", "F16", "F17", "F18", "F19", "F20",
                            "F21", "F22", "F23", "F24", "F25", "F26", "F27", "F28", "F29", "F30",
                            "F31", "F32", "F33", "F34", "F35", "F36", "F37", "F38", "F39", "F40",
                            "F41", "F42", "F43", "F44", "F45"])
        df.to_csv (path + filename, mode="a" ,index = False, header=first, encoding='gb18030')
        first = False

def out_put(scene, path = '../../datas/'):
    get_trans(scene, path)
    get_stores(scene, path)
    get_f_t(scene, path)
if __name__ == '__main__':
    scene = 'Abnormal_transfer'
    out_put(scene)
