# car_inventory_app/urls.py

from django.urls import path
from .views import index, add_car, get_cars

from django.conf import settings
from django.conf.urls.static import static

#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


urlpatterns = [
    path('', index, name='index'),
    path('api/add_car/', add_car, name='add_car'),
    path('api/get_cars/', get_cars, name='get_cars'),
]
