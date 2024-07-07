from django.shortcuts import render
from rest_framework import viewsets

from .models import Appointment
from .serializers import AppointmentSerializer


# Create your views here.
class AppointmentViewSet(viewsets.ModelViewSet):
    # step 0: query to get all appointment data
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


    # step 1: custom query to get all the appointment data only for a specific patient
    def get_queryset(self):
        # step 2: প্রথমে super() দ্বারা আগের সব appointment queryset data নিয়ে নিলাম
        queryset = super().get_queryset()

        # step 3: URL এর request এর 'patient_id' নামের parameter থেকে patient_id কে get করছি মানে নিয়ে নিচ্ছি
        print(self.request.query_params)
        patient_id = self.request.query_params.get('patient_id')

        # step 4: URL এর request এর 'patient_id' ওয়ালা কোন patient যদি আমাদের data model এ থাকে, তাহলে শুধুমাত্র তার appointment data গুলো queryset থেকে filter করে বের করে নিচ্ছি।
        if patient_id:
            # step 5: আগের total queryset কে নতুন filtered queryset দ্বারা replace বা overwrite করে দিচ্ছি।
            queryset = queryset.filter(patient_id = patient_id)

        # step 6: finally, filtered queryset data কে return করে দিচ্ছি।
        return queryset
