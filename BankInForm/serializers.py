from rest_framework import serializers
from .models import InformationsOfBank,BankLeader, NewAccountForm


class InformationsOfBankSerializers(serializers.ModelSerializer):
    class Meta:
        model = InformationsOfBank
        fields = '__all__'


class BankLeaderSerializers(serializers.ModelSerializer):
    class Meta:
        model = BankLeader
        fields = '__all__'


class NewAccountFormSerializers(serializers.ModelSerializer):
    class Meta:
        model = NewAccountForm
        fields = '__all__'