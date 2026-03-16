import os

# Create _personalities folder if it doesn't exist
os.makedirs("_personalities", exist_ok=True)

# Read data files (UTF‑8 without BOM)
with open("_data/names.txt", "r", encoding="utf-8") as f:
    names = [line.strip() for line in f if line.strip()]

with open("_data/personality.txt", "r", encoding="utf-8") as f:
    # Personality file may contain paragraphs separated by '---'
    content = f.read()
    personalities = [p.strip() for p in content.split("\n\n---\n\n") if p.strip()]

# Ensure same number of entries
if len(names) != len(personalities):
    raise ValueError(f"Count mismatch: {len(names)} names, {len(personalities)} personalities")

# Generate one markdown file per character
for name, personality in zip(names, personalities):
    # Create a filename-safe slug
    slug = name.lower().replace(" ", "-").replace("'", "").replace(".", "")
    filename = f"_personalities/{slug}.md"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"""---
name: "{name}"
personality: |
{personality}
---

<!-- Additional content can go here if needed -->
""")

print(f"✅ Generated {len(names)} personality pages.")
