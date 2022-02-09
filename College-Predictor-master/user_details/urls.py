from django.urls import re_path
from . import views

app_name='USER_DETAILS'

urlpatterns=[
 re_path(r'^Fill-Academic-profile/$',views.profile_views,name='userprofile'),
 re_path(r'^Fill-Preferences/$',views.preferences_views,name='userpreferences'),
 re_path(r'^Fill-Preferences/inter/$',views.intermediate_view,name='intermediate'),
 re_path(r'^result/$',views.results_view,name='results'),
]