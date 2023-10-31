import csv
import json
import vyhledani_prvku
import vlastnosti_prvku
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
    print("1. Periodická Tabulka")
    print("2. Vyhledat prvky")
    print("3. Skupenství")
    print("4. Molekulová hmotnost")
    print("5. Konec")
    choice = input("Vyberte akci (1-5): ")
    return choice

# Hlavní část programu
def main():
    elements = load_elements_csv('elements.csv')
    groups = load_groups_json('groups.json')
    print(elements)
    print(groups)

    """while True:
        choice = select_action()

        if choice == '1':
            pass
        elif choice == '2':
            pass
        elif choice == '3':
            pass
        elif choice == '4':
            pass
        elif choice == '5':
            pass
        else:
            print("Neplatná volba. Zvolte číslo od 1 do 7.")
        """
if __name__ == "__main__":
    main()
