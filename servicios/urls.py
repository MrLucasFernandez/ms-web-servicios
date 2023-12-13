from django.urls import path
from . import views

urlpatterns = [
    #path('',views.inicio, name=''),
    path('',views.ListarServicios, name='servicios'),
    path('areas/',views.ListarAreas, name='areas'),
    path('detalle/<str:pk>',views.FiltrarServicio, name='detalle'),
    path('crear', views.CrearServicio, name="crear"),
    path('actualizar/<str:pk>/', views.ActualizarServicio, name="actualizar"),
    path('eliminar/<str:pk>/', views.EliminarServicio, name="eliminar"),
    ]