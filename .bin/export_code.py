import os
from datetime import datetime
import pyperclip  # Add this import for clipboard operations

def get_language_from_extension(filename):
    """Determine language based on file extension"""
    extension_map = {
        '.py': 'python',
        '.js': 'javascript',
        '.ts': 'typescript',
        '.tsx': 'typescript',
        '.json': 'json',
        '.html': 'html',
        '.css': 'css',
        '.cpp': 'cpp',
        '.c': 'c',
        '.java': 'java',
        '.sh': 'bash',
        '.md': 'markdown',
        '.sql': 'sql',
        '.xml': 'xml',
        '.yaml': 'yaml',
        '.yml': 'yaml',
        '.txt': 'text',
        '.ini': 'ini',
        '.conf': 'conf',
        '.php': 'php',
        '.rb': 'ruby',
        '.go': 'go',
        '.rs': 'rust'
    }
    
    _, ext = os.path.splitext(filename.lower())
    return extension_map.get(ext, '')

def list_directory_contents(path, f, clipboard_content, level=1, ignore_list=None):
    """Recursively list contents of a directory"""
    try:
        items = sorted(os.listdir(path))
        for item in items:
            if ignore_list and (item in ignore_list or os.path.join(path, item) in ignore_list):
                continue
                
            if item.lower().endswith('.md') or item == os.path.basename(__file__):
                continue
                
            item_path = os.path.join(path, item)
            header_marks = '#' * (level + 1)
            
            if os.path.isfile(item_path):
                file_time = os.path.getmtime(item_path)
                modified_time = datetime.fromtimestamp(file_time).strftime('%Y-%m-%d %H:%M:%S')
                
                content = f"{header_marks}# 📄 {item}\n\n* Last Modified : `{modified_time}`\n\n"
                f.write(content)
                clipboard_content.append(content)
                
                try:
                    with open(item_path, 'r', encoding='utf-8') as content_file:
                        file_content = content_file.read()
                        if file_content.strip():
                            language = get_language_from_extension(item)
                            code_block = f"```{language}\n{file_content}\n```\n\n"
                            f.write(code_block)
                            clipboard_content.append(code_block)
                except Exception as e:
                    error_msg = f"> ⚠️ Unable To Read File Contents : {str(e)}\n\n"
                    f.write(error_msg)
                    clipboard_content.append(error_msg)
            
            elif os.path.isdir(item_path):
                dir_content = f"{header_marks} 📁 {item}/\n\n"
                f.write(dir_content)
                clipboard_content.append(dir_content)
                list_directory_contents(item_path, f, clipboard_content, level + 1, ignore_list)
                f.write("---\n\n")
                clipboard_content.append("---\n\n")

    except PermissionError:
        error_msg = "> ⚠️ Permission Denied To Access Some Contents\n\n"
        f.write(error_msg)
        clipboard_content.append(error_msg)
    except Exception as e:
        error_msg = f"> ⚠️ Error Accessing Contents: {str(e)}\n\n"
        f.write(error_msg)
        clipboard_content.append(error_msg)

def create_directory_report(ignore_list=None):
    """Generate directory report and copy to clipboard"""
    current_path = os.getcwd()
    output_file = ".bin/directory_report.md"
    clipboard_content = []  # List to store content for clipboard
    
    with open(output_file, 'w', encoding='utf-8') as f:
        # Write header
        header = "# 📁 Directory Structure Report\n\n"
        header += "## 📌 Overview\n\n"
        header += f"* **Base Directory :** `{current_path}`\n"
        header += f"* **Report Generated :** `{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}`\n\n"
        header += "---\n\n"
        header += "## 📂 Directory Structure\n\n"
        
        f.write(header)
        clipboard_content.append(header)
        
        items = sorted(os.listdir(current_path))
        for item in items:
            if ignore_list and (item in ignore_list or os.path.join(current_path, item) in ignore_list):
                continue
                
            if item.lower() == "raw models" or item.lower().endswith('.md') or item == os.path.basename(__file__):
                continue
                
            item_path = os.path.join(current_path, item)
            if os.path.isdir(item_path):
                dir_content = f"## 📁 {item}/\n\n"
                f.write(dir_content)
                clipboard_content.append(dir_content)
                list_directory_contents(item_path, f, clipboard_content, 2, ignore_list)
                f.write("---\n\n")
                clipboard_content.append("---\n\n")
            else:
                file_time = os.path.getmtime(item_path)
                modified_time = datetime.fromtimestamp(file_time).strftime('%Y-%m-%d %H:%M:%S')
                
                content = f"## 📄 {item}\n\n* Last Modified : `{modified_time}`\n\n"
                f.write(content)
                clipboard_content.append(content)
                
                try:
                    with open(item_path, 'r', encoding='utf-8') as content_file:
                        file_content = content_file.read()
                        if file_content.strip():
                            language = get_language_from_extension(item)
                            code_block = f"```{language}\n{file_content}\n```\n\n"
                            f.write(code_block)
                            clipboard_content.append(code_block)
                except Exception as e:
                    error_msg = f"> ⚠️ Unable To Read File Contents : {str(e)}\n\n"
                    f.write(error_msg)
                    clipboard_content.append(error_msg)
                f.write("---\n\n")
                clipboard_content.append("---\n\n")

    # Copy entire content to clipboard
    try:
        pyperclip.copy(''.join(clipboard_content))
        print("Content Copied To Clipboard! 📋")
    except Exception as e:
        print(f"Failed To copy To Clipboard : {str(e)}")

    print(f"Directory Report Has Been Generated : {output_file}")
    print("Report Generated Auccessfully! ✨")

if __name__ == "__main__":
    ignore_list = ['.git', '.gitignore', 'logs', '__pycache__', '.env', "venv", ".bin", "assets"]
    create_directory_report(ignore_list)