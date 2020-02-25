from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Client

# Create your views here.

def index(request):
    latest_client_list = Client.objects.order_by('id')[:5]
    context = {
        'latest_client_list': latest_client_list,
    }
    return render(request, 'clientdb/index.html', context)

class ClientList(LoginRequiredMixin, ListView):
    login_url = 'user:login'
    template_name = 'clientdb/client_list.html'
    paginate_by = 10
    model = Client
    context_object_name = 'latest_client_list'

    # def get_queryset(self):
    #     """ Return last five clients."""
    #     return Client.objects.order_by('id')[:5]

class ClientCreateView(LoginRequiredMixin, CreateView):
    login_url = 'user:login'

    model = Client 
    fields = ('client_ref', 'lastname', 'firstname', 'dob','hk_id', 'sex', 'tel','address','area')

class ClientDetailView(LoginRequiredMixin, DetailView):
    login_url = 'user:login'

    template_name = 'clientdb/client_detail.html'
    model = Client

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context