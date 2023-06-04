from django.db import models

class Project(models.Model):
    title =models.CharField(max_length=100)
    description=models.TextField(blank=True)
    technology=models.TextField(max_length=20)
    crear_at=models.DateTimeField(auto_now_add=True)
