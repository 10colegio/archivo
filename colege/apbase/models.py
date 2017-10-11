from django.db import models

class Nota(models.Model):
	estudiante = models.CharField(max_length=50)
	area= models.CharField(max_length=50)
	asignatura= models.CharField(max_length=50)
	docente= models.CharField(max_length=50)
	periodo= models.CharField(max_length=50)
	año= models.CharField(max_length=50)

class Estudiante(models.Model):
	nombre = models.CharField(max_length=50)
	apellido= models.CharField(max_length=50)
	nacimiento = models.DateField()
	grado = models.CharField(max_length=2)

	

	
	

# Create your models here.
