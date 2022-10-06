from django.db import models
from datetime import datetime
from django.db import models
from django.contrib.auth.models import *

class Information(models.Model):
    title = models.TextField(null=True, blank=True)
    image = models.CharField(max_length=300, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateField(default=datetime.now, null=True, blank=True)
    modified_at = models.DateField(default=datetime.now, null=True, blank=True)
