from django.urls import path, include
from api import views

urlpatterns = [
    #--------- AUTHENTICATIONS URLs ---------#
    path('auth/register',views.UserRegisterView.as_view(),name="user_register"),#Registrar un usuario
    path('auth/login',views.UserLoginView.as_view(),name="user_login"),#Iniciar sesion
    path('auth/profile',views.UserProfileView.as_view(),name="user_user"),#Datos del usuario authenticado
    path('auth/changepassword',views.UserChangePasswordView.as_view(),name="user_changepassword"),#Cambiar la contraseña
    path('auth/forgotpassword/',include('django_rest_passwordreset.urls'),name="user_forgotpassword"),#Recuperar la contraseña
    path('auth/refresh-token', views.UserRefreshTokenView.as_view(), name='user_refreshtoken'),

    #------ USER URLs ------#
    path('users', views.UserListView.as_view(), name='user-list'),
    path('users/<int:id>', views.UserForIdView.as_view(), name='user-detail'),
    # path('users/delete/<int:id>', views.UserDeleteView.as_view(), name='user-delete'),
]