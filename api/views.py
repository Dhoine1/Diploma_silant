from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import Group
from api.serializers import MachineSerializer, MachineViewSerializer, TOSerializer, ReclamationsSerializer, \
    TOViewSerializer, ReclamationsViewSerializer
from service.models import Machine, TO, Reclamations


# Пагинация
class ListPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


# Общедоступная информация по машинам
class MachineViewset(generics.ListAPIView):
    queryset = Machine.objects.get_queryset().order_by('id')
    serializer_class = MachineSerializer
    pagination_class = ListPagination


# Список машин клиента/сервисной компании
class MyMachineViewset(generics.ListAPIView):
    serializer_class = MachineSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = ListPagination

    def get_queryset(self):
        manager_group = Group.objects.get(name='managers')
        service_group = Group.objects.get(name='service_organization')
        if manager_group in self.request.user.groups.all() or self.request.user.is_superuser == 1:
            queryset = Machine.objects.get_queryset().order_by('id')
        elif service_group in self.request.user.groups.all():
            queryset = Machine.objects.filter(service_company__client_id=self.request.user.id).order_by('id')
        else:
            queryset = Machine.objects.filter(client_id=self.request.user.id).order_by('id')
        return queryset


# Полная информация по конкретной машине
class MachineAPIView(APIView):
    def get(self, request, pk):
        manager_group = Group.objects.get(name='managers')
        queryset = Machine.objects.filter(id__exact=pk)
        currentmachine = Machine.objects.get(id=pk)
        if manager_group in self.request.user.groups.all() or self.request.user.is_superuser == 1 \
                or self.request.user.id == currentmachine.client.id \
                or self.request.user.id == currentmachine.service_company.client.id:
            return Response({'machine': MachineViewSerializer(queryset, many=True).data})
        else:
            return Response({'machine': MachineSerializer(queryset, many=True).data})


# Список ТО
class TOViewset(generics.ListAPIView):
    serializer_class = TOSerializer
    permission_classes = (IsAuthenticated, )
    pagination_class = ListPagination

    def get_queryset(self):
        manager_group = Group.objects.get(name='managers')
        service_group = Group.objects.get(name='service_organization')
        if manager_group in self.request.user.groups.all() or self.request.user.is_superuser == 1:
            queryset = TO.objects.get_queryset().order_by('id')
        elif service_group in self.request.user.groups.all():
            queryset = TO.objects.filter(machine__service_company__client_id=self.request.user.id).order_by('id')
        else:
            queryset = TO.objects.filter(machine__client_id=self.request.user.id).order_by('id')
        return queryset


# Кoнкретное ТО
class TOAPIView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, pk):
        manager_group = Group.objects.get(name='managers')
        currentto = TO.objects.get(id=pk)
        if manager_group in self.request.user.groups.all() or self.request.user.is_superuser == 1 \
                or (currentto.organization.client and self.request.user.id == currentto.organization.client.id) \
                or self.request.user.id == currentto.machine.client.id:
            queryset = TO.objects.filter(id__exact=pk)
        else:
            queryset = TO.objects.none()
        return Response({'to': TOViewSerializer(queryset, many=True).data})


# Список рекламаций
class ReclamationsViewset(generics.ListAPIView):
    serializer_class = ReclamationsSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = ListPagination

    def get_queryset(self):
        manager_group = Group.objects.get(name='managers')
        service_group = Group.objects.get(name='service_organization')
        if manager_group in self.request.user.groups.all() or self.request.user.is_superuser == 1:
            queryset = Reclamations.objects.get_queryset().order_by('id')
        elif service_group in self.request.user.groups.all():
            queryset = Reclamations.objects.filter(service_company_id=self.request.user.id).order_by('id')
        else:
            queryset = Reclamations.objects.filter(machine__client_id=self.request.user.id).order_by('id')
        return queryset


# Конкретная рекламация
class ReclamationsAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        manager_group = Group.objects.get(name='managers')
        currentreclamation = Reclamations.objects.get(id=pk)
        if manager_group in self.request.user.groups.all() or self.request.user.is_superuser == 1 \
                or self.request.user.id == currentreclamation.service_company.id \
                or self.request.user.id == currentreclamation.machine.client.id:
            queryset = Reclamations.objects.filter(id__exact=pk)
        else:
            queryset = Reclamations.objects.none()
        return Response({'reclamations': ReclamationsViewSerializer(queryset, many=True).data})
