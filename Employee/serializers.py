from rest_framework import serializers
from .models import EmpolyeeInformation, PassbookInform,BankHRInform,CheckBook

class EmpolyeeInformationSerializers(serializers.ModelSerializer):
    class Meta:
        model = EmpolyeeInformation
        fields = '__all__'


class PassbookInformSerializers(serializers.ModelSerializer):
    class Meta:
        model = PassbookInform
        fields ='__all__'


class BankHRInformSerializers(serializers.ModelSerializer):
    class Meta:
        model = BankHRInform
        fields = '__all__'


class CheckBookSerializers(serializers.ModelSerializer):
    class Meta:
        model = CheckBook
        fields = '__all__'