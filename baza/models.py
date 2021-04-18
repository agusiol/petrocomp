from django.db import models
from django.urls import reverse


class Klient(models.Model):
    prefixnip = models.CharField(max_length=2, default='PL')
    nip = models.CharField(max_length=10)
    nazwa = models.CharField(max_length=100)
    pelna_nazwa = models.CharField(max_length=255)
    ulica = models.CharField(max_length=100)
    miejscowosc = models.CharField(max_length=100)
    kod_pocztowy = models.CharField(max_length=6)
    telfon = models.CharField(max_length=15, blank=True)
    email = models.EmailField(blank=True)

    #
    def __str__(self):
        return self.nazwa

    def get_absolute_url(self):
        return reverse('klient_szczegoly', args=[self.id])


class Lokalizacja(models.Model):
    klient = models.ForeignKey(Klient, on_delete=models.CASCADE)
    nazwa = models.CharField(max_length=255)
    ulica = models.CharField(max_length=100)
    miejscowosc = models.CharField(max_length=100)
    kod_pocztowy = models.CharField(max_length=6)
    telfon = models.CharField(max_length=15, blank=True)
    email = models.EmailField(blank=True)
    extra_info = models.TextField(max_length=256, blank=True)

    def __str__(self):
        return self.nazwa

    def get_absolute_url(self):
        return reverse('lokalizacja_szczegoly', args=[self.id])

class Moduly(models.Model):
    nazwa = models.CharField(max_length=100)
    def __str__(self):
        return self.nazwa

class Licencja(models.Model):
    lokalizacja = models.OneToOneField(Lokalizacja, on_delete=models.CASCADE)
    modul = models.ManyToManyField(Moduly)
    nazwa = models.CharField(max_length=255)
    data_utworzenia = models.DateTimeField(auto_now=True)

    WERSJE = [
        (1, 'XL-1'),
        (3, 'XL-3'),
        (5, 'XL-5'),

    ]

    wersja_programu = models.IntegerField(choices=WERSJE)





    def __str__(self):
        return self.nazwa
