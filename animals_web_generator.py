import json


def load_data(file_path):
    """
    Load JSON data from a file.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


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


def generate_html(template_path, output_path, animals_data):
    """
    Read template, replace placeholder, and write output file.
    """
    with open(template_path, "r", encoding="utf-8") as file:
        template_content = file.read()

    animals_html = serialize_all_animals(animals_data)
    final_html = template_content.replace("__REPLACE_ANIMALS_INFO__", animals_html)

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(final_html)


def main():
    data = load_data("animals_data.json")
    generate_html(
        template_path="animals_template.html",
        output_path="animals.html",
        animals_data=data,
    )
    print("✅ animals.html successfully generated!")


if __name__ == "__main__":
    main()
