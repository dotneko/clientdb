from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, CreateView
from .models import Client

# Create your views here.

def index(request):
    latest_client_list = Client.objects.order_by('id')[:5]
    context = {
        'latest_client_list': latest_client_list,
    }
    return render(request, 'clientdb/index.html', context)

class ClientList(ListView):
    template_name = 'clientdb/client_list.html'
    model = Client
    context_object_name = 'latest_client_list'

    def get_queryset(self):
        """ Return last five clients."""
        return Client.objects.order_by('id')[:5]

class ClientCreateView(CreateView):
    model = Client 
    fields = ('client_ref', 'full_name', 'dob','hk_id', 'sex', 'tel','address','area')

def detail(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    return render(request, 'clientdb/detail.html', {'client': client })