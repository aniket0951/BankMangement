from django.db import models
from BankInForm.models import MyBaseModel



class AccountLogin(MyBaseModel):
    user_name = models.CharField(max_length=255)
    address = models.CharField(max_length=100)
    email_id = models.CharField(max_length=255)
    acco_no = models.IntegerField()
    phone_no = models.IntegerField()
    password = models.IntegerField()

    verbose_name = 'Account logins'
    verbose_name_plural = 'Account Login'


class AccountSignUp(MyBaseModel):
    email_id = models.CharField(max_length=255)
    create_password = models.IntegerField()
    confirm_password = models.IntegerField()
    forword_password = models.IntegerField()
    user_signature = models.CharField(max_length=255)


class AccountRegister(MyBaseModel):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    accou_type = models.CharField(max_length=100)
    gender = models.CharField(max_length=255)
    birth_date = models.DateTimeField(auto_now_add=True)
    password = models.IntegerField()
    password_confirmation = models.IntegerField()
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=255)
    postal_code = models.IntegerField()


class TransactionReport(MyBaseModel):
    t_date = models.DateTimeField(auto_now_add=True)
    transaction_type = models.CharField(max_length=255)
    amount = models.IntegerField()
    balance_after_transaction = models.IntegerField()


class DeleteAccount(MyBaseModel):
    name = models.CharField(max_length=255)
    account_no = models.IntegerField()
    email = models.CharField(max_length=100)


class WithdrawMoneyFromBank(MyBaseModel):
    name = models.CharField(max_length=255)
    b_name = models.CharField(max_length=100)
    account_no = models.IntegerField()
    rupees = models.IntegerField()
    words_rupees = models.CharField(max_length=100)
    phone_no = models.IntegerField()
    signature = models.CharField(max_length=100)


class ShowAccount(MyBaseModel):
    account_no = models.IntegerField()
    acco_holder_name = models.CharField(max_length=100)
    account_type = models.CharField(max_length=100)
    balance_amount = models.IntegerField()