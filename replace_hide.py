import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace class="... hide ..." with class="... hidden ..."
new_content = re.sub(r'class="([^"]*)\bhide\b([^"]*)"', r'class="\1hidden\2"', content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Replacement complete.")
