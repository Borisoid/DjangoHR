from django.contrib import admin
from .models import (
    Department,
    Workgroup,
    Employee,
)

admin.site.register(Department)
admin.site.register(Workgroup)
admin.site.register(Employee)
