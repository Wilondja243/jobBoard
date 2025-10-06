from uuid import uuid4
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ROLE_CHOICES = (
        ('candidate', 'Candidate'),
        ('employer', ('Employer'))
    )

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)