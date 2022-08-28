from django.shortcuts import render
from luzChurchAdmin.models import *
# Create your views here.

def portfolio_home(request):
    moto_details = Moto.objects.all().values().last()
    office_history_details = OfficeHistory.objects.all().values().last()
    section1_details = {
        "moto_details": moto_details,
        "office_history_details": office_history_details
    }
    return render(request,template_name = "portfolio_temp/index.html", context = section1_details)

