from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import EmpolyeeInformationModelViewSet,employee_,PassbookInformModelViewSet,BankHRInformModelViewSet,CheckBookModelViewSet,check_, bank_hr

router = DefaultRouter()
router.register("emp_inform",EmpolyeeInformationModelViewSet)
router.register("passbook_",PassbookInformModelViewSet)
router.register("hr_information", BankHRInformModelViewSet)
router.register("check_book", CheckBookModelViewSet)

urlpatterns = [
    *router.urls,
    path('employee_',employee_),
    path('check_',check_),
    path('bank_hr',bank_hr),
]