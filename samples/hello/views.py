from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

# Create your views here.

def helloworld(request):
    logging.error('Hello world DJ4E in the log...')
    print('Hello world DJ4E in a print statement...')
    response = """<html><body><p>Hello world DJ4E in HTML</p>
    <p>
    </p>
    </body></html>"""
    return HttpResponse(response)

