from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name = 'main'),
    path('bank', views.bank, name = 'bank'),
    path('internalCode', views.internalCode, name='internalCode'),
]
