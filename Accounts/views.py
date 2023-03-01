from django.shortcuts import render

from rest_framework.decorators import api_view,action
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, AllowAny
from Utils import custom_viewsets
from .models import AccountRegister
from .serializers import AccountRegisterSerializers


class AccountRegisterModelViewSet(custom_viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    model = AccountRegister
    queryset = AccountRegister.objects.all()
    serializer_class = AccountRegisterSerializers
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
