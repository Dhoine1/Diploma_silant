from rest_framework import serializers

from service.models import *


# Модели справочников и юзер
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name')


class TechModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatalogModelTech
        fields = ('id', 'name', 'description')


class EngineModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatalogModelEngine
        fields = ('id', 'name', 'description')


class TransmissionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatalogModelTransmission
        fields = ('id', 'name', 'description')


class MainBridgeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatalogModelMainBridge
        fields = ('id', 'name', 'description')


class ControlBridgeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatalogModelControlBridge
        fields = ('id', 'name', 'description')


class CatalogTOModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatalogTO
        fields = ('id', 'name', 'description')


class FailureNodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatalogFailureNode
        fields = ('id', 'name', 'description')


class RecoveryMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatalogRecoveryMethod
        fields = ('id', 'name', 'description')


class ServiceCompanyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatalogServiceCompany
        fields = ('id', 'name', 'description')


# список машин для неавторизированных пользователей
class MachineSerializer(serializers.ModelSerializer):
    tech_model = TechModelSerializer(read_only=True)
    engine_model = EngineModelSerializer(read_only=True)
    transmission_model = TransmissionModelSerializer(read_only=True)
    main_bridge_model = MainBridgeModelSerializer(read_only=True)
    control_bridge_model = ControlBridgeModelSerializer(read_only=True)

    class Meta:
        model = Machine
        fields = ['id', 'factory_number', 'tech_model', 'engine_model', 'factory_engine', 'transmission_model',
                  'factory_transmission', 'main_bridge_model', 'factory_main_bridge', 'control_bridge_model',
                  'factory_control_bridge', ]


# список машин для владельцев и менеджеров
class MachineViewSerializer(serializers.ModelSerializer):
    tech_model = TechModelSerializer(read_only=True)
    engine_model = EngineModelSerializer(read_only=True)
    transmission_model = TransmissionModelSerializer(read_only=True)
    main_bridge_model = MainBridgeModelSerializer(read_only=True)
    control_bridge_model = ControlBridgeModelSerializer(read_only=True)
    client = ClientSerializer(read_only=True)
    service_company = ServiceCompanyModelSerializer(read_only=True)

    class Meta:
        model = Machine
        fields = ['id', 'factory_number', 'tech_model', 'engine_model', 'factory_engine', 'transmission_model',
                  'factory_transmission', 'main_bridge_model', 'factory_main_bridge', 'control_bridge_model',
                  'factory_control_bridge', 'contract', 'delivery_data', 'consignee', 'address', 'equipment',
                  'client', 'service_company']


# Список ТО
class TOSerializer(serializers.ModelSerializer):
    type = CatalogTOModelSerializer(read_only=True)
    organization = ServiceCompanyModelSerializer(read_only=True)

    class Meta:
        model = TO
        fields = ('id', 'type', 'date', 'order_number', 'order_date', 'organization')


# Конекретное ТО
class TOViewSerializer(serializers.ModelSerializer):
    type = CatalogTOModelSerializer(read_only=True)
    organization = ServiceCompanyModelSerializer(read_only=True)

    class Meta:
        model = TO
        fields = ('id', 'type', 'date', 'operating_time', 'order_number', 'order_date', 'organization', 'machine', )


# Список рекламаций
class ReclamationsSerializer(serializers.ModelSerializer):
    node = FailureNodeSerializer(read_only=True)
    service_company = ClientSerializer(read_only=True)

    class Meta:
        model = Reclamations
        fields = ('id', 'machine', 'date', 'node', 'repair_date', 'service_company')


# Конкретная рекламация
class ReclamationsViewSerializer(serializers.ModelSerializer):
    node = FailureNodeSerializer(read_only=True)
    service_company = ClientSerializer(read_only=True)
    recovery_method = RecoveryMethodSerializer(read_only=True)

    class Meta:
        model = Reclamations
        fields = ('id', 'machine', 'date', 'work_time', 'node', 'description', 'recovery_method',
                  'repair_parts', 'repair_date', 'downtime', 'service_company', )
