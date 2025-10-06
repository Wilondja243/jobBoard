
from uuid import uuid4
from django.db import models
from django.conf import settings


class Offer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    employer = models.ForeignKey('EmployerProfil', on_delete=models.SET_NULL, null=True, related_name="offers")
    title = models.CharField(max_length=50)
    competence = models.CharField(max_length=100)
    experience = models.CharField(max_length=100, null=True, blank=True)
    delay = models.CharField(max_length=50, null=True, blank=True)
    profil = models.CharField(max_length=150, null=True, blank=True)
    description = models.TextField()

    contract_type = models.CharField(max_length=20)
    salary = models.IntegerField(null=True, blank=True)
    workplace = models.CharField(max_length=50)

    company_name = models.CharField(max_length=50)
    activity_sector = models.CharField(max_length=50, null=True, blank=True)
    coordinate = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class EmployerProfil(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    logo = models.ImageField(upload_to="profil_employer", null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    phone_number = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CandidateProfil(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profil_image = models.ImageField(upload_to="profil_candidate", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Application(models.Model):
    STATUS_CHOICES = (
        ("PENDIG", "EN ATTENTE"),
        ("ACCEPTED", "ACCEPTER"),
    )
    
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    job_offer = models.ForeignKey(Offer, on_delete=models.CASCADE, related_name="applications" )
    user = models.ForeignKey(CandidateProfil, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS_CHOICES, max_length=50, default="PENDIG")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



