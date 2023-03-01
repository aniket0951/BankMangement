from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import InformationsOfBankModelViewSet,inform_,BankLeaderModelViewSet,NewAccountFormModelViewSet

router = DefaultRouter()
router.register("bank_inform",InformationsOfBankModelViewSet)
router.register("bank_boss",BankLeaderModelViewSet)
router.register("new_account", NewAccountFormModelViewSet)

urlpatterns = [
    *router.urls,
    path('inform_',inform_),

]