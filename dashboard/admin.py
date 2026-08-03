from django.contrib import admin
from .models import Case, Notification
from .forms import CaseForm


# ACC ADMIN BRANDING

admin.site.site_header = "ACC Case Management System"
admin.site.site_title = "ACC Administration Portal"
admin.site.index_title = "Anti-Corruption Commission Dashboard"



@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):

    form = CaseForm

    list_display = (
        "case_code",
        "sector",
        "institution",
        "status",
        "created_at",
    )

    list_filter = (
        "sector",
        "institution",
        "status",
    )

    ordering = (
        "-created_at",
    )


    class Media:
        js = (
            "dashboard/institution.js",
        )



@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "date",
        "time",
    )

    ordering = (
        "date",
        "time",
    )