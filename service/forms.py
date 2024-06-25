from django import forms
from .models import Machine, TO, Reclamations
from django.forms import DateInput


# Форма для редактирования/создания машины
class MachineForm(forms.ModelForm):
    class Meta:
        model = Machine
        fields = [
            'factory_number',
            'tech_model',
            'engine_model',
            'factory_engine',
            'transmission_model',
            'factory_transmission',
            'main_bridge_model',
            'factory_main_bridge',
            'control_bridge_model',
            'factory_control_bridge',
            'contract',
            'delivery_data',
            'consignee',
            'address',
            'equipment',
            'client',
            'service_company',
        ]

        widgets = {
            'delivery_data': DateInput(format='%Y-%m-%d', attrs={'type': 'date'}, ),
            'contract': forms.Textarea(attrs={'rows': 2, 'cols': 22}),
            'consignee': forms.Textarea(attrs={'rows': 2, 'cols': 22}),
            'address': forms.Textarea(attrs={'rows': 4, 'cols': 22}),
            'equipment': forms.Textarea(attrs={'rows': 4, 'cols': 22}),
            'service_company': forms.Select(attrs={'width': 177}),
            }


# Форма для редактирования/создания ТО
class TOForm(forms.ModelForm):

    class Meta:
        model = TO
        fields = [
            'type',
            'date',
            'operating_time',
            'order_number',
            'order_date',
            'organization',
            'machine',
        ]

        widgets = {
            'date': DateInput(format='%Y-%m-%d', attrs={'type': 'date'}, ),
            'order_date': DateInput(format='%Y-%m-%d', attrs={'type': 'date'}, ),
        }


# Форма для редактирования/создания рекламации
class ReclamationsForm(forms.ModelForm):
    class Meta:
        model = Reclamations
        fields = [
            'work_time',
            'date',
            'node',
            'description',
            'recovery_method',
            'repair_parts',
            'repair_date',
            'machine',
        ]

        widgets = {
            'date': DateInput(format='%Y-%m-%d', attrs={'type': 'date'}, ),
            'repair_date': DateInput(format='%Y-%m-%d', attrs={'type': 'date'}, ),
            'description': forms.Textarea(attrs={'rows': 3, 'cols': 22}),
            'repair_parts': forms.Textarea(attrs={'rows': 3, 'cols': 22}),
        }
