import os
import re

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    return re.sub(r'[-\s]+', '-', text).strip('-')

# Paths
names_file = '_data/names.txt'
personality_file = '_data/personality.txt'
output_dir = '_personalities'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

with open(names_file, 'r', encoding='utf-8') as f:
    names = [line.strip() for line in f if line.strip()]

# Split by the triple dash separator
with open(personality_file, 'r', encoding='utf-8') as f:
    content_list = f.read().split('---')

for i, name in enumerate(names):
    if i < len(content_list):
        slug = slugify(name)
        file_name = f"{slug}.md"
        
        # CLEANING: Remove extra whitespace from the text
        body_text = content_list[i].strip()
        
        # CORRECT STRUCTURE: 
        # 1. Front Matter (Metadata)
        # 2. Closing dashes
        # 3. Actual Body Content
        full_file_content = (
            f"---\n"
            f"layout: personality\n"
            f"title: \"{name}\"\n"
            f"description: \"Explore the detailed psychological traits and personality analysis of {name}.\"\n"
            f"---\n\n" # This second '---' ends the metadata
            f"{body_text}" # This is the "Content" Jekyll will display
        )
        
        with open(os.path.join(output_dir, file_name), 'w', encoding='utf-8') as f:
            f.write(full_file_content)

print(f"Fixed! Generated {len(names)} pages with visible content.")
# After reading names from _data/names.txt, add these lines:
with open("_data/names.txt", "r", encoding="utf-8") as f:
    names = [line.strip() for line in f if line.strip()]

# --- NEW: Clean up name formatting ---
cleaned_names = []
for name in names:
    # Replace " And " with " and " (standardize)
    name = name.replace(" And ", " and ")
    # Optional: remove any extra spaces
    name = " ".join(name.split())
    cleaned_names.append(name)
