
# Create your models here.
from django.db import models
import string
import random

class ShortenedURL(models.Model):
    original_url = models.URLField()
    short_code = models.CharField(max_length=6, unique=True)

    def save(self, *args, **kwargs):
        if not self.short_code:
            self.short_code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        super().save(*args, **kwargs)
