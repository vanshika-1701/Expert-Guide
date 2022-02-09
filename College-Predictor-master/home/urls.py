from django.urls import re_path
from . import views

app_name='HOME'

urlpatterns=[
 re_path(r'^$',views.home_views,name='homepage'),
 re_path(r'^instructions/$',views.inst_views,name='inst'),
]