import main
from  translate import Translator

translator = Translator(from_lang='en', to_lang='cs')

def vygeneruj_csv():
    csv_table = "English, Czech\n"

    for row in main.elements:
        csv_table += f"{row['Element']}, {row['Element']} \n"

    with open('translations.csv', 'w') as file:
        file.write(csv_table)