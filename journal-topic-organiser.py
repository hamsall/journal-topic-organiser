import re
import os
from datetime import datetime
from tkinter import Tk, filedialog

def extract_sections(input_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    section_dict = {}
    current_heading = None
    current_content = []

    for line in lines:
        match_heading = re.match(r'^---\s*([A-Za-z0-9\s]+)\s*---$', line.strip())
        if match_heading:
            if current_heading is not None:
                section_dict[current_heading] = current_content.copy()
            current_heading = match_heading.group(1).strip().rstrip(':')
            current_content = []
        elif current_heading is not None:
            current_content.append(line.rstrip())

    # Capture the last section
    if current_heading is not None and current_content:
        section_dict[current_heading] = current_content.copy()

    return section_dict

def get_files_in_date_range(folder_path, start_date, end_date):
    files = []
    for root, dirs, filenames in os.walk(folder_path):
        for filename in filenames:
            if filename.endswith('.txt'):  # Adjust file extension if needed
                file_path = os.path.join(root, filename)
                creation_date_str = get_file_creation_date(file_path)
                try:
                    creation_date = datetime.strptime(creation_date_str, "%d%m%y")
                    if start_date <= creation_date <= end_date:
                        files.append(file_path)
                except ValueError:
                    # Skip files that don't match the expected date format
                    continue
    return files

def get_file_creation_date(file_path):
    # Extract the last 6 digits of the file name
    file_name = os.path.basename(file_path)
    creation_date = file_name[-10:-4]
    return creation_date

def write_sections(output_folder, sections, creation_date):
    for heading, content_lines in sections.items():
        filename = f'{heading.lower().replace(" ", "_")}.txt'
        output_file_path = os.path.join(output_folder, filename)

        # Create a unique heading for this entry
        unique_heading = f'---{heading}{creation_date}---'

        if os.path.exists(output_file_path):
            with open(output_file_path, 'r+') as file:
                content = file.read()
                if unique_heading not in content:
                    file.seek(0, 2)  # Move to the end of the file
                    file.write(f'\n\n{unique_heading}\n')
                    file.write('\n'.join(content_lines))
        else:
            # File does not exist, create a new file with the heading
            with open(output_file_path, 'w') as file:
                file.write(f'{unique_heading}\n')
                file.write('\n'.join(content_lines))

if __name__ == "__main__":
    # Use Tkinter to select the input folder path interactively
    root = Tk()
    root.withdraw()
    input_folder_path = filedialog.askdirectory(title="Select Input Folder")
    root.destroy()

    output_folder_path = 'quests'

    if not os.path.exists(output_folder_path):
        os.makedirs(output_folder_path)

    # Define date range
    end_date = datetime(2024, 9, 12)
    start_date = datetime(2024, 7, 1)

    # Get files within the date range
    input_file_paths = get_files_in_date_range(input_folder_path, start_date, end_date)

    for input_file_path in input_file_paths:
        sections = extract_sections(input_file_path)
        creation_date = get_file_creation_date(input_file_path)
        write_sections(output_folder_path, sections, creation_date)

    print(f"Processed {len(input_file_paths)} files.")