from django import (
    forms,
)

from .models import (
    Department,
    Workgroup,
    Employee,
)


class EmployeeFilrerForm(forms.Form):
    name = forms.CharField(
        max_length=Employee._meta.get_field('name').max_length,
        required=False,
    )
    department = forms.ModelChoiceField(
        Department.objects.all(),
        required=False,
    )
    workgroup = forms.ModelChoiceField(
        Workgroup.objects.all(),
        required=False,
    )
