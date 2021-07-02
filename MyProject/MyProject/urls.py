from django.contrib import admin
from django.urls import path, include
from api_basic import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('api/', include('api_basic.urls', namespace='api')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
