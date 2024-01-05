from django.urls import path, include
from backendCV import views

urlpatterns = [
    #--------- AUTHENTICATIONS URLs ---------#
    path('auth/login', views.UserLoginView.as_view(), name='login'),
    path('auth/register', views.UserRegisterView.as_view(), name='register'),
    path('auth/change-password', views.UserChangePasswordView.as_view(), name='change-password'),
    path('auth/refresh-token', views.UserRefreshTokenView.as_view(), name='refresh-token'),
    path('auth/forgot-password', include('django_rest_passwordreset.urls', namespace='forgot-password')),

    #------ USER URLs ------#
    path('user', views.UserList.as_view(), name='user-list'),
    path('user/<int:id>', views.UserForId.as_view(), name='user-detail'),
]