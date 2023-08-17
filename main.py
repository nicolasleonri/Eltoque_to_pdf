from bs4 import BeautifulSoup
from weasyprint import HTML, CSS, default_url_fetcher
from urllib.request import Request, urlopen

### FUNCTIONS ###


def request_url(url):
    req = Request(str(url), headers={'User-Agent': 'Mozilla/5.0'})
    web_byte = urlopen(req).read()
    webpage = web_byte.decode('utf-8')
    return webpage

### CONFIGURATIONS ###


options = {
    'uncompressed_pdf': False,
    'presentational_hints': False,
    'optimize_images': True,
    'jpeg_quality': 95,
    'dpi': 300,
    'enable_hinting': False,
    'full_fonts': True,
    'pdf_forms': False,
}

css = CSS(string = '''@page { size: A3; margin: 1.5cm; }''')

media = CSS(string = '@media { type: print; margin-left: 0px; }')

### READ SOUP AND EDIT HTML ###

webpage = request_url(
    "https://eltoque.com/por-que-la-bancarizacion-forzosa-fracaso-antes-de-empezar")
soup = BeautifulSoup(webpage, 'lxml')

parent_element = soup.find(id='super-page-wrapper')

# Remove innecesary elements
child_elements = list(parent_element.children)
for idx, val in enumerate(child_elements):
    if idx < 4 or idx > 4:
        val.decompose()

# Changes margin
element = soup.select_one('.iNddtr')
if element:
    # Modify the value of the 'margin-left' property
    element['style'] = 'margin-left: 0px;'

### PRINT HTML ###

html = HTML(string=str(soup), encoding="UTF-8", media_type=[media])

pdf = html.write_pdf(zoom=1, stylesheets=[css], options=options)

output_path = 'test.pdf'
with open(output_path, 'wb') as file:
    file.write(pdf)
