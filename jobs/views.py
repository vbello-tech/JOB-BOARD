from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import *
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .forms import *
from accounts.views import get_user
# Create your views here.


class UploadJobs(CreateView,LoginRequiredMixin):
        model = Upload
        form_class = JobUploadForm
        template_name = 'jobs/upload.html'
        success_url = '/job-list/'



class AllJobs(ListView, LoginRequiredMixin):
        model = Upload
        template_name = 'jobs/list.html'
        paginate_by = 3










