from django.http import HttpResponse
class AppMaintainance(object):
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,request):
        return HttpResponse('<h1>currently our application is under maintainance ..please try again sometime.!</h1>')

           
