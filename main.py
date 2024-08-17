def count_words(file_path):
    with open(file_path) as f:
        files_contents = f.read()
        words = files_contents.split()
        counter = 0
        for word in words:
            counter += 1
        return counter


def main():
    file_path = "books/frankenstein.txt"
    with open(file_path) as f:
        files_contents = f.read()
        print(files_contents)
    
    print(f" Word count: {count_words(file_path)}")


main()