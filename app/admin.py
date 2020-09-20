from django.contrib import admin



# UnRegister Group
from django.contrib.auth.models import Group
admin.site.unregister(Group)

# Customize Contacts
class ContactsAdmin(admin.ModelAdmin):
    # columns to diplay
    list_display = ('id', 'name', 'gender', 'email', 'info', 'phone')
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

