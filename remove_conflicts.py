import re
import os

def remove_merge_conflicts_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()

        # Define the regex pattern to remove merge conflict markers and their content
        pattern = re.compile(r'<<<<<<< HEAD.*?=======.*?>>>>>>> \w+', re.DOTALL)
        cleaned_content = re.sub(pattern, '', content)

        with open(file_path, 'w') as file:
            file.write(cleaned_content)
        print(f"Cleaned conflicts in {file_path}")

    except PermissionError:
        print(f"PermissionError: {file_path}")
    except Exception as e:
        print(f"An error occurred with {file_path}: {e}")

def process_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):  # Process only Python files
                file_path = os.path.join(root, file)
                remove_merge_conflicts_from_file(file_path)

# Path to your project directory
project_directory = 'C:/Users/enyoh/traveblo-online-main'
process_directory(project_directory)
