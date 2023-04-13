from datetime import timedelta
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from datacenter.models import Passcard, Visit
from datacenter.storage_information_view import get_duration, format_duration

LONG_VISIT_MINUTES = 60


def is_visit_long(visit, minutes=LONG_VISIT_MINUTES):
    duration = get_duration(visit)
    return duration > timedelta(minutes=minutes)


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)

    visits = Visit.objects.filter(passcard=passcard).order_by('-entered_at')

    this_passcard_visits = []
    for visit in visits:
        duration = get_duration(visit)
        is_strange = is_visit_long(visit)

        this_passcard_visits.append({
            'entered_at': visit.entered_at,
            'duration': duration,
            'is_strange': is_strange
        })

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
