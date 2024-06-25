# Generated by Django 4.2.13 on 2024-06-13 07:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('service', '0003_alter_machine_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalogservicecompany',
            name='client',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='TO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата проведения ТО')),
                ('operating_time', models.IntegerField(verbose_name='Наработка (м/час)')),
                ('order_number', models.CharField(max_length=25, unique=True, verbose_name='Номер заказ-наряда')),
                ('order_date', models.DateField(verbose_name='Дата заказ-наряда')),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.machine', verbose_name='Машина')),
                ('organization', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='service.catalogservicecompany', verbose_name='Организация проводившая ТО')),
                ('type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='service.catalogto', verbose_name='Вид ТО')),
            ],
        ),
    ]
