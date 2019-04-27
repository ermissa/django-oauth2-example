from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from rest_framework.routers import DefaultRouter

from resource_server.views import ResourceViewSet

router = DefaultRouter()
router.register('resource', ResourceViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Authentication
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('authentication/', include('application.urls')),

    #API
    path('v1/', include(router.urls)),
]