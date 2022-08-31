from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.index, name='app_home'),
]
