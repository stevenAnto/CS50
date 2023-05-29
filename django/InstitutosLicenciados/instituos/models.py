from django.db import models

class InstitutosConLicencia(models.Model):
    region = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    personJuridica = models.CharField(max_length=100)
    sedeLocal = models.CharField(max_length=50)
    direccion = models.CharField(max_length=150)
    programasLicenciados = models.CharField(max_length=100)
    nivel = models.CharField(max_length=50)
    modalidad = models.CharField(max_length=20)

# Create your models here.
