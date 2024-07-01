def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f'The file at {file_path} was not found.')

if __name__ == "__main__":
    file_path = 'example.txt'  # Substitua pelo caminho do seu arquivo
    read_file(file_path)
