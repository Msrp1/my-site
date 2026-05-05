from websit.views import about_view, contact_view, index_view

from django.urls import *

urlpatterns = [
    path('home',index_view),
    path('about',about_view),
    path('contact',contact_view)
]
