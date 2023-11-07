from translate import Translator
import xml.etree.ElementTree as ET

translator = Translator(from_lang='en', to_lang='cs')

def row_period(row, found_data):
    print(f"Symbol: {row['Symbol']}")
    print(f"Element: {translator.translate(row['Element'])}")
    print(f"Číslo: {row['AtomicNumber']}")
    print(f"Hmotnost: {row['AtomicMass']}")
    print(f"Protonove_cislo: {row['NumberofProtons']}")
    print(f"Elektronove_cislo: {row['NumberofElectrons']}")
    print(f"Neutronove_cislo: {row['NumberofNeutrons']}")
    print(f"Periodicke_cislo: {row['Period']}")
    print(f"Cislo_skupiny: {row['Group']}")
    print(f"Radioaktivni: {row['Radioactive']}")
    print(f"Naturalní: {row['Natural']}")
    print(f"Kov: {row['Metal']}")
    print(f"Nekov: {row['Nonmetal']}")
    print(f"Metalloid: {row['Metalloid']}")
    print(f"Typ: {row['Type']}")
    print("------------------------------------------------")

    found_data.append({
        "Symbol": row['Symbol'],
        "Element": translator.translate(row['Element']),
        "Číslo": row['AtomicNumber'],
        "Hmotnost": row['AtomicMass'],
        "Protonove cislo": row['NumberofProtons'],
        "Elektronove cislo": row['NumberofElectrons'],
        "Neutronove cislo": row['NumberofNeutrons'],
        "Periodicke cislo": row['Period'],
        "cislo skupiny": row['Group'],
        "Radioaktivni": row['Radioactive'],
        "Naturalní": row['Natural'],
        "Kov": row['Metal'],
        "Nekov": row['Nonmetal'],
        "Metalloid": row['Metalloid'],
        "Typ": row['Type']
    })
def vyhledavani_prvku(vyhledavan, elements):
    vyhledavan = vyhledavan.lower()
    found_data = []

    for row in elements:
        for key, value in row.items():
            if (vyhledavan in value.lower()) and (len(vyhledavan) == len(value)):
                row_period(row, found_data)
                break
            elif vyhledavan.startswith("cislo"):
                cislo = input("Zadej atomove cislo: ")
                for row in elements:
                    if row['AtomicNumber'].lower() == cislo:
                        row_period(row, found_data)
                        break
            elif vyhledavan.startswith("perioda"):
                perioda = input("Zadej periodicke cislo: ")
                for row in elements:
                    if row['Period'].lower() == perioda:
                        row_period(row, found_data)
                        break
            elif vyhledavan.startswith("neutron"):
                neutron = input("Zadej pocet neutronu: ")
                for row in elements:
                    if row['NumberofNeutrons'].lower() == neutron:
                        row_period(row, found_data)
                        break
            elif vyhledavan.startswith("proton"):
                proton = input("Zadej protonove cislo: ")
                for row in elements:
                    if row['NumberofProtons'].lower() == proton:
                        row_period(row, found_data)
                        break
            elif vyhledavan.startswith("elektron"):
                elektron = input("Zadej pocet elektronu: ")
                for row in elements:
                    if row['NumberofElectrons'].lower() == elektron:
                        row_period(row, found_data)
                        break
            elif vyhledavan.startswith("skupina"):
                elektron = input("Zadej cislo skupiny: ")
                for row in elements:
                    if row['Group'].lower() == elektron:
                        row_period(row, found_data)
                        break
            elif vyhledavan.startswith("radioactive"):
                rad = input("Radioaktivní: ")
                for row in elements:
                    if row['Radioactive'].lower() == rad:
                        row_period(row, found_data)
                        break
            elif vyhledavan.startswith("natural"):
                neut = input("Naturální: ")
                for row in elements:
                    if row['Natural'].lower() == neut:
                        row_period(row, found_data)
                break
            elif vyhledavan.startswith("metal"):
                metal = input("Kov: ")
                for row in elements:
                    if row['Metal'].lower() == metal:
                        row_period(row, found_data)
                break
            elif vyhledavan.startswith("nonmetal"):
                nometal = input("Nekov: ")
                for row in elements:
                    if row['Nonmetal'].lower() == nometal:
                        row_period(row, found_data)
                        break
            elif vyhledavan.startswith("metalloid"):
                metall = input("metalloid: ")
                for row in elements:
                    if row['Metalloid'].lower() == metall:
                        row_period(row, found_data)
                        break
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
    print("Pkoud chcete vyhledávat pomocí čísla, tak napiště jednu z moznostic cislo, perioda, neutron, proton, elektron, skupina")
    print("Další možnosti vyhledvávání: Radioactive, Natural, Metal, Nonmetal,	Metalloid")
    vyhledavani = input("Zadej vlastnost prvku: ")
    save_to_xml(vyhledavani_prvku(vyhledavani, elements), "M.xml")


