from django.urls import path
from .views import ContactListView, create_contact, ContactDetailView, ContactUpdateView  # Import the create_contact view

urlpatterns = [
    path("", ContactListView.as_view(), name="contact_list"),
    path("create/", create_contact, name="contact_form"),  # Add the path for creating contacts
    path("contacts/<int:pk>/", ContactDetailView.as_view(), name="contact_detail"),
    path("contacts/<int:pk>/update", ContactUpdateView.as_view(), name="contact_update"),
]