
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from jobBoard.app.authentification.views import login_view, signupView, logoutView
from jobBoard.app.job.candidate_views import (
    candidateProfilView,
    posterView,
    homeView
)
from jobBoard.app.job.employer_views import (
    dashboardView,
    offerFormView,
    offerView,
    employer_profil_view,
    detailOfferView,
    delete_offer,
    update_offer,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/login/', login_view, name='login'),
    path('account/signup/', signupView, name='signup'),
    path('logout/', logoutView, name="logout"),

    path('dashboard/', dashboardView, name='dashboard'),
    path('dashboard/profil/', employer_profil_view, name="employer_profile"),
    path('employer_offer/', offerView, name="employer_offer"),
    path('employer_offer/<uuid:offer_id>/', detailOfferView, name="offer_detail"),
    path('dashboard/post/', offerFormView, name='offerForm'),
    path('employer_offer/<uuid:offer_id>/update/', update_offer, name="update_offer"),
    path('employer_offer/<uuid:offer_id>/delete/', delete_offer, name="delete_offer"),

    path('', homeView, name="home"),
    path('profil/', candidateProfilView, name="candidate_profil"),
    path('offer/uuid:<offer_id>/', posterView, name="apply_for_job"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
