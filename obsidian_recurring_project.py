import os
import argparse

def create_file(directory, filename, project_to_add):
    
    # Create the directory if it does not exist
    os.makedirs(directory, exist_ok=True)

    # Project files are all templates stored in the Resources/Template direcory
    # Open the file for processing

    template_directory = "/home/scot/mylife/03 - Resources/templates/"
    project_template = os.path.join(template_directory, project_to_add)
    project = open(project_template, 'r')

    # Define the full path of the file
    file_path = os.path.join(directory, filename)

    # Write the text to the file
    with open(file_path, 'w') as file:
        file.write(project.read())
    
    print(f"File '{filename}' created in directory '{directory}' with the provided text.")
    project.close()

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Create a file with specific text in a specified directory.")
    parser.add_argument("directory", type=str, help="The directory where the file will be created.")
    parser.add_argument("filename", type=str, help="The name of the file to be created.")
    parser.add_argument("project_to_add", type=str, help="The text to include in the file.")
    
    # Parse arguments
    args = parser.parse_args()
    
    # Call the function with the parsed arguments
    create_file(args.directory, args.filename, args.project_to_add)

if __name__ == "__main__":
    main()