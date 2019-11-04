from django.shortcuts import render, redirect
from django.views.generic import CreateView, FormView
from django.urls import reverse 
from .forms import UploadDataForm
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages


class DataUploadView(LoginRequiredMixin, FormView):
    login_url = 'admin:login'
    
    form_class = UploadDataForm
    template_name = 'agency/upload.html'           

    def form_valid(self, form):
        form.load_data()
        return super().form_valid(form)

    def get_success_url(self):
        messages.success(self.request, "File Upload Successfully!")
        return reverse('agency:filter')
