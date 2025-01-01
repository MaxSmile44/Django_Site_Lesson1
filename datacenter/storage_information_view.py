from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


MINUTES=60

def storage_information_view(request):
    non_closed_visits = []
    one_visit = dict()
    for visit in Visit.objects.filter(leaved_at=None):
        one_visit['who_entered'] = visit.passcard
        one_visit['entered_at'] = visit.entered_at.astimezone().strftime("%d %b %Y г. %H:%M")
        one_visit['duration'] = str(Visit.get_duration(visit)).split('.')[0]
        one_visit['is_strange'] = Visit.is_visit_long(Visit.get_duration(visit), MINUTES)
        non_closed_visits.append(one_visit.copy())
    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
