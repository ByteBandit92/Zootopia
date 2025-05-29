import json


def load_data(file_path):
    """Loads a JSON file and returns the data."""
    with open(file_path, "r") as handle:
        return json.load(handle)


def serialize_animal(animal_obj):
    """Serializes a single animal object into an HTML list item."""
    lines = ['<li class="cards__item">']

    # Title (Name)
    if 'name' in animal_obj:
        lines.append(f'  <div class="card__title">{animal_obj["name"]}</div>')

    # Characteristics
    characteristics = animal_obj.get('characteristics', {})
    locations = animal_obj.get('locations', [])

    lines.append('  <p class="card__text">')
    if 'diet' in characteristics:
        lines.append(f'    <strong>Diet:</strong> {characteristics["diet"]}<br/>')
    if locations:
        lines.append(f'    <strong>Location:</strong> {locations[0]}<br/>')
    if 'type' in characteristics:
        lines.append(f'    <strong>Type:</strong> {characteristics["type"]}<br/>')
    lines.append('  </p>')

    lines.append('</li>')
    return '\n'.join(lines) + '\n'



def main():
    # Load the animal data
    try:
      animals_data = load_data('animals_data.json')
    except:
      print("Could not load animals_data.json")

    # Load the HTML template
    with open('animals_template.html', 'r') as template_file:
        template_content = template_file.read()

    # Generate the HTML for all animals
    animals_html = ''
    for animal in animals_data:
        animals_html += serialize_animal(animal)

    # Replace the placeholder with the animals HTML
    new_html_content = template_content.replace('__REPLACE_ANIMALS_INFO__', animals_html)

    # Write the final HTML to a file
    with open('animals.html', 'w') as output_file:
        output_file.write(new_html_content)

    print("✅ animals.html created")


if __name__ == "__main__":
    main()
