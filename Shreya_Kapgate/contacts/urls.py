from django.urls import path
from .views import ContactListView, create_contact, ContactDetailView  # Import the create_contact view

urlpatterns = [
    path("", ContactListView.as_view(), name="contact_list"),
    path("create/", create_contact, name="contact_form"),  # Add the path for creating contacts
    path("contacts/<int:pk>/", ContactDetailView.as_view(), name="contact_detail"),
]