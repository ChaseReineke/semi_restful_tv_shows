from django.urls import path     
from . import views

urlpatterns = [
    path('', views.shows),
    path('new', views.new),
    path('new/create', views.create),
    path('edit/<int:id>', views.edit),
    path('edit_show/<int:id>', views.edit_show),
    path('info/<int:id>', views.info),
    path('delete/<int:id>', views.delete),
]