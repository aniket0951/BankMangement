from rest_framework import serializers
from .models import EmpolyeeInformation, PassbookInform

class EmpolyeeInformationSerializers(serializers.ModelSerializer):
    class Meta:
        model = EmpolyeeInformation
        fields = '__all__'


class PassbookInformSerializers(serializers.ModelSerializer):
    class Meta:
        model = PassbookInform
        fields ='__all__'