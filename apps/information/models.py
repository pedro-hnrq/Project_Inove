from django.db import models
from django.utils.translation import gettext_lazy as _

class Geo(models.Model):
    lat = models.CharField(_('Latitude'), max_length=50)
    lng = models.CharField(_('Longitude'), max_length=50)

    class Meta:
        db_table = "geo"
        verbose_name = _("Geolocalização")
        verbose_name_plural = _("Geolocalizações")

    def __str__(self):
        return f"{self.lat}, {self.lng}"

class Address(models.Model):
    street = models.CharField(_('Logradouro'), max_length=100)
    suite = models.CharField(_('Complemento'), max_length=100)
    city = models.CharField(_('Cidade'), max_length=100)
    zipcode = models.CharField(_('CEP'), max_length=20)
    geo = models.OneToOneField(Geo, on_delete=models.CASCADE, related_name='address')

    class Meta:
        db_table = "addresses"
        verbose_name = _("Endereço")
        verbose_name_plural = _("Endereços")

    def __str__(self):
        return f"Endereço é CEP {self.zipcode} e cidade {self.city}"

class Company(models.Model):
    name_company = models.CharField(_('Nome'), max_length=100)
    catchPhrase = models.CharField(_('Slogan'), max_length=200)
    bs = models.CharField(_('BS'), max_length=200)

    class Meta:
        db_table = "companies"
        verbose_name = _("Empresa")
        verbose_name_plural = _("Empresas")

    def __str__(self):
        return f"Empresa: {self.name_company}"