from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django import views
from django.views import generic
from sip.models import Event
from sip.forms import EventForm

# Create your views here.

class EventListViewBase(generic.ListView):
    model = Event
    template_name = 'home.html'


class EventListViewHome(EventListViewBase):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pote_do_banco"] = {'nome': 'Janderson'}
        return context

class EventCreateView(generic.FormView):
    template_name = 'event.html'
    # success_url = '/' # we dont need it cause form_valid_method use get_absolute_url from models to redirect the user
    form_class = EventForm

    def form_valid(self, form):
        event = Event.objects.create(**form.cleaned_data)
        return super().form_valid(form)
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["pote_do_banco"] = {'nome': 'Janderson'}
    #     return context

    
    

