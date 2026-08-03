from django.contrib import admin

from .models import (
    Report,
    Case,
    Officer,
    CaseStatusHistory,
    AuditLog
)

admin.site.register(Report)
admin.site.register(Case)
admin.site.register(Officer)
admin.site.register(CaseStatusHistory)
admin.site.register(AuditLog)