import requests
from bs4 import BeautifulSoup

URL = "https://www.gov.br/ans/pt-br/assuntos/consumidor/o-que-o-seu-plano-de-saude-deve-cobrir-1/o-que-e-o-rol-de-procedimentos-e-evento-em-saude"
r = requests.get(URL)
print(r.content)

soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib
print(soup.prettify())

for pdf in pdfs:
        if (".pdf" in pdfs):
            i+= 1
            zip.write("pdf"+str(i)+".pdf")
            print("File ", i, "compressed")
