from django.db import models
from apps.product.models import Product
from apps.users.models import User
from django.utils.translation import ugettext as _
from django.utils.timezone import now

class CheckList(models.Model):
    receiver = models.ForeignKey(User,on_delete=models.CASCADE,related_name='products_received',verbose_name=_('Quien Recibe'))
    deliver = models.ForeignKey(User,on_delete=models.CASCADE,related_name='products_delivered',verbose_name=_('Quien Entrega'))
    check_date = models.DateTimeField(verbose_name=_('Fecha Chequeo'),default=now)

class CheckedProduct(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name=_('Producto'))
    checklist = models.ForeignKey(CheckList,on_delete=models.CASCADE,verbose_name=_('Lista Chequeo'))
    packing_list = models.CharField(max_length=25,verbose_name=_('Lista de Empaque'),blank=True,null=True)
    quantity = models.IntegerField(verbose_name=_('Corrugadas Chequeadas'))

