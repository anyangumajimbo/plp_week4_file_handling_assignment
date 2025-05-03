import os

def read_and_modify_file():
    filename = input("Enter the filename to read from: ").strip()

    # Check if the filename is empty
    if not filename:
        print("Error: No filename provided.")
        return

    # Add a default extension if none is provided
    if not os.path.splitext(filename)[1]:
        filename += ".txt"

    try:
        # Check if the file exists before opening
        if not os.path.exists(filename):
            print(f"Error: The file '{filename}' does not exist.")
            return

        with open(filename, 'r') as infile:
            content = infile.read()
            modified_content = content.upper()  # Modify as needed

        new_filename = "modified_" + os.path.basename(filename)
        with open(new_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"Modified content has been written to '{new_filename}'.")

    except IOError as e:
        print(f"Error: An I/O error occurred: {e}")

if __name__ == "__main__":
    read_and_modify_file()