from rest_framework.routers import SimpleRouter
from apps.users.viewsets import UserViewSet
from apps.authentication.viewsets import LoginViewSet, RegistrationViewSet, RefreshViewSet
from django.urls import path, include

routes = SimpleRouter()

# AUTHENTICATION
routes.register(r'api/auth/login', LoginViewSet, basename='auth-login')
routes.register(r'api/auth/register', RegistrationViewSet, basename='auth-register')
routes.register(r'api/auth/refresh', RefreshViewSet, basename='auth-refresh')

# USER
routes.register(r'api/user', UserViewSet, basename='user')


urlpatterns = [
   path('',include(routes.urls))
    ]
    