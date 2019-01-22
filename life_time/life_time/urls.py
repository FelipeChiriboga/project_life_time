"""life_time URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from life.views import main, sub_person_1, sub_person_2, sub_relation, sub_times

urlpatterns = [
    path('admin/', admin.site.urls),
    path('first_person/', sub_person_1),
    path('second_person/', sub_person_2),
    path('relation/', sub_relation),
    path('days_hours/', sub_times),

    path('', main),
]
