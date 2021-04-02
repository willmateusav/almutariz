"""Users views."""

from django.views.generic import FormView, CreateView, TemplateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import render # NEW LINE

# class IndexView(CreateView):
#     template_name = 'index.html'
#     success_url = reverse_lazy('users:index')

def IndexView(request):
   return render(request, 'index.html')

def ImagesView(request):
   return render(request, 'blog-grid.html')