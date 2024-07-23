from django.db import models
from account.models import User

from django.utils.translation import gettext_lazy as _

class Post(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(_('Titulo'), max_length=255, db_index=True)
    body = models.TextField(_('Assunto'))


    class Meta: 
        db_table = "posts"
        verbose_name = _("Postagem")
        verbose_name_plural = _("Postagens")

    def __str__(self):
        return self.title




# class Comment(models.Model):
#     postId = models.ForeignKey(Post, on_delete=models.CASCADE)
#     name = models.CharField(_('Nome'), max_length=200)
#     email = models.EmailField(_('Email'))
#     body = models.TextField(_('Assunto'))


#     class Meta: 
#         db_table = "comments"
#         verbose_name = _("Comentario")
#         verbose_name_plural = _("Comentarios")

#     def __str__(self):
#         return self.title

