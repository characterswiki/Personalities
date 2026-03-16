import os

os.makedirs("_personalities", exist_ok=True)

with open("_data/names.txt", "r", encoding="utf-8") as f:
    names = [line.strip() for line in f if line.strip()]

with open("_data/personality.txt", "r", encoding="utf-8") as f:
    content = f.read()
    personalities = [p.strip() for p in content.split("\n\n---\n\n") if p.strip()]

if len(names) != len(personalities):
    raise ValueError(f"Count mismatch: {len(names)} names, {len(personalities)} personalities")

for name, personality in zip(names, personalities):
    slug = name.lower().replace(" ", "-").replace("'", "").replace(".", "")
    filename = f"_personalities/{slug}.md"

    # Indent each line of the personality text
    indented_personality = "\n".join("  " + line for line in personality.split("\n"))

    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"""---
name: "{name}"
personality: |
{indented_personality}
---
""")

print(f"✅ Generated {len(names)} personality pages.")
