from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from cases.models import Case, CaseStatusHistory

def update_case_status(request, id):
    case = get_object_or_404(Case, id=id)

    if not request.user.is_staff:
        return HttpResponse("Not allowed", status=403)

    if request.method == "POST":

        selected_status = request.POST.get("status")
        custom_status = request.POST.get("custom_status")

        # custom status override
        if custom_status and custom_status.strip():
            case.status = selected_status
            case.custom_status = custom_status
        else:
            case.status = selected_status
            case.custom_status = None

        case.save()

        # log history
        CaseStatusHistory.objects.create(
            case=case,
            status=case.status,
            changed_by=request.user.username
        )

        return redirect('cases')

    return render(request, 'cases/update_case_status.html', {'case': case})