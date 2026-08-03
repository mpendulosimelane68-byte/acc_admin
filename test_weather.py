import requests

response = requests.get("https://wttr.in/Manzini?format=j1")

data = response.json()

print(data["current_condition"][0]["temp_C"])
print(data["current_condition"][0]["weatherDesc"][0]["value"])