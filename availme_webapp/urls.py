from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.index, name='app_home'),
    path('appfetch', view=views.master_api, name='master_api_gateway'),
]
