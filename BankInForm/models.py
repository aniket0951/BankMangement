from django.db import models

# Create your models here.
class MyBaseModel(models.Model):
    id = models.AutoField(primary_key = True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)



class InformationsOfBank(MyBaseModel):
    b_name = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=155)
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    employee = models.IntegerField()
    department = models.IntegerField()


class BankLeader(MyBaseModel):
    boss_name = models.CharField(max_length=255)
    address = models.CharField(max_length=155, default=True)
    educations = models.CharField(max_length=255)
    email_id = models.CharField(max_length=155)
    branch = models.CharField(max_length=155)
    payment = models.IntegerField()
    age = models.IntegerField()

    verbose_name = 'Bank leaders'
    verbose_name_plural = 'Bank leader'


class NewAccountForm(MyBaseModel):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=155)
    district = models.CharField(max_length=100)
    catrgory = models.CharField(max_length=100)
    equcational_qulification = models.CharField(max_length=155)
    occupation = models.CharField(max_length=100)
    email_id = models.CharField(max_length=100)