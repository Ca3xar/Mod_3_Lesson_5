import os 


def list_directory_contents(path):
    try:
        if not os.path.isdir(path):
            print(f"The path '{path}' is not a valid directory.")
            return
        print(f"Contents of '{path}':\n")
        for entry in os.listdir(path):
            entry_path = os.path.join(path, entry)

            if os.path.isdir(entry_path):
                print(f"[DIR] {entry}")
            else:
                print(f"[FILE] {entry}")

    except FileNotFoundError:
        print(f"The directory '{path}' does not exist.")
    except PermissionError:
        print(f"Permission denied to access the directory '{path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    path = input("enter the directory path: ").strip()
    list_directory_contents(path)

if __name__ == "__main__":
    main() 