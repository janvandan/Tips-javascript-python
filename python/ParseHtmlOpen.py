from bs4 import BeautifulSoup
from datetime import datetime
import time

nomFichier = "SourceExemple1.html"

fichierOpen = open(nomFichier, "r")

# print("fichier = ", fichier.read())

text = fichierOpen.read()
fichierOpen.close()

# suite idem https

dataHTML = BeautifulSoup(text, 'html.parser')

# print("data =", dataHTML)

# tagAtrouver = 'input[class="tokens-input-text"]'
# soup.findAll('span', attrs={'id' : 'productTitle'}) :
# ---------------------------------
dateActuelle = datetime.now()
heureActuelle = dateActuelle.strftime("%H:%M:%S")
jourActuel = dateActuelle.strftime("%d/%m/%y")

print("Jour = ", jourActuel, "Heure = ", heureActuelle)

print("dataHTML.title = ", dataHTML.title)
print("dataHTML.title.get_text() = ", dataHTML.title.get_text())
print('dataHTML.a["href"] = ', dataHTML.a["href"])

champsOu = dataHTML.find_all('input', attrs={'name' : 'where'})

print( "champsOu =", champsOu)

for x in champsOu:
    print("texte =", x.text.strip)

print( 'dataHTML.find_all("forms") = ', dataHTML.find_all("form"))
