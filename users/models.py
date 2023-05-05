from django.contrib.auth.models import AbstractUser
from django.db import models
import secrets
import uuid

class CustomUser(AbstractUser):
    secretKey = models.UUIDField(default=uuid.uuid4,editable=False)
