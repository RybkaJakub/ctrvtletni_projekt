from translate import Translator  # Importování Translator z knihovny translate pro překlad textu
import xml.etree.ElementTree as ET  # Importování ElementTree z knihovny xml pro práci s XML

# Inicializace globálních proměnných
active = "None"  # Aktivní kritérium pro vyhledávání
text = "None"    # Textový vstup pro uživatele

# Inicializace překladače pro překlad z angličtiny do češtiny
translator = Translator(from_lang='en', to_lang='cs')

# Funkce pro výpis informací o prvcích a jejich přidání do seznamu found_data
def row_period(row, found_data):
    print(f"Symbol: {row['Symbol'] if row['Symbol'] != '' else 'Žádný'}")
    print(f"Element: {translator.translate(row['Element']) if row['Element'] != '' else 'Žádný'}")
    print(f"Cislo: {row['AtomicNumber'] if row['AtomicNumber'] != '' else 'Žádné'}")
    print(f"Hmotnost: {row['AtomicMass'] if row['AtomicMass'] != '' else 'Žádná'}")
    print(f"Protonové číslo: {row['NumberofProtons'] if row['NumberofProtons'] != '' else 'Žádné'}")
    print(f"Elektronové číslo: {row['NumberofElectrons']}")
    print(f"Neutronové číslo: {row['NumberofNeutrons'] if row['NumberofNeutrons'] != '' else 'Žádné'}")
    print(f"Periodické číslo: {row['Period'] if row['Period'] != '' else 'Žádné'}")
    print(f"Čislo skupiny: {row['Group'] if row['Group'] != '' else 'Žádné'}")
    print(f"Radioaktivní: {'Ano' if row['Radioactive'] == 'yes' else 'Ne'}")
    print(f"Naturání: {'Ano' if row['Natural'] == 'yes' else 'Ne'}")
    print(f"Kov: {'Ano' if row['Metal'] == 'yes' else 'Ne'}")
    print(f"Nekov: {'Ano' if row['Nonmetal'] == 'yes' else 'Ne'}")
    print(f"Polokov: {'Ano' if row['Metalloid'] == 'yes' else 'Ne'}")
    print(f"Typ: {row['Type'] if row['Type'] != '' else 'Žádný'}")
    print("------------------------------------------------")

    # Přidání informací o prvku do seznamu found_data
    found_data.append({
        "Symbol": row['Symbol'],
        "Element": translator.translate(row['Element']),
        "Cislo": row['AtomicNumber'],
        "Hmotnost": row['AtomicMass'],
        "Protonove_cislo": row['NumberofProtons'],
        "Elektronove_cislo": row['NumberofElectrons'],
        "Neutronove_cislo": row['NumberofNeutrons'],
        "Periodicke_cislo": row['Period'],
        "cislo_skupiny": row['Group'],
        "Radioaktivni": row['Radioactive'],
        "Naturalni": row['Natural'],
        "Kov": row['Metal'],
        "Nekov": row['Nonmetal'],
        "Metalloid": row['Metalloid'],
        "Typ": row['Type']
    })

# Funkce pro přepínání aktivního kritéria podle vstupního argumentu
def switch_case(argument):
    global active
    global text
    # Nastavení aktivního kritéria a textového vstupu podle vstupního argumentu
    if argument == "cislo":
        active = "AtomicNumber"
        text = "Zadej atomové číslo: "
    elif argument == "perioda":
        active = "Period"
        text = "Zadej periodické číslo: "
    elif argument == "neutron":
        active = "NumberofNeutrons"
        text = "Zadej počet neutronů: "
    elif argument == "proton":
        active = "NumberofProtons"
        text = "Zadej počet protonů: "
    elif argument == "elektron":
        active = "NumberofElectrons"
        text = "Zadej počet elektronů: "
    elif argument == "skupina":
        active = "Group"
        text = "Zadej číslo skupiny: "
    elif argument == "radioaktivni":
        active = "Radioactive"
        text = "Radioaktivní [ano/ne]: "
    elif argument == "prirodni":
        active = "Natural"
        text = "Naturální [ano/ne]: "
    elif argument == "polokovy":
        active = 'Metalloid'
        text = "Metaloid [ano/ne]: "
    elif argument == "kovy":
        active = "Metal"
        text = "Kov [ano/ne]: "
    elif argument == "nekovy":
        active = "Nonmetal"
        text = "Nekov [ano/ne]: "
    else:
        active = "Hledani"
        text = ""

# Funkce pro vyhledávání prvků podle zadaných kritérií
def vyhledavani_prvku(vyhledavan, elements):
    vyhledavan = vyhledavan.lower()
    found_data = []

    switch_case(vyhledavan)
    # Pokud není aktivní kritérium "Hledani", vyžádá se od uživatele vstup
    if (active != "Hledani"):
        vstup = input(text)
        # Převede odpověď "ano" na "yes" a "no" na prázdný řetězec
        if (vstup == "ano"):
            vstup = "yes"
        elif (vstup == "ne"):
            vstup = ""
    # Prochází prvky a porovnává je s kritériem
    for row in elements:
        if (active == "Hledani"):
            for key, value in row.items():
                # Pokud se vyhledávaný text shoduje s hodnotou a délka je stejná, vypíše informace o prvku
                if (vyhledavan in value.lower()) and (len(vyhledavan) == len(value)):
                    row_period(row, found_data)
                    break
        else:
            # Porovnává hodnotu prvku s odpovědí od uživatele
            if (row[active].lower() == vstup):
                row_period(row, found_data)

    return found_data  # Vrací seznam nalezených prvků

# Funkce pro ukládání dat o prvcích do XML
def save_to_xml(data, xml_filename):
    root = ET.Element("data")  # Vytvoření kořenového elementu "data"

    # Pro každý prvek v seznamu vytvoří element "record" a vnoří do něj informace o prvku
    for item in data:
        record = ET.Element("record")
        for key, value in item.items():
            sub_element = ET.Element(key)
            sub_element.text = value
            record.append(sub_element)
        root.append(record)

    tree = ET.ElementTree(root)  # Vytvoření stromu z kořenového elementu
    tree.write(xml_filename, encoding="utf-8")  # Uložení stromu do XML souboru

def prvek(elements):
    print("Pokud chcete vyhledávat pomocí čísla, napište jednu z možností: Cislo, Perioda, Neutron, Proton, Elektron, Skupina")
    print("Další možnosti vyhledávání: Radioaktivni, Prirodni, Kovy, Nekovy, Polokovy")
    vyhledavani = input("Vyberte z možností nebo zadejte vlastnost prvku: ")
    save_to_xml(vyhledavani_prvku(vyhledavani, elements), "Prvky.xml")
    print("Data byla uložena do Prvky.xml .")

