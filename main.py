import pdfkit
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

def request_url(url):
    # Create a request object with the given URL and a user-agent header
    req = Request(str(url), headers={'User-Agent': 'Mozilla/5.0'})
    # Use the urlopen function to open the request object and read the contents
    web_byte = urlopen(req).read()
    # Convert the byte data to a UTF-8 encoded string
    webpage = web_byte.decode('utf-8')
    # Return the webpage string
    return webpage


input = ["https://eltoque.com/mas-violencia-y-desapariciones-forzadas-protestas-en-caimanera-cuba", ]


options = {
    'page-size': 'A3',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
    'no-pdf-compression' : None,
    'encoding': "UTF-8",
    'enable-external-links' : None,
    'background' : None,
    'enable-internal-links' : None,
    'enable-javascript' : None,
    'images' : None,
    #'javascript-delay' : 1000,
    'disable-smart-shrinking' : None,
    'no-stop-slow-scripts' : None,
    'page-width' : '32.51cm',
    'enable-forms' : None,
    'print-media-type' : None,
}

for idx, val in enumerate(input):
    pdfkit.from_url(str(val), str(str(idx)+'.pdf'),options=options)
