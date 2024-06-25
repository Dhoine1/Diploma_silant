from django.shortcuts import redirect

from .models import *

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import Group
from django.urls import reverse_lazy

from .filters import MachineFilter, MymachineFilter, TOFilter, ReclamationsFilter
from .forms import MachineForm, TOForm, ReclamationsForm
from django.contrib.auth.mixins import LoginRequiredMixin


# Стартовая страница со списком всех машин
class Index(ListView):
    model = Machine
    ordering = ['factory_number']
    template_name = 'index.html'
    context_object_name = 'machine'
    paginate_by = 10

    def get_queryset(self):
        if self.request.GET:
            queryset = super().get_queryset()
            self.filterset = MachineFilter(self.request.GET, queryset)
            return self.filterset.qs
        else:
            queryset = Machine.objects.all().order_by('factory_number')
            self.filterset = MachineFilter(self.request.GET, queryset)
            return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


# Информация о конкретной машине
class MachineDetail(DetailView):
    model = Machine
    template_name = 'machine_view.html'
    context_object_name = 'machine_view'


# Экран списка машин клиента
class Mymachines(LoginRequiredMixin, ListView):
    model = Machine
    ordering = ['delivery_data']
    template_name = 'mymachines.html'
    context_object_name = 'machine'
    paginate_by = 10

    def get_queryset(self):
        if self.request.GET:
            manager_group = Group.objects.get(name='managers')
            service_group = Group.objects.get(name='service_organization')
            if manager_group in self.request.user.groups.all() or self.request.user.is_superuser == 1:
                queryset = super().get_queryset().order_by('-delivery_data')
                self.filterset = MymachineFilter(self.request.GET, queryset)
                return self.filterset.qs
            elif service_group in self.request.user.groups.all():
                queryset = super().get_queryset().filter(service_company__client_id=self.request.user.id).order_by('-delivery_data')
                self.filterset = MymachineFilter(self.request.GET, queryset)
                return self.filterset.qs
            else:
                queryset = super().get_queryset().filter(client_id=self.request.user.id).order_by('-delivery_data')
                self.filterset = MymachineFilter(self.request.GET, queryset)
                return self.filterset.qs
            return queryset
        else:
            manager_group = Group.objects.get(name='managers')
            service_group = Group.objects.get(name='service_organization')
            if manager_group in self.request.user.groups.all() or self.request.user.is_superuser == 1:
                queryset = Machine.objects.all().order_by('-delivery_data')
            elif service_group in self.request.user.groups.all():
                queryset = Machine.objects.filter(service_company__client_id=self.request.user.id).order_by('-delivery_data')
            else:
                queryset = Machine.objects.filter(client_id=self.request.user.id).order_by('-delivery_data')
            return queryset

    def get_context_data(self, *args, **kwargs):
        context = super(Mymachines, self).get_context_data(**kwargs)
        context['tech_model'] = CatalogModelTech.objects.all().order_by('name')
        context['engine_model'] = CatalogModelEngine.objects.all().order_by('name')
        context['transmission_model'] = CatalogModelTransmission.objects.all().order_by('name')
        context['control_bridge_model'] = CatalogModelControlBridge.objects.all().order_by('name')
        context['main_bridge_model'] = CatalogModelMainBridge.objects.all().order_by('name')
        return context


# Содание записи о машине
class MachineCreate(LoginRequiredMixin, CreateView):
    form_class = MachineForm
    model = Machine
    template_name = 'machine_edit.html'
    success_url = 'mymachines'


# Редактирование записи о машине
class MachineUpdate(LoginRequiredMixin, UpdateView):
    form_class = MachineForm
    model = Machine
    template_name = 'machine_edit.html'
    success_url = 'mymachines'


# Удаление записи о машине
class MachineDelete(LoginRequiredMixin, DeleteView):
    model = Machine
    template_name = 'machine_delete.html'
    success_url = reverse_lazy('index')


# Список ТО
class Myto(LoginRequiredMixin, ListView):
    model = TO
    ordering = ['-date']
    template_name = 'myto.html'
    context_object_name = 'to'
    paginate_by = 10

    def get_queryset(self):
        if self.request.GET:
            manager_group = Group.objects.get(name='managers')
            service_group = Group.objects.get(name='service_organization')
            if manager_group in self.request.user.groups.all() or self.request.user.is_superuser == 1:
                queryset = super().get_queryset().order_by('-date')
            elif service_group in self.request.user.groups.all():
                queryset = TO.objects.filter(machine__service_company__client_id=self.request.user.id).order_by('-date')
            else:
                queryset = TO.objects.filter(machine__client_id=self.request.user.id).order_by('-date')
            self.filterset = TOFilter(self.request.GET, queryset)
            return self.filterset.qs
        else:
            manager_group = Group.objects.get(name='managers')
            service_group = Group.objects.get(name='service_organization')
            if manager_group in self.request.user.groups.all() or self.request.user.is_superuser == 1:
                queryset = TO.objects.all().order_by('-date')
            elif service_group in self.request.user.groups.all():
                queryset = TO.objects.filter(machine__service_company__client_id=self.request.user.id).order_by('-date')
            else:
                queryset = TO.objects.filter(machine__client_id=self.request.user.id).order_by('-date')
            return queryset

    def get_context_data(self, *args, **kwargs):
        context = super(Myto, self).get_context_data(**kwargs)
        context['type'] = CatalogTO.objects.all().order_by('name')
        manager_group = Group.objects.get(name='managers')
        service_group = Group.objects.get(name='service_organization')
        if manager_group in self.request.user.groups.all() or self.request.user.is_superuser == 1:
            machine_list = Machine.objects.all()
        elif service_group in self.request.user.groups.all():
            machine_list = Machine.objects.filter(service_company__client_id=self.request.user.id)
        else:
            machine_list = Machine.objects.filter(client_id=self.request.user.id)
        context['machine'] = machine_list.values('factory_number').order_by('factory_number')
        context['organization'] = CatalogServiceCompany.objects.all().order_by('name')
        return context


# Просмотр записи о ТО
class TODetail(LoginRequiredMixin, DetailView):
    model = TO
    template_name = 'to_view.html'
    context_object_name = 'to_view'


# Создание ТО
class TOCreate(LoginRequiredMixin, CreateView):
    form_class = TOForm
    model = TO
    template_name = 'to_edit.html'
    success_url = 'myto'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        manager_group = Group.objects.get(name='managers')
        service_group = Group.objects.get(name='service_organization')
        if manager_group in self.request.user.groups.all() or self.request.user.is_superuser == 1:
            context['client_machine'] = Machine.objects.all()
        elif service_group in self.request.user.groups.all():
            context['client_machine'] = Machine.objects.filter(service_company__client_id=self.request.user.id)
        else:
            context['client_machine'] = Machine.objects.filter(client_id=self.request.user.id)
        context['enable_create'] = True
        return context


# Редактирование ТО
class TOUpdate(LoginRequiredMixin, UpdateView):
    form_class = TOForm
    model = TO
    template_name = 'to_edit.html'
    success_url = 'myto'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        manager_group = Group.objects.get(name='managers')
        service_group = Group.objects.get(name='service_organization')
        if manager_group in self.request.user.groups.all() or self.request.user.is_superuser == 1:
            context['client_machine'] = Machine.objects.all()
        elif service_group in self.request.user.groups.all():
            context['client_machine'] = Machine.objects.filter(service_company__client_id=self.request.user.id)
        else:
            context['client_machine'] = Machine.objects.filter(client_id=self.request.user.id)
        return context


# Удаление записи о ТО
class TODelete(LoginRequiredMixin, DeleteView):
    model = TO
    template_name = 'to_delete.html'
    success_url = reverse_lazy('index')


# Список рекламаций
class ReclamationsView(LoginRequiredMixin, ListView):
    model = Reclamations
    ordering = ['-date']
    template_name = 'reclamations.html'
    context_object_name = 'reclamations'
    paginate_by = 10

    def get_queryset(self):
        if self.request.GET:
            manager_group = Group.objects.get(name='managers')
            service_group = Group.objects.get(name='service_organization')
            if manager_group in self.request.user.groups.all() or self.request.user.is_superuser == 1:
                queryset = super().get_queryset().order_by('-date')
            elif service_group in self.request.user.groups.all():
                queryset = Reclamations.objects.filter(service_company_id=self.request.user.id).order_by('-date')
            else:
                queryset = Reclamations.objects.filter(machine__client_id=self.request.user.id).order_by('-date')
            self.filterset = ReclamationsFilter(self.request.GET, queryset)
            return self.filterset.qs
        else:
            manager_group = Group.objects.get(name='managers')
            service_group = Group.objects.get(name='service_organization')
            if manager_group in self.request.user.groups.all() or self.request.user.is_superuser == 1:
                queryset = Reclamations.objects.all().order_by('-date')
            elif service_group in self.request.user.groups.all():
                queryset = Reclamations.objects.filter(service_company_id=self.request.user.id).order_by('-date')
            else:
                queryset = Reclamations.objects.filter(machine__client_id=self.request.user.id).order_by('-date')
            return queryset

    def get_context_data(self, *args, **kwargs):
        context = super(ReclamationsView, self).get_context_data(**kwargs)
        context['node'] = CatalogFailureNode.objects.all().order_by('name')
        context['recovery_method'] = CatalogRecoveryMethod.objects.all().order_by('name')
        context['service_company'] = CatalogServiceCompany.objects.all().order_by('name')
        return context


# Просмотр записи о рекламации
class ReclamationDetailView(LoginRequiredMixin, DetailView):
    model = Reclamations
    template_name = 'reclamation_view.html'
    context_object_name = 'reclamations_view'


# Создание рекламации
class ReclamationCreate(LoginRequiredMixin, CreateView):
    form_class = ReclamationsForm
    model = Reclamations
    template_name = 'reclamations_edit.html'
    success_url = 'reclamations'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        manager_group = Group.objects.get(name='managers')
        service_group = Group.objects.get(name='service_organization')
        if manager_group in self.request.user.groups.all() or self.request.user.is_superuser == 1:
            context['client_machine'] = Machine.objects.all()
        elif service_group in self.request.user.groups.all():
            context['client_machine'] = Machine.objects.filter(service_company__client_id=self.request.user.id)
            context['enable_create'] = True
        return context

    def post(self, request):
        form = ReclamationsForm(request.POST)
        if form.is_valid():
            downtime = int((form.cleaned_data['repair_date'] - form.cleaned_data['date']).days)
            company = self.request.user
            reclam = Reclamations(date=form.cleaned_data['date'],
                                  work_time=form.cleaned_data['work_time'],
                                  node=form.cleaned_data['node'],
                                  description=form.cleaned_data['description'],
                                  recovery_method=form.cleaned_data['recovery_method'],
                                  repair_parts=form.cleaned_data['repair_parts'],
                                  repair_date=form.cleaned_data['repair_date'],
                                  machine=form.cleaned_data['machine'],
                                  downtime=downtime,
                                  service_company=company)
            reclam.save()
        return redirect('Reclamations')


# Редактирование рекламации
class ReclamationUpdate(LoginRequiredMixin, UpdateView):
    form_class = ReclamationsForm
    model = Reclamations
    template_name = 'reclamations_edit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        manager_group = Group.objects.get(name='managers')
        service_group = Group.objects.get(name='service_organization')
        if manager_group in self.request.user.groups.all() or self.request.user.is_superuser == 1:
            context['client_machine'] = Machine.objects.all()
        elif service_group in self.request.user.groups.all():
            context['client_machine'] = Machine.objects.filter(service_company__client_id=self.request.user.id)
        return context

    def post(self, request, pk):
        form = ReclamationsForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['date']:
                to_date = form.cleaned_data['date']
            else:
                to_date = Reclamations.object.get(id=form.cleaned_data['id']).date
            if form.cleaned_data['repair_date']:
                from_date = form.cleaned_data['repair_date']
            else:
                from_date = Reclamations.object.get(id=form.cleaned_data['id']).repair_date
            downtime = int((from_date - to_date).days)
            company = self.request.user
            reclam = Reclamations(pk=pk,
                                  date=form.cleaned_data['date'],
                                  work_time=form.cleaned_data['work_time'],
                                  node=form.cleaned_data['node'],
                                  description=form.cleaned_data['description'],
                                  recovery_method=form.cleaned_data['recovery_method'],
                                  repair_parts=form.cleaned_data['repair_parts'],
                                  repair_date=form.cleaned_data['repair_date'],
                                  machine=form.cleaned_data['machine'],
                                  downtime=downtime,
                                  service_company=company)
            reclam.save()
        return redirect('Reclamations')


# Удаление рекламации
class ReclamationDelete(LoginRequiredMixin, DeleteView):
    model = Reclamations
    template_name = 'reclamation_delete.html'
    success_url = reverse_lazy('index')
