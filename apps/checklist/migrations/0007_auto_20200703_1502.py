# Generated by Django 3.0.3 on 2020-07-03 20:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('checklist', '0006_auto_20200701_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checklist',
            name='check_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha Chequeo'),
        ),
    ]
