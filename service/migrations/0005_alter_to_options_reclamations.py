# Generated by Django 4.2.13 on 2024-06-17 11:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('service', '0004_catalogservicecompany_client_to'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='to',
            options={'verbose_name': 'TO', 'verbose_name_plural': 'TO'},
        ),
        migrations.CreateModel(
            name='Reclamations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата отказа')),
                ('work_time', models.IntegerField(verbose_name='Наработка (м/час)')),
                ('description', models.TextField(verbose_name='Описание отказа')),
                ('repair_parts', models.TextField(verbose_name='Используемые запчасти')),
                ('repair_date', models.DateField(verbose_name='Дата восстановления')),
                ('downtime', models.IntegerField(null=True, verbose_name='Время простоя техники')),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.machine', verbose_name='Машина')),
                ('node', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.catalogfailurenode', verbose_name='Узел отказа')),
                ('recovery_method', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.catalogrecoverymethod', verbose_name='метод восстановления')),
                ('service_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Сервисная компания')),
            ],
            options={
                'verbose_name': 'Рекламация',
                'verbose_name_plural': 'Рекламации',
            },
        ),
    ]