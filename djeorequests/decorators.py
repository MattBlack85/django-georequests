from __future__ import unicode_literals

from functools import wraps

from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.utils.encoding import python_2_unicode_compatible

HTTP_METHODS = set(("DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT"))


@python_2_unicode_compatible
class HttpMethodError(Exception):
    std_msg = "One or more HTTP method does not exist"

    def __init__(self, msg=None):
        self.msg = msg or self.std_msg

    def __str__(self):
        return self.msg


def only_superuser(f):
    @wraps(f)
    def wrapper(request, *args, **kwargs):
        if request.user.is_superuser:
            return f(request, *args, **kwargs)
        raise PermissionDenied()
    return wrapper


def allowed_methods(http_methods):
    if isinstance(http_methods, list):
        for method in http_methods:
            if not method.upper() in HTTP_METHODS:
                raise HttpMethodError()

        def decorate(f):
            @wraps(f)
            def wrapper(request, *args, **kwargs):
                if request.method in http_methods:
                    return f(request, *args, **kwargs)
                return HttpResponse(status=405)
            return wrapper
        return decorate
    raise TypeError("You have to pass a list")
