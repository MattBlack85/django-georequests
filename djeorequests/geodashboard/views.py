from django.http import HttpResponse

from djeorequests.decorators import allowed_methods, only_superuser


@only_superuser
@allowed_methods(["GET"])
def dashview(request):
    return HttpResponse()
