from rest_framework import viewsets, permissions
from .models import (Tenant, Companies, Countries, Employees, StatesOrProvinces,
                     Locations, Currencies, HealthInsurances, JobFamilies, JobPositions,
                     BusinessUnits, CostCenters, InternalOrders, PayGroups, UnionSubgroups,
                     WorkScheduled)
from .serializers import (TenantSerializer, CompaniesSerializer, CountriesSerializer,
                         EmployeesSerializer, StatesOrProvincesSerializer, LocationsSerializer,
                         CurrenciesSerializer, HealthInsurancesSerializer, JobFamiliesSerializer,
                         JobPositionsSerializer, BusinessUnitsSerializer, CostCentersSerializer,
                         InternalOrdersSerializer, PayGroupsSerializer, UnionSubgroupsSerializer,
                         WorkScheduledSerializer)

class TenantViewSet(viewsets.ModelViewSet):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer
    permission_classes = [permissions.IsAuthenticated]

class CompaniesViewSet(viewsets.ModelViewSet):
    queryset = Companies.objects.all()
    serializer_class = CompaniesSerializer
    permission_classes = [permissions.IsAuthenticated]

class CountriesViewSet(viewsets.ModelViewSet):
    queryset = Countries.objects.all()
    serializer_class = CountriesSerializer
    permission_classes = [permissions.IsAuthenticated]

class EmployeesViewSet(viewsets.ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer
    permission_classes = [permissions.IsAuthenticated]

class StatesOrProvincesViewSet(viewsets.ModelViewSet):
    queryset = StatesOrProvinces.objects.all()
    serializer_class = StatesOrProvincesSerializer
    permission_classes = [permissions.IsAuthenticated]

class LocationsViewSet(viewsets.ModelViewSet):
    queryset = Locations.objects.all()
    serializer_class = LocationsSerializer
    permission_classes = [permissions.IsAuthenticated]

class CurrenciesViewSet(viewsets.ModelViewSet):
    queryset = Currencies.objects.all()
    serializer_class = CurrenciesSerializer
    permission_classes = [permissions.IsAuthenticated]

class HealthInsurancesViewSet(viewsets.ModelViewSet):
    queryset = HealthInsurances.objects.all()
    serializer_class = HealthInsurancesSerializer
    permission_classes = [permissions.IsAuthenticated]

class JobFamiliesViewSet(viewsets.ModelViewSet):
    queryset = JobFamilies.objects.all()
    serializer_class = JobFamiliesSerializer
    permission_classes = [permissions.IsAuthenticated]

class JobPositionsViewSet(viewsets.ModelViewSet):
    queryset = JobPositions.objects.all()
    serializer_class = JobPositionsSerializer
    permission_classes = [permissions.IsAuthenticated]

class BusinessUnitsViewSet(viewsets.ModelViewSet):
    queryset = BusinessUnits.objects.all()
    serializer_class = BusinessUnitsSerializer
    permission_classes = [permissions.IsAuthenticated]

class CostCentersViewSet(viewsets.ModelViewSet):
    queryset = CostCenters.objects.all()
    serializer_class = CostCentersSerializer
    permission_classes = [permissions.IsAuthenticated]

class InternalOrdersViewSet(viewsets.ModelViewSet):
    queryset = InternalOrders.objects.all()
    serializer_class = InternalOrdersSerializer
    permission_classes = [permissions.IsAuthenticated]

class PayGroupsViewSet(viewsets.ModelViewSet):
    queryset = PayGroups.objects.all()
    serializer_class = PayGroupsSerializer
    permission_classes = [permissions.IsAuthenticated]

class UnionSubgroupsViewSet(viewsets.ModelViewSet):
    queryset = UnionSubgroups.objects.all()
    serializer_class = UnionSubgroupsSerializer
    permission_classes = [permissions.IsAuthenticated]

class WorkScheduledViewSet(viewsets.ModelViewSet):
    queryset = WorkScheduled.objects.all()
    serializer_class = WorkScheduledSerializer
    permission_classes = [permissions.IsAuthenticated]