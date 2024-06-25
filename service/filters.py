import django_filters
from django_filters import FilterSet


# Фильтр поиска по номеру машины
class MachineFilter(FilterSet):
    factory_number = django_filters.CharFilter(
        field_name='factory_number',
        label="Заводской номер машины",
        lookup_expr='exact',
    )


# Фильтр на странице "мои машины"
class MymachineFilter(FilterSet):
    tech_model = django_filters.CharFilter(
        field_name='tech_model__name',
        label="Модель техники",
        lookup_expr='exact',
    )

    engine_model = django_filters.CharFilter(
        field_name='engine_model__name',
        label="Заводской номер машины",
        lookup_expr='exact',
    )

    transmission_model = django_filters.CharFilter(
        field_name='transmission_model__name',
        label="Mодель трансмиссии",
        lookup_expr='exact',
    )

    control_bridge_model = django_filters.CharFilter(
        field_name='control_bridge_model__name',
        label='модель управляемого моста',
        lookup_expr='exact'
    )

    main_bridge_model = django_filters.CharFilter(
        field_name='main_bridge_model__name',
        label='модель ведущего моста',
        lookup_expr='exact',
    )


# Фильтр на странице ТО
class TOFilter(FilterSet):
    type = django_filters.CharFilter(
        field_name='type__name',
        label="Вид ТО",
        lookup_expr='exact',
    )

    machine = django_filters.CharFilter(
        field_name='machine__factory_number',
        label="Заводской номер машины",
        lookup_expr='exact',
    )

    organization = django_filters.CharFilter(
        field_name='organization__name',
        label="сервисная компания",
        lookup_expr='exact',
    )


# Фильтр на странице Рекламации
class ReclamationsFilter(FilterSet):
    node = django_filters.CharFilter(
        field_name='node__name',
        label='Узел отказа',
        lookup_expr='exact',
    )

    recovery_method = django_filters.CharFilter(
        field_name='recovery_method__name',
        label='Mетод восстановления',
        lookup_expr='exact',
    )

    service_company = django_filters.CharFilter(
        field_name='service_company__first_name',
        label='Сервисная компания',
        lookup_expr='exact',
    )
