from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404
from accounts.decorators import soignant_required, patient_required
from .models import MedicalRecord
from .forms import MedicalRecordForm


@login_required
@patient_required
def mes_dossiers_view(request):
    dossiers = MedicalRecord.objects.filter(patient=request.user).order_by('-date_consultation')
    return render(request, 'records/mes_dossiers.html', {'dossiers': dossiers})


@login_required
def detail_dossier_view(request, pk):
    dossier = get_object_or_404(MedicalRecord, pk=pk)
    if request.user != dossier.patient and request.user != dossier.soignant:
        raise Http404
    retour_url = 'mes_dossiers' if request.user.is_patient() else 'accueil'
    return render(request, 'records/detail_dossier.html', {
        'dossier': dossier,
        'retour_url': retour_url,
    })


@login_required
@soignant_required
def creer_dossier_view(request):
    if request.method == 'POST':
        form = MedicalRecordForm(request.POST)
        if form.is_valid():
            dossier = form.save(commit=False)
            dossier.soignant = request.user
            dossier.save()
            return redirect('accueil')
    else:
        form = MedicalRecordForm()
    return render(request, 'records/creer_dossier.html', {'form': form})