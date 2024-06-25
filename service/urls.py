from django.urls import path
from .views import *


urlpatterns = [
    path('', Index.as_view(), name='index'),
    # машины
    path('machine/<int:pk>', MachineDetail.as_view(), name="machine_view"),
    path('mymachines', Mymachines.as_view(), name='mymachines'),
    path('create', MachineCreate.as_view(), name='machine_create'),
    path('machine/<int:pk>/edit', MachineUpdate.as_view(), name='machine_update'),
    path('machine/<int:pk>/delete', MachineDelete.as_view(), name='machine_delete'),
    # TO
    path('myto', Myto.as_view(), name='myto'),
    path('myto/<int:pk>', TODetail.as_view(), name="to_view"),
    path('create_to', TOCreate.as_view(), name='to_create'),
    path('myto/<int:pk>/edit', TOUpdate.as_view(), name='to_update'),
    path('myto/<int:pk>/delete', TODelete.as_view(), name='to_delete'),
    # Рекламации
    path('reclamations', ReclamationsView.as_view(), name='Reclamations'),
    path('reclamations/<int:pk>', ReclamationDetailView.as_view(), name="Reclamation_view"),
    path('create_reclamation', ReclamationCreate.as_view(), name='Reclamations_create'),
    path('reclamations/<int:pk>/edit', ReclamationUpdate.as_view(), name='Reclamation_update'),
    path('reclamations/<int:pk>/delete', ReclamationDelete.as_view(), name='Reclamation_delete'),
]
