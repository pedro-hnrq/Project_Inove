from django.db import models
from django.utils.translation import gettext_lazy as _

class User(models.Model):
    name = models.CharField(_('Nome'), max_length=100)
    username = models.CharField(_('Username'), max_length=100)
    email = models.EmailField(_('E-mail'))

    class Meta:
        db_table = "users"
        verbose_name = _("Usuário")
        verbose_name_plural = _("Usuários")

    def __str__(self):
        return self.name
