import os
import re
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def format_equations(content):
    # Regular expression to match equations
    pattern = r'\$\$(.*?)\$\$'
    
    def repl(match):
        equation = match.group(1).strip()
        return f'\n$$\n{equation}\n$$\n'
    
    # Replace inline equations with block equations
    formatted_content = re.sub(pattern, repl, content, flags=re.DOTALL)
    return formatted_content

def process_markdown_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        formatted_content = format_equations(content)
        
        if content != formatted_content:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(formatted_content)
            logging.info(f"Updated: {file_path}")
        else:
            logging.info(f"No changes needed: {file_path}")
    except Exception as e:
        logging.error(f"Error processing {file_path}: {str(e)}")

def process_current_directory():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    logging.info(f"Processing Markdown files in: {current_dir}")
    
    for file in os.listdir(current_dir):
        if file.endswith('.md'):
            file_path = os.path.join(current_dir, file)
            process_markdown_file(file_path)

if __name__ == "__main__":
    logging.info("Starting to process Markdown files in the current directory.")
    process_current_directory()
    logging.info("Finished processing all Markdown files.")
