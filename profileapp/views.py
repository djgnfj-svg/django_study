from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from profileapp.models import Profile
from profileapp.forms import ProfileCreationForm
# Create your views here.

class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'profileapp/create.html'