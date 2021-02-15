from django.urls import (
    path,
)
from .views import (
    ListEmployees,
)


urlpatterns = [
    path('', ListEmployees.as_view())
]
