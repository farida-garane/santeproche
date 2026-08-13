from django.shortcuts import render, redirect, get_object_or_404
from accounts.decorators import centre_required
from .models import HealthCenter
from .forms import HealthCenterForm


def liste_centres_view(request):
    centres = HealthCenter.objects.all()

    ville = request.GET.get('ville', '').strip()
    type_centre = request.GET.get('type_centre', '').strip()
    est_ouvert = request.GET.get('est_ouvert', '')

    if ville:
        centres = centres.filter(ville__icontains=ville)
    if type_centre:
        centres = centres.filter(type_centre=type_centre)
    if est_ouvert == 'oui':
        centres = centres.filter(est_ouvert=True)
    elif est_ouvert == 'non':
        centres = centres.filter(est_ouvert=False)

    return render(request, 'centers/liste.html', {
        'centres': centres,
        'types_centre': HealthCenter.TypeCentre.choices,
        'filtres': {
            'ville': ville,
            'type_centre': type_centre,
            'est_ouvert': est_ouvert,
        },
    })


def detail_centre_view(request, pk):
    centre = get_object_or_404(HealthCenter, pk=pk)
    return render(request, 'centers/detail.html', {'centre': centre})


@centre_required
def creer_centre_view(request):
    if request.method == 'POST':
        form = HealthCenterForm(request.POST)
        if form.is_valid():
            centre = form.save(commit=False)
            centre.gerant = request.user
            centre.save()
            return redirect('detail_centre', pk=centre.pk)
    else:
        form = HealthCenterForm()
    return render(request, 'centers/creer.html', {'form': form})


@centre_required
def modifier_centre_view(request, pk):
    centre = get_object_or_404(HealthCenter, pk=pk, gerant=request.user)
    if request.method == 'POST':
        form = HealthCenterForm(request.POST, instance=centre)
        if form.is_valid():
            form.save()
            return redirect('detail_centre', pk=centre.pk)
    else:
        form = HealthCenterForm(instance=centre)
    return render(request, 'centers/modifier.html', {'form': form})