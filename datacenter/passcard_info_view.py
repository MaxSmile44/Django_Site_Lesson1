from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from pytz import timezone
from django.shortcuts import get_object_or_404


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits = Visit.objects.values().filter(passcard=passcard)
    our_timezone = timezone('Europe/Moscow')
    this_passcard_visits = []
    this_passcard_visits_dict = dict()
    for visit in visits:
        this_passcard_visits_dict['entered_at'] = visit['entered_at'].astimezone(our_timezone).strftime("%d %b %Y г. %H:%M")
        if visit not in Visit.objects.values().filter(leaved_at=None):
            this_passcard_visits_dict['duration'] = Visit.format_duration(Visit.get_duration(visit))
            this_passcard_visits_dict['is_strange'] = Visit.is_visit_long(Visit.get_duration(visit), minutes=60)
        else:
            this_passcard_visits_dict['duration'] = Visit.format_duration(Visit.get_duration(visit, already_left=False))
            this_passcard_visits_dict['is_strange'] = Visit.is_visit_long(Visit.get_duration(visit, already_left=False), minutes=60)
        copy_this_passcard_visits_dict = this_passcard_visits_dict.copy()
        this_passcard_visits.append(copy_this_passcard_visits_dict)
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits  # данные по посещениям каждого сотрудника
    }

    return render(request, 'passcard_info.html', context)
