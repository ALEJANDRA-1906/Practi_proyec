from django.shortcuts import render
from django.views.generic import ListView

from core.models import Persona
# Create your views here.


class PersonView(ListView):
    model = Persona
    template_name = "persona.html"