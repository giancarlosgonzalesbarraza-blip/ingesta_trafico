
import requests
import json

GEOPORTAL = "https://geoportal.valencia.es/server/rest/services/OPENDATA"
url = f"{GEOPORTAL}/Trafico/MapServer/188/query"
params = {"where": "1=1", "outFields": "*", "f": "json"}

resp = requests.get(url, params=params, timeout=60)
resp.raise_for_status()

registros = [f["attributes"] for f in resp.json()["features"]]

with open("trafico_raw.json", "w", encoding="utf-8") as archivo:
    json.dump(registros, archivo, ensure_ascii=False, indent=2)


