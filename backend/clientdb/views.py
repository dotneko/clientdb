from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView
from .models import Profile

# Create your views here.

def index(request):
    latest_client_list = Profile.objects.order_by('id')[:5]
    context = {
        'latest_client_list': latest_client_list,
    }
    return render(request, 'clientdb/index.html', context)

class ProfileList(ListView):
    template_name = 'clientdb/profile_list.html'
    model = Profile
    context_object_name = 'latest_client_list'

    def get_queryset(self):
        """ Return last five clients."""
        return Profile.objects.order_by('id')[:5]

def detail(request, profile_id):
    client = get_object_or_404(Profile, pk=profile_id)
    return render(request, 'clientdb/detail.html', {'client': client })