from django.shortcuts import render
from django.views.generic.edit import CreateView


# Create your views here.
class SignUpPage(CreateView):
    form_class = UserCreationForm
    