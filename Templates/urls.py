from django.conf.urls import url
from . import views
from . import jinja2_env

urlpatterns = [
    url(r'^Templates/index/$', views.index),
    # url(r'^Templates/index/$', jinja2_env.index),
]