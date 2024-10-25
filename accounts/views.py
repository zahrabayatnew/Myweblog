from django.shortcuts import render
from .forms import CustomUserCreationForm

def signupview(request):
    form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})