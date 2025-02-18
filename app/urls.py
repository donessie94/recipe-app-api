"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from drf_spectacular.views import(SpectacularAPIView, SpectacularSwaggerView)
from django.contrib import admin
#include import (a helper function) allow us to include urls from a different app
from django.urls import path, include

#this maps URLs to Views (Views define how request are handled)
urlpatterns = [
    path('admin/', admin.site.urls),                  #we name it api-shema
    path('api/schema/', SpectacularAPIView.as_view(), name='api-schema'), #SpectacularAPIView.as_view() generates the schema file needed for our autodocumentation
    path('api/docs/',                   #it will use the 'api-schema' we defined above
         SpectacularSwaggerView.as_view(url_name='api-schema'), name='api-docs'),
    #here we connect the user app
    path('api/user', include('user.urls')),
]
