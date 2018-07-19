# from django.http.response import HttpResponse
# from django.http import HttpResponse
from django.http import HttpResponse


def check_ip(view_fun):

    def wrapper(request,*args,**kwargs):
        ip=request.META.get("REMOTE_ADDR")
        if ip in [
            "127.0.0.1"
        ]:
            return HttpResponse("no way")

        return view_fun(request,*args,**kwargs)
    return wrapper