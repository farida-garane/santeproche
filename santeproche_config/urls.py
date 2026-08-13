from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from records.models import MedicalRecord
from centers.models import HealthCenter


def accueil_view(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        if user.is_patient():
            context['role_dashboard'] = 'patient'
            context['dossiers'] = (
                MedicalRecord.objects.filter(patient=user)
                .order_by('-date_consultation')[:5]
            )
        elif user.is_soignant():
            context['role_dashboard'] = 'soignant'
            context['dossiers'] = (
                MedicalRecord.objects.filter(soignant=user)
                .select_related('patient')
                .order_by('-date_consultation')[:5]
            )
        elif user.is_centre():
            context['role_dashboard'] = 'centre'
            context['centre'] = HealthCenter.objects.filter(gerant=user).first()
    return render(request, 'accueil.html', context)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', accueil_view, name='accueil'),
    path('centers/', include('centers.urls')),
    path('records/', include('records.urls')),

]
