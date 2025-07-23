# -*- coding: utf-8 -*-
"""
  Author: LiangJing
   Time : 2023/5/18
    File: urls_operator.py
"""

from django.urls import re_path as url
from app01.views.views_operator import operator_view

urlpatterns = [
    # 数据生成
    url('operator/operatorGenerate/', operator_view.operatorGenerate),
    # 数据删除
    url('operator/RecreateTable/',operator_view.RecreateTable),
    # 数据下载
    url('operator/download/', operator_view.download),
    # 数据初始化
    url('operator/operatorInit/', operator_view.operatorInit),
    # 获取列表
    url('operator/fetchList/', operator_view.fetchList),
]