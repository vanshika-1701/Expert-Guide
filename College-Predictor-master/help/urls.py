from django.urls import re_path
from . import views

app_name='HELP'

urlpatterns=[
	re_path(r'^$',views.help_view,name='helpapp'),
]