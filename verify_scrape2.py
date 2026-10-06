import os

files = [
    "scrapeado/index.html",
    "scrapeado/contacto.html",
]

for f in files:
    if os.path.exists(f):
        with open(f, 'r', encoding='utf-8') as fp:
            content = fp.read()
        style_pos = content.find('<style>')
        script_pos = content.find('<script>')
        style_end = content.find('</style>')
        script_end = content.find('</script>')
        print(f"{f}:")
        print(f"  <style> at pos {style_pos}, </style> at {style_end}")
        print(f"  <script> at pos {script_pos}, </script> at {script_end}")
        if style_pos >= 0 and style_end >= 0:
            css_len = style_end - style_pos
            print(f"  CSS length: {css_len} chars")
        if script_pos >= 0 and script_end >= 0:
            js_len = script_end - script_pos
            print(f"  JS length: {js_len} chars")
        # Show snippet around style tag
        if style_pos >= 0:
            print(f"  Style context: ...{content[max(0,style_pos-50):style_pos+100]}...")