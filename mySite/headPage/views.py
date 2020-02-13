from django.http import HttpResponse, HttpResponseNotFound
from django.views import View
import datetime

class MyView(View):

    def get(self, request, *args, **kwargs):
        body = 'Hello, World!' + MyView.current_datetime()
        return HttpResponse(body)

    def my_view(self, request):
        if request:
            return HttpResponseNotFound('<h1>Page not found</h1>')
        else:
            return HttpResponse('<h1>Page was found</h1>')
        
        return HttpResponse(status=201)

    @staticmethod
    def current_datetime():
        now = datetime.datetime.today()
        html = "<html><body><br> It is now: %s.</body></html>" % now
        return '' + html
