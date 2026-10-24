from django.shortcuts import render

def request_form(request):
    return render(request, 'requests_app/request_form.html')

def request_dashboard(request):
    return render(request, 'requests_app/request_dashboard.html')
