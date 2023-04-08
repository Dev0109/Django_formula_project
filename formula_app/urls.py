from django.urls import path
from . import views

urlpatterns = [
    path('', views.formula, name='formula'),
    path('submit/', views.submit, name="submit"),
]