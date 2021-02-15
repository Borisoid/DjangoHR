from django.urls import (
    path,
)
from .views import (
    ListEmployees,
    AddEmployee,
)


urlpatterns = [
    path('view/employee_list', ListEmployees.as_view(), name='employee_list'),
    path('add/employee', AddEmployee.as_view(), name='add_employee'),
]
