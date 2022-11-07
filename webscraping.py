# Importar as bibliotecas necessárias
import requests
from bs4 import BeautifulSoup
from zipfile import ZipFile

# url de onde iremos fazer o download dos pdf's
url = "https://www.gov.br/ans/pt-br/assuntos/consumidor/o-que-o-seu-plano-de-saude-deve-cobrir-1/o-que-e-o-rol-de-procedimentos-e-evento-em-saude"

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

links = soup.find_all('a')

pdfs = links

i = 0 

for link in links:
    if('.pdf' in link.get('href', [])):
        i += 1
        print("Downloading file: ", i)

        response = requests.get(link.get('href'))

        pdf = open("pdf"+str(i)+".pdf", 'wb')
        pdf.write(response.content)
        pdf.close()
        print("File ", i, "downloaded")

print("Todos os PDFS foram baixados")

