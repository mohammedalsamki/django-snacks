from .views import HomeView, AboutView
from django.urls import path

urlpatterns =[
    path('', HomeView.as_view(), name = 'snacks-home'),
    path('about', AboutView.as_view(), name = 'about'),
]
