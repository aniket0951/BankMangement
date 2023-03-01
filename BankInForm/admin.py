from django.contrib import admin
from .models import InformationsOfBank,BankLeader


class InformationsOfBankAdmin(admin.ModelAdmin):
    list_display = ('b_name','city','state','district','branch','employee','department')


class BankLeaderAdmin(admin.ModelAdmin):
    list_display = ('boss_name','address','educations','email_id','branch','payment','age')

admin.site.register(InformationsOfBank,InformationsOfBankAdmin)
admin.site.register(BankLeader,BankLeaderAdmin)