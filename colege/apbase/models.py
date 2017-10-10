from django.db import models

class Nota(models.Model):
	estudiante = models.CharField(max_length=50)
	area= models.CharField(max_length=50)
	asignatura= models.CharField(max_length=50)
	docente= models.CharField(max_length=50)
	periodo= models.CharField(max_length=50)
	año= models.CharField(max_length=50)

	
	
	

# Create your models here.
