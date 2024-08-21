from django.db import models

class Package(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField()
    authorized = models.BooleanField(default=False)
    authorized_at = models.DateField(default=None, null=True, blank=True)
    risk = models.CharField(max_length=1)