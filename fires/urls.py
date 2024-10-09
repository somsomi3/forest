from django.urls import path
from .views import forest_fire_view

urlpatterns = [
    path('forest-fire/', forest_fire_view, name='forest_fire_info'),
]
