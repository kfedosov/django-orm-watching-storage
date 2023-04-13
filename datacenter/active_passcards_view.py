from django.shortcuts import render
from datacenter.models import Passcard
from django.http import HttpResponseServerError


def active_passcards_view(request):
    try:
        active_passcards = Passcard.objects.filter(is_active=True)
        context = {
            'active_passcards': active_passcards,  # люди с активными пропусками
        }
        return render(request, 'active_passcards.html', context)
    except Exception:
        return HttpResponseServerError("Произошла ошибка при загрузке страницы")
