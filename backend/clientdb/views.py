from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

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
    paginate_by = 20
    model = Client
    context_object_name = 'latest_client_list'

    # def get_queryset(self):
    #     """ Return last five clients."""
    #     return Client.objects.order_by('id')[:5]

class SearchResultsView(ListView):
    model = Client
    template_name = 'clientdb/search_results.html'
    context_object_name = 'search_result_list'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Client.objects.filter(
            Q(lastname__icontains=query) |
            Q(firstname__icontains=query) |
            Q(hk_id__icontains=query) |
            Q(tel__icontains=query) 
        )
        return object_list

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