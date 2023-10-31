import csv
import json

# Načtení dat z CSV souboru
def load_elements_csv(filename):
    elements = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            elements.append(row)
    return elements

# Načtení dat ze JSON souboru
def load_groups_json(filename):
    with open(filename, 'r') as jsonfile:
        groups = json.load(jsonfile)
    return groups

# Funkce pro výběr akce z menu
def select_action():
    print("1. Vyhledat prvek")
    print("2. Zobrazit vlastnosti prvku")
    print("3. Vypočítat průměrnou relativní atomovou hmotnost")
    print("4. Generovat HTML tabulku")
    print("5. Exportovat do XML")
    print("6. Vytvořit Markdown soubor")
    print("7. Konec")
    choice = input("Vyberte akci (1-7): ")
    return choice

# Hlavní část programu
def main():
    elements = load_elements_csv('elements.csv')
    groups = load_groups_json('groups.json')

    while True:
        choice = select_action()

        if choice == '1':
            # Implementujte vyhledání prvku
            pass
        elif choice == '2':
            # Implementujte zobrazení vlastností prvku
            pass
        elif choice == '3':
            # Implementujte výpočet průměrné relativní atomové hmotnosti
            pass
        elif choice == '4':
            # Implementujte generování HTML tabulky
            pass
        elif choice == '5':
            # Implementujte export do XML
            pass
        elif choice == '6':
            # Implementujte vytvoření Markdown souboru
            pass
        elif choice == '7':
            break
        else:
            print("Neplatná volba. Zvolte číslo od 1 do 7.")

if __name__ == "__main__":
    main()
