from django.shortcuts import get_object_or_404, render

from .models import Profile

# Create your views here.

def index(request):
    latest_client_list = Profile.objects.order_by('-id')[:5]
    context = {
        'latest_client_list': latest_client_list,
    }
    return render(request, 'clientdb/index.html', context)

def detail(request, profile_id):
    client = get_object_or_404(Profile, pk=profile_id)
    return render(request, 'clientdb/detail.html', {'client': client })