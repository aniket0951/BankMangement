from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from Utils import custom_viewsets
from rest_framework.permissions import IsAdminUser,AllowAny
from .models import EmpolyeeInformation,PassbookInform
from .serializers import EmpolyeeInformationSerializers,PassbookInformSerializers



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