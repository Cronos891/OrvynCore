from django.contrib import admin
from .models import (
    Tenant, Companies, Countries, Employees, StatesOrProvinces,
    Locations, Currencies, HealthInsurances, JobFamilies, JobPositions,
    BusinessUnits, CostCenters, InternalOrders, PayGroups, UnionSubgroups,
    WorkScheduled
)


@admin.register(JobFamilies)
class JobFamiliesAdmin(admin.ModelAdmin):
    list_display = ('job_family_name', 'job_family_group', 'tenant_id')
    search_fields = ('job_family_name', 'job_family_group')


@admin.register(JobPositions)
class JobPositionsAdmin(admin.ModelAdmin):
    list_display = ('job_code', 'job_position_name', 'job_family_name', 'tenant_id')
    list_filter = ('job_family_name',)
    search_fields = ('job_code', 'job_position_name')


@admin.register(BusinessUnits)
class BusinessUnitsAdmin(admin.ModelAdmin):
    list_display = ('business_unit_id', 'business_unit', 'tenant_id')
    search_fields = ('business_unit_id', 'business_unit')


@admin.register(CostCenters)
class CostCentersAdmin(admin.ModelAdmin):
    list_display = ('cost_center_code', 'cost_center_name', 'tenant_id')
    search_fields = ('cost_center_code', 'cost_center_name')


@admin.register(InternalOrders)
class InternalOrdersAdmin(admin.ModelAdmin):
    list_display = ('internal_order_code', 'internal_order_name', 'tenant_id')
    search_fields = ('internal_order_code', 'internal_order_name')


@admin.register(PayGroups)
class PayGroupsAdmin(admin.ModelAdmin):
    list_display = ('pay_group_code', 'pay_group_name', 'tenant_id')
    search_fields = ('pay_group_code', 'pay_group_name')


@admin.register(UnionSubgroups)
class UnionSubgroupsAdmin(admin.ModelAdmin):
    list_display = ('subgroup_code', 'subgroup_name', 'tenant_id')
    search_fields = ('subgroup_code', 'subgroup_name')


@admin.register(WorkScheduled)
class WorkScheduledAdmin(admin.ModelAdmin):
    list_display = ('shift_code', 'shift_description', 'tenant_id')
    search_fields = ('shift_code', 'shift_description')


@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    list_display = ('tenant_id', 'name', 'created_at', 'updated_at')
    search_fields = ('tenant_id', 'name')


@admin.register(Companies)
class CompaniesAdmin(admin.ModelAdmin):
    list_display = ('company_code', 'company', 'tenant_id', 'company_status')
    list_filter = ('company_status', 'tenant_id')
    search_fields = ('company_code', 'company')


@admin.register(Countries)
class CountriesAdmin(admin.ModelAdmin):
    list_display = ('country_code', 'country', 'tenant_id', 'salary_multiplier')
    search_fields = ('country_code', 'country')


@admin.register(Employees)
class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'full_legal_name', 'company_code', 'status_of_employee')
    list_filter = ('status_of_employee', 'gender', 'company_code')
    search_fields = ('employee_id', 'full_legal_name', 'corporate_email')
    readonly_fields = ('age', 'years_of_service')


@admin.register(StatesOrProvinces)
class StatesOrProvincesAdmin(admin.ModelAdmin):
    list_display = ('region_code', 'region', 'country_code', 'tenant_id')
    search_fields = ('region_code', 'region')


@admin.register(Locations)
class LocationsAdmin(admin.ModelAdmin):
    list_display = ('location_code', 'location_name', 'region_code', 'country_code')
    search_fields = ('location_code', 'location_name')


@admin.register(Currencies)
class CurrenciesAdmin(admin.ModelAdmin):
    list_display = ('currency_code', 'currency', 'country_code', 'tenant_id')
    search_fields = ('currency_code', 'currency')


@admin.register(HealthInsurances)
class HealthInsurancesAdmin(admin.ModelAdmin):
    list_display = ('health_insurance_code', 'health_insurance_name', 'health_insurance_plan', 'tenant_id')
    search_fields = ('health_insurance_code', 'health_insurance_name')