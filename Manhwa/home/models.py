from django.db import models

class Manhwa(models.Model):
    data = models.JSONField()