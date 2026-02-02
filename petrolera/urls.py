from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PozoViewSet

router = DefaultRouter()
router.register(r'pozos', PozoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]