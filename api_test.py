
import requests
from requests.structures import CaseInsensitiveDict

url = "http://127.0.0.1:5000/predict"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/json"

data = """
{
  "data": {
    "MedInc": 1.6812,
    "HouseAge": 25.0,
    "AveBedrms": 1.022284,
    "Population": 1392.0,
    "AveOccup": 3.877437,
    "Latitude": 36.06,
    "Longitude": -119.01
  }
}
"""


resp = requests.post(url, headers=headers, data=data)
print(resp)


# print(resp.content)