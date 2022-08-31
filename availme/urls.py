from django.contrib import admin
from django.urls import path, include

import availme_webapp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('availme_webapp.urls')),
]
