from django.shortcuts import render
from django.http import HttpResponse

def request_form(request):
    html = """
        <html>

        </html>
    """
    return HttpResponse(html)
