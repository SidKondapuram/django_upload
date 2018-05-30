from django.urls import path
from . import views
from django.conf.urls import include



urlpatterns = [
    path('', views.model_form_upload, name='form-upload'),
    path('index/', views.index, name='index'),
]
