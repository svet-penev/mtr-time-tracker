from django.conf.urls import url, include

from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token

from time_tracker.views import CompanyViewSet , ProjectViewSet, ProfileViewSet


router = routers.DefaultRouter()
router.register(r"companies", CompanyViewSet)
router.register(r"projects", ProjectViewSet)
router.register(r"profiles", ProfileViewSet)

urlpatterns = [
    url(r'', include(router.urls)),
    url(r"^auth/jwt/new/", obtain_jwt_token),
    url(r"^auth/jwt/refresh/", refresh_jwt_token),
    url(r"^auth/jwt/verify/", verify_jwt_token),
]