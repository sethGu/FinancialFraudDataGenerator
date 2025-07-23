from django.urls import re_path as url

from app01.views.views_0 import view_0, duration

urlpatterns = [
    # 登录等
    url('user_login/', view_0.user_login),
    url('user_info/', view_0.user_info),
    url('user_logout/', view_0.user_logout),
    url('user_update_password/', view_0.user_update_password),
    # 日期选择
    url('durationChoose/', duration.durationChoose),
    url('durationSet/', duration.durationSet),
    # 日志
    url('logs/', view_0.log_change),
]
