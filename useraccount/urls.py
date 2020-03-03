
from django.urls import path, include
from . import views

urlpatterns = [
    path('api/user/', include('useraccount.api.user.urls')),
    path('api/amount/', include('useraccount.api.amount.urls')),

    path('', views.home, name='home'),
    path('login', views.login_page, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('registration', views.registration_page, name='registration'),
]
