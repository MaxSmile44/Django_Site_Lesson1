from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render, get_object_or_404


MINUTES=60

def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []
    one_visit = dict()
    for visit in visits:
        one_visit['entered_at'] = visit.entered_at.astimezone().strftime("%d %b %Y г. %H:%M")
        one_visit['duration'] = str(Visit.get_duration(visit)).split('.')[0]
        one_visit['is_strange'] = Visit.is_visit_long(Visit.get_duration(visit), MINUTES)
        this_passcard_visits.append(one_visit.copy())
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits  # данные по посещениям каждого сотрудника
    }

    return render(request, 'passcard_info.html', context)
