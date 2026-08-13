from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_centres_view, name='liste_centres'),
    path('creer/', views.creer_centre_view, name='creer_centre'),
    path('<int:pk>/', views.detail_centre_view, name='detail_centre'),
    path('<int:pk>/modifier/', views.modifier_centre_view, name='modifier_centre'),
]