import csv
import json

import vyhledani_prvku
import vypocet_hmotnosti
import vytvoreni_markdown
import vytvoreni_html

# Načtení dat z CSV souboru
def load_elements_csv(filename):
    elements = []
    # Otevření CSV souboru pro čtení s explicitní specifikací kódování
    with open(filename, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        # Procházení řádků CSV souboru a přidání každého řádku do seznamu
        for row in reader:
            elements.append(row)
    return elements

# Načtení dat ze JSON souboru
def load_groups_json(filename):
    # Otevření JSON souboru pro čtení s explicitní specifikací kódování
    with open(filename, 'r', encoding='utf-8') as jsonfile:
        groups = json.load(jsonfile)
    return groups

# Funkce pro výběr akce z menu
def select_action():
    # Výpis nabídky akcí
    print("------------------------------------------------")
    print("1. Periodická Tabulka")
    print("2. Vyhledat prvky")
    print("3. Výpočet průměrné atomové hmotnosti")
    print("4. Markdown soubor")
    print("5. Konec")
    print("------------------------------------------------")
    # Uživatelský vstup pro výběr akce
    choice = input("Vyberte akci (1-5): ")
    return choice

# Načtení dat z CSV a JSON souboru
elements = load_elements_csv('elements.csv')
groups = load_groups_json('groups.json')

# Hlavní část programu
def main():
    # Nekonečná smyčka pro opakovaný výběr akcí, dokud uživatel nezvolí "Konec"
    while True:
        # Volání funkce pro výběr akce a uložení výběru do proměnné
        choice = select_action()

        # Větvení podle volby uživatele
        if choice == '1':
            vytvoreni_html.vytvor_html(elements)
            # 'pass' je zde záměrně, aby bylo jasné, že se zatím v těle podmínky nic dalšího neděje
            pass
        elif choice == '2':
            vyhledani_prvku.prvek(elements)
            pass
        elif choice == '3':
            vypocet_hmotnosti.prumerna_hmotnost(elements)
            pass
        elif choice == '4':
            vytvoreni_markdown.vytvoreni_markdown(elements)
            pass
        elif choice == '5':
            # Ukončení smyčky v případě volby "Konec"
            break
        else:
            # Výpis chybové zprávy v případě neplatné volby
            print("Neplatná volba. Zvolte číslo od 1 do 5.")

# Zajištění, že se funkce main() spustí pouze při přímém spuštění tohoto skriptu
if __name__ == "__main__":
    main()
