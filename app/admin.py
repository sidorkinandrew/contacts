from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

# UnRegister Group
from django.contrib.auth.models import Group
admin.site.unregister(Group)

# Customize Contacts
class ContactsAdmin(ImportExportModelAdmin):  # admin.ModelAdmin):
    # columns to diplay
    list_display = ('id', 'name', 'gender', 'email', 'info', 'phone')
    # clickable columns
    list_display_links = ('id', 'name')
    # columns to edit
    list_editable = ('info',)
    # entries per page
    list_per_page = 10
    # search fields
    search_fields = list_display
    # filterable columns
    list_filter = ('gender', 'date_added')


# Register Contact
from .models import Contact
admin.site.register(Contact, ContactsAdmin)

