from django.utils.deprecation import MiddlewareMixin


class Mymiddleware(MiddlewareMixin):
    def __init__(self, get_response=None):
        super().__init__(get_response)

    def process_request(self, request):
        print("brfore view function")

    def process_response(self, request, response):
        print("after views function")
        return response
