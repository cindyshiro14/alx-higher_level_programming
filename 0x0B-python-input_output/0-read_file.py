def read_file(filename=""):
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')

# For testing purposes
if __name__ == "__main__":
    read_file("my_file_0.txt")
