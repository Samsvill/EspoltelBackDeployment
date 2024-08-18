from django.urls import path
from . import views

urlpatterns = [
    path('proyectos/', views.ProyectoListCreateByUserAPIView.as_view(), name='proyecto-list-create'),
    path('proyectos/<int:pk>/', views.ProyectoDetailAPIView.as_view(), name='proyecto-detail'),
    path('proyectos/<int:proyecto_id>/items/', views.BudgetItemCreateAPIView.as_view(), name='crear-budget-items'),
    path('proyectos/all/', views.ProyectoGetAllAPIView.as_view(), name='proyectos-all'),
]