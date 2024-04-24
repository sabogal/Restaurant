from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from apps.user.models import *
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType


class UserAdmin(admin.ModelAdmin):
    search_fields = ('id','username','name','last_name','document','number_phone')
    list_display = ('id','username','name','last_name','document','number_phone','is_active')
    list_filter = ['is_active']


admin.site.register(User, UserAdmin)
admin.site.register(Permission)
admin.site.register(ContentType)

