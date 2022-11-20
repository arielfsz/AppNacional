from django.db import models



class Futbolista(models.Model):

    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    nacimiento = models.DateField()
    posicion = models.CharField(max_length=20)



class Torneo(models.Model):

    nombre = models.CharField(max_length=20)
    año = models.IntegerField()
    caracter = models.CharField(max_length=20)
    nacionalidad = models.CharField(max_length=20)



class Tecnico(models.Model):

    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    nacimiento = models.DateField()