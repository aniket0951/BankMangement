from django.contrib import admin

from .models import AccountLogin,AccountSignUp,AccountRegister,TransactionReport,DeleteAccount,WithdrawMoneyFromBank,ShowAccount

class AccountLoginAdmin(admin.ModelAdmin):
    list_display = ('user_name','address','email_id','acco_no','phone_no','password')


class AccountSignUpAdmin(admin.ModelAdmin):
    list_display = ('email_id','create_password','confirm_password','forword_password','user_signature')


class AccountRegisterAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','email','accou_type','gender','birth_date','password',
                    'password_confirmation','street_address','city','country','postal_code')
    

class TransactionReportAdmin(admin.ModelAdmin):
    list_display = ('t_date','transaction_type','amount','balance_after_transaction')


class DeleteAccountAdmin(admin.ModelAdmin):
    list_display = ('name','account_no','email')


class WithdrawMoneyFromBankAdmin(admin.ModelAdmin):
    list_display = ('name','b_name','account_no','rupees','words_rupees','phone_no','signature')


class ShowAccountAdmin(admin.ModelAdmin):
    list_display = ('account_no','acco_holder_name','account_type','balance_amount')

admin.site.register(AccountLogin,AccountLoginAdmin)
admin.site.register(AccountSignUp,AccountSignUpAdmin)
admin.site.register(AccountRegister,AccountRegisterAdmin)
admin.site.register(TransactionReport,TransactionReportAdmin)
admin.site.register(DeleteAccount,DeleteAccountAdmin)
admin.site.register(WithdrawMoneyFromBank,WithdrawMoneyFromBankAdmin)
admin.site.register(ShowAccount,ShowAccountAdmin)