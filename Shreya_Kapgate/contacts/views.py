from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Contact

class ContactListView(ListView):
    model = Contact