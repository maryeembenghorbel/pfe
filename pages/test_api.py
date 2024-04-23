from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Asset, RecommendationRec, RecommendationVulnerability, Reporting, Role, Scan, ScanResult, User, Vulnerability
from .serializers import AssetSerializer, RecommendationRecSerializer, RecommendationVulnerabilitySerializer, ReportingSerializer, RoleSerializer, ScanSerializer, ScanResultSerializer, UserSerializer, VulnerabilitySerializer

class AssetViewSetTestCase(APITestCase):
    def setUp(self):
        self.asset1 = Asset.objects.create(ip_address="192.168.1.1", host_name="host1", os="Linux", asset_type="Server", last_scan_date="2023-04-01")
        self.asset2 = Asset.objects.create(ip_address="192.168.1.2", host_name="host2", os="Windows", asset_type="Workstation", last_scan_date="2023-04-02")

    def test_list_assets(self):
        url = reverse('asset-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.data
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]['ip_address'], self.asset1.ip_address)
        self.assertEqual(data[1]['ip_address'], self.asset2.ip_address)

    def test_create_asset(self):
        url = reverse('asset-list')
        data = {'ip_address': '192.168.1.3', 'host_name': 'host3', 'os': 'Linux', 'asset_type': 'Server', 'last_scan_date': '2023-04-03'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Asset.objects.count(), 3)

    # Ajoutez d'autres méthodes de test pour d'autres vues...

class RecommendationRecViewSetTestCase(APITestCase):
    def setUp(self):
        self.recommendation_rec1 = RecommendationRec.objects.create(action_description="Action 1", status="Pending")
        self.recommendation_rec2 = RecommendationRec.objects.create(action_description="Action 2", status="Approved")

    def test_list_recommendation_recs(self):
        url = reverse('recommendationrec-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.data
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]['action_description'], self.recommendation_rec1.action_description)
        self.assertEqual(data[1]['action_description'], self.recommendation_rec2.action_description)

    # Ajoutez d'autres méthodes de test pour d'autres vues...

# Ajoutez des classes de test pour d'autres vues de votre API...

