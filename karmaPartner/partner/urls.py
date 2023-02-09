from django.urls import path

from .views import *


urlpatterns = [


    path('', home),
    path('cat/<int:catid>', categories),

]