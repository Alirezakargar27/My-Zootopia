import data_fetcher

def serialize_animal(animal):
    """Serializes a single animal to an HTML string."""
    name = animal.get("name", "Unknown")
    diet = animal.get("characteristics", {}).get("diet", "Unknown")
    locations = animal.get("locations", ["Unknown"])
    animal_type = animal.get("characteristics", {}).get("type", "Unknown")

    return f"""
    <li class="cards__item">
        <div class="card__title">{name}</div>
        <p class="card__text">
            <strong>Location:</strong> {locations[0]}<br/>
            <strong>Type:</strong> {animal_type}<br/>
            <strong>Diet:</strong> {diet}<br/>
        </p>
    </li>
    """

def generate_animal_info_html(animals_data):
    """Generates a string with the animal information in HTML format."""
    return ''.join(serialize_animal(animal) for animal in animals_data)

def generate_html_content(template_path, animal_info_html):
    """Generates the final HTML content by replacing the placeholder."""
    with open(template_path, 'r') as file:
        template_content = file.read()
    return template_content.replace('__REPLACE_ANIMALS_INFO__', animal_info_html)

def save_html(content, file_path):
    """Saves the given content to a file."""
    with open(file_path, "w") as file:
        file.write(content)

def main():
    """Main function to load data, generate HTML content, and save it."""
    # Ask the user for an animal name
    animal_name = input("Enter a name of an animal: ")

    # Fetch data from the API using data_fetcher
    animals_data = data_fetcher.fetch_data(animal_name)

    # Check if the API returned no animals or if the response contains an error
    if not animals_data or len(animals_data) == 0:
        animal_info_html = f"<h2>The animal \"{animal_name}\" doesn't exist.</h2>"
    else:
        # Generate animal info string in HTML format
        animal_info_html = generate_animal_info_html(animals_data)

    # Generate HTML content
    html_content = generate_html_content('animals_template.html', animal_info_html)

    # Save the HTML content to a file
    save_html(html_content, 'animals.html')
    print("Website was successfully generated to the file animals.html.")

if __name__ == "__main__":
    main()