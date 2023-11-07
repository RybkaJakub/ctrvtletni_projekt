import csv
import json

import vyhledani_prvku
import vypocet_hmotnosti
import vytvoreni_markdown
import vytvoreni_html

# Načtení dat z CSV souboru
def load_elements_csv(filename):
    elements = []
    with open(filename,'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            elements.append(row)
    return elements

# Načtení dat ze JSON souboru
def load_groups_json(filename):
    with open(filename, 'r', encoding='utf-8') as jsonfile:
        groups = json.load(jsonfile)
    return groups

# Funkce pro výběr akce z menu
def select_action():
    print("------------------------------------------------")
    print("1. Periodická Tabulka")
    print("2. Vyhledat prvky")
    print("3. Výpočet průměrné atomové hmotnosti")
    print("4. Markdown soubor")
    print("5. Konec")
    print("------------------------------------------------")
    choice = input("Vyberte akci (1-5): ")
    return choice

elements = load_elements_csv('elements.csv')
groups = load_groups_json('groups.json')

# Hlavní část programu
def main():

    while True:
        choice = select_action()

        if choice == '1':
            vytvoreni_html.vytvor_html(elements)
            pass
        elif choice == '2':
            vyhledani_prvku.prvek(elements)
            pass
        elif choice == '3':
            vypocet_hmotnosti.prumerna_hmotnost(elements, groups)
            pass
        elif choice == '4':
            vytvoreni_markdown.vytvoreni_markdown(elements, groups)
            pass
        elif choice == '5':
            break
        else:
            print("Neplatná volba. Zvolte číslo od 1 do 5.")

if __name__ == "__main__":
    main()