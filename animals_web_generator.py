import data_fetcher


def serialize_animal(animal_obj):
    """
    Convert a single animal dictionary into an HTML <li> string.
    """
    lines = ["<li class=\"cards__item\">"]

    # Name
    name = animal_obj.get("name", "")
    lines.append(f"  <div class=\"card__title\">{name}</div>")

    # Details block
    lines.append("  <p class=\"card__text\">")

    # Diet
    diet = animal_obj.get("characteristics", {}).get("diet")
    if diet:
        lines.append(f"      <strong>Diet:</strong> {diet}<br/>")

    # Location (first in list)
    locations = animal_obj.get("locations", [])
    if locations:
        lines.append(f"      <strong>Location:</strong> {locations[0]}<br/>")

    # Type
    animal_type = animal_obj.get("characteristics", {}).get("type")
    if animal_type:
        lines.append(f"      <strong>Type:</strong> {animal_type}<br/>")

    lines.append("  </p>")
    lines.append("</li>")

    return "\n".join(lines)


def serialize_all_animals(data):
    """
    Convert a list of animal dictionaries into a full HTML <ul> block.
    """
    items = [serialize_animal(animal) for animal in data]
    return "<ul class=\"cards\">\n" + "\n".join(items) + "\n</ul>"


def generate_html(template_path, output_path, animals_data, animal_name):
    """
    Read template, replace placeholder, and write output file.
    """
    with open(template_path, "r", encoding="utf-8") as file:
        template_content = file.read()

    # If no data, show a friendly message instead of animal cards
    if not animals_data:
        animals_html = f"""
        <div style="text-align:center; margin-top:50px;">
            <h2 style="color:#b22222;">The animal "{animal_name}" doesn't exist 🦓❌</h2>
            <p style="color:#555;">Try searching for something else, like <em>Fox</em> or <em>Tiger</em>.</p>
        </div>
        """
    else:
        animals_html = serialize_all_animals(animals_data)

    final_html = template_content.replace("__REPLACE_ANIMALS_INFO__", animals_html)

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(final_html)


def main():
    # Ask user for animal name
    animal_name = input("Enter a name of an animal: ").strip()

    print(f"Fetching data for '{animal_name}' from API...")
    data = data_fetcher.fetch_data(animal_name)

    generate_html(
        template_path="animals_template.html",
        output_path="animals.html",
        animals_data=data,
        animal_name=animal_name,
    )

    print("✅ Website was successfully generated to the file animals.html.")


if __name__ == "__main__":
    main()
