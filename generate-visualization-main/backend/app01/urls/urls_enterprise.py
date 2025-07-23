# -*- coding: utf-8 -*-
"""
  Author: LiangJing
   Time : 2023/5/15
    File: urls_enterprise.py
"""
from django.urls import re_path as url
from app01.views.views_enterprise import enterprise_view

urlpatterns = [
    # 工商企业数据生成
    url('enterprise/enterpriseGenerate/', enterprise_view.enterpriseGenerate),
    # 数据删除
    url('enterprise/RecreateTable/',enterprise_view.RecreateTable),
    # 数据下载
    url('enterprise/download/', enterprise_view.download),
    # 数据初始化
    url('enterprise/enterpriseInit/', enterprise_view.enterpriseInit),
    # 获取列表
    url('enterprise/fetchList/', enterprise_view.fetchList),
]
