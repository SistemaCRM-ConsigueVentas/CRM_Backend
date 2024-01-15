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

    #------ ROLE URLs ------#
    path('roles', views.RoleListCreateView.as_view(), name='role-list'),
    path('roles/create', views.RoleListCreateView.as_view(), name='role-create'),

    #------ GROUP URLs  (para los grupos de permisos ejemplo(administrador,empleado))------#
    path('groups',views.GroupListView.as_view(), name='group-list'),
    path('groups/create',views.GroupCreateView.as_view(), name='group-create'),

    #------ PERMISSIONS URLs  (para los permisos de cada modelo ejemplo(crear empleado,editar empleado ,etc))------#
    path('permissions',views.PermissionsListView.as_view(), name='permission-list'),
    # path('groups/create',views.GroupCreateView.as_view(), name='group-create'),

    #------ USER URLs ------#
    path('users', views.UserListView.as_view(), name='user-list'),
    path('users/create', views.UserCreateView.as_view(), name='user-create'),
    path('users/<int:id>', views.UserForIdView.as_view(), name='user-detail'),
    path('users/update/<int:id>', views.UserUpdateView.as_view(), name='user-update'),
    path('users/delete/<int:id>', views.UserDeleteView.as_view(), name='user-delete'),
    
    
    #------ CLIENT URLs #------#
    path('clients', views.ClientListCreateView.as_view(), name='client-list'),
    path('clients/create', views.ClientListCreateView.as_view(), name='client-create'),
    path('clients/<int:pk>', views.ClientDetailUpdateDestroyView.as_view(), name='client-detail'),
    path('clients/update/<int:pk>', views.ClientDetailUpdateDestroyView.as_view(), name='client-update'),
    path('clients/delete/<int:pk>', views.ClientDetailUpdateDestroyView.as_view(), name='client-delete'),
    
    #------ SALE URLs #------#

    path('sales', views.SaleListCreateView.as_view(), name='sale-list'),
    path('sales/create', views.SaleListCreateView.as_view(), name='sale-create'),
    path('sales/<int:pk>', views.SaleDetailUpdateDestroyView.as_view(), name='sale-detail'),
    path('sales/update/<int:pk>', views.SaleDetailUpdateDestroyView.as_view(), name='sale-update'),
    path('sales/delete/<int:pk>', views.SaleDetailUpdateDestroyView.as_view(), name='sale-delete'),
    
]