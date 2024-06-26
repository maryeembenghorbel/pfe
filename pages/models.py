from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser
import hashlib,base64


class Asset(models.Model):
    asset_id = models.AutoField(primary_key=True)
    ip_address = models.CharField(max_length=255)
    host_name = models.CharField(max_length=255)
    os = models.CharField(max_length=255)
    asset_type = models.CharField(max_length=255)
    last_scan_date = models.DateTimeField()

class RecommendationRec(models.Model):
    recommendationrec_id = models.AutoField(primary_key=True)
    action_description = models.CharField(max_length=255)
    status = models.CharField(max_length=45)
    vulnerabilities = models.ManyToManyField('Vulnerability', through='RecommendationVulnerability')

class RecommendationVulnerability(models.Model):
    recommendation_rec = models.ForeignKey(RecommendationRec, on_delete=models.CASCADE)
    vulnerability = models.ForeignKey('Vulnerability', on_delete=models.CASCADE)

class Reporting(models.Model):
    report_id = models.AutoField(primary_key=True)
    creation_time = models.DateTimeField()
    scanrslt_id = models.ForeignKey('ScanResult', on_delete=models.CASCADE)

class Role(models.Model):
    role_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=45)

class Scan(models.Model):
    scan_id = models.AutoField(primary_key=True)
    scan_type = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    scanner_used = models.CharField(max_length=255)
    asset = models.ForeignKey('Asset', on_delete=models.CASCADE)

class ScanResult(models.Model):
    scanrslt_id = models.AutoField(primary_key=True)
    scan = models.ForeignKey('Scan', on_delete=models.CASCADE)
    asset = models.ForeignKey('Asset', on_delete=models.CASCADE)
    vulnerability = models.ForeignKey('Vulnerability', on_delete=models.CASCADE)
    result_time = models.DateTimeField()



class User(models.Model):
    # Assuming user_id is the primary key and auto-generated by the database
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=100)
    role = models.ForeignKey('Role', on_delete=models.CASCADE)

    def __str__(self):
        return self.user_name
        
    #def hashed_password(self):
        # Hash the password using a secure hash algorithm (e.g., SHA-256)
        #return hashlib.sha256(self.password.encode()).hexdigest()
        
class Vulnerability(models.Model):
    vulnerability_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    severity = models.CharField(max_length=255)
    cvss_score = models.DecimalField(max_digits=4, decimal_places=2)
    
    def __str__(self):
        return self.name
    
    



