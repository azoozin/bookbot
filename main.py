def main():
    with open("books/frankenstein.txt") as f:
        files_contents = f.read()
        print(files_contents)

main()