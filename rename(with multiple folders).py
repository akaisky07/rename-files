import os

parent_directory = "data"

# Get the list of folders in the parent directory
folders = os.listdir(parent_directory)

# Iterate through each folder
for folder_name in folders:
    folder_path = os.path.join(parent_directory, folder_name)
    
    # Check if the path is a directory
    if os.path.isdir(folder_path):
        # Get the list of PDF files in the folder
        pdf_files = [file for file in os.listdir(folder_path) ]
        
        # Rename each PDF file in the folder
        for i, pdf_file in enumerate(pdf_files):
            old_file_path = os.path.join(folder_path, pdf_file)
            new_file_name = f"{folder_name}-{i+1}.pdf"
            new_file_path = os.path.join(folder_path, new_file_name)
            
            # Rename the file
            os.rename(old_file_path, new_file_path)
            
            # Print the renamed file path
            print(f"Renamed: {new_file_path}")

