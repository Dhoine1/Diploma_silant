from django.urls import path
from rest_framework.schemas import get_schema_view

from api.views import *

urlpatterns = [
   # машины
   path('api/v1/machinelist', MachineViewset.as_view()),
   path('api/v1/mymachinelist', MyMachineViewset.as_view()),
   path('api/v1/<int:pk>/machine', MachineAPIView.as_view()),
   # ТО
   path('api/v1/tolist', TOViewset.as_view()),
   path('api/v1/<int:pk>/to', TOAPIView.as_view()),
   # рекламации
   path('api/v1/reclamationslist', ReclamationsViewset.as_view()),
   path('api/v1/<int:pk>/reclamation', ReclamationsAPIView.as_view()),
   # описание API
   path('openapi', get_schema_view(title="Silant", description="API for Silant"), name='openapi-schema'),
]
