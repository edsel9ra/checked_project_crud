# Generated by Django 3.0.2 on 2020-05-17 18:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0002_delete_checklist'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_date', models.DateTimeField(verbose_name='Fecha Chequeo')),
                ('deliver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products_delivered', to=settings.AUTH_USER_MODEL, verbose_name='Quien Entrega')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products_received', to=settings.AUTH_USER_MODEL, verbose_name='Quien Recibe')),
            ],
        ),
        migrations.CreateModel(
            name='CheckedProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('packing_list', models.CharField(blank=True, max_length=25, null=True, verbose_name='Lista Empaque')),
                ('quantity', models.IntegerField(verbose_name='Cantidad Chequeo')),
                ('checklist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checklist.CheckList', verbose_name='Lista Chequeo')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Product', verbose_name='Producto')),
            ],
        ),
    ]