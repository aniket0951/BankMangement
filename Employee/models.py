from django.db import models
from BankInForm.models import MyBaseModel
# Create your models here.


class EmpolyeeInformation(MyBaseModel):
    no_emp = models.IntegerField()
    branch = models.CharField(max_length=155)
    payment = models.IntegerField()
    department = models.CharField(max_length=155)
    education = models.CharField(max_length=255)
    experience = models.IntegerField()



class PassbookInform(MyBaseModel):
    branch = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    tel_no = models.IntegerField()
    telephone = models.IntegerField()
    MICR_code = models.IntegerField()
    IFSC_code = models.CharField(max_length=100)
    account_type = models.CharField(max_length=255)
    account_no = models.CharField(max_length=100)
    passbook_no = models.IntegerField()
    acc_open_date = models.DateTimeField(auto_now_add=True)
    passbook_type = models.CharField(max_length=100)
    self_address = models.CharField(max_length=255)


class BankHRInform(MyBaseModel):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    education = models.CharField(max_length=255)
    branch_name = models.CharField(max_length=100)
    phone_no = models.IntegerField()
    payment = models.IntegerField()
    email = models.CharField(max_length=100)


class CheckBook(MyBaseModel):
    account_no = models.IntegerField()
    rupees = models.IntegerField()
    pay = models.IntegerField()
    signature = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    day = models.CharField(max_length=100) 


