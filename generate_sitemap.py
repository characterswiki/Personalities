import os
from datetime import datetime

# Configuration
BASE_URL = "https://personalitytraits.vercel.app"
PERSONALITIES_DIR = "_personalities"
OUTPUT_FILE = "sitemap.xml"
TODAY = datetime.now().strftime("%Y-%m-%d")

# Start XML
sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n'
sitemap += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'

# Add homepage
sitemap += f"""  <url>
    <loc>{BASE_URL}/</loc>
    <lastmod>{TODAY}</lastmod>
    <changefreq>daily</changefreq>
    <priority>1.0</priority>
  </url>
"""

# Add about and privacy (if they exist)
for page in ["about", "privacy"]:
    sitemap += f"""  <url>
    <loc>{BASE_URL}/{page}</loc>
    <lastmod>{TODAY}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.5</priority>
  </url>
"""

# Add each character page
if os.path.exists(PERSONALITIES_DIR):
    for filename in os.listdir(PERSONALITIES_DIR):
        if filename.endswith(".md"):
            # Remove .md extension to get slug
            slug = filename[:-3]
            sitemap += f"""  <url>
    <loc>{BASE_URL}/{slug}</loc>
    <lastmod>{TODAY}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
"""

sitemap += "</urlset>"

# Write to file
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(sitemap)

print(f"✅ Generated sitemap with {sitemap.count('<url>')} URLs in {OUTPUT_FILE}")
