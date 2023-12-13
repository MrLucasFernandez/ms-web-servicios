from django.db import models

# Create your models here.

class Area(models.Model):
    id_area    = models.BigAutoField(db_column='idArea', primary_key=True)
    descripcion     = models.CharField(max_length=25)
    
    def __str__(self):
        return str(self.descripcion)
class Servicio(models.Model):
    id_servicio     = models.AutoField(primary_key=True)
    id_area         = models.ForeignKey('Area', on_delete=models.CASCADE, db_column='idArea')
    nombre          = models.CharField(max_length=30)
    descripcion     = models.CharField(max_length=200)
    valor           = models.IntegerField()
    def __str__(self):
        return "ID: "+str(self.id_servicio)+" "+str(self.nombre)+" /"+str(self.id_area)