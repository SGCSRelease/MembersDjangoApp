from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from .models import Penalty
from .models import Profile
# Create your views here.

def list(request):
    return HttpResponse("List of Release Members.")

def profile(request, member_id):
    try:
        num_profile = Profile.objects.get(pk=member_id)
    except Profile.DoesNotExist:
        raise Http404("No profile is uploaded")
    return render(request, 'members/profile.html', {'Profile': num_profile})

def penalty(request, member_id):
    try:
        num_penalty = Penalty.objects.get(pk=member_id)
    except Penalty.DoesNotExist:
        raise Http404("No penalty exists")
    return render(request, 'members/penalty.html', {'Penalty': num_penalty})
