from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import EmpolyeeInformationModelViewSet,employee_,PassbookInformModelViewSet

router = DefaultRouter()
router.register("emp_inform",EmpolyeeInformationModelViewSet)
router.register("passbook_",PassbookInformModelViewSet)

urlpatterns = [
    *router.urls,
    path('employee_',employee_),
]