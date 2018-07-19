import json

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views import View

from users.decoreters import check_ip


def index(request):
    """

    :param request:
    :param a:
    :param b:
    :return:
    """

    # return HttpResponse("hellooooooo django")
    return render(request, 'users/index.html')


def news(request, a, b):
    str = "a=%s,b=%s" % (a, b)
    return HttpResponse(str)


def news2(request):
    a = request.GET.get("a")
    b = request.GET.get("b")
    taxt = "a=%s,b=%s" % (a, b)
    return HttpResponse(taxt)


def news3(request):
    a = request.POST.get("a")
    b = request.POST.getlist("b")
    tex = "%s %s" % (a, b)
    return HttpResponse(tex)


def news4(request):
    print(request.META.get("REMOTE_ADDR"))
    print(request.META.get("CONTENT_TYPE"))

    json_str = request.body
    json_str = json_str.decode()

    dict_data = json.loads(json_str)
    a = dict_data.get("a")
    b = dict_data.get("b")
    tex = "%s %s" % (a, b)
    return HttpResponse(tex)


# def resp(request):
# response = HttpResponse("index", content_type="text.html", status=201)
# response = HttpResponse('{"name":"hahha}', content_type="applacation/json", status=201)
# response["a"] = 1
# response["b"] = 2
# return response
# response = JsonResponse({"name":"hahha"})
# response["a"] = 1
# response["b"] = 2
# return response
def set_cookie(request):
    response = HttpResponse("set cookie ok")
    response.set_cookie("user_id", 15)
    response.set_cookie("user_name", "hape")
    return response


def get_cookie(request):
    user_id = request.COOKIES.get("user_id")
    user_name = request.COOKIES.get("user_name")
    TEXT = "user_id=%s,user_name=%s" % (user_id, user_name)
    return HttpResponse(TEXT)


def set_session(request):
    request.session["user_id"] = 10
    request.session["user_name"] = "admin"

    return HttpResponse("set session ok")


def get_session(request):
    user_id = request.session.get("user_id")
    user_name = request.session.get("user_name")

    text = 'user_id=%s ,user_name=%s ' % (user_id, user_name)
    return HttpResponse(text)

@check_ip
def post(request):
    return render(request, "users/post.html")


def do_post(request):
    title = request.POST.get("title")
    content = request.POST.get("content")
    text="title=%s,content=%s" %(title,content)
    return HttpResponse(text)


class posttiezhi(View):
    @method_decorator(check_ip)
    def get(self,request):
        return render(request,"users/post2.html")

    def post(self,request):
         title=request.POST.get("title")
         content=request.POST.get("content")
         text = "title=%s,content=%s" % (title, content)
         return HttpResponse(text)




class posttiezhi1(View):




    @method_decorator(check_ip)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request):
        return render(request,"users/post2.html")

    def post(self,request):
         title=request.POST.get("title")
         content=request.POST.get("content")
         text = "title=%s,content=%s" % (title, content)
         return HttpResponse(text)


class check_ipmixin():
    @method_decorator(check_ip)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class posttiezhi2(check_ipmixin,View):


    def get(self, request):
        return render(request, "users/post2.html")

    def post(self, request):
        title = request.POST.get("title")
        content = request.POST.get("content")
        text = "title=%s,content=%s" % (title, content)
        return HttpResponse(text)


