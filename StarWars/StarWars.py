import swapi

import json


def getCharacterInfo():
    name = input("Enter the Name of a Star Wars Character.....From a Galaxy Far Far Away!: ")
    query = "https://swapi.co/api/people/?search=" + name
    result = swapi.swapi.all_resource_urls(query)
    if len(result) < 1:
        print("The Force is Not With You.... Please Enter Another Name")
    return result

def getID(url):
    n = len(url)
    id = url[28:n-1]
    return id

def characterInfo(character):
    print("Name: ", character.name, '\n')
    print("Birth Year: ", character.birth_year, '\n')
    print("Eye Color: ", character.eye_color, '\n')
    print("Gender: ", character.gender, '\n')
    print("Hair Color: ", character.hair_color, '\n')
    print("Height: ", character.height, "centimeters", '\n')
    print("Weight: ", character.mass, 'kilos ', '\n')



result = getCharacterInfo()
#Get the ID from the URl
id = getID(result[0])
id = int(id)
character = swapi.get_person(id)
characterInfo(character)
spec = character.get_species()
for sp in spec.iter():
    print(sp.name)
    print()
Home = character.get_homeworld()
print("Home World: ", Home.name, "\n")
print("StarShips: ")
starShips = character.get_starships()
for s in starShips.iter():
    print(s.name)
    print()
print("Vehicles: ")
vehicles = character.get_vehicles()
for v in vehicles.iter():
    print(v.name)
    print()
print("Films: ")
films = character.get_films()
for f in films.iter():
    print(f.title)






