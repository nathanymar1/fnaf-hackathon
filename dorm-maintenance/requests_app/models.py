from django.db import models

class MaintenanceRequest(models.Model):
    class IssueType(models.TextChoices):
        PLUMBING = "plumbing", "Plumbing"
        ELECTRICAL = "electrical", "Electrical"
        FURNITURE = "furniture", "Furniture"
        APPLIANCES = "appliances", "Appliances"
        HVAC = "hvac", "HVAC"
        STRUCTURAL = "structural", "Structural"
        LOCKS = "locks", "Locks"
        PEST = "pest", "Pest Control"
        OTHER = "other", "Other"

    class Urgency(models.TextChoices):
        LOW = "low", "Low"
        MEDIUM = "medium", "Medium"
        HIGH = "high", "High"

    urgency = models.CharField(max_length=10, choices=Urgency.choices, blank=True)
    summary = models.TextField(blank=True)

    building = models.CharField(max_length=100)
    room = models.CharField(max_length=10)
    email = models.EmailField(max_length=254)
    description = models.TextField()
    issue_type = models.CharField(
        max_length=20,
        choices=IssueType.choices,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)


