# Portfolio Project #3: Star Catalog Explorer

# What it does: Browse famous stars, search, sort by brightness/distance, explore constellations

# How it works:

# Create database of 10 stars with properties:
# Name, coordinates, magnitude, distance, constellation
# Show menu with options
# Depending on choice:
# List all: Loop through all stars, print in order by magnitude
# Search: Get search term, loop through stars, print matches
# Sort by brightness: Sort list by magnitude, print
# Sort by distance: Sort list by distance, print
# Find by constellation: Get constellation name, find stars in it
# For each operation, format output nicely with columns/alignment
# Loop menu until exit

# Data structure:

# Use dictionary for each star (name as key, properties as values)
# Or list of dictionaries

# Key Concepts:

# Complex dictionaries
# Sorting with sorted() and lambda
# String searching with .lower() and "in"
# Enumeration with enumerate()
# Table formatting

stars_data = [
    {
        "Name": "Sirius",
        "Magnitude": -1.46,
        "Distance": 8.6,
        "Constellation": "Canis Major" 
    },
    {
        "Name": "Betelgeuse",
        "Magnitude": 0.50,
        "Distance": 640,
        "Constellation": "Orion" 
    },
    {
        "Name": "Canopus",
        "Magnitude": -0.74,
        "Distance": 310,
        "Constellation": "Carnia" 
    },
    {
        "Name": "Vega",
        "Magnitude": 0.03,
        "Distance": 25,
        "Constellation": "Lyra" 
    },
    {
        "Name": "R136A1",
        "Magnitude": -12.6,
        "Distance": 160000,
        "Constellation": "Dorado"
    },
    {
        "Name": "Capella",
        "Magnitude": 0.08,
        "Distance": 43,
        "Constellation": "Auriga" 
    },
    {
        "Name": "Altair",
        "Magnitude": 0.76,
        "Distance": 17,
        "Constellation": "Aquila" 
    },
    {
        "Name": "Rigel",
        "Magnitude": 0.18,
        "Distance": 860,
        "Constellation": "Orion" 
    },
    {
        "Name": "Procyon",
        "Magnitude": 0.40,
        "Distance": 11.4,
        "Constellation": "Canis Minor" 
    },
    {
        "Name": "Arcturus",
        "Magnitude": -0.04,
        "Distance": 37,
        "Constellation": "Bootes" 
    }
]

choice = True
while choice == True:
    print("1. List all stars.\n2. Search by name\n3. Sort by brightness(magnitude)\n4. Sort by distance\n5. Find by constellation\n6. Exit")
    option = int(input("Enter your choice(1-6): "))

    match option:
        case 1:
            for star in stars_data:
                print(star["Name"], star["Magnitude"], star["Distance"], star["Constellation"])
                print("." * 10)
            print("-*" * 20)

        case 2:
            star_name = input("Enter Star name: ")
            found = False
            for star in stars_data:
                if star_name.lower() == star["Name"].lower():
                    print(star["Name"], star["Magnitude"], star["Distance"], star["Constellation"])
                    print("." * 10)
                    found = True
                    break
            if not found:
                print("No Information...")
            print("-*" * 20)
                
        case 3:
            sorted_list = sorted(stars_data, key= lambda stars : stars["Magnitude"])
            for star in sorted_list:
                print(star["Name"], star["Magnitude"], star["Distance"], star["Constellation"])
                print("." * 10)
            print("-*" * 20)

        case 4:
            sorted_list = sorted(stars_data, key= lambda star : star["Distance"])
            for star in sorted_list:
                print(star["Name"], star["Magnitude"], star["Distance"], star["Constellation"])
                print("." * 10)
            print("-*"*20)

        case 5:
            const_name = input("Enter Constellation name: ")
            found = False
            for const in stars_data:
                if const_name.lower() == const["Constellation"].lower():
                    print(const["Name"], const["Magnitude"], const["Distance"], const["Constellation"])
                    found = True
                    print("." * 10)
            if not found:
                print("No Information...")
            print("-*"*20)
        case 6:
            choice = False
            print("Exiting Loop, Have a nice day!")