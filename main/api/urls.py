from django.urls import path
from . import views

urlpatterns = [
    path('organizations/', views.OrganizationList.as_view()),
    path('departments/', views.DepartmentList.as_view()),
    path('employees/', views.EmployeeList.as_view()),
    path('login/', views.login)
]
