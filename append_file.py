import os
import argparse

def append_file(directory, filename, text_to_add):
    # Create the directory if it does not exist
    os.makedirs(directory, exist_ok=True)
    
    # Define the full path of the file to be appended
    file_path = os.path.join(directory, filename)

    # Define the full path of the source file of text to be added
    # append_path = os.path.join(directory, filename)
    
    append_text = open(text_to_add, 'r')

    # Write the text to the file
    with open(file_path, 'a+') as file:
        file.write(append_text.read())
    
    print(f"Text was appended to file '{filename}' in directory '{directory}'.")

    append_text.close()

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Create a file with specific text in a specified directory.")
    parser.add_argument("directory", type=str, help="The directory where the file will be appended.")
    parser.add_argument("filename", type=str, help="The name of the file to be appended.")
    parser.add_argument("text_to_add", type=str, help="The file containing text to appended to the file.")
    
    # Parse arguments
    args = parser.parse_args()
    
    # Call the function with the parsed arguments
    append_file(args.directory, args.filename, args.text_to_add)

if __name__ == "__main__":
    main()
