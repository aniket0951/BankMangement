from django.contrib import admin
from .models import InformationsOfBank,BankLeader, NewAccountForm


class InformationsOfBankAdmin(admin.ModelAdmin):
    list_display = ('b_name','city','state','district','branch','employee','department')


class BankLeaderAdmin(admin.ModelAdmin):
    list_display = ('boss_name','address','educations','email_id','branch','payment','age')


class NewAccountFormAdmin(admin.ModelAdmin):
    list_display = ('name','address','district','catrgory','equcational_qulification','occupation','email_id')

admin.site.register(InformationsOfBank,InformationsOfBankAdmin)
admin.site.register(BankLeader,BankLeaderAdmin)
admin.site.register(NewAccountForm,NewAccountFormAdmin)