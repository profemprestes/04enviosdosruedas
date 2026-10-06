import re
with open('scrapeado/index.html', 'r', encoding='utf-8') as f:
    content = f.read()
matches = re.findall(r'href=([\"\'])([^\"\']+)\1', content)
for m in matches:
    print(m[1])