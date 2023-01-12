from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView

from joburi.models import Joburi


# Create your views here.
class JoburiView(LoginRequiredMixin, ListView):
    model = Joburi
    template_name = 'joburi/joburi_index.html'

class CreateJoburiView(LoginRequiredMixin, CreateView):
    model = Joburi
    fields = ['type', 'url', 'title', 'description', 'salary', 'currency', 'city']
    template_name = 'joburi/joburi_form.html'

    def get_success_url(self):
        return reverse('joburi:lista_joburi')

class UpdateJoburiView(LoginRequiredMixin, UpdateView):
    model = Joburi
    fields = ['type', 'url', 'title', 'description', 'salary', 'currency', 'city']
    template_name = 'joburi/joburi_form.html'

    def get_success_url(self):
        return reverse('joburi:lista_joburi')

@login_required
def delete_job(request, pk):
    Joburi.objects.filter(id=pk).update(active=0)
    return redirect('joburi:lista_joburi')

@login_required
def activate_job(request, pk):
    Joburi.objects.filter(id=pk).update(active=1)
    return redirect('joburi:lista_joburi')
