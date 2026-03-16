import os

# Create _personalities folder if it doesn't exist
os.makedirs("_personalities", exist_ok=True)

# Read names.txt (one name per line)
with open("_data/names.txt", "r", encoding="utf-8") as f:
    names = [line.strip() for line in f if line.strip()]

# Read personality.txt – blocks separated by "\n\n---\n\n"
with open("_data/personality.txt", "r", encoding="utf-8") as f:
    content = f.read()
    # Split on the separator used in the Colab output
    personalities = [p.strip() for p in content.split("\n\n---\n\n") if p.strip()]

# Verify counts match
if len(names) != len(personalities):
    raise ValueError(
        f"❌ Count mismatch: names.txt has {len(names)} entries, "
        f"personality.txt has {len(personalities)} entries. "
        "Both files must have the same number of entries."
    )

print(f"✅ Found {len(names)} entries. Generating pages...")

for name, personality in zip(names, personalities):
    # Create a safe filename slug
    # Remove any characters that are not alphanumeric or space, then replace spaces with hyphens
    slug = ''.join(c for c in name if c.isalnum() or c.isspace()).rstrip()
    slug = slug.replace(" ", "-").lower()
    # Fallback if slug becomes empty
    if not slug:
        slug = "character"

    filename = f"_personalities/{slug}.md"

    # Indent every line of the personality text by two spaces
    indented_personality = "\n".join("  " + line for line in personality.split("\n"))

    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"""---
name: "{name}"
personality: |
{indented_personality}
---
""")

print(f"✅ Generated {len(names)} personality pages in _personalities/")
