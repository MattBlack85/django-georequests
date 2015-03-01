import datetime as dt
from datetime import datetime

from django.db.models import Count
from django.shortcuts import render


from djeorequests.decorators import allowed_methods, only_superuser
from djeorequests.geodashboard import COUNTRY_LIST
from .models import Visit


@only_superuser
@allowed_methods(["GET"])
def dashview(request):
    today = datetime.now()
    month_ago = today - dt.timedelta(days=30)
    visits = Visit.objects.filter(date__gte=month_ago, date__lte=today) \
                          .values('country') \
                          .annotate(total=Count('country')) \
                          .order_by('total')[:10]

    country_data = [{"hc-key": country, "value": 0} for country in COUNTRY_LIST]
    for visit in visits:
        country_data.append({"hc-key": str(visit['country']), "value": visit['total']})
        country_data.remove({"hc-key": visit['country'], "value": 0})

    context = {
        'top_10': country_data
    }

    return render(request, 'geodashboard/base.html', context)
