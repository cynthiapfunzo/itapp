
from django.http import HttpResponse

def admin_dashboard(request):
    return HttpResponse("Admin Dashboard")

def employee_dashboard(request):
    return HttpResponse("Employee Dashboard")



