from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):
  return render(request, 'home.html', {
    'form': UserCreationForm
  })

def signup(request):
  return render(request, 'signup.html', {
    'form': UserCreationForm
  })