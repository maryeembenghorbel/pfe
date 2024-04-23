from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import AssetViewSet, RecommendationRecViewSet, RecommendationVulnerabilityViewSet, ReportingViewSet, RoleViewSet, ScanViewSet, ScanResultViewSet, UserViewSet, VulnerabilityViewSet

#  un routeur par défaut
router = DefaultRouter()

# Enregistrer les ViewSets avec le routeur
router.register(r'assets', AssetViewSet)
router.register(r'recommendations', RecommendationRecViewSet)
router.register(r'recommendation_vulnerabilities', RecommendationVulnerabilityViewSet)
router.register(r'reportings', ReportingViewSet)
router.register(r'roles', RoleViewSet)
router.register(r'scans', ScanViewSet)
router.register(r'scan_results', ScanResultViewSet)
router.register(r'users', UserViewSet)
router.register(r'vulnerabilities', VulnerabilityViewSet)

# Définir les URLs de votre API
urlpatterns = [
    path('', include(router.urls)),
]
