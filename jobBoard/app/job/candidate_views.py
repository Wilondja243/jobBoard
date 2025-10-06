from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.contrib import messages

from jobBoard.app.authentification.models import User
from .models import Offer, Application, CandidateProfil


@login_required
def homeView(request):
    context = {
        'offers': Offer.objects.all()
    }
    return render(request, "job/candidate/home.html", context)


@login_required
def posterView(request, offer_id):
    job_offer = get_object_or_404(Offer, id=offer_id)

    has_applied = Application.objects.filter(user__user=request.user, job_offer=job_offer).exists()

    if request.method == "POST":
        if has_applied:
            messages.error(request, "Offre déjà postulé")
            return redirect('home')
        try:
            Application.objects.create(
                job_offer = job_offer,
                user = request.user.candidateprofil,
                status = "PENDING"
            )
            messages.success(request, "Candidature soumise avec succès !")
            return redirect('home')
        
        except Exception as e:
            print(str(e))
            return redirect('apply_for_job', offer_id=offer_id)

    return render(request, "job/candidate/detail.html", {'has_applied': has_applied, 'job_offer': job_offer})

@login_required
def candidateProfilView(request):
    return render(request, "job/candidate/candidateProfil.html")