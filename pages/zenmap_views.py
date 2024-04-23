from rest_framework.views import APIView
from rest_framework.response import Response
import subprocess

class ZenmapScanView(APIView):
    def post(self, request):
        ip_address = request.data.get('ip_address')
        if not ip_address:
            return Response({'error': 'Please provide an IP address'}, status=400)

        # Exécute le scan avec Zenmap
        try:
            output = subprocess.run(['zenmap', '-T4', '-F', ip_address], capture_output=True, text=True)
            # Récupère les résultats du scan à partir de output.stdout
            scan_results = output.stdout
            return Response({'scan_results': scan_results})
        except Exception as e:
            return Response({'error': str(e)}, status=500)