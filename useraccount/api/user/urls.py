
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from useraccount.api.user.views import *

urlpatterns = [
    path('registration', register_user, name='registration'),
    path('login', obtain_auth_token, name='login'),
    path('all', get_all_user, name='all_user'),
]
