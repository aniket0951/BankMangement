from rest_framework import serializers
from .models import AccountLogin, AccountSignUp, AccountRegister,TransactionReport,DeleteAccount,WithdrawMoneyFromBank,ShowAccount


class AccountLoginSerializers(serializers.ModelSerializer):
    class Meta:
        model = AccountLogin
        fields = '__all__'


class AccountSignUpSerializers(serializers.ModelSerializer):
    class Meta:
        model = AccountSignUp
        fields = '__all__'


class AccountRegisterSerializers(serializers.ModelSerializer):
    class Meta:
        model = AccountRegister
        fields = '__all__'


class TransactionReportSerializers(serializers.ModelSerializer):
    class Meta:
        model = TransactionReport
        fields = '__all__'


class DeleteAccountSerializers(serializers.ModelSerializer):
    class Meta:
        model = DeleteAccount
        fields = '__all__'


class WithdrawMoneyFromBankSerializers(serializers.ModelSerializer):
    class Meta:
        model = WithdrawMoneyFromBank
        fields = '__all__'


class ShowAccountSerializers(serializers.ModelSerializer):
    class Meta:
        model = ShowAccount
        fields = '__all__'