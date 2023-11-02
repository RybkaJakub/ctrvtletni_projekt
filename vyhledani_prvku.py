import main
from translate import Translator
import xml.etree.ElementTree as ET

translator = Translator(from_lang='en', to_lang='cs')


def vyhledavani_prvku(vyhledavan):
    vyhledavan = vyhledavan.lower()
    found_data = []

    for row in main.elements:
        for key, value in row.items():
            if (vyhledavan in value.lower()) and (len(vyhledavan) == len(value)):
                print(f"Symbol: {row['Symbol']}")
                print(f"Název: {translator.translate(row['Element'])}")
                print(f"Číslo: {row['AtomicNumber']}")
                print(f"Hmotnost: {row['AtomicMass']}")

                found_data.append({
                    "Symbol": row['Symbol'],
                    "Název": translator.translate(row['Element']),
                    "Číslo": row['AtomicNumber'],
                    "Hmotnost": row['AtomicMass']
                })
                break

    return found_data

def save_to_xml(data, xml_filename):
    # Vytvořte kořenový element XML
    root = ET.Element("data")

    # Vytvořte elementy pro každý záznam v datech
    for item in data:
        record = ET.Element("record")
        for key, value in item.items():
            sub_element = ET.Element(key)
            sub_element.text = value
            record.append(sub_element)
        root.append(record)

    # Vytvořte strom XML souboru
    tree = ET.ElementTree(root)

    # Uložte XML soubor
    tree.write(xml_filename)

def prvek():
    vyhledavani = input("Zadej vlastnost prvku: ")
    save_to_xml(vyhledavani_prvku(vyhledavani), "M.xml")


