from django.urls import (
    path,
)
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
)


urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='log_in'),  # noqa
    path('logout/', LogoutView.as_view(), name='log_out'),
]
