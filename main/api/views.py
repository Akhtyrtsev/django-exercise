from .models import Organization, Department, Employee
from .serializers import OrganizationSerializer, DepartmentSerializer, EmployeeSerializer
from rest_framework import generics, filters, permissions
from .paginators import CountPagination
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
from django.core.mail import send_mail


@api_view(["POST"])
def login(request):
    email = request.data.get("email")
    if email is None:
        return Response({'error': 'Please provide email'},
                        status=HTTP_400_BAD_REQUEST)

    user = User.objects.get(email=email)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)

    token = Token.objects.create(user=user)

    send_mail('Token', token.key, 'mytestmail842@gmail.com',
              [email], fail_silently=False)
    return Response({'token': token.key},
                    status=HTTP_200_OK)


class OrganizationList(generics.ListAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = '__all__'


class DepartmentList(generics.ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    pagination_class = CountPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'organization__name']
    ordering_fields = '__all__'
    permission_classes = [permissions.IsAuthenticated]


class EmployeeList(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'department__name', 'status__name']
    ordering_fields = '__all__'
    permission_classes = [permissions.IsAdminUser]



# Create your views here.
