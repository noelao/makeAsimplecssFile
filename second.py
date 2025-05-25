import re

def beautify_css(css):
    # Tambahkan newline setelah setiap deklarasi
    css = re.sub(r';', ';\n  ', css)
    
    # Tambahkan newline dan indentasi setelah buka kurung {
    css = re.sub(r'{', ' {\n  ', css)
    
    # Tambahkan newline sebelum tutup kurung }
    css = re.sub(r'}', '\n}\n', css)
    
    # Hapus spasi berlebih
    css = re.sub(r'[ \t]+', ' ', css)
    
    # Hapus newline ganda
    css = re.sub(r'\n{2,}', '\n', css)
    
    return css.strip()

minified_css = "body{color:red;background-color:white;}h1{font-size:20px;}"
pretty_css = beautify_css(minified_css)

print(pretty_css)