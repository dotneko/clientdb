from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

from .models import Client
from .forms import ClientForm

class ClientList(LoginRequiredMixin, ListView):
    login_url = 'user:login'
    template_name = 'clientdb/client_list.html'
    paginate_by = 20
    model = Client
    context_object_name = 'latest_client_list'

    # def get_queryset(self):
    #     """ Return last five clients."""
    #     return Client.objects.order_by('id')[:5]

class SearchResults(ListView):
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

class ClientCreate(LoginRequiredMixin, CreateView):
    login_url = 'user:login'
    template_name = 'clientdb/client_form.html'
    form_class = ClientForm

class ClientDetail(LoginRequiredMixin, DetailView):
    login_url = 'user:login'
    template_name = 'clientdb/client_detail.html'
    model = Client

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class ClientUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'clientdb/update_form.html'
    form_class = ClientForm
    model = Client

class ClientDelete(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('clientdb:ClientList')