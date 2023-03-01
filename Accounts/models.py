from django.db import models
from BankInForm.models import MyBaseModel



class AccountRegister(MyBaseModel):
    user_name = models.CharField(max_length=255)
    address = models.CharField(max_length=100)
    email_id = models.CharField(max_length=255)
    acco_no = models.IntegerField()
    phone_no = models.IntegerField()
    password = models.IntegerField()
    
