from django.contrib import admin
from . models import District,Branch

class DistrictAdmin(admin.ModelAdmin):
    List_display = ['district']
admin.site.register(District,DistrictAdmin)

class BranchAdmin(admin.ModelAdmin):
    List_display = ['branch']
admin.site.register(Branch,BranchAdmin)




