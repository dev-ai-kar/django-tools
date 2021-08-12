from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

# Create your views here.

def index(request):
    response = """<html><body><p>User Model Sample Code</p>
    <p>This sample project has no user interface - it is all about playing with data models.</p>
    <p>If you have created a superuser account, you can visit the <a href="/admin">Admin</a> pages.</p>
   
    </body></html>"""
    return HttpResponse(response)

