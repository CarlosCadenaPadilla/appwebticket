from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from .models import Event
from .forms import EventForm


# Create your views here.

class EventListView(ListView):
    model = Event

class EventDetailView(DetailView):
    model = Event  

class EventCreate(CreateView):
    model = Event
    form_class = EventForm
    success_url = reverse_lazy('events:events')  
    
class EventUpdate(UpdateView):
    model = Event
    fields = ['title','description','link']
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('events:update', args = [self.object.id]) + '?ok'

class EventDelete(DeleteView):
    model = Event
    success_url = reverse_lazy('events:events')        
