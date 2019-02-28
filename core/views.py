from django.shortcuts import render, HttpResponse
from django.views.generic.base import TemplateView

# Create your views here.

class HomePageView(TemplateView):
    template_name = "core/home.html"
    
    def get(self, request, *args, **kwargs):
        return render(request,self.template_name, {'title':"MEJOR APP"})   

class TicketPageView(TemplateView):
    template_name = "core/tickets.html"

class ContactPageView(TemplateView):
    template_name = "core/contact.html"