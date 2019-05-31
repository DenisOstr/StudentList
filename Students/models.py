from django.db import models

class Students(models.Model):
	insuranceNumber = models.CharField(max_length = 255)
	lastName = models.CharField(max_length = 255)
	firstName = models.CharField(max_length = 255)
	yearOfBirth = models.CharField(max_length = 255)
	cityOfBirth = models.CharField(max_length = 255)
	university = models.CharField(max_length = 255)