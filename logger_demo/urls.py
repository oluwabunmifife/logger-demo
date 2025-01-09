from django.contrib import admin
from django.urls import path, include
from demo.views import sample_view, metrics_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sample/', sample_view),
    path('', include('django_prometheus.urls')),
    path('metrics/', metrics_view, name='metrics'),
]