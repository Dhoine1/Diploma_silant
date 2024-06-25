from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Справочник Модель техники
class CatalogModelTech(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name="Модель")
    description = models.TextField(null=True, verbose_name="Описание")

    class Meta:
        verbose_name = 'Модель техники'
        verbose_name_plural = 'Модели техники'

    def __str__(self):
        return self.name


# Справочник Модель двигателя
class CatalogModelEngine(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name="Модель")
    description = models.TextField(null=True, verbose_name="Описание")

    class Meta:
        verbose_name = 'Модель двигателя'
        verbose_name_plural = 'Модели двигателей'

    def __str__(self):
        return self.name


# Справочник Модель трансмиссии
class CatalogModelTransmission(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name="Модель")
    description = models.TextField(null=True, verbose_name="Описание")

    class Meta:
        verbose_name = 'Модель трансмиссии'
        verbose_name_plural = 'Модели трансмиссии'

    def __str__(self):
        return self.name


# Справочник Модель ведущего моста
class CatalogModelMainBridge(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name="Модель")
    description = models.TextField(null=True, verbose_name="Описание")

    class Meta:
        verbose_name = 'Модель ведущего моста'
        verbose_name_plural = 'Модели ведущего моста'

    def __str__(self):
        return self.name


# Справочник Модель управляемого моста
class CatalogModelControlBridge(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name="Модель")
    description = models.TextField(null=True, verbose_name="Описание")

    class Meta:
        verbose_name = 'Модель управляемого моста'
        verbose_name_plural = 'Модели управляемого моста'

    def __str__(self):
        return self.name


# Справочник Вид ТО
class CatalogTO(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name="Вид ТО")
    description = models.TextField(null=True, verbose_name="Описание")

    class Meta:
        verbose_name = 'Вид ТО'
        verbose_name_plural = 'Виды ТО'

    def __str__(self):
        return self.name


# Справочник Узел отказа
class CatalogFailureNode(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name="Узел")
    description = models.TextField(null=True, verbose_name="Описание")

    class Meta:
        verbose_name = 'Узел отказа'
        verbose_name_plural = 'Узлы отказа'

    def __str__(self):
        return self.name


# Справочник Способ восстановления
class CatalogRecoveryMethod(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name="Способ")
    description = models.TextField(null=True, verbose_name="Описание")

    class Meta:
        verbose_name = 'Способ восстановления'
        verbose_name_plural = 'Способы восстановления'

    def __str__(self):
        return self.name


# Сервисная компания
class CatalogServiceCompany(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name="Способ")
    description = models.TextField(null=True, verbose_name="Описание")
    client = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Сервисная компания'
        verbose_name_plural = 'Сервисные компании'

    def __str__(self):
        return self.name


# Машина
class Machine(models.Model):
    factory_number = models.CharField(max_length=20, unique=True, verbose_name='Зав. № машины')
    tech_model = models.ForeignKey(CatalogModelTech, null=True, on_delete=models.SET_NULL,
                                   verbose_name='Модель техники')
    engine_model = models.ForeignKey(CatalogModelEngine, null=True, on_delete=models.SET_NULL,
                                     verbose_name='Модель двигателя')
    factory_engine = models.CharField(max_length=20, unique=True, verbose_name='Зав. № двигателя')

    transmission_model = models.ForeignKey(CatalogModelTransmission, null=True, on_delete=models.SET_NULL,
                                           verbose_name='Модель трансмиссии')
    factory_transmission = models.CharField(max_length=20, unique=True, verbose_name='Зав. № трансмиссии')
    main_bridge_model = models.ForeignKey(CatalogModelMainBridge, null=True, on_delete=models.SET_NULL,
                                          verbose_name='Модель ведущего моста')
    factory_main_bridge = models.CharField(max_length=20, unique=True, verbose_name='Зав. № ведущего моста')
    control_bridge_model = models.ForeignKey(CatalogModelControlBridge, null=True, on_delete=models.SET_NULL,
                                             verbose_name='Модель управляемого моста')
    factory_control_bridge = models.CharField(max_length=20, unique=True, verbose_name='Зав. № управляемого моста')
    contract = models.TextField(verbose_name='Договор поставки')
    delivery_data = models.DateField(verbose_name='Дата отгрузки')
    consignee = models.TextField(verbose_name='Грузополучатель')
    address = models.TextField(verbose_name='Адрес поставки')
    equipment = models.TextField(null=True, verbose_name='Комплектация')
    client = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Клиент')
    service_company = models.ForeignKey(CatalogServiceCompany, null=True, on_delete=models.SET_NULL,
                                        verbose_name='Сервисная компания')

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'

    def __str__(self):
        return f'{self.factory_number} Модель: {self.tech_model}.'

    def get_absolute_url(self):
        return reverse('index')


# TO
class TO(models.Model):
    type = models.ForeignKey(CatalogTO, on_delete=models.SET_NULL, null=True, verbose_name="Вид ТО")
    date = models.DateField(verbose_name="Дата проведения ТО")
    operating_time = models.IntegerField(verbose_name="Наработка (м/час)")
    order_number = models.CharField(max_length=25, unique=True, verbose_name="Номер заказ-наряда")
    order_date = models.DateField(verbose_name="Дата заказ-наряда")
    organization = models.ForeignKey(CatalogServiceCompany, null=True, on_delete=models.SET_NULL,
                                     verbose_name="Организация проводившая ТО")
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, verbose_name="Машина")

    class Meta:
        verbose_name = 'TO'
        verbose_name_plural = 'TO'

    def get_absolute_url(self):
        return reverse('index')


# Рекламации
class Reclamations(models.Model):
    date = models.DateField(verbose_name="Дата отказа")
    work_time = models.IntegerField(verbose_name="Наработка (м/час)")
    node = models.ForeignKey(CatalogFailureNode, on_delete=models.CASCADE, verbose_name="Узел отказа")
    description = models.TextField(verbose_name="Описание отказа")
    recovery_method = models.ForeignKey(CatalogRecoveryMethod, on_delete=models.CASCADE,
                                        verbose_name="метод восстановления")
    repair_parts = models.TextField(blank=True, verbose_name="Используемые запчасти")
    repair_date = models.DateField(verbose_name="Дата восстановления")
    downtime = models.IntegerField(null=True, verbose_name="Время простоя техники")
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, verbose_name="Машина")
    service_company = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Сервисная компания')

    class Meta:
        verbose_name = 'Рекламация'
        verbose_name_plural = 'Рекламации'

    def get_absolute_url(self):
        return reverse('index')

    def __str__(self):
        return f'{self.machine} Дата отказа: {self.date}. Дата восстановления: {self.repair_date}'
