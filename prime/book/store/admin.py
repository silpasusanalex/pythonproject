from django.contrib import admin
from store.models import Table
# class UserAdmin(admin.ModelAdmin):
# 	 	fields = ['name','password','branch','admn_no','year','access']


admin.site.register(Table)
