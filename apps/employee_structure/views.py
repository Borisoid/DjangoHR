from django.shortcuts import (  # noqa
    render,
)
from django.views.generic import (  # noqa
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
)

from .models import (
    Employee,
)
from .forms import (
    EmployeeFilrerForm,
)


class ListEmployees(ListView):
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
