from django.db import models
from pytz import timezone
import datetime


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )

    def get_duration(visit, already_left=True):
        if already_left:
            duration = visit['leaved_at'] - visit['entered_at']
        else:
            our_timezone = timezone('Europe/Moscow')
            now = datetime.datetime.now().astimezone(our_timezone)
            duration = now - visit['entered_at']
        return duration.seconds

    def format_duration(duration):
        hours, other = divmod(duration, 3600)
        minutes, seconds = divmod(other, 60)
        return f'{int(hours):02}:{int(minutes):02}:{int(seconds):02}'

    def is_visit_long(duration, minutes=60):
        return True if duration > minutes * 60 else False