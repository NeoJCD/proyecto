from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView
from petrolera.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('api/petrolera/', include('petrolera.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]