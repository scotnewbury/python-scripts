import os
import argparse

def append_file(directory, filename, text):
    # Create the directory if it does not exist
    os.makedirs(directory, exist_ok=True)
    
    # Define the full path of the file
    file_path = os.path.join(directory, filename)
    
    # Write the text to the file
    with open(file_path, 'a+') as file:
        file.write(text)
    
    print(f"Text was appended to file '{filename}' in directory '{directory}'.")

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Create a file with specific text in a specified directory.")
    parser.add_argument("directory", type=str, help="The directory where the file will be appended.")
    parser.add_argument("filename", type=str, help="The name of the file to be appended.")
    parser.add_argument("text", type=str, help="The text to appended to the file.")
    
    # Parse arguments
    args = parser.parse_args()
    
    # Call the function with the parsed arguments
    append_file(args.directory, args.filename, args.text)

if __name__ == "__main__":
    main()
