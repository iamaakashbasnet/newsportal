from datetime import datetime
from django.http.response import HttpResponse
from .models import ViewCounter


def views_counter_manager(request):
    current_day = int(datetime.now().strftime('%d'))

    if datetime.now().strftime('%b') == 'Feb':
        if current_day == 28:
            ViewCounter.objects.all().update(views=0)
    else:
        if current_day == 30:
            ViewCounter.objects.all().update(views=0)

    db_day = ViewCounter.objects.get(day=current_day)
    db_day.views += 1
    db_day.save()

    return HttpResponse('Updated!')
