import sys

def find_name_by_email(email, file_path):
    with open(file_path, 'r') as file:
        for line in file:
            if email in line:
                name, surname, _ = line.strip().split('\t')
                return name
    return None

def generate_letter(name):
    return (f"Dear {name}, welcome to our team. We are sure that it will be a pleasure to work with "
            f"you. That’s a precondition for the professionals that our company hires.")

def main():
    if len(sys.argv) != 3:
        raise Exception("Invalid number of arguments")

    email = sys.argv[1]
    file_path = sys.argv[2]

    name = find_name_by_email(email, file_path)
    if name:
        letter = generate_letter(name)
        print(letter)
    else:
        print(f"Email {email} not found in the file.")

if __name__ == "__main__":
    main()
