import os
import re
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_line_indentation(line):
    """Get the indentation (tabs and spaces) from the beginning of a line"""
    match = re.match(r'^(\s*)', line)
    return match.group(1) if match else ''

def is_in_list_context(lines, equation_line_index):
    """Check if the equation is within a list item context and return the appropriate indentation"""
    # Look backwards from the equation to find the most recent list item
    for i in range(equation_line_index - 1, -1, -1):
        line = lines[i].strip()
        
        # Skip empty lines
        if not line:
            continue
            
        # Check if this line is a list item (-, *, +, or numbered)
        if re.match(r'^(\s*)[-*+]\s', lines[i]) or re.match(r'^(\s*)\d+\.\s', lines[i]):
            # Get the indentation of the list item
            list_indentation = get_line_indentation(lines[i])
            # Add one level of indentation (tab) for the content within the list item
            return list_indentation + '\t'
        
        # If we hit a line that starts at the beginning (no indentation) and is not empty,
        # we've likely left the list context
        if not get_line_indentation(lines[i]):
            break
    
    return ''

def format_equations(content):
    lines = content.split('\n')
    result_lines = []
    i = 0
    
    while i < len(lines):
        line = lines[i]
        
        # Check for inline equations ($$...$$) that should be converted to block format
        inline_pattern = r'\$\$(.*?)\$\$'
        match = re.search(inline_pattern, line)
        
        if match:
            equation = match.group(1).strip()
            
            # Check if this equation is in a list context
            indentation = is_in_list_context(lines, i)
            
            # Split the line into parts before and after the equation
            before_eq = line[:match.start()]
            after_eq = line[match.end():]
            
            # Add the part before the equation (if any)
            if before_eq.strip():
                result_lines.append(before_eq.rstrip())
            
            # Add the formatted block equation with proper indentation
            result_lines.append('')  # Empty line before equation
            result_lines.append(f'{indentation}$$')
            result_lines.append(f'{indentation}{equation}')
            result_lines.append(f'{indentation}$$')
            result_lines.append('')  # Empty line after equation
            
            # Add the part after the equation (if any)
            if after_eq.strip():
                result_lines.append(indentation + after_eq.lstrip())
        else:
            # Check for multi-line equations that span multiple lines
            if line.strip() == '$$':
                # Found start of block equation, check if it needs indentation
                indentation = is_in_list_context(lines, i)
                
                if indentation:
                    # Apply indentation to the equation block
                    result_lines.append('')  # Empty line before
                    result_lines.append(f'{indentation}$$')
                    i += 1
                    
                    # Process equation content until closing $$
                    while i < len(lines) and lines[i].strip() != '$$':
                        equation_line = lines[i]
                        # If the equation line has content, apply indentation
                        if equation_line.strip():
                            result_lines.append(f'{indentation}{equation_line.strip()}')
                        else:
                            result_lines.append('')
                        i += 1
                    
                    # Add closing $$ with indentation
                    if i < len(lines):
                        result_lines.append(f'{indentation}$$')
                    result_lines.append('')  # Empty line after
                else:
                    # No indentation needed, keep as is
                    result_lines.append(line)
            else:
                # Regular line, keep as is
                result_lines.append(line)
        
        i += 1
    
    return '\n'.join(result_lines)

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
