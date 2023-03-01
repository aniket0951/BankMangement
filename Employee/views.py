from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from Utils import custom_viewsets
from rest_framework.permissions import IsAdminUser,AllowAny
from .models import EmpolyeeInformation,PassbookInform, BankHRInform, CheckBook
from .serializers import EmpolyeeInformationSerializers,PassbookInformSerializers, BankHRInformSerializers, CheckBookSerializers



class EmpolyeeInformationModelViewSet(custom_viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    model = EmpolyeeInformation
    queryset = EmpolyeeInformation.objects.all()
    serializer_class = EmpolyeeInformationSerializers
    create_success_message = 'the employee information create'
    list_success_message = "the employee list returend success"
    retrieve_success_message = "the employee retrieve returend success"
    status_code = 400
    response = {
        "status":None,
        "mssage": None,
        "data": None
    }

    @action(detail=False, methods=['POST'])
    def emp_inform(self, request):
        self.response.update({
            "status": True,
            "mssage": 'The employee inform complate success !',
            "data": {}
        })

        return Response(self.response)


@api_view(['DELETE'])
def employee_(request):
    id = request.data.get('id')
    if id is None or id == "":
        return Response('employee please id')
    EmpolyeeInformation.objects.filter(
        id= id).delete()
    response = {
        "status": True,
        "msg": 'employee id delete success',
        "data": {}
    }
    return Response(response)


class PassbookInformModelViewSet(custom_viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    model = PassbookInform
    queryset = PassbookInform.objects.all()
    serializer_class = PassbookInformSerializers
    list_success_message = 'the passbook data list returend success'
    retrieve_success_message = 'the passbook data retrieve'
    create_success_message = 'the passbook is create'
    status_code = 400
    response = {
        "status":None,
        "msg":None,
        "data":None
    }

    @action(detail=False, methods=['POST'])
    def passbook_(self, request):
        self.response.update({
            "status": True,
            "msg": 'the passbookn ready',
            "data":{}
        })

        return Response(self.response)


class BankHRInformModelViewSet(custom_viewsets.ModelViewSet):
    # permission_classes = [AllowAny]
    model = BankHRInform
    queryset = BankHRInform.objects.all()
    serializer_class = BankHRInformSerializers
    create_success_message = 'The hr inform create success'
    list_success_message = 'The hr data featch list returend success'
    retrieve_success_message = 'the hr data retrieve success'
    status_code = 400
    response = {
        "status": None,
        "msg": None,
        "data": None
    }

    @action(detail=False, methods=['POST'])
    def hr_information(self, request):
        self.response.update({
            "status": True,
            "msg": 'the hr inform correct',
            "data":{}
        })

        return Response(self.response)

@api_view(['DELETE'])
def bank_hr(request):
    id = request.data.get('id')
    if id is None or id == "":
        return Response('please hr id')
    BankHRInform.objects.filter(id=id).delete()
    response = {
        "status": True,
        "msg": 'the hr id delete success',
        "data": {}
    }
    return Response(response)


class CheckBookModelViewSet(custom_viewsets.ModelViewSet):
    model = CheckBook
    queryset = CheckBook.objects.all()
    serializer_class = CheckBookSerializers
    create_success_message = 'The check book is create'
    list_success_message = 'The check book data is list success'
    retrieve_success_message = 'The check book is retrieve success'
    status_code = 400
    response = {
        "status":None,
        "massage":None,
        "data": None
    }

    @action(detail=False, methods=['POST'])
    def check_book(self, request):
        self.response.update({
            "sattus":True,
            "massage":'The check book is update',
            "data":{}
        })

        return Response(self.response)


@api_view(['DELETE'])
def check_(request):
    id = request.data.get('id')
    if id is None or id == "":
        return Response('plase check book id ')
    CheckBook.objects.filter(id=id).delete()
    response = {
        "status": True,
        "massage": 'the check book ke id delete success',
        "data":{}
    }
    return Response(response)