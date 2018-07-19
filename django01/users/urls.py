from django.conf.urls import url

from users import views

urlpatterns = [
    url(r'^index$',views.index),

    # url(r"^news/(\d+)/(\d+)$",views.news),
    url(r"^news/(?P<a>\d+)/(?P<b>\d+)$",views.news),


    url(r"^news2$",views.news2),
    url(r"^news3$",views.news3),
    url(r"^news4$",views.news4),
    # url(r"^resp$",views.resp),

    url(r"^set_cookie$",views.set_cookie),
    url(r"^get_cookie$",views.get_cookie),

    url(r"^set_session$",views.set_session),
    url(r"^get_session$",views.get_session),



    url(r"^post$",views.post),
    url(r"^do_post$",views.do_post),

    url(r"^post2$",views.posttiezhi.as_view()),

    url(r"^post3$",views.posttiezhi1.as_view()),

    url(r"^post4$",views.posttiezhi2.as_view()),

]
