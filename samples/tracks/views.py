from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

# Create your views here.

def index(request):
    response = """<html><body><p>Tracks Data Modeling Example</p>
    <p>This example needs to be run in the Django shell in the command line
    and <a href="/admin">the admin console</a> after making a superuser.
    </body></html>"""
    return HttpResponse(response)
