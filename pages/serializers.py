from rest_framework import serializers
from .models import Asset, RecommendationRec, RecommendationVulnerability, Reporting, Role, Scan, ScanResult, User, Vulnerability

class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = ['asset_id', 'ip_address', 'host_name', 'os', 'asset_type', 'last_scan_date']

class RecommendationRecSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecommendationRec
        fields = ['recommendationrec_id', 'action_description', 'status', 'vulnerabilities']

class RecommendationVulnerabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = RecommendationVulnerability
        fields = ['recommendation_rec', 'vulnerability']

class ReportingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reporting
        fields = ['report_id', 'creation_time', 'scanrslt_id']

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['role_id', 'description']

class ScanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scan
        fields = ['scan_id', 'scan_type', 'start_time', 'end_time', 'scanner_used', 'asset']

class ScanResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScanResult
        fields = ['scanrslt_id', 'scan', 'asset', 'vulnerability', 'result_time']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'user_name', 'email', 'password', 'role']

class VulnerabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vulnerability
        fields = ['vulnerability_id', 'name', 'description', 'severity', 'cvss_score']

