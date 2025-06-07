import os
import re

def center_images(directory):
    # Regular expression to match Markdown image links
    image_pattern = r'!\[\[(.+?)\|(\d+)\]\]'
    
    # Walk through all files in the directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                
                # Read the content of the file
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Function to replace matches
                def replace_match(match):
                    full_match = match.group(0)
                    if 'center' in full_match:
                        return full_match  # Already centered, no change
                    else:
                        return f'![[{match.group(1)}|center|{match.group(2)}]]'
                
                # Replace image links
                new_content = re.sub(image_pattern, replace_match, content)
                
                # Write the modified content back to the file
                if new_content != content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Updated: {file_path}")

# Use the current directory
current_directory = '.'
center_images(current_directory)
