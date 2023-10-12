from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.urls import reverse

from django.shortcuts import get_object_or_404
from django.views import generic

from .models import Frequency


class IndexView(generic.ListView): # Generic view version
    context_object_name = "all_freq_list" 
    template_name = "freq/index.html" # This is the template that determines how this data looks
    

    def get_queryset(self):
        """Return all frequencies"""
        return Frequency.objects.order_by("name")

class StationView(generic.DetailView): # Generic view version
    model = Frequency   # The model to pull from
    context_object_name = "frequency" 
    template_name = "freq/station.html" # This is the template that determines how this data looks
    

    def get_context_data(self, **kwargs):
        """Return single station"""
        freq = super().get_object()
        context = super().get_context_data(**kwargs)
        context['map_west'] = freq.longitude - .1
        context['map_east'] = freq.longitude + .1
        context['map_north'] = freq.latitude + .1
        context['map_south'] = freq.latitude - .1
        return context