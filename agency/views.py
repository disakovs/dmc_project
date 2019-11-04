from django.shortcuts import render, redirect
from django.views.generic import CreateView, FormView
from django.urls import reverse 
from .forms import UploadDataForm
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.mixins import LoginRequiredMixin
from .utils import update_or_create_debtordata
from django.contrib import messages


class DataUploadView(LoginRequiredMixin, FormView):
    login_url = 'admin:login'
    
    form_class = UploadDataForm
    template_name = 'agency/upload.html'           

    def form_valid(self, form):
        form.load_data()
        return super().form_valid(form)

    """
    def post(self, request, *args, **kwargs):
        form = self.get_form(self.form_class)
        csv_file = request.FILES['csv_file']
        
        #if need to save file:
        #fs = FileSystemStorage()
        #fs.save(file.name, file)
        
        #check if csv format
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'File is not a CSV type')
            print('everything was going fine')
            return redirect('oarex:upload')
        
        update_or_create_debtordata(csv_file)

        
        if form.is_valid():
            print('yay its good')
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    """
    
    def get_success_url(self):
        messages.success(self.request, "File Upload Successfully!")
        return reverse('agency:filter')
