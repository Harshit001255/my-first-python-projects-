import requests
import datetime

base_url = "https://api.nasa.gov/planetary/apod"
api_key = "IXf4s7VBJj9r8ISB8HwCKJpm5s5JNooRhvDv3w1X"

date = input("Enter date (YYYY-MM-DD) or press enter for today: ")
if date == "":
    today = datetime.date.today()
    date = str(today)

complete_URL = base_url + "?" + "api_key=" + api_key + "&date=" + date
print(complete_URL)

response = requests.get(complete_URL)
if response.status_code == 200:
    print("Success! Here's your data")
    data = response.json()
    title = data["title"]
    url = data["url"]
    exp = data["explanation"]
    print(title)
    print(url)
    print(exp)
elif response.status_code == 404:
    print("Not found!")
elif response.status_code == 403:
    print("Permission denied (bad API key)")
elif response.status_code == 500:
    print("Server error!")
else:
    print("Error!")
