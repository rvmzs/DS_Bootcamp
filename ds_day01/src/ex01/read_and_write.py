def read_csv(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines

def write_tsv(file_path, lines):
    with open(file_path, 'w') as file:
        for line in lines:
            new_line = ''
            in_quotes = False
            for c in line:
                if c == '"':
                    in_quotes = not in_quotes
                if c == ',' and not in_quotes:
                    new_line += '\t'
                else:
                    new_line += c
            file.write(new_line)

def main():
    input_file = 'ds.csv'
    output_file = 'ds.tsv'

    lines = read_csv(input_file)
    write_tsv(output_file, lines)

if __name__ == "__main__":
    main()
