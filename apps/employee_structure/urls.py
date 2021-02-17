from django.urls import (
    path,
)
from .views import (
    AddDepartment,
    AddEmployee,
    AddWorkgroup,
    DeleteDepartment,
    DeleteEmployee,
    DeleteWorkgroup,
    EditDepartment,
    EditEmployee,
    EditWorkgroup,
    GetDepartment,
    GetEmployee,
    GetWorkgroup, ListDepartments,
    ListEmployees,
    ListWorkgroups,
)


urlpatterns = [
    path('view/employee_list/', ListEmployees.as_view(), name='employee_list'),
    path('view/workgroup_list/', ListWorkgroups.as_view(), name='workgroup_list'),  # noqa
    path('view/department_list/', ListDepartments.as_view(), name='department_list'),  # noqa

    path('view/employee/<pk>/', GetEmployee.as_view(), name='view_employee'),
    path('view/workgroup/<pk>/', GetWorkgroup.as_view(), name='view_workgroup'),  # noqa
    path('view/department/<pk>', GetDepartment.as_view(), name='view_department'),  # noqa

    path('delete/employee/<pk>/', DeleteEmployee.as_view(), name='delete_employee'),  # noqa
    path('delete/workgroup/<pk>', DeleteWorkgroup.as_view(), name='delete_workgroup'),  # noqa
    path('delete/department/<pk>', DeleteDepartment.as_view, name="delete_department"),  # noqa

    path('add/employee/', AddEmployee.as_view(), name='add_employee'),
    path('add/workgroup/', AddWorkgroup.as_view(), name='add_workgroup'),
    path('add/department/', AddDepartment.as_view(), name='add_department'),

    path('edit/employee/<pk>/', EditEmployee.as_view(), name='edit_employee'),
    path('edit/workgroup/<pk>/', EditWorkgroup.as_view(), name='edit_workgroup'),  # noqa
    path('edit/department/<pk>/', EditDepartment.as_view(), name='edit_department'),  # noqa
]
