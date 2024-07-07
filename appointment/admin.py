from django.contrib import admin
from .models import Appointment

# to implement email sending functionality
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string




# Register your models here.
class AppointmentAdmin(admin.ModelAdmin):
    def patient_name(self, obj):
        return obj.patient.user.first_name
    
    def doctor_name(self, obj):
        return obj.doctor.user.first_name

    list_display = ['doctor_name', 'patient_name', 'appointment_types', 'appointment_status', 'symptom', 'time', 'cancel']


    def save_model(self, request, obj, form, change):
        obj.save()      # appointment_status save korte...

        if obj.appointment_status == 'Running' and obj.appointment_types == 'Online':
            # email sending implementation
            email_subject = 'Your online appointment is available now'
            email_body = render_to_string('admin_email.html', {
                'patient': obj.patient,
                'doctor': obj.doctor,
            })

            email = EmailMultiAlternatives(email_subject, '', to = [obj.patient.user.email])
            email.attach_alternative(email_body, 'text/html')
            email.send()


admin.site.register(Appointment, AppointmentAdmin)