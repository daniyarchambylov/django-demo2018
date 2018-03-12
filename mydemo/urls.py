"""mydemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from demoapp import views as demoapp_views

urlpatterns = [
    path('', demoapp_views.demo_page, name='demo-home'),
    path('cars/<int:id>/', demoapp_views.car_details_view, name='car-details'),
    re_path(r'^cars-reg/(?P<id>\d+)/$', demoapp_views.car_details_view, name='car-details2'),
    path('55/', demoapp_views.demo_page555, name='demo-home5'),
    path('66/', demoapp_views.demo_page666, name='demo-home6'),
    path('88/', demoapp_views.demo_page777, name='demo-home7'),
    path('info/', demoapp_views.second_page, name='demo-paragraphs'),
    path('forms/', demoapp_views.form_view, name='demo-form'),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
