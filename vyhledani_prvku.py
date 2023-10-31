import main
from  translate import Translator

translator = Translator(from_lang='en', to_lang='cs')
def vyhledavani_prvku(vyhledavan):
            csv_reader = main.elements
            for row in csv_reader:
                if row['Symbol'] == vyhledavan:
                    print(f"Symbol: {row['Symbol']}")
                    print(f"Název: {translator.translate(row['Element'])}")
                    print(f"Číslo: {row['AtomicNumber']}")
                    print(f"Hmotnost: {row['AtomicMass']}")
                    break  # Můžete ukončit cyklus, jakmile prvek najdete

def prvek():
    vyhledavani = input("zadej vlastnost prvku: ")
    vyhledavani_prvku(vyhledavani)
