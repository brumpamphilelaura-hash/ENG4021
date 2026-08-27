from django.db import models


class Product(models.Model):
    name = models.CharField('nome', max_length=120)
    description = models.TextField('descrição')
    price = models.DecimalField('preço', max_digits=10, decimal_places=2)
    is_active = models.BooleanField('produto ativo', default=True)
    created_at = models.DateTimeField('criado em', auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'produto'
        verbose_name_plural = 'produtos'

    def __str__(self):
        return self.name
