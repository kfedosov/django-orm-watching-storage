from datetime import timedelta
import django

LONG_VISIT_MINUTES = 60


def is_visit_long(visit, minutes=LONG_VISIT_MINUTES):
    duration = get_duration(visit)
    return duration > timedelta(minutes=minutes)


def get_duration(visit):
    entered_at = visit.entered_at
    now = django.utils.timezone.now()
    if visit.leaved_at:
        now = visit.leaved_at
    duration = now - entered_at
    return duration


def format_duration(duration):
    hours = duration.seconds // 3600
    minutes = (duration.seconds % 3600) // 60
    seconds = duration.seconds % 60
    return f'{hours:02d}:{minutes:02d}'