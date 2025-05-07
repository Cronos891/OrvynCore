from rest_framework import serializers
from .models import (Tenant, Companies, Countries, Employees, StatesOrProvinces,
                    Locations, Currencies, HealthInsurances, JobFamilies, JobPositions,
                    BusinessUnits, CostCenters, InternalOrders, PayGroups, UnionSubgroups,
                    WorkScheduled)


class TenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields = '__all__'


class CountriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Countries
        fields = '__all__'


class StatesOrProvincesSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatesOrProvinces
        fields = '__all__'


class LocationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locations
        fields = '__all__'


class CurrenciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Currencies
        fields = '__all__'


class HealthInsurancesSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthInsurances
        fields = '__all__'


class JobFamiliesSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobFamilies
        fields = '__all__'


class JobPositionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPositions
        fields = '__all__'


class BusinessUnitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessUnits
        fields = '__all__'


class CostCentersSerializer(serializers.ModelSerializer):
    class Meta:
        model = CostCenters
        fields = '__all__'


class InternalOrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = InternalOrders
        fields = '__all__'


class PayGroupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PayGroups
        fields = '__all__'


class UnionSubgroupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnionSubgroups
        fields = '__all__'


class WorkScheduledSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkScheduled
        fields = '__all__'


class CompaniesSerializer(serializers.ModelSerializer):
    company_location = LocationsSerializer(read_only=True)
    company_country = CountriesSerializer(read_only=True)

    class Meta:
        model = Companies
        fields = '__all__'


class EmployeesSerializer(serializers.ModelSerializer):
    # Nested serializers for related fields
    scheduled_weekly_hours = WorkScheduledSerializer(read_only=True)
    job_code = JobPositionsSerializer(read_only=True)
    job_position_name = JobPositionsSerializer(read_only=True)
    job_profile = JobPositionsSerializer(read_only=True)
    job_family_name = JobPositionsSerializer(read_only=True)
    job_family_group = JobPositionsSerializer(read_only=True)
    business_unit = BusinessUnitsSerializer(read_only=True)
    function = BusinessUnitsSerializer(read_only=True)
    sub_function = BusinessUnitsSerializer(read_only=True)
    country = CountriesSerializer(read_only=True)
    region = StatesOrProvincesSerializer(read_only=True)
    location_code = LocationsSerializer(read_only=True)
    location_name = LocationsSerializer(read_only=True)
    company_code = CompaniesSerializer(read_only=True)
    cost_center_code = CostCentersSerializer(read_only=True)
    cost_center_name = CostCentersSerializer(read_only=True)
    internal_order_code = InternalOrdersSerializer(read_only=True)
    internal_order_name = InternalOrdersSerializer(read_only=True)
    union_name = UnionSubgroupsSerializer(read_only=True)
    manager_id = BusinessUnitsSerializer(read_only=True)
    manager_full_legal_name = BusinessUnitsSerializer(read_only=True)
    manager_first_name = BusinessUnitsSerializer(read_only=True)
    manager_last_name = BusinessUnitsSerializer(read_only=True)
    management_level_1 = BusinessUnitsSerializer(read_only=True)
    management_level_2 = BusinessUnitsSerializer(read_only=True)
    pay_group_name = PayGroupsSerializer(read_only=True)
    category = UnionSubgroupsSerializer(read_only=True)
    grade_level = UnionSubgroupsSerializer(read_only=True)
    currency = CurrenciesSerializer(read_only=True)
    health_insurance_code = HealthInsurancesSerializer(read_only=True)
    health_insurance_name = HealthInsurancesSerializer(read_only=True)
    health_insurance_plan = HealthInsurancesSerializer(read_only=True)

    class Meta:
        model = Employees
        fields = '__all__'