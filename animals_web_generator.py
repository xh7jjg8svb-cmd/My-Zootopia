import json

def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)

def print_animal_info(animals):
    """Prints selected information about each animal"""
    for animal in animals:
        print("------")
        # Name
        if "name" in animal:
            print(f"Name: {animal['name']}")

        # Ernährung (diet)
        diet = animal.get("characteristics", {}).get("diet")
        if diet:
            print(f"Ernährung: {diet}")

        # Erster Ort
        locations = animal.get("locations")
        if locations and len(locations) > 0:
            print(f"Ort: {locations[0]}")

        # Typ
        animal_type = animal.get("characteristics", {}).get("type")
        if animal_type:
            print(f"Typ: {animal_type}")

def main():
    """Main function"""
    file_path = "animals_data.json"
    animals = load_data(file_path)
    print_animal_info(animals)

if __name__ == "__main__":
    main()
