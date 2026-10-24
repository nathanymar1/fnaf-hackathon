from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import MaintenanceRequest
from .forms import RequestForm
from .services.gemini import analyze_request

def request_form(request):
    if request.method == "POST":
        form = RequestForm(request.POST)
        if form.is_valid():
            obj = form.save()

            # try:
            #     result = analyze_request(obj.description)
            #     obj.issue_type = result["category"]
            #     obj.urgency = result["priority"]
            #     obj.summary = result["explanation"]
            # except Exception as e:
            #     print("Gemini failed:", e)
            #     obj.issue_type = MaintenanceRequest.IssueType.OTHER
            #     obj.summary = obj.description[:200]

            result = analyze_request(obj.description)
            obj.issue_type = result["category"]
            obj.urgency = result["priority"]
            obj.summary = result["explanation"]

            obj.save()
            return redirect("requests_app:thanks")
    else:
        form = RequestForm()

    return render(request, "requests_app/request_form.html", {"form": form})

def request_dashboard(request):
    processed = MaintenanceRequest.objects.exclude(issue_type="").order_by("-created_at")
    return render(request, "requests_app/request_dashboard.html", {"requests": processed})

def thanks(request):
    return render(request, "requests_app/thanks.html")

@require_POST
def request_delete(request, pk):
    obj = get_object_or_404(MaintenanceRequest, pk=pk)
    obj.delete()
    return redirect("requests_app:list")