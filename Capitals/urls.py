from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url

from core import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('core/', include('core.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    url(r'^signup$', views.signup, name='signup'),
]
