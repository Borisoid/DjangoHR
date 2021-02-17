from django import (
    forms,
)

from .models import (
    Department,
    Workgroup,
    Employee,
)


class EmployeeFilterForm(forms.Form):
    name = forms.CharField(
        max_length=Employee._meta.get_field('name').max_length,
        required=False,
    )
    workgroup = forms.ModelChoiceField(
        Workgroup.objects.all(),
        required=False,
    )
    department = forms.ModelChoiceField(
        Department.objects.all(),
        required=False,
    )


class WorkgroupFilterForm(forms.Form):
    name = forms.CharField(
        max_length=Workgroup._meta.get_field('name').max_length,
        required=False,
    )
    department = forms.ModelChoiceField(
        Department.objects.all(),
        required=False,
    )


class DepartmentFilterForm(forms.Form):
    name = forms.CharField(
        max_length=Department._meta.get_field('name').max_length,
        required=False,
    )
