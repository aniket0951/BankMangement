from django.urls import path

from rest_framework.routers import DefaultRouter
from .views import AccountRegisterModelViewSet

router = DefaultRouter()
router.register("account_regis",AccountRegisterModelViewSet)

urlpatterns = [
    *router.urls,
]