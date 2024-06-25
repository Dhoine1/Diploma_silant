# Generated by Django 4.2.13 on 2024-06-07 10:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('service', '0002_alter_catalogmodelcontrolbridge_options_machine'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Клиент'),
        ),
    ]
