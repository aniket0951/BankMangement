from django.shortcuts import render

from rest_framework.decorators import api_view,action
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, AllowAny
from Utils import custom_viewsets
from .models import AccountLogin, AccountSignUp, AccountRegister, TransactionReport, DeleteAccount, WithdrawMoneyFromBank, ShowAccount
from .serializers import AccountLoginSerializers, AccountSignUpSerializers, AccountRegisterSerializers,TransactionReportSerializers,DeleteAccountSerializers, WithdrawMoneyFromBankSerializers,ShowAccountSerializers


class AccountLoginModelViewSet(custom_viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    model = AccountLogin
    queryset = AccountLogin.objects.all()
    serializer_class = AccountLoginSerializers
    list_success_message = 'The account login list returend success'
    create_success_message = 'the login account create success'
    retrieve_success_message = 'account login in data retrieve success'
    status_code = 400
    response = {
        "status":None,
        "massage":None,
        "data": None
    }

    @action(detail=False, methods=['POST'])
    def account_regis(self,request):
        self.response.update({
            "status": True,
            "massage":'the account register success',
            "data": {}
        })
        return Response(self.response)


class AccountSignUpModelViewSet(custom_viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    model = AccountSignUp
    queryset = AccountSignUp.objects.all()
    serializer_class = AccountSignUpSerializers
    create_success_message = 'the sign up account is create'
    list_success_message = 'account signup the data list returend success'
    retrieve_success_message = 'the signup data retrieve success'
    status_code = 600
    response = {
        "status": None,
        "msg": None,
        "data": None
    }

    @action(detail=False, methods=['POST'])
    def accou_signup(self, request):
        self.response.update({
            "status": True,
            "msg": 'the account signup success',
            "data": {}   
        })
        return Response(self.response)


@api_view(['DELETE'])
def sign_up(request):
    id = request.data.get('id')
    if id is None or id =="":
        return Response('account please id')
    AccountSignUp.objects.filter(id=id).delete()
    response = {
        "status": True,
        "msg": 'the signup id delete success',
        "data": {}    
    }
    return Response(response)   


class AccountRegisterModelViewSet(custom_viewsets.ModelViewSet):
    model = AccountRegister
    queryset = AccountRegister.objects.all()
    serializer_class = AccountRegisterSerializers
    create_success_message = 'The account register success'
    list_success_message = 'account register data list  returend success'
    retrieve_success_message = 'the account retrieve success'
    status_code = 400
    response = {
        "status": None,
        "mssage": None,
        "data": None
    }

    @action(detail=False, methods=['PUT'])
    def account_register(self, request):
        self.response.update({
            "status": True,
            "mssage": 'the account register success',
            "data": {}
        })
        return Response(self.response)


class TransactionReportModelViewSet(custom_viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    model = TransactionReport
    queryset = TransactionReport.objects.all()
    serializer_class = TransactionReportSerializers
    create_success_message = 'the transaction report create'
    list_success_message = 'the transaction list data success'
    retrieve_success_message = 'the transaction retrieve success'
    status_code = 400
    response = {
        "satus": None,
        "msg": None,
        "data": None
    }

    @action(detail=False, methods=['PUT'])
    def transaction_report(self, request):
        self.response.update({
            "status": True,
            "msg": 'the transaction success',
            "data": {}
        })
        return Response(self.response)


class DeleteAccountModelViewSet(custom_viewsets.ModelViewSet):
    # permission_classes = [IsAdminUser]
    model = DeleteAccount
    queryset = DeleteAccount.objects.all()
    serializer_class = DeleteAccountSerializers
    create_success_message = 'the delete account create'
    list_success_message = 'the  delete account list data success'
    retrieve_success_message = 'the delete data retrieve success'
    status_code = 400
    response = {
        "status": None,
        "msg":None,
        "data": None
    }

    @action(detail=False, methods=['POST'])
    def delete_acco(self, reqest):
        self.response.update({
            "status": True,
            "msg": 'the account delete success',
            "data": {}
        })

        return Response(self.response)


class WithdrawMoneyFromBankModelViewSet(custom_viewsets.ModelViewSet):
    model = WithdrawMoneyFromBank
    queryset = WithdrawMoneyFromBank.objects.all()
    serializer_class = WithdrawMoneyFromBankSerializers
    create_success_message = 'the with drow money success'
    list_success_message = 'the with drow money data list returend success'
    status_code = 400
    response = {
        "status": None,
        "massage": None,
        "data": None
    }

    @action(detail=False, methods=['POST'])
    def withdrow_money(self, request):
        self.response.update({
            "status": True,
            "massage": 'the withdrow money success',
            "data": {}
        })
        return Response(self.response)
    

@api_view(['DELETE'])
def withdrow_money_(request):
    id = request.data.get('id')
    if id is None or id == "":
        return Response('Please money id')
    WithdrawMoneyFromBank.objects.filter(id=id).delete()
    response = {
        "status": 600,
        "msg": 'the with drow money id delete success',
        "data": {}
    }

    return Response(response)


class ShowAccountModelViewSet(custom_viewsets.ModelViewSet):
    model = ShowAccount
    queryset = ShowAccount.objects.all()
    serializer_class = ShowAccountSerializers
    create_success_message = 'the show account data create success'
    list_success_message = 'the show account data list success'
    retrieve_success_message = 'The show account is retrieve data success'
    status_code = 400
    response = {
        "status": None,
        "msg": None,
        "data": None
    }

    @action(detail=False, methods=['POST'])
    def show_account(self, request):
        self.response.update({
            "status": True,
            "msg": 'the show account data success',
            "data": {}
        })

        return Response(self.response)