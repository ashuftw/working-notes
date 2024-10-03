import os
import re
from datetime import datetime

def update_frontmatter(filename):
    # Extract date and title from filename
    match = re.match(r'(\d{6})\s(.+)\.md', filename)
    if not match:
        print(f"Skipping {filename}: doesn't match expected format")
        return

    date_str, title = match.groups()
    date = datetime.strptime(date_str, '%y%m%d').strftime('%Y-%m-%d')

    # Read the file content
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()

    # Check if front matter exists
    front_matter_pattern = re.compile(r'^---\s*\n(.*?)\n---\s*\n', re.DOTALL)
    front_matter_match = front_matter_pattern.match(content)

    new_front_matter = f"""---
title: {title}
draft: false
date: {date}
---

"""

    if front_matter_match:
        # Update existing front matter
        updated_content = front_matter_pattern.sub(new_front_matter, content)
    else:
        # Add new front matter
        updated_content = new_front_matter + content

    # Write updated content back to file
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(updated_content)

    print(f"Updated {filename}")

# Process all .md files in the current directory
for filename in os.listdir('.'):
    if filename.endswith('.md'):
        update_frontmatter(filename)
