from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/update/', views.update_case_status, name='update_case_status'),
]