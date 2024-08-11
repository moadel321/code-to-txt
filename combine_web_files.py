import os

def combine_web_files(root_dir, output_file):
    """
    Combine all PHP, JS, CSS, HTML, Python, Ruby, Java, C/C++, C#, Swift, Go, Perl, TypeScript,
    Shell Scripts, XML, JSON, and YAML files from the given directory and its subdirectories
    into a single output file.

    Args:
    root_dir (str): The root directory to start searching for files
    output_file (str): The name of the file where all contents will be written
    """
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for root, dirs, files in os.walk(root_dir):
            for file in files:
                # Check if the file has one of the desired extensions
                if file.endswith(('.php', '.js', '.css', '.html', '.htm', '.py', 
                                  '.rb', '.java', '.c', '.cpp', '.h', '.cs', 
                                  '.swift', '.go', '.pl', '.pm', '.ts', 
                                  '.sh', '.bash', '.xml', '.json', '.yaml', '.yml')):
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r', encoding='utf-8') as infile:
                        # Write file path and content to the output file
                        outfile.write(f"File: {file_path}\n\n")
                        outfile.write(infile.read())
                        # Add a separator between files
                        outfile.write("\n\n" + "="*80 + "\n\n")

def main():
    """
    Main function to get user input and initiate the file combination process.
    """
    # Get input from user
    root_directory = input("Enter the root directory path: ")
    output_file = input("Enter the output file name (including .txt extension): ")
    
    # Combine the files
    combine_web_files(root_directory, output_file)
    
    # Confirm operation completion
    print(f"All relevant files have been combined into {output_file}")

# Ensure that main() is only called if the script is run directly
if __name__ == "__main__":
    main()
