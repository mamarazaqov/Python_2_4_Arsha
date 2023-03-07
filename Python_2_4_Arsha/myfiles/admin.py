from django.contrib import admin
from myfiles.models import *
# Register your models here.

class AdminPort(admin.ModelAdmin):
    list_display = ['id','nomi','comp_nomi','date','rasm1']
admin.site.register(Portfolio,AdminPort)

class AdminTur(admin.ModelAdmin):
    list_display = ['id','nomi']
admin.site.register(Type,AdminTur)

class AdminServices(admin.ModelAdmin):
    list_display = ['rasmi','nomi','text','sana']
admin.site.register(Services,AdminServices)

class AdminTeam(admin.ModelAdmin):
    list_display = ['ismi','familyasi','yoshi','sana','text','rasmi']
admin.site.register(Team,AdminTeam)

# class AdminTur(admin.ModelAdmin):
#     list_display = ['id','nomi']
# admin.site.register(Type1,AdminTur)
#
# class AdminTur(admin.ModelAdmin):
#     list_display = ['id','nomi']
# admin.site.register(Type2,AdminTur)
