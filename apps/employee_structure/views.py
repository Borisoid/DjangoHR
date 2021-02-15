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


class ListEmployees(ListView):
    template_name = 'employee_list.html'
    queryset = Employee.objects \
        .prefetch_related('workgroup', 'workgroup__department') \
        .all()
    context_object_name = 'employees'
