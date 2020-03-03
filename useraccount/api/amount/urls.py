
from django.urls import path
from useraccount.api.amount.views import *

urlpatterns = [
    path('all-payment/', get_all_payment, name='all_payment'),
    path('all-payment/<user>', get_user_all_payment, name='user_all_payment'),
]

