from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include

import availme_webapp

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('website.urls')),
    path('', include('availme_webapp.urls')), # FOr now

    path('app/', include('availme_webapp.urls')),
] + staticfiles_urlpatterns()
