"""Users views."""

from django.views.generic import FormView, CreateView, TemplateView
from landing.users.forms import LeadForm
from django.urls import reverse_lazy
from django.contrib import messages

class IndexView(CreateView):
    template_name = 'index.html'
    success_url = reverse_lazy('users:index')

# class IndexEsView(IndexView):
#     template_name = 'index-es.html'
#     success_url = reverse_lazy('users:index-es')