import os

files = [
    "scrapeado/index.html",
    "scrapeado/contacto.html",
]

for f in files:
    if os.path.exists(f):
        with open(f, 'r', encoding='utf-8') as fp:
            content = fp.read()
        # Check end of file
        last_500 = content[-500:]
        print(f"{f} - Last 500 chars:")
        print(last_500)
        print("---")
        # Count script tags
        script_opens = content.count('<script>')
        script_closes = content.count('</script>')
        print(f"  <script> count: {script_opens}, </script> count: {script_closes}")
        # Check if our injected script is at the end
        if content.strip().endswith('</script></body></html>') or content.strip().endswith('</script>\n</body>\n</html>'):
            print("  Ends properly with script->body->html")
        else:
            print(f"  Ends with: ...{content[-100:]}")