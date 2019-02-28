from django.urls import path
from .views import HomePageView, TicketPageView, ContactPageView


urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('tickets/',TicketPageView.as_view(), name="tickets"),
    path('contact/',ContactPageView.as_view(), name="contact"),
]

