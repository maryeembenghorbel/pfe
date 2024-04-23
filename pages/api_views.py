from rest_framework import viewsets
from .models import Asset, RecommendationRec, RecommendationVulnerability, Reporting, Role, Scan, ScanResult, User, Vulnerability
from .serializers import AssetSerializer, RecommendationRecSerializer, RecommendationVulnerabilitySerializer, ReportingSerializer, RoleSerializer, ScanSerializer, ScanResultSerializer, UserSerializer, VulnerabilitySerializer

class AssetViewSet(viewsets.ModelViewSet):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer

class RecommendationRecViewSet(viewsets.ModelViewSet):
    queryset = RecommendationRec.objects.all()
    serializer_class = RecommendationRecSerializer

class RecommendationVulnerabilityViewSet(viewsets.ModelViewSet):
    queryset = RecommendationVulnerability.objects.all()
    serializer_class = RecommendationVulnerabilitySerializer

class ReportingViewSet(viewsets.ModelViewSet):
    queryset = Reporting.objects.all()
    serializer_class = ReportingSerializer

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class ScanViewSet(viewsets.ModelViewSet):
    queryset = Scan.objects.all()
    serializer_class = ScanSerializer

class ScanResultViewSet(viewsets.ModelViewSet):
    queryset = ScanResult.objects.all()
    serializer_class = ScanResultSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class VulnerabilityViewSet(viewsets.ModelViewSet):
    queryset = Vulnerability.objects.all()
    serializer_class = VulnerabilitySerializer
