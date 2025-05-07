from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'tenants', views.TenantViewSet)
router.register(r'companies', views.CompaniesViewSet)
router.register(r'countries', views.CountriesViewSet)
router.register(r'employees', views.EmployeesViewSet)
router.register(r'states-provinces', views.StatesOrProvincesViewSet)
router.register(r'locations', views.LocationsViewSet)
router.register(r'currencies', views.CurrenciesViewSet)
router.register(r'health-insurances', views.HealthInsurancesViewSet)
router.register(r'job-families', views.JobFamiliesViewSet)
router.register(r'job-positions', views.JobPositionsViewSet)
router.register(r'business-units', views.BusinessUnitsViewSet)
router.register(r'cost-centers', views.CostCentersViewSet)
router.register(r'internal-orders', views.InternalOrdersViewSet)
router.register(r'pay-groups', views.PayGroupsViewSet)
router.register(r'union-subgroups', views.UnionSubgroupsViewSet)
router.register(r'work-scheduled', views.WorkScheduledViewSet)

urlpatterns = [
    path('', include(router.urls)),
]