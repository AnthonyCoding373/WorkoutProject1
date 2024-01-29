import sys

def get_original_content(original_file):
    """Retrieves the files contents, returns list of file lines"""
    try:
        lines = []
        with open(original_file, "r") as file:
            contents = file.readlines()
        for row in contents:
            lines.append(row)
        return lines.copy()
    except FileNotFoundError as fe:
        print(f"{fe}: File Not Found Error, ensure the file's name is inputted properly")
    except UnicodeDecodeError as ude:
        print(f"{ude}: File type cannot be read")

def encrypt_data(lines):
    '''Reverses the lines and returns it as a list'''
    encrypted_lines = []
    for line in lines:
        line_stripped = line.strip("\n")
        reversed_line = line_stripped[::-1] + "\n"
        encrypted_lines.append(reversed_line)
    return encrypted_lines.copy()


def write_to_encrypted(encrypted_file, encrypted_contents):
    '''Writes the reversed lines to the encrypted file'''
    try:
        with open(encrypted_file, "w") as file:
            file.writelines(encrypted_contents)
    except:
        print("An error has occured")


def main():
    original_file = sys.argv[1]
    encrypted_file = sys.argv[2]
    contents = get_original_content(original_file)
    encrypted_contents = encrypt_data(contents)
    write_to_encrypted(encrypted_file, encrypted_contents)
    

if __name__ == "__main__":
    main()