from django.contrib import admin
from .models import EmpolyeeInformation,PassbookInform,BankHRInform,CheckBook


class EmpolyeeInformationAdmin(admin.ModelAdmin):
    list_display = ('no_emp','branch','payment','department','education','experience')


class PassbookInformAdmin(admin.ModelAdmin):
    list_display = ('branch','address','tel_no','telephone','MICR_code','IFSC_code','account_type',
                    'account_no','passbook_no','acc_open_date','passbook_type','self_address')

class BankHRInformAdmin(admin.ModelAdmin):
    list_display = ('name','address','education','branch_name','phone_no','payment','email')


class CheckBookAdmin(admin.ModelAdmin):
    list_display = ('account_no','rupees','pay','signature','date','day')

admin.site.register(EmpolyeeInformation,EmpolyeeInformationAdmin)
admin.site.register(PassbookInform,PassbookInformAdmin)
admin.site.register(BankHRInform,BankHRInformAdmin)
admin.site.register(CheckBook,CheckBookAdmin)