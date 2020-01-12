from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from dj_reg_redux.models import Notice
from dj_reg_redux.models import Branch
from dj_reg_redux.models import Profile
# Register your models here.


class NoticeAdmin(ModelAdmin):
    list_display = ["subject", "created_at"]
    search_fields = ["subject", "message"]
    list_filter = ["created_at", "branch"]


admin.site.register(Notice, NoticeAdmin)
admin.site.register(Branch)
admin.site.register(Profile)
