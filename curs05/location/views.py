from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView

from location.models import location


# Create your views here.
class locationView(LoginRequiredMixin, ListView):
    model = location
    template_name = 'location/location_index.html'

class CreateLocationView(LoginRequiredMixin, CreateView):
    model = location
    fields = ['city', 'country']
    template_name = 'location/location_form.html'

    def get_success_url(self):
        return reverse('location:lista_locatii')

class UpdateLocationView(LoginRequiredMixin, UpdateView):
    model = location
    fields = ['city', 'country']
    template_name = 'location/location_form.html'

    def get_success_url(self):
        return reverse('location:lista_locatii')

@login_required
def delete_location(request, pk):
    location.objects.filter(id=pk).update(active=0)
    return redirect('location:lista_locatii')

@login_required
def activate_location(request, pk):
    location.objects.filter(id=pk).update(active=1)
    return redirect('location:lista_locatii')
