import json

cities = {
    "Kolkata": 15000000,
    "Delhi": 32000000,
    "Mumbai": 21000000
}

with open("cities.json", "w") as f:
    json.dump(cities, f, indent=4)

with open("cities.json", "r") as f:
    cities = json.load(f)

print("Cities and their population:")
for city, population in cities.items():
    print(city, ":", population)

new_city = input("\nEnter a new city: ")
new_population = int(input("Enter its population: "))

cities[new_city] = new_population

with open("cities.json", "w") as f:
    json.dump(cities, f, indent=4)

print("\nUpdated cities:")
for city, population in cities.items():
    print(city, ":", population)