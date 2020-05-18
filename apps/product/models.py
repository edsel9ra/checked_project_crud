from django.db import models
from django.utils.translation import ugettext as _

class Product(models.Model):
    code = models.IntegerField(verbose_name='Codigo Producto')
    description = models.CharField(max_length=45,verbose_name=_('Descripción'),blank=True,null=True)
    presentation = models.CharField(max_length=45,verbose_name=_('Presentación'),blank=True,null=True)
    corrugated_quantity = models.IntegerField(verbose_name=_('Unidades Corrugadas'))