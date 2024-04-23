import requests

# Remplacez les valeurs suivantes par vos clés d'API et l'URL de votre instance Nessus Essentials
ACCESS_KEY = "ab73bd41c94fad3a6d8beb6dc27008dc5ee4c1664504a92d02ec977251734f28"
SECRET_KEY = "5706ffbedfc18e1c110947a7f31a9be8455e00591973189810c89d54ab29f148"
NESSUS_URL = "https://192.168.110.138:8834"

def get_scans_in_progress():
    endpoint = f"{NESSUS_URL}/scans"
    headers = {
        "X-ApiKeys": f'accessKey="{ACCESS_KEY}"; secretKey="{SECRET_KEY}"',
        "Content-Type": "application/json"
    }
    try:
        response = requests.get(endpoint, headers=headers)
        if response.status_code == 200:
            scans = response.json()["scans"]
            return scans
        else:
            print(f"Erreur lors de la récupération des scans : {response.status_code}")
            return None
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
        return None

# Exemple d'utilisation
if __name__ == "__main__":
    scans = get_scans_in_progress()
    if scans:
        print("Scans en cours :")
        for scan in scans:
            print(f"- {scan['name']}")
    else:
        print("Aucun scan en cours.")
