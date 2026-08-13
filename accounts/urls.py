from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path('inscription/', views.inscription_view, name='inscription'),
    path('connexion/', LoginView.as_view(template_name='accounts/connexion.html'), name='login'),
    path('deconnexion/', views.deconnexion_view, name='deconnexion'),
]
