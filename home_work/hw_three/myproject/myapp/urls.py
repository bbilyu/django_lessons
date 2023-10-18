from django.urls import path

from .views import DateOrders
from myapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('orders_products/<int:client_id>/<int:days>', DateOrders.as_view(), name='month_post'),
]