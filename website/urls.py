from django.urls import path
from website.views import about_view, contact_view, index_view

urlpatterns = [
    path('', index_view, name='index'),
    path('about', about_view, name='about'),
    path('contact', contact_view, name='contact'),
]
