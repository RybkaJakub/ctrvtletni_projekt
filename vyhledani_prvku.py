from translate import Translator
import xml.etree.ElementTree as ET
active = "None"
text = "None"

translator = Translator(from_lang='en', to_lang='cs')

def row_period(row, found_data):
    print(f"Symbol: {row['Symbol'] if row['Symbol'] != '' else 'Žádný'}")
    print(f"Element: {translator.translate(row['Element']) if row['Element'] != '' else 'Žádný'}")
    print(f"Číslo: {row['AtomicNumber'] if row['AtomicNumber'] != '' else 'Žádné'}")
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

    found_data.append({
        "Symbol": row['Symbol'],
        "Element": translator.translate(row['Element']),
        "Císlo": row['AtomicNumber'],
        "Hmotnost": row['AtomicMass'],
        "Protonove_cislo": row['NumberofProtons'],
        "Elektronove_cislo": row['NumberofElectrons'],
        "Neutronove_cislo": row['NumberofNeutrons'],
        "Periodicke_cislo": row['Period'],
        "cislo_skupiny": row['Group'],
        "Radioaktivni": row['Radioactive'],
        "Naturalní": row['Natural'],
        "Kov": row['Metal'],
        "Nekov": row['Nonmetal'],
        "Metalloid": row['Metalloid'],
        "Typ": row['Type']
    })

def switch_case(argument):
    global active
    global text
    if argument == "cislo":
        active = "AtomicNumber"
        text = "Zadej atomové číslo: "
    elif argument == "perioda":
        active = "Period"
        text = "Zadej periodicke cislo: "
    elif argument == "neutron":
        active = "NumberofNeutrons"
        text = "Zadej pocet neutronu: "
    elif argument == "proton":
        active = "NumberofProtons"
        text = "Zadej pocet protonu: "
    elif argument == "elektron":
        active = "NumberofElectrons"
        text = "Zadej pocet elektronu: "
    elif argument == "skupina":
        active = "Group"
        text = "Zadej cislo skupiny: "
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
        text = "Nekov  [ano/ne]: "
    else:
        active = "Hledani"
        text = ""

def vyhledavani_prvku(vyhledavan, elements):
    vyhledavan = vyhledavan.lower()
    found_data = []

    switch_case(vyhledavan)
    if (active != "Hledani"):
        vstup = input(text)
        if (vstup == "ano"):
            vstup = "yes"
        elif (vstup == "no"):
            vstup = ""
    for row in elements:
        if (active == "Hledani"):
            for key, value in row.items():
                if (vyhledavan in value.lower()) and (len(vyhledavan) == len(value)):
                    row_period(row, found_data)
                    break
        else:
            if (row[active].lower() == vstup):
                row_period(row, found_data)

    return found_data


def save_to_xml(data, xml_filename):
    root = ET.Element("data")

    for item in data:
        record = ET.Element("record")
        for key, value in item.items():
            sub_element = ET.Element(key)
            sub_element.text = value
            record.append(sub_element)
        root.append(record)

    tree = ET.ElementTree(root)
    tree.write(xml_filename, encoding="utf-8")

def prvek(elements):
    print("Pokud chcete vyhledávat pomocí čísla, tak napiště jednu z možností: Cislo, Perioda, Neutron, Proton, Elektron, Skupina")
    print("Další možnosti vyhledvávání: Radioaktivni, Prirodni, Kovy, Nekovy, Polokovy")
    vyhledavani = input("Vyber z možností a nebo zadej vlastnost prvku: ")
    save_to_xml(vyhledavani_prvku(vyhledavani, elements), "Prvky.xml")

