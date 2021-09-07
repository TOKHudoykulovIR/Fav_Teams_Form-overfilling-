from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator

class FormInfo(models.Model):

	GENDER = [
		('', ''),
		('Erkak', 'Erkak'),
		('Ayol', 'Ayol')
	]

	REGIONS = [
		('', ''),
		('Andijon', 'Andijon viloyati'),
		('Buxoro', 'Buxoro viloyati'),
		('Jizzax', 'Jizzax viloyati'),
		('Qashqadaryo', 'Qashqadaryo viloyati'),
		('Navoiy', 'Navoiy viloyati'),
		('Namangan', 'Namangan viloyati'),
		('Samarqand', 'Samarqand viloyati'),
		('Surxondaryo', 'Surxondaryo viloyati'),
		('Sirdaryo', 'Sirdaryo viloyati'),
		('Toshkent vil', 'Toshkent viloyati'),
		('Toshkent sh', 'Toshkent shahri'),
		('Fargʻona', 'Fargʻona viloyati'),
		('Xorazm', 'Xorazm viloyati'),
		('Qoraqalpogʻiston', 'Qoraqalpogʻiston Respublikasi')
	]

	TEAMS = [
		('', ''),
		('ARS', 'Arsenal'),
		('CHE', 'Chelsea'),
		('LIV', 'Liverpool'),
		('MU', 'Manchester United'),
		('MCI', 'Manchester City'),   
		('TOT', 'Tottenham'), 
		('BAY', 'Bayern Munich'),
		('BVB', 'Borussia Dortmund'),
		('ATM', 'Atletico Madrid'),
		('BAR', 'Barcelona'),
		('RM', 'Real Madrid'),
		('JUV', 'Juventus'),
		('INT', 'Inter'),
		('ROMA', 'Roma'),
		('NAP', 'Napoli'),
		('ACM', 'Milan'),
		('PSG', 'Paris Saint-Germain'),
		('OL', 'Olympique Lyonnais'),
		('LIL', 'Lille')
	]


	name 			   = models.CharField('Ism', max_length = 50, blank = True)
	surname 		   = models.CharField('Familiya', max_length = 50, blank = True)
	gender 		       = models.CharField('Jins*', max_length = 10, choices = GENDER)
	age 			   = models.PositiveIntegerField('Yosh*', validators = [MinValueValidator(5), MaxValueValidator(90)])
	place_of_birth 	   = models.CharField("Tug'ilgan Joyi*", max_length = 50, choices = REGIONS)
	place_of_residence = models.CharField("Yashash Joyi*", max_length = 50, choices = REGIONS)
	favorite_team	   = models.CharField('Jamoa*', max_length = 50, choices = TEAMS)


	def get_absolute_url(self):
		return reverse('create_form')

