from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from datacenter.utils import *


MINUTES=60

def storage_information_view(request):
    non_closed_visits = []
    for visit in Visit.objects.filter(leaved_at=None):
        one_visit = {
            'who_entered': visit.passcard,
            'entered_at': visit.entered_at.astimezone().strftime("%d %b %Y г. %H:%M"),
            'duration': format_duration(get_duration(visit)),
            'is_strange':  is_visit_long(get_duration(visit), MINUTES)
        }
        non_closed_visits.append(one_visit.copy())
    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
