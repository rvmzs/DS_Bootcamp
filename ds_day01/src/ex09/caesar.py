import sys

def caesar_cipher(text, shift, encode=True):
    result = []
    for char in text:
        if not char.isascii():
            raise Exception("The script does not support your language yet.")
        if char.isalpha(): 
            if char.islower():
                base = ord('a')
            else:
                base = ord('A')

            if encode:
                new_char = chr((ord(char) - base + shift) % 26 + base)
            else:
                new_char = chr((ord(char) - base - shift) % 26 + base)

            result.append(new_char)
        else:
            result.append(char)  

    return ''.join(result)

def main():
    if len(sys.argv) != 4:
        raise Exception("Invalid number of arguments")

    action = sys.argv[1]
    text = sys.argv[2]
    shift = int(sys.argv[3])

    if action == 'encode':
        encoded_text = caesar_cipher(text, shift, encode=True)
        print(encoded_text)
    elif action == 'decode':
        decoded_text = caesar_cipher(text, shift, encode=False)
        print(decoded_text)
    else:
        raise Exception("Invalid action. Use 'encode' or 'decode'.")

if __name__ == "__main__":
    main()
