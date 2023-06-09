
import requests
from requests.structures import CaseInsensitiveDict

url = "https://californiahousepriceprediction.herokuapp.com/predict_api"

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


print(resp.content)