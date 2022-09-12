from bs4 import BeautifulSoup # Instalace: v příkazovém řádku zadejte "pip install beautifulsoup4"
import requests # "pip install requests"

velikost = input("Zadejte hledanou velikost: ").lower()
rozmezi = input("Zadejte rozmezí čísel vyhledávaných plakátů, oddělte čárkou (příklad: 16000,17777): ").split(",")

pocet = 0
print("\nHledám...\n")

for i in range(int(rozmezi[0]),int(rozmezi[1])): # Čísla v závorce = libovolně přepisovatelné rozmezí id plakátů, které program zkontroluje. 8030-43186 by mělo zahrnovat všechny plakáty.
    url = "https://www.terryhoponozky.cz/plakat/" + str(i)

    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, "lxml")
    formaty = str(soup.find_all("p"))
    formaty += str(soup.find("select"))

    if velikost in formaty.lower():
        print(url)
        pocet +=1

print("\nNalezeno " + str(pocet) + " výsledků")
