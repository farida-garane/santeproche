from django.urls import path
from . import views

urlpatterns = [
    path('mes-dossiers/', views.mes_dossiers_view, name='mes_dossiers'),
    path('<int:pk>/', views.detail_dossier_view, name='detail_dossier'),
    path('creer/', views.creer_dossier_view, name='creer_dossier'),
]