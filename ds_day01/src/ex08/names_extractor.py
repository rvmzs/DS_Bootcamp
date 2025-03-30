import sys

def extract_names(email):
    local_part, domain = email.split('@')
    name, surname = local_part.split('.')
    name = name.capitalize()
    surname = surname.capitalize()
    return name, surname, email

def process_file(input_file, output_file):
    with open(input_file, 'r') as infile:
        emails = infile.readlines()

    with open(output_file, 'w') as outfile:
        outfile.write("Name\tSurname\tE-mail\n")
        for email in emails:
            email = email.strip()
            if email:
                name, surname, email = extract_names(email)
                outfile.write(f"{name}\t{surname}\t{email}\n")

def main():
    if len(sys.argv) != 2:
        raise Exception("Invalid number of arguments")

    input_file = sys.argv[1]
    output_file = 'employees.tsv'

    process_file(input_file, output_file)

if __name__ == "__main__":
    main()
