import os
import re

workspace_dir = r"c:\Users\Admin\Desktop\meclix2"

files_to_update = [
    "index.css",
    "index.html",
    "about.html",
    "lockers.html",
    "keyknox.html",
    "it-lockers.html",
    "visitor-lockers.html",
    "tool-lockers.html",
    "server-racks.html",
    "premise-workplace.html",
    "plant-maintenance.html",
    "software.html"
]

print("Starting Barlow -> Poppins font migration...")

for filename in files_to_update:
    filepath = os.path.join(workspace_dir, filename)
    if not os.path.exists(filepath):
        print(f"File not found: {filename}")
        continue
        
    print(f"Processing: {filename}")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # 1. Replace Google Fonts imports/links
    # Replace URL-encoded or regular Barlow with Poppins in font URLs
    content = content.replace("Barlow:wght@300;400;500;600;700;800;900", "Poppins:wght@300;400;500;600;700;800;900")
    content = content.replace("Barlow%3A300%2C400%2C500%2C600%2C700%2C800", "Poppins%3A300%2C400%2C500%2C600%2C700%2C800")
    content = content.replace("family=Barlow", "family=Poppins")
    
    # 2. Replace CSS variable definitions
    content = content.replace("Barlow, sans-serif", "Poppins, sans-serif")
    content = content.replace("'Barlow', sans-serif", "'Poppins', sans-serif")
    content = content.replace('"Barlow", sans-serif', '"Poppins", sans-serif')
    
    # 3. Replace direct font-family declarations
    content = content.replace("font-family: Barlow;", "font-family: Poppins;")
    content = content.replace("font-family: 'Barlow';", "font-family: 'Poppins';")
    content = content.replace('font-family: "Barlow";', 'font-family: "Poppins";')
    content = content.replace("font-family:Barlow;", "font-family:Poppins;")
    
    # Case-insensitive general replacement for style block edge cases if any
    content = re.sub(r'font-family:\s*Barlow\b', 'font-family: Poppins', content, flags=re.IGNORECASE)
    content = re.sub(r'font-family:\s*[\'"]Barlow[\'"]\b', 'font-family: \'Poppins\'', content, flags=re.IGNORECASE)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Font migration completed successfully!")
