from rest_framework import serializers
from .models import AccountRegister


class AccountRegisterSerializers(serializers.ModelSerializer):
    class Meta:
        mode = AccountRegister
        fields = '__all__'