from django.shortcuts import render
from datacenter.models import Visit
import django.utils.timezone
from visit_duration import format_duration, get_duration, is_visit_long


def storage_information_view(request):
    active_visits = Visit.objects.filter(leaved_at=None)

    non_closed_visits = []
    for active_visit in active_visits:
        owner_name = active_visit.passcard
        who_entered = owner_name.owner_name
        entered_at = django.utils.timezone.localtime(active_visit.entered_at)
        duration = format_duration(get_duration(active_visit))
        is_strange = is_visit_long(active_visit)

        non_closed_visits.append({
            'who_entered': who_entered,
            'entered_at': entered_at,
            'duration': duration,
            'is_strange': is_strange
        })

    if not non_closed_visits:
        context = {'message': 'Нет активных посещений'}
    else:
        context = {'non_closed_visits': non_closed_visits}

    return render(request, 'storage_information.html', context)

