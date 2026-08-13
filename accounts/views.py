from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import InscriptionForm


def inscription_view(request):
    if request.method == 'POST':
        form = InscriptionForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('accueil')
    else:
        form = InscriptionForm()
    return render(request, 'accounts/inscription.html', {'form': form})


def deconnexion_view(request):
    logout(request)
    return redirect('accueil')
