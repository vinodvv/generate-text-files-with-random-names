import random
import string


def generate_random_text(length):
    """Generates a random string of specified length."""
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))


def create_new_file():
    """Creates a new text file with a random name and writes random name as text."""
    random_name = generate_random_text(10)
    file_name = f"files/{random_name}.txt"

    with open(file_name, "w") as file:
        random_text = random_name
        file.write(random_text)

    print(f"New file created: {file_name}")


if __name__ == "__main__":
    create_new_file()
