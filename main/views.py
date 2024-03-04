from django.shortcuts import render, redirect
from .models import Food, Entry, User, Calorie
from .forms import FoodForm, EntryForm, CaloriesForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'main/home.html')

def profile(request):
    return render(request, 'main/profile.html')