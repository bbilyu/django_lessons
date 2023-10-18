import datetime
import random
from datetime import date, timedelta
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import logging
from django.views.generic import TemplateView
from django.views.generic import ListView

from .models import Order, Client, Product

logger = logging.getLogger(__name__)

def index(request):
    return render(request,"myapp/index.html")



class DateOrders(TemplateView):
    template_name = 'myapp/orders_from_specific_client.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        client_id = kwargs["client_id"]
        end_date = datetime.datetime.now()
        start_date= end_date - timedelta(days=kwargs["days"])
        orders = Order.objects.filter(client_id=client_id, order_date__gte=start_date).order_by('-id').distinct()
        context["orders"] = orders
        return context