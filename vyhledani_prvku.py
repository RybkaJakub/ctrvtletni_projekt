import main
from  translate import Translator

translator = Translator(from_lang='en', to_lang='cs')
def vyhledavani_prvku(vyhledavan):
        vyhledavan = vyhledavan.lower()
        for row in main.elements:
            for key, value in row.items():
                if (vyhledavan in value.lower()) and (len(vyhledavan) == len(value)):
                    print(f"Symbol: {row['Symbol']}")
                    print(f"Název: {translator.translate(row['Element'])}")
                    print(f"Číslo: {row['AtomicNumber']}")
                    print(f"Hmotnost: {row['AtomicMass']}")
                    break  # Můžete ukončit cyklus, jakmile prvek najdete

def prvek():
    vyhledavani = input("zadej vlastnost prvku: ")
    vyhledavani_prvku(vyhledavani)
