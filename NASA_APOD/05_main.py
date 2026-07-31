import requests
import datetime
import random

def response(x):
    complete_URL = base_url + "?" + "api_key=" + api_key + "&date=" + x
    response = requests.get(complete_URL)
    if response.status_code == 200:
        print("Success! Here's your data")
        data = response.json()
        title = data["title"]
        url = data["url"]
        exp = data["explanation"]
        return{"Title": title,
                "url": url,
                "Explanation": exp,
                "Date": x}
        
    elif response.status_code == 404:
        print("Not found!")
        return None
    elif response.status_code == 403:
        print("Permission denied (bad API key)")
        return None
    elif response.status_code == 500:
        print("Server error!")
        return None
    else:
        print("Error!")
        return None

base_url = "https://api.nasa.gov/planetary/apod"
api_key = "IXf4s7VBJj9r8ISB8HwCKJpm5s5JNooRhvDv3w1X"

choice = True
while choice == True:
    print("1. Get Today's APOD\n2. Search by Date\n3. Random Date\n4. View Saved Favorites\n5. Save Current to Favorites\n6. Exit")

    option = int(input("Enter your Choice: "))
    match option:
        case 1:
            today = datetime.date.today()
            date = str(today)
            current_apod = response(date)
            print(current_apod)
        case 2:
            date = input("Enter date (YYYY-MM-DD): ")
            current_apod = response(date)
            print(current_apod)
        case 3:
            start_date = "1995-06-16"
            end_date = datetime.date.today()

            date_object1 = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
            date_object2 = end_date

            total_days = date_object2 - date_object1

            ran_days = random.randint(0, total_days.days)
            from datetime import timedelta
            ran_date = str(date_object1 + timedelta(ran_days))

            current_apod = response(ran_date)
            print(current_apod)
        case 4:
            try:
                f = open("NASA_APOD/favourite.txt", "r")
                view = f.read()
                f.close()
            except FileNotFoundError:
                print("No favorites saved yet!")
            else:
                if view == "":
                    print("No favorites saved yet!")
                else:
                    blocks = view.split("---")
                    favourites_list = []

                    for block in blocks:
                        if len(block.strip()) > 10:
                            lines = block.split("\n")
                            title = ""
                            url = ""
                            date = ""
                            explanation = ""

                            for line in lines:
                                if ":" in line:
                                    key, value = line.split(":", 1)

                                    key = key.strip()
                                    value = value.strip()

                                    if key == "Title":
                                        title = value
                                    elif key == "URL":
                                        url = value
                                    elif key == "Date":
                                        date = value
                                    elif key == "Explanation":
                                        explanation = value

                            favourite = {
                                "title": title,
                                "url": url,
                                "date": date,
                                "explanation": explanation
                            }
                            if favourite["title"] != "":
                                favourites_list.append(favourite)
                    for index, fav in enumerate(favourites_list):
                        number = index + 1
                        print(f"{number}. {fav['title']} - {fav['date']}")
                        print(f"   URL: {fav['url']}")
                        print(f"   Explanation: {fav['explanation']}")
                        print("-" * 50)

        case 5:
            if 'current_apod' not in locals() or current_apod is None:
                print("Please fetch an APOD first (cases 1-3)!")
            else:
                title = current_apod["Title"]
                url = current_apod["url"]
                date = current_apod["Date"]
                explanation = current_apod["Explanation"]

                formatted_data = f"""Title: {title}
URL: {url}
Date: {date}
Explanation: {explanation}
---
"""

                f = open("NASA_APOD/favourite.txt", "a")
                new_data = f.write(formatted_data)
                f.close()

                print("Saved successfully...")

        case 6 :
            print("Have a nice day!")
            choice = False
        case _:
            print("Enter 1 to 6 only...")
