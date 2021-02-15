from django.shortcuts import (  # noqa
    render,
)
from django.views.generic import (  # noqa
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.decorators import (
    login_required,
)
from django.urls import (
    reverse_lazy,
)

from .models import (
    Employee,
    Workgroup,
    Department,
)
from .forms import (
    EmployeeFilrerForm,
)


class LoginRequiredMixin:
    @classmethod
    def as_view(cls):
        return login_required(super(LoginRequiredMixin, cls).as_view())


class ListEmployees(LoginRequiredMixin, ListView):
    template_name = 'employee_list.html'
    context_object_name = 'employees'

    def get_queryset(self):
        queryset = Employee.objects \
            .prefetch_related('workgroup', 'workgroup__department')

        if self.request.GET:

            form = EmployeeFilrerForm(self.request.GET)
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
        context['filter_form'] = EmployeeFilrerForm(self.request.GET)
        return context


class GetEmployee(LoginRequiredMixin, ListView):
    model = Employee
    template_name = 'employee_page.html'
    context_object_name = 'employee'

    def get_queryset(self):
        return Employee.objects \
            .prefetch_related('workgroup', 'workgroup__department') \
            .get(pk=self.kwargs.get('pk'))


class DeleteEmployee(LoginRequiredMixin, DeleteView):
    model = Employee
    template_name = 'submit_delete_page.html'
    success_url = reverse_lazy('employee_list')


class AddEmployee(LoginRequiredMixin, CreateView):
    model = Employee
    fields = '__all__'
    template_name = 'form_page.html'
    success_url = reverse_lazy('employee_list')


class AddWorkgroup(LoginRequiredMixin, CreateView):
    model = Workgroup
    fields = '__all__'
    template_name = 'form_page.html'
    success_url = reverse_lazy('employee_list')


class GetWorkgroup(LoginRequiredMixin, ListView):
    model = Workgroup
    template_name = 'workgroup_page.html'
    context_object_name = 'workgroup'

    def get_queryset(self):
        return Workgroup.objects \
            .prefetch_related('department') \
            .get(pk=self.kwargs.get('pk'))


class DeleteWorkgroup(LoginRequiredMixin, DeleteView):
    model = Workgroup
    template_name = 'submit_delete_page.html'
    success_url = reverse_lazy('employee_list')


class AddDepartment(LoginRequiredMixin, CreateView):
    model = Department
    fields = '__all__'
    template_name = 'form_page.html'
    success_url = reverse_lazy('employee_list')


class GetDepartment(LoginRequiredMixin, ListView):
    model = Department
    template_name = 'department_page.html'
    context_object_name = 'department'

    def get_queryset(self):
        return Department.objects \
            .get(pk=self.kwargs.get('pk'))


class DeleteDepartment(LoginRequiredMixin, DeleteView):
    model = Department
    template_name = 'submit_delete_page.html'
    success_url = reverse_lazy('employee_list')
