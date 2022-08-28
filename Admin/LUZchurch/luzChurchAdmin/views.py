from django.shortcuts import render
from .models import *
from django.http import JsonResponse
# Create your views here.

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def homepage_admin(request):
    return render(request,template_name = "admin-temp/main-slider.html")

def admin_instructions(request):
    return render(request,template_name = "admin-temp/instructions.html")


def homepage_section1(request):
    homepage_values = homepage_section1_data(request)
    data = {"homepage_values":homepage_values}
    print(data)
    return render(request,template_name = "admin-temp/homepage-section1.html",context = data)


def homepage_section1_data(request):
    moto_details = Moto.objects.all().values().last()
    office_history_details = OfficeHistory.objects.all().values().last()
    homepage_sec_details = {
        "moto_details": moto_details,
        "office_history_details": office_history_details
    }
    print(moto_details,office_history_details)
    if is_ajax(request):
        return JsonResponse({"message":'Retrived Successfully',"data": homepage_sec_details}, status=200)
    else:
        return homepage_sec_details

# ADD CHURCH MOTO
def add_church_moto(request):
    moto = request.POST.get('church_moto')

    homepage_section1_table = Moto()
    homepage_section1_table.moto = moto

    if is_ajax(request) and request.method == 'POST':
        homepage_section1_table.save()
        return JsonResponse({"message":'Updated Moto Successfully'}, status=200)
    else:
        homepage_section1_table.save()
        return "Updated Moto Successfully"


# ADD CHURCH SHORT HISTORY AND CONTACT NUMBER
def add_history_office(request):

    short_history = request.POST.get('short_history')
    church_office = request.POST.get('church_office')
    church_mobile = request.POST.get('church_mobile')
    print(short_history,church_office,church_mobile)
    office_history_table = OfficeHistory()
    office_history_table.short_history = short_history
    office_history_table.church_office = church_office
    office_history_table.church_mobile = church_mobile

    if is_ajax(request) and request.method == 'POST':
        office_history_table.save()
        return JsonResponse({"message":'Data Updated Successfully'}, status=200)
    else:
        office_history_table.save()
        return "Updated Moto Successfully"