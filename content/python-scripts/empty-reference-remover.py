import re
import os
import shutil

def clean_markdown(content):
    # Pattern to match reference sections (including variations of "References")
    # Includes optional horizontal rule before or after the section
    reference_pattern = r'(?:^|\n)(?:---\s*\n)?#+\s*References?.*?(?:\n---)?(?=\n#+|\Z)'
    
    # Function to check if a reference section is empty
    def is_empty_section(section):
        # Remove the header, horizontal rules, and check if the remaining content is just whitespace
        content = re.sub(r'(---\s*\n)?(#+\s*References?.*?\n)(.*?)(\n---)?', r'\3', section, flags=re.IGNORECASE | re.DOTALL)
        return not content.strip()

    # Find all reference sections
    reference_sections = re.finditer(reference_pattern, content, re.DOTALL | re.IGNORECASE)

    # Remove empty reference sections
    for section in reversed(list(reference_sections)):
        if is_empty_section(section.group()):
            content = content[:section.start()] + content[section.end():]

    return content

def process_markdown_files():
    # Get all Markdown files in the current directory
    markdown_files = [f for f in os.listdir('.') if f.endswith('.md')]

    for file_name in markdown_files:
        file_path = file_name
        temp_file_path = 'temp_' + file_name

        # Read the content of the file
        with open(file_path, 'r') as file:
            content = file.read()

        # Clean the content
        cleaned_content = clean_markdown(content)

        # Write the cleaned content to a temporary file
        with open(temp_file_path, 'w') as file:
            file.write(cleaned_content)

        # Replace the original file with the cleaned version
        shutil.move(temp_file_path, file_path)

        print(f"Processed and updated: {file_name}")

# Run the script
if __name__ == "__main__":
    process_markdown_files()
