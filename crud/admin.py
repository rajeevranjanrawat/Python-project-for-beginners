from django.contrib import admin

# Register your models here.
from crud.models import Employee, Education

admin.site.register(Employee)
admin.site.register(Education)