import pdfkit 



input = ["https://eltoque.com/mas-violencia-y-desapariciones-forzadas-protestas-en-caimanera-cuba", ]


options = {
    'page-size': 'Letter',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
    'encoding': "UTF-8",
    #"--no-background": None,
    #"--no-custom-header-propagation": None,
    #"--no-images": None,
    "--enable-forms": None,
    #"--print-media-type": None,
}

for idx, val in enumerate(input):
    pdfkit.from_url(str(val), str(str(idx)+'.pdf'),options=options)