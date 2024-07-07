from django.shortcuts import render
from rest_framework import viewsets

from .models import Doctor, Specialization, Designation, AvailableTime, Review
from .serializers import DoctorSerializer, SpecializationSerializer, DesignationSerializer, AvailableTimeSerializer, ReviewSerializer


from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


# necessary importing for pagination
from rest_framework import pagination, filters





# pagination implementation
class DoctorPagination(pagination.PageNumberPagination):
    page_size = 1   # item per page
    page_size_query_param = page_size
    max_page_size = 100

    

# Create your views here.
class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    # implementing pagination
    pagination_class = DoctorPagination



class SpecializationViewSet(viewsets.ModelViewSet):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer


class DesignationViewSet(viewsets.ModelViewSet):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer



class AvailableTimeForSpecificDoctor(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        doctor_id = request.query_params.get('doctor_id')

        if doctor_id:
            # এক্ষেত্রে, Doctor model এ available_time যেহেতু ManyToManyField দ্বারা related মানে connected, তাই, Doctor কে এখানে doctor নামে access করে filter করতে পারছে।
            return queryset.filter(doctor = doctor_id)
        
        # to show all available times if any filtering is not applied
        return queryset



class AvailableTimeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = AvailableTime.objects.all()
    serializer_class = AvailableTimeSerializer

    # to implement filtering...
    filter_backends = [AvailableTimeForSpecificDoctor]



class ReviewViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
