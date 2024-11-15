from django.urls import path
from .views import Registerview, Protectedview,Logoutview,UserProfileview
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)


urlpatterns = [
    path('register/', Registerview.as_view(), name='register'),
    path('profile/', UserProfileview.as_view(), name='profile'),
    path('protected/', Protectedview.as_view(), name='protected'),
     path('logout/', Logoutview.as_view(), name='logout'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]