from django.shortcuts import render
from .models import Case


def cases(request):

    cases = Case.objects.all().order_by('-id')

    # FILTERS
    region = request.GET.get('region')
    status = request.GET.get('status')
    gender = request.GET.get('gender')
    age_group = request.GET.get('age_group')

    if region:
        cases = cases.filter(region=region)

    if status:
        cases = cases.filter(status=status)

    if gender:
        cases = cases.filter(gender=gender)

    if age_group:
        cases = cases.filter(age_group=age_group)

    return render(request, "dashboard/cases.html", {
        "cases": cases
    })