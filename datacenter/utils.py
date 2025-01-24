from django.utils import timezone
from datacenter.models import Visit


MINUTES_PER_HOUR = 60
SECONDS_PER_HOUR = 3600
SECONDS_PER_MINUTE = 60

def get_duration(visit):
    if visit not in Visit.objects.filter(leaved_at=None):
        duration = visit.leaved_at - visit.entered_at
    else:
        duration = timezone.localtime() - visit.entered_at.astimezone()
    return duration

def format_duration(duration):
    hours, other = divmod(duration.total_seconds(), SECONDS_PER_HOUR)
    minutes, seconds = divmod(other, SECONDS_PER_MINUTE)
    return f'{int(hours):02}:{int(minutes):02}:{int(seconds):02}'

def is_visit_long(duration, minutes=MINUTES_PER_HOUR):
    return duration.total_seconds() > minutes * SECONDS_PER_MINUTE