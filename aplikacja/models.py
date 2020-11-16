from django.db import models

# Create your models here.
class Asortyment(models.Model):
    MAGAZYN = (
        ('Magazyn A','Magazyn A'),
        ('Magazyn B','Magazyn B'),
        ('Magazyn C','Magazyn C')
    )
    OS = (
        ('Strujaca','Sterujaca'),
        ('Naped', 'Naped'),
        ('Naczepa', 'Naczepa')

    )
    
    marka =models.CharField(max_length=30, default='anything')
    bieznik =models.CharField(max_length=30, default='anything')
    szerokosc =models.CharField(max_length=10, default='anything')
    profil = models.CharField(max_length=10, default='anything')
    srednica = models.CharField(max_length=10, default='anything')
    os =models.CharField(max_length=15, default='anything', choices=OS)
    glebokosc_bieznika = models.CharField(max_length=10, default='anything')
    nosnosc = models.CharField(max_length=10, default='anything')
    predkosc = models.CharField(max_length=10, default='anything')
    DOT = models.CharField(max_length=10, default='anything')
    magazyn = models.CharField(max_length=10, default='anything', choices=MAGAZYN)
    nap_na_zimno = models.CharField(max_length=10, default='anything')
    nap_na_goraco = models.CharField(max_length=10, default='anything')
    cena = models.CharField(max_length=10, default='anything')
    
    
    def __str__(self):
        return self.marka


      