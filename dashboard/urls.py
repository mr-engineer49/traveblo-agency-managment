from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = 'dashboard'


urlpatterns = [
    path("dashboards/", views.dashboard, name="dashboard"),
    path("insights/", views.insights, name="insights"),
    path("inbox/", views.inbox, name="inbox"),
]
#path("<int:pk>/delete/", views.delete, name="delete"),
#path("<int:pk>/edit/", views.edit, name="edit"),
