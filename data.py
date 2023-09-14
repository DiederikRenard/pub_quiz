import requests

PARAMETERS = {
    "amount": 20,
    "type": "boolean",
}
response = requests.get("https://opentdb.com/api.php?", params=PARAMETERS)
response.raise_for_status()

questions = response.json()


question_data = questions["results"]
