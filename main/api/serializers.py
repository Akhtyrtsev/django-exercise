from rest_framework import serializers
from .models import Organization, Department, Employee, Status


class MyField(serializers.RelatedField):
    def to_representation(self, value):
        return value.name


class OrganizationSerializer(serializers.ModelSerializer):
    departments_count = serializers.SerializerMethodField('get_departments_count')
    employees_count = serializers.SerializerMethodField('get_employees_count')
    departments = MyField(many=True, read_only=True)

    def get_departments_count(self, obj):
        return obj.departments.all().count()

    def get_employees_count(self, obj):
        employees_count = 0
        for i in obj.departments.all():
            employees_count += i.employees.all().count()
        return employees_count

    class Meta:
        model = Organization
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):
    employees_count = serializers.SerializerMethodField('get_employees_count')
    employees = MyField(many=True, read_only=True)
    organization = MyField(many=False, queryset=Organization.objects.all())

    def get_departments_count(self, obj):
        return Department.objects.all().count()

    def get_employees_count(self, obj):
        return obj.employees.all().count()

    class Meta:
        model = Organization
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):

    status = MyField(many=False, queryset=Status.objects.all())
    department = MyField(many=False, queryset=Department.objects.all())

    class Meta:
        model = Employee
        fields = '__all__'

