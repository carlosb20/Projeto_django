from django.db import models

class Orcamento(models.Model):
    peca = models.CharField(max_length=30)
    preco = models.DecimalField(decimal_places=2,max_digits=10)

    def __str__(self):
        return self.peca
