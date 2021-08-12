from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.utils.html import escape
from django.views import View

# Create your views here.
def funky(request):
    response = """<html><body><p>This is the funky function sample</p>
    </body></html>"""
    return HttpResponse(response)

def danger(request) :
    response = """<html><body>
    <p>Your guess was """+request.GET['guess']+"""</p>
    </body></html>"""
    return HttpResponse(response)

def game(request) :
    response = """<html><body>
    <p>Your guess was """+escape(request.GET['guess'])+"""</p>
    </body></html>"""
    return HttpResponse(response)

def rest(request, guess) :
    response = """<html><body>
    <p>Your guess was """+escape(guess)+"""</p>
    </body></html>"""
    return HttpResponse(response)

# This is a command to the browser
def bounce(request) :
    return HttpResponseRedirect('http://127.0.0.1:8000/simple.htm')

# https://docs.djangoproject.com/en/3.0/topics/class-based-views/
class MainView(View) :
    def get(self, request):
        response = """<html><body><p>Hello world MainView in HTML</p>
        
        </body></html>"""
        return HttpResponse(response)

class RestMainView(View) :
    def get(self, request, guess):
        print("We got a slug from the URL",guess);
        response = """<html><body>
        <p>Your guess was """+escape(guess)+"""</p>
        </body></html>"""
        return HttpResponse(response)

