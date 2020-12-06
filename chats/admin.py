from django.contrib import admin
from .models import Chat,Feedback
# Register your models here.




# change Register your models data's list views attribite.
class ChatAdmin(admin.ModelAdmin):
    list_display = ( 'created', 'consultation_id', 'sender', 'message')   # display items
    # list_display_links = ('id', 'name')  #clickable display items
    list_filter = ('sender',)   # filter display items
    # list_editable = ('mobile_no')   # editable list item
    search_fields = ('created', 'consultation_id', 'sender', 'message')  # search panels filter items
    list_per_page = 10   # display list per page

# change Register your models data's list views attribite.
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ( 'created', 'sender')   # display items
    # list_display_links = ('id', 'name')  #clickable display items
    list_filter = ('created',)   # filter display items
    # list_editable = ('mobile_no')   # editable list item
    search_fields = ('created', 'sender')  # search panels filter items
    list_per_page = 10   # display list per page





admin.site.register(Chat, ChatAdmin)
admin.site.register(Feedback, FeedbackAdmin)