from django.urls import re_path,include
from . import views


app_name='ACCOUNTS'

urlpatterns = [
    re_path(r'^login/$',views.login_view,name='login'),
    re_path(r'^signup/$',views.signup_view,name='signup'),
    re_path(r'^logout/$',views.logout_view,name='logout'),
    re_path(r'^Profile/$',views.accounts_profile_view,name='accounts_profile_view'),
    re_path(r'^Profile/Edit/$',views.accounts_profile_edit,name='accounts_profile_edit'),
    re_path(r'^Profile/Edit/Change-Password$',views.change_password,name='change_password'),
]