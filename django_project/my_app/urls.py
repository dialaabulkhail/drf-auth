from django.urls import path
from .views import AnimalListView
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('animals-list', AnimalListView.as_view(), name='animals_list'),
    path('token', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
