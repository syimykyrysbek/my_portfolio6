from django.contrib import admin
from main.models import Contact
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ['email', 'number_of_telephone', 'message', 'sent_at']
    list_filter = ['sent_at']
    search_fields = ['email', 'number_of_telephone', 'message', 'sent_at']
    list_editable = ['number_of_telephone']
admin.site.register(Contact, ContactAdmin)