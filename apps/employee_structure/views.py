from django.shortcuts import (  # noqa
    redirect, render,
)
from django.views.generic import (  # noqa
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
    DetailView,
)
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
)
from django.urls import (
    reverse_lazy,
)
from django import (
    forms,
)

from .models import (
    Employee,
    Workgroup,
    Department,
)
from .forms import (
    EmployeeFilterForm,
    WorkgroupFilterForm,
    DepartmentFilterForm,
)


class ListEmployees(LoginRequiredMixin, ListView):
    template_name = 'employee_list.html'
    context_object_name = 'employees'

    def get_queryset(self):
        queryset = Employee.objects \
            .prefetch_related('workgroup__department')

        if self.request.GET:

            form = EmployeeFilterForm(self.request.GET)
            if form.is_valid():
                form.cleaned_data = {
                    key: value
                    for key, value
                    in form.cleaned_data.items()
                    if value
                }

                name = form.cleaned_data.pop('name', None)
                if name:
                    queryset = queryset.filter(name__icontains=name)

                workgroup = form.cleaned_data.pop('workgroup', None)
                if workgroup:
                    queryset = queryset.filter(workgroup=workgroup)

                department = form.cleaned_data.pop('department', None)
                if department:
                    queryset = queryset.filter(
                        workgroup__department=department
                    )

        return queryset.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = EmployeeFilterForm(self.request.GET)
        return context


class ListWorkgroups(LoginRequiredMixin, ListView):
    template_name = 'workgroup_list.html'
    context_object_name = 'workgroups'

    def get_queryset(self):
        queryset = Workgroup.objects \
            .prefetch_related('department')

        if self.request.GET:

            form = WorkgroupFilterForm(self.request.GET)
            if form.is_valid():
                form.cleaned_data = {
                    key: value
                    for key, value
                    in form.cleaned_data.items()
                    if value
                }

                name = form.cleaned_data.pop('name', None)
                if name:
                    queryset = queryset.filter(name__icontains=name)

                department = form.cleaned_data.pop('department', None)
                if department:
                    queryset = queryset.filter(department=department)

        return queryset.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = WorkgroupFilterForm(self.request.GET)
        return context


class ListDepartments(LoginRequiredMixin, ListView):
    template_name = 'department_list.html'
    context_object_name = 'departments'

    def get_queryset(self):
        queryset = Department.objects

        if self.request.GET:

            form = DepartmentFilterForm(self.request.GET)
            if form.is_valid():
                form.cleaned_data = {
                    key: value
                    for key, value
                    in form.cleaned_data.items()
                    if value
                }

                name = form.cleaned_data.pop('name', None)
                if name:
                    queryset = queryset.filter(name__icontains=name)

        return queryset.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = DepartmentFilterForm(self.request.GET)
        return context


class GetEmployee(LoginRequiredMixin, DetailView):
    model = Employee
    template_name = 'employee_page.html'
    context_object_name = 'employee'


class GetWorkgroup(LoginRequiredMixin, DetailView):
    model = Workgroup
    template_name = 'workgroup_page.html'
    context_object_name = 'workgroup'


class GetDepartment(LoginRequiredMixin, DetailView):
    model = Department
    template_name = 'department_page.html'
    context_object_name = 'department'


class AddEmployee(LoginRequiredMixin, CreateView):
    model = Employee
    fields = '__all__'
    template_name = 'form_page.html'
    success_url = reverse_lazy('employee_list')

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.fields['hired_date'].widget = forms.DateInput(format=r'%Y-%m-%d')
        return form


class AddWorkgroup(LoginRequiredMixin, CreateView):
    model = Workgroup
    fields = '__all__'
    template_name = 'form_page.html'
    success_url = reverse_lazy('employee_list')


class AddDepartment(LoginRequiredMixin, CreateView):
    model = Department
    fields = '__all__'
    template_name = 'form_page.html'
    success_url = reverse_lazy('employee_list')


class DeleteEmployee(LoginRequiredMixin, DeleteView):
    model = Employee
    template_name = 'submit_delete_page.html'
    success_url = reverse_lazy('employee_list')


class DeleteWorkgroup(LoginRequiredMixin, DeleteView):
    model = Workgroup
    template_name = 'submit_delete_page.html'
    success_url = reverse_lazy('employee_list')


class DeleteDepartment(LoginRequiredMixin, DeleteView):
    model = Department
    template_name = 'submit_delete_page.html'
    success_url = reverse_lazy('employee_list')


class EditEmployee(LoginRequiredMixin, UpdateView):
    model = Employee
    fields = '__all__'
    template_name = 'form_page.html'
    template_name_suffix = 'form'
    success_url = reverse_lazy('employee_list')

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.fields['hired_date'].widget = forms.DateInput(format=r'%Y-%m-%d')
        return form


class EditWorkgroup(LoginRequiredMixin, UpdateView):
    model = Workgroup
    fields = '__all__'
    template_name = 'form_page.html'
    template_name_suffix = 'form'
    success_url = reverse_lazy('employee_list')


class EditDepartment(LoginRequiredMixin, UpdateView):
    model = Department
    fields = '__all__'
    template_name = 'form_page.html'
    template_name_suffix = 'form'
    success_url = reverse_lazy('employee_list')
