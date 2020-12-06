from django.contrib import admin
from .models import patient , doctor , diseaseinfo , consultation,rating_review

# Register your models here.


# change Register your models data's list views attribite.
class PatientAdmin(admin.ModelAdmin):
    list_display = ( 'user', 'name', 'dob', 'mobile_no', 'address')   # display items
    # list_display_links = ('id', 'name')  #clickable display items
    list_filter = ('address',)   # filter display items
    # list_editable = ('mobile_no')   # editable list item
    search_fields = ('name', 'dob', 'address')  # search panels filter items
    list_per_page = 10   # display list per page



# change Register your models data's list views attribite.
class DoctorAdmin(admin.ModelAdmin):
    list_display = ( 'user', 'name', 'dob','qualification','specialization', 'mobile_no', 'rating')   # display items
    # list_display_links = ('id', 'name')  #clickable display items
    list_filter = ('specialization',)   # filter display items
    # list_editable = ('mobile_no')   # editable list item
    search_fields = ('name', 'dob', 'qualification','specialization', 'rating')  # search panels filter items
    list_per_page = 10   # display list per page



# change Register your models data's list views attribite.
class DiseaseInfoAdmin(admin.ModelAdmin):
    list_display = ( 'patient', 'diseasename', 'no_of_symp','consultdoctor','confidence')   # display items
    # list_display_links = ('id', 'name')  #clickable display items
    list_filter = ('diseasename',)   # filter display items
    # list_editable = ('mobile_no')   # editable list item
    search_fields = ('patient', 'diseasename', 'consultdoctor','confidence')  # search panels filter items
    list_per_page = 10   # display list per page


# change Register your models data's list views attribite.
class ConsultAdmin(admin.ModelAdmin):
    list_display = ( 'patient', 'doctor', 'diseaseinfo','consultation_date','status')   # display items
    # list_display_links = ('id', 'name')  #clickable display items
    list_filter = ('consultation_date',)   # filter display items
    # list_editable = ('mobile_no')   # editable list item
    search_fields = ('patient', 'doctor', 'diseaseinfo','consultation_date','status')  # search panels filter items
    list_per_page = 10   # display list per page


# change Register your models data's list views attribite.
class rating_reviewAdmin(admin.ModelAdmin):
    list_display = ( 'patient', 'doctor', 'rating','review')   # display items
    # list_display_links = ('id', 'name')  #clickable display items
    list_filter = ('review',)   # filter display items
    # list_editable = ('mobile_no')   # editable list item
    search_fields = ('patient', 'doctor', 'rating','review')  # search panels filter items
    list_per_page = 10   # display list per page



admin.site.register(patient,PatientAdmin)
admin.site.register(doctor, DoctorAdmin)
admin.site.register(diseaseinfo, DiseaseInfoAdmin)
admin.site.register(consultation, ConsultAdmin)
admin.site.register(rating_review, rating_reviewAdmin)
