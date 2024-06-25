from django.contrib import admin
from .models import *


class CatalogModelTechAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


class CatalogModelEngineAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


class CatalogModelTransmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


class CatalogModelMainBridgeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


class CatalogModelControlBridgeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


class CatalogTOAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


class CatalogFailureNodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


class CatalogRecoveryMethodAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


class CatalogServiceCompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


class MachineAdmin(admin.ModelAdmin):
    list_display = ('factory_number', 'tech_model', 'service_company', 'client_name')

    @admin.display(description='Покупатель')
    def client_name(self, machine: Machine):
        return machine.client.first_name


class TOAdmin(admin.ModelAdmin):
    list_display = ("type", "date", "machine", "order_number")


class ReclamationsAdmin(admin.ModelAdmin):
    list_display = ("machine", "date", "node", "repair_date")


admin.site.register(CatalogModelTech, CatalogModelTechAdmin)
admin.site.register(CatalogModelEngine, CatalogModelEngineAdmin)
admin.site.register(CatalogModelTransmission, CatalogModelTransmissionAdmin)
admin.site.register(CatalogModelMainBridge, CatalogModelMainBridgeAdmin)
admin.site.register(CatalogModelControlBridge, CatalogModelControlBridgeAdmin)
admin.site.register(CatalogTO, CatalogTOAdmin)
admin.site.register(CatalogFailureNode, CatalogFailureNodeAdmin)
admin.site.register(CatalogRecoveryMethod, CatalogRecoveryMethodAdmin)
admin.site.register(CatalogServiceCompany, CatalogServiceCompanyAdmin)
admin.site.register(Machine, MachineAdmin)
admin.site.register(TO, TOAdmin)
admin.site.register(Reclamations, ReclamationsAdmin)
