from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from pytz import timezone


def storage_information_view(request):
    our_timezone = timezone('Europe/Moscow')
    non_closed_visits = []
    non_closed_dict = dict()
    for visit in Visit.objects.values().filter(leaved_at=None):
        non_closed_dict['who_entered'] = Passcard.objects.filter(id = visit['passcard_id'])[0].owner_name
        non_closed_dict['entered_at'] = visit['entered_at'].astimezone(our_timezone).strftime("%d %b %Y г. %H:%M")
        non_closed_dict['duration'] = Visit.format_duration(Visit.get_duration(visit, already_left=False))
        non_closed_dict['is_strange'] = Visit.is_visit_long(Visit.get_duration(visit, already_left=False), minutes=60)
        copy_non_closed_dict = non_closed_dict.copy()
        non_closed_visits.append(copy_non_closed_dict)
    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
