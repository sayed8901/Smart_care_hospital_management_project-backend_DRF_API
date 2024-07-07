from django.contrib import admin
from .models import ContactUs

# Register your models here.
# admin.site.register(ContactUs)

class ContactUsModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone', 'problem']

admin.site.register(ContactUs, ContactUsModelAdmin)