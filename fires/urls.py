from django.urls import path,  include
from . import views

from .views import forest_fire_view

urlpatterns = [
    # path('', views.index, name='index'),
    path('accounts/', include('accounts.urls')),

    path('forest-fire/', forest_fire_view, name='forest_fire_info'),
]
