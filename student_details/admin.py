from django.contrib import admin
from .models import Students, Admission, FeePaid
# Register your models here.


class StudentDisplay(admin.ModelAdmin):
    list_display = ('name','contact_no','address','gender','highest_education',)

class AdmissionDisplay(admin.ModelAdmin):
    list_display = ('student','course_joined','joining_date','completion_date','course_status','course_fee',)

class FeePaidDisplay(admin.ModelAdmin):
    list_display = ('admission','fee_paid','payment_mode','paid_to','fee_paid_date',)


admin.site.register(Students,StudentDisplay)
admin.site.register(Admission,AdmissionDisplay)
admin.site.register(FeePaid,FeePaidDisplay)