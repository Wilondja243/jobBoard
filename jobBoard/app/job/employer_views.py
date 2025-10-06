from django.db.models import Count, Sum
from django.contrib import messages
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404

from jobBoard.app.authentification.models import User
from jobBoard.app.job.models import Offer, Application, EmployerProfil
from .forms import OfferForm, EmployerProfilForm


@never_cache
@login_required
def dashboardView(request):
    offer = Offer.objects.filter(employer__user=request.user).aggregate(
        total_offer=Count('id', distinct=True),
        total_offer_poster=Count('applications__job_offer', distinct=True),
        total_candidate_offer_poster=Count('applications__user', distinct=True)
    )
    print(offer)

    context = {
        "offer": offer,
        "candidate_poster": Application.objects.filter(job_offer__employer__user=request.user).select_related('job_offer', 'user'),
    }
    return render(request, 'job/employer/dashboard.html', context)


@never_cache
@login_required
def offerView(request):
    offers = Offer.objects.filter(employer__user=request.user).order_by('created_at')
    return render(request, 'job/employer/employer_offer.html', {'offers': offers})

@never_cache
@login_required
def detailOfferView(request, offer_id):
    offer = get_object_or_404(Offer, id=offer_id)
    print(offer.title)
    return render(request, "job/employer/employer_offer_detail.html", {'offer': offer})

@never_cache
@login_required
def offerFormView(request):
    if request.method == "POST":
        form = OfferForm(request.POST)

        if form.is_valid():
            offer = form.save(commit=False)
            offer.employer = request.user.employerprofil
            offer.save()

            messages.success(request, "L'offre a été crée avec success.")
            return redirect('dashboard')
    else:
        form = OfferForm()

    return render(request, 'job/employer/offerForm.html', {'form': form, 'title': "Crée l'offre"})


@never_cache
@login_required
def update_offer(request, offer_id):
    offer = get_object_or_404(Offer, id=offer_id)

    if request.method == "POST":
        form = OfferForm(request.POST, instance=offer)

        if form.is_valid():
            form.save()
            messages.success(request, "L'offre a été mise à jour avec succès.")
            return redirect("offer_detail", offer_id=offer.id)
    else:
        form = OfferForm(instance=offer)

    return render(request, "job/employer/offerForm.html", {'form': form, 'offer': offer, 'title': "Modifier l'offre"})


@never_cache
@login_required
def delete_offer(request, offer_id):
    offer = get_object_or_404(Offer, id=offer_id)

    if request.method == "POST":
        offer.delete()
        messages.success(request, "L'offre supprimée avec success.")
        return redirect('dashboard')
    
    return render(request, "job/employer/delete_offer.html", {'offer': offer})


@never_cache
@login_required
def employer_profil_view(request):
    user = get_object_or_404(User, id=request.user.id)
    employer_profil = user.employerprofil

    offers = Offer.objects.filter(employer__user=request.user).annotate(
        total_candidate=Count('applications')
    )

    return render(request, "job/employer/employerProfile.html", {'profil': employer_profil, 'offers': offers})

@never_cache
@login_required
def update_profile(request, profile_id):
    profile = get_object_or_404(EmployerProfil, id=profile_id)

    if request.method == "POST":
        form = EmployerProfilForm(request.POST, files=request.FILES, instance=profile)

        if form.is_valid():
            form.save()
            messages.success(request, "Profil a été mise à jour avec succès.")
            return redirect("employer_profile", profile_id=profile.id)
    else:
        form = EmployerProfilForm(instance=profile)

    return render(request, "job/employer/update_profile.html", {'form': form})