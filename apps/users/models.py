from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext as _
from django.utils.timezone import now

class User(AbstractUser):
    code = models.IntegerField(verbose_name=_('Codigo Empleado'),default=1234)
    area = models.CharField(max_length=25,verbose_name=_('Area'),blank=True,null=True)
    birth_date = models.DateField(verbose_name=_('Fecha Nacimiento'),default=now)
    is_base = models.BooleanField(verbose_name=_('Es Base'),default=False)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)