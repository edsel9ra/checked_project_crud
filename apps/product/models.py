from django.db import models
from django.utils.translation import ugettext as _
from apps.users.models import User

class Product(models.Model):
    code = models.IntegerField(verbose_name='Codigo Producto')
    description = models.CharField(max_length=45,verbose_name=_('Descripción'),blank=True,null=True)
    presentation = models.CharField(max_length=45,verbose_name=_('Presentación'),blank=True,null=True)
    corrugated_quantity = models.IntegerField(verbose_name=_('Unidades Corrugadas'))

class CheckList(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name=_('Producto'))
    packing_list = models.CharField(max_length=25,verbose_name=_('Lista Empaque'),blank=True,null=True)
    quantity = models.IntegerField(verbose_name=_('Cantidad Chequeo'))
    receiver = models.ForeignKey(User,on_delete=models.CASCADE,related_name='products_received',verbose_name=_('Quien Recibe'))
    deliver = models.ForeignKey(User,on_delete=models.CASCADE,related_name='products_delivered',verbose_name=_('Quien Entrega'))
    check_date = models.DateField(verbose_name=_('Fecha Chequeo'))
