from django.urls import path

from rest_framework.routers import DefaultRouter
from .views import AccountLoginModelViewSet, AccountSignUpModelViewSet, sign_up, AccountRegisterModelViewSet,TransactionReportModelViewSet, DeleteAccountModelViewSet,WithdrawMoneyFromBankModelViewSet,withdrow_money_,ShowAccountModelViewSet

router = DefaultRouter()
router.register("account_login",AccountLoginModelViewSet)
router.register("accou_signup",AccountSignUpModelViewSet)
router.register("account_register",AccountRegisterModelViewSet)
router.register("transaction_report",TransactionReportModelViewSet)
router.register("delete_acco",DeleteAccountModelViewSet)
router.register("withdrow_money",WithdrawMoneyFromBankModelViewSet)
router.register("show_account", ShowAccountModelViewSet)

urlpatterns = [
    *router.urls,
    path('sign_up',sign_up),
    path('withdrow_money',withdrow_money_),
]