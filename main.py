import re

def minify_css(css):
    css = re.sub(r'\s+', ' ', css)            # Collapse whitespace
    css = re.sub(r'\s*{\s*', '{', css)        # Remove spaces around {
    css = re.sub(r'\s*}\s*', '}', css)        # Remove spaces around }
    css = re.sub(r'\s*:\s*', ':', css)        # Remove spaces around :
    css = re.sub(r';\s*', ';', css)           # Remove spaces after ;
    css = re.sub(r'\s*;\s*}', '}', css)       # Remove last semicolon before }
    return css.strip()

# Example usage
with open("style.css", "r") as f:
    raw_css = f.read()

clean_css = minify_css(raw_css)

with open("style.min.css", "w") as f:
    f.write(clean_css)
