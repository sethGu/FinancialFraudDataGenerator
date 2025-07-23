"""sf_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path
#
# urlpatterns = [
#     path("admin/", admin.site.urls),
# ]
from django.conf.urls import include
from django.urls import re_path as url
from django.contrib import admin

from django.views.generic import TemplateView  # 新增

from app01.urls import urls_0
from app01.urls import urls_abnormal
from app01.urls import urls_credit_card
from app01.urls import urls_gambling
from app01.urls import urls_marketing
from app01.urls import urls_register
from app01.urls import urls_store_fraud
from app01.urls import urls_enterprise
from app01.urls import urls_operator

urlpatterns = [

    url(r'^admin/', admin.site.urls),

    url(r'^api/', include(urls_0)),

    url(r'^api_abnormal/', include(urls_abnormal)),

    url(r'^api_credit_card/', include(urls_credit_card)),

    url(r'^api_gambling/', include(urls_gambling)),

    url(r'^api_marketing/', include(urls_marketing)),

    url(r'^api_register/', include(urls_register)),

    url(r'^api_store_fraud/', include(urls_store_fraud)),

    url(r'^api_enterprise/', include(urls_enterprise)),

    url(r'^api_operator/', include(urls_operator)),

    # 新增

    url(r'^$', TemplateView.as_view(template_name="index.html"))

]
