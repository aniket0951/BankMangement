from django.shortcuts import render
from rest_framework.response import Response
from Utils import custom_viewsets
from rest_framework.decorators import action, api_view
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.viewsets import ModelViewSet
from .models import InformationsOfBank, BankLeader,NewAccountForm
from .serializers import InformationsOfBankSerializers, BankLeaderSerializers, NewAccountFormSerializers


class InformationsOfBankModelViewSet(custom_viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    model = InformationsOfBank
    queryset = InformationsOfBank.objects.all()
    serializer_class = InformationsOfBankSerializers
    list_success_message = " bank inform list returend success"
    retrieve_success_message = "bank inform retrieve returend success"
    create_success_message = "information of bankcreate"
    status_code = 400
    response = {
        "status": None,
        "msg": None,
        "data": None
    }

    @action(detail=False, methods=['POST'])
    def bank_inform(self, request):
        self.response.update({
            "status": True,
            "msg": "the information of bank great",
            "data": {}
        })
        return Response(self.response)


@api_view(['POST'])
def inform_(request):
    b_name = request.data.get('b_name')
    city = request.data.get('city')
    state = request.data.get('state')
    district = request.data.get('district')
    branch = request.data.get('branch')
    employee = request.data.get('employee')
    department = request.data.get('department')

    if b_name and city:
        res = InformationsOfBank.objects.create(b_name=b_name, city=city, state=state, district=district,
                                                branch=branch, employee=employee, department=department)
        serializers = InformationsOfBankSerializers(res)
        response = {
            "status": True,
            "massage": "the good informatio of bank",
            "data": serializers.data
        }
        return Response(response)
    else:
        return Response('The no happy !')


class BankLeaderModelViewSet(custom_viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    model = BankLeader
    queryset = BankLeader.objects.all()
    serializer_class = BankLeaderSerializers
    list_success_message = " bank boss list returend success"
    retrieve_success_message = "bank boss retrieve returend success"
    create_success_message = "boss of bank create"
    status_code = 400
    response = {
        "status":None,
        "mssage": None,
        "data": None
    }
    
    @action(detail=False, methods=['POST'])
    def bank_boss(self,request):
        self.response.update({
            "status": True,
            "mssage":"the boss is data success !",
            "data": {}
        })

        return Response(self.response)



class NewAccountFormModelViewSet(custom_viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    model = NewAccountForm
    queryset = NewAccountForm.objects.all()
    serializer_class = NewAccountFormSerializers
    create_success_message = 'the new account create success'
    list_success_message = "the new account list returend success"
    retrieve_success_message = "new account retrieve returend success"
    status_code = 400
    response = {
        "status":None,
        "mssage": None,
        "data":None
    }

    @action(detail=False, methods=['POST'])
    def account_form(self, request):
        self.response.update({
            "status":True,
            "mssage":'the new account success',
            "data": {}
        })
        
        return Response(self.response)