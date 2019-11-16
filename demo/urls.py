"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
import users.urls  # 先导入应用的urls模块
from users import views
import person.urls  # 先导入应用的urls模块
from person import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),  # django默认包含的

    # 添加
    # url(r'^person/', include('person.urls')),

    # url(r'^person/', include(person.urls)),  # 添加应用的路由

    # url(r'^person/index/$', views.index),

    # 添加
    # url(r'^users/', include('users.urls')),

    # url(r'^users/', include(users.urls)),  # 添加应用的路由

    # url(r'^users/index/$', views.index),

    # url(r'^', include('person.urls')),
    # url(r'^person/get_body_form/$', views.get_body_form),

    url(r'^', include('person.urls', namespace='person')),
    # url(r'^', include('person.urls', namespace='preson')),
    url(r'^', include('Templates.urls', namespace='Templates')),
]
