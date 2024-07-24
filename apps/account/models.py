from django.db import models
from information.models import Address, Company
from django.utils.translation import gettext_lazy as _

class User(models.Model):
    name = models.CharField(_('Nome'), max_length=100)
    username = models.CharField(_('Username'), max_length=100)
    email = models.EmailField(_('E-mail'))
    phone = models.CharField(_('Telefone'), max_length=45)
    website = models.CharField(_('Website'), max_length=100)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, related_name='user')
    company = models.OneToOneField(Company, on_delete=models.CASCADE, related_name='user')

    class Meta:
        db_table = "users"
        verbose_name = _("Usuário")
        verbose_name_plural = _("Usuários")

    def __str__(self):
        return self.name
