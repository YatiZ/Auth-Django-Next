from django.urls import path, re_path
from .views import (
    CustomTokenObtainPairView,
    CustomTokenRefreshView,
    CustomTokenVerfiyView,
    LogoutView,
    CustomProviderAuthView
)

urlpatterns = [
    re_path(
        r'^o/(?P<provider>\S+)/$',
        CustomProviderAuthView.as_view(),
        name='provider_auth_view'
    ),
    path('jwt/create/',CustomTokenObtainPairView.as_view()),
    path('jwt/refresh/',CustomTokenRefreshView.as_view()),
    path('jwt/verify/',CustomTokenVerfiyView.as_view()),
    path('logout/',LogoutView.as_view()),
]
