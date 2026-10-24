from django.shortcuts import render
from .models import MaintenanceRequest

def request_form(request):
    return render(request, 'requests_app/request_form.html')

def request_dashboard(request):
    processed = MaintenanceRequest.objects.exclude(issue_type="").order_by("-created_at")
    return render(request, "requests_app/request_dashboard.html", {"requests": processed})
