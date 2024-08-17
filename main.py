def count_words(file_path):
    with open(file_path) as f:
        files_contents = f.read()
        words = files_contents.split()
        counter = 0
        for word in words:
            counter += 1
        return counter

def count_characters(file_path):
    alphabet_counter = {
        'a': 0,
        'b': 0,
        'c': 0,
        'd': 0,
        'e': 0,
        'f': 0,
        'g': 0,
        'h': 0,
        'i': 0,
        'j': 0,
        'k': 0,
        'l': 0,
        'm': 0,
        'n': 0,
        'o': 0,
        'p': 0,
        'q': 0,
        'r': 0,
        's': 0,
        't': 0,
        'u': 0,
        'v': 0,
        'w': 0,
        'x': 0,
        'y': 0,
        'z': 0,
        }

    alphabet = [
        'a',
        'b',
        'c',
        'd',
        'e',
        'f',
        'g',
        'h',
        'i',
        'j',
        'k',
        'l',
        'm',
        'n',
        'o',
        'p',
        'q',
        'r',
        's',
        't',
        'u',
        'v',
        'w',
        'x',
        'y',
        'z',
    ]

    with open(file_path) as f:
        files_contents = f.read().lower()
        for i in range(0, len(files_contents)):
            for char in alphabet:
                if char == files_contents[i]:
                    alphabet_counter[char] += 1 

        for i in range(0, len(alphabet)):
            print(f"The {alphabet[i]} character was found {alphabet_counter[alphabet[i]]} times")

def main():
    # file_path = "books/frankenstein.txt"
    while True:
        print("--- Choose option: ---")
        print("1. File text report.")
        print("2. Exit.")
        user_input = input()
        if user_input == '2':
            break
        elif user_input == '1':
            try: 
                file_path = input("Enter file path:")
                
                with open(file_path) as f:
                    files_contents = f.read()
                    print(files_contents)
                
                    print(f"--- Begin report of {file_path} ---")
                    print(f"{count_words(file_path)} words found in the document")
                    count_characters(file_path)
                    print("--- End report ---")
                    print("File path not found.")
            except Exception:
                print("File path not found.")
                print(" ")
        else:
            print("Invalid input. Please enter one of the option numbers.")
            print(" ")
                


main()