"""
Beautiful Soup Cheat Sheet (Python)
Comprehensive overview of common classes, methods, and usage patterns.
Run this file or copy snippets as needed.
"""

from bs4 import BeautifulSoup

html_doc = """
<html>
  <head><title>The Dormouse's story</title></head>
  <body>
    <p class="title"><b>The Dormouse's story</b></p>
    <p class="story">Once upon a time there were three little sisters;
      <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
      <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
      <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    </p>
    <p class="story">...</p>
  </body>
</html>
"""

# -----------------------------
# 1. PARSING HTML
# -----------------------------
soup = BeautifulSoup(html_doc, "html.parser")  # Other parsers: "lxml", "html5lib"

# -----------------------------
# 2. BASIC ACCESSORS
# -----------------------------
print(soup.title)                      # <title>The Dormouse's story</title>
print(soup.title.text)                # The Dormouse's story
print(soup.p)                         # First <p> tag
print(soup.a)                         # First <a> tag
print(soup.find('p'))                 # First p
print(soup.find_all('p'))             # List of all p tags

# -----------------------------
# 3. FINDING TAGS
# -----------------------------
# find(name, attrs, recursive, text, **kwargs)
# find_all(name, attrs, limit, **kwargs)

print(soup.find('a', {"id": "link2"}))              # Find by attributes
print(soup.find_all('a', class_="sister"))          # Find all with class
print(soup.find('a').get('href'))                    # Get attribute

# Using CSS selectors
print(soup.select('p.story'))                        # All <p class="story">
print(soup.select_one('a#link1'))                    # Specific element

# -----------------------------
# 4. ACCESS TAG ATTRIBUTES
# -----------------------------
tag = soup.a
print(tag['href'])               # Access attribute
print(tag.get('class'))          # Access class list
print(tag.get('id'))             # Access id

# -----------------------------
# 5. MODIFYING THE TREE
# -----------------------------
tag['href'] = "http://new-url.com"    # Modify attribute
tag['newAttr'] = "value"               # Add attribute

del tag['newAttr']                     # Delete attribute

tag.string = "Updated Text"           # Replace tag text

# -----------------------------
# 6. NAVIGATION
# -----------------------------
# .parent, .parents, .children, .descendants, .next_sibling, .previous_sibling

print(soup.a.parent.name)                     # Parent tag name
for child in soup.body.children:
    print(child)

for desc in soup.body.descendants:
    print(desc)

print(soup.a.next_sibling)                    # Next sibling

# -----------------------------
# 7. STRIPPING TEXT
# -----------------------------
print(soup.get_text())                # Extract all text from document

# -----------------------------
# 8. CREATING & INSERTING TAGS
# -----------------------------
new_tag = soup.new_tag('a', href='http://added.com')
new_tag.string = "Added Link"
soup.body.append(new_tag)             # Insert at end

soup.body.insert(1, new_tag)          # Insert by index

# -----------------------------
# 9. DECOMPOSE, EXTRACT, CLEAR
# -----------------------------
t = soup.find('p', class_='title')
t.extract()                            # Remove and return

# remove completely (no return)
# t.decompose()

# clear contents of a tag
# t.clear()

# -----------------------------
# 10. PRETTIFY OUTPUT
# -----------------------------
print(soup.prettify())

# -----------------------------
# 11. COMMON PATTERNS
# -----------------------------
# Extract all links
links = [a['href'] for a in soup.find_all('a', href=True)]
print(links)

# Extract text of all <p> tags
texts = [p.get_text(strip=True) for p in soup.find_all('p')]
print(texts)

# Find by multiple attributes
print(soup.find('a', {"class": "sister", "id": "link3"}))

# -----------------------------
# 12. HANDLING BROKEN HTML
# -----------------------------
bad_html = "<p><b>Broken tag<p>Another paragraph"
bad_soup = BeautifulSoup(bad_html, "html.parser")
print(bad_soup.prettify())

# -----------------------------
# 13. USING LXML FOR SPEED
# -----------------------------
# soup = BeautifulSoup(html_doc, "lxml")
# Much faster parsing

# -----------------------------
# 14. PARSING XML (optional)
# -----------------------------
# xml_soup = BeautifulSoup(xml_doc, 'xml')
# xml_soup.find('tagname')

# -----------------------------
# END OF CHEATSHEET
# -----------------------------