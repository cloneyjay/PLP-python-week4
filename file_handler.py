try:
    # Get filename from user
    filename = input("Enter the input filename: ")
    
    # Try to open and read the file
    with open(filename, 'r') as input_file:
        content = input_file.read()
    
    # Process the content (convert to uppercase)
    modified_content = content.upper()
    
    # Create output filename
    output_file = 'modified_' + filename
    
    # Write modified content to new file
    with open(output_file, 'w') as output_file:
        output_file.write(modified_content)
        
    print(f"Successfully created {output_file} with modified content.")
except IOError:
    print(f"Error: Could not read the file '{input_file}'.")
    
except FileNotFoundError:
    print(f"Error: The file '{input_file}' was not found.")
except PermissionError:
    print("Error: Permission denied to access the file.")
except Exception as e:
    print(f"An unexpected error occurred: {str(e)}")


