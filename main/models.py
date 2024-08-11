from django.db import models
from django.conf import settings


class Resume(models.Model):
    polzovatel = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nazvanie_vakansii = models.CharField(verbose_name="Nazvanie Vakansii", max_length=200)
    imya = models.CharField(verbose_name="Imya", max_length=50)
    familiya = models.CharField(verbose_name="Familiya", max_length=50)
    otchestvo = models.CharField(verbose_name="Otchestvo", max_length=50, blank=True)
    data_rozhdeniya = models.IntegerField(verbose_name="Data Rozhdeniya")
    email = models.EmailField(verbose_name="Email")
    navyki = models.TextField(verbose_name="Navyki")
    opyt = models.TextField(verbose_name="Opyt")
    obrazovanie = models.TextField(verbose_name="Obrazovanie")

    def __str__(self):
        return f'{self.imya} {self.familiya} - {self.nazvanie_vakansii}'


class Vacancy(models.Model):
    rabotodatel = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nazvanie = models.CharField(verbose_name="Nazvanie", max_length=200)
    nazvanie_kompanii = models.CharField(verbose_name="Nazvanie Kompanii", max_length=200)
    zarplata = models.DecimalField(verbose_name="Zarplata", max_digits=10, decimal_places=2)
    trebovanie_navyki = models.TextField(verbose_name="Trebovanie Navyki")
    obyazannosti = models.TextField(verbose_name="Obyazannosti")
    adres = models.CharField(verbose_name="Adres", max_length=300)

    def __str__(self):
        return self.nazvanie
