

from django.contrib import admin
from .models import Category, Lender, Equipment, Employee, EquipmentIssue

admin.site.register(Category)
admin.site.register(Lender)
admin.site.register(Equipment)
admin.site.register(Employee)
admin.site.register(EquipmentIssue)
