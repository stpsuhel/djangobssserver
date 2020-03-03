from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from useraccount.models import Users, Amount


class MyUserAccount(UserAdmin):
    list_display = ('id', 'name', 'username', 'email', 'created_at', 'last_login', 'is_staff', 'is_superuser')
    search_fields = ('email', 'username')
    readonly_fields = ('created_at', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


# class UserPayment(UserAdmin):
#     list_display = ('paymentMonth', 'paymentDay', 'paymentTime', 'money', 'userId', 'created_at')
#     search_fields = ('userId', 'paymentMonth')
#     readonly_fields = 'created_at'
#
#     filter_horizontal = ()
#     list_filter = ()
#     fieldsets = ()


admin.site.register(Users, MyUserAccount)
admin.site.register(Amount)
