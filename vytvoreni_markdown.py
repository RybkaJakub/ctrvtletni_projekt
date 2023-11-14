def select_action():
    # Výpis nabídky akcí
    print("------------------------------------------------")
    print("Vyber si možnost!")
    print("------------------------------------------------")
    print("1. Skupina")
    print("2. Perioda")
    print("3. Konec")
    print("------------------------------------------------")
    # Uživatelský vstup pro výběr akce
    return input("Vyberte akci (1-3): ")

def get_input(text):
    # Obecná funkce pro získání uživatelského vstupu s daným textem
    return input(text)

def groupmarkdown(elements):
    # Funkce pro vytvoření markdown souboru pro skupinu prvků
    input_ = get_input("Zadej číslo skupiny: ")
    markdownFile = f"# Skupina prvku - {input_}\n"
    if (int(input_) > 18):
        # Ošetření neplatné volby skupiny
        print("Neplatná možnost!")
        return
    for row in elements:
        if (row['Group'] == input_):
            markdownFile += f"## {row['Element']} \n"
            for key, value in row.items():
                if (key == "Element"):
                    pass
                else:
                    markdownFile += f"- {key} : {value} \n"
    # Uložení markdown do souboru
    with open('group.md', 'w', encoding='utf-8') as file:
        file.write(markdownFile)
    print("Byl vytvořen soubor group.md!")

def periodmarkdown(elements):
    # Funkce pro vytvoření markdown souboru pro periodu prvků
    input_ = get_input("Zadej číslo periody: ")
    markdownFile = f"# Perioda prvku - {input_}\n"
    if (int(input_) > 7):
        # Ošetření neplatné volby periody
        print("Neplatná možnost!")
        return
    for row in elements:
        perioda = row['Period']
        if perioda:
            if (row['Period'] == input_):
                markdownFile += f"## {row['Element']} \n"
                for key, value in row.items():
                    if (key == "Element"):
                        pass
                    else:
                        markdownFile += f"- {key} : {value} \n"
            else:
                pass
        else:
            pass
    # Uložení markdown do souboru
    with open('period.md', 'w', encoding='utf-8') as file:
        file.write(markdownFile)
    print("Byl vytvořen soubor period.md!")

def vytvoreni_markdown(elements):
    # Nekonečná smyčka pro opakovaný výběr akcí, dokud uživatel nezvolí "Konec"
    while True:
        # Volání funkce pro výběr akce a uložení výběru do proměnné
        choice = select_action()

        # Větvení podle volby uživatele
        if choice == '1':
            groupmarkdown(elements)
            # 'pass' je zde záměrně, aby bylo jasné, že se zatím v těle podmínky nic dalšího neděje
            pass
        elif choice == '2':
            periodmarkdown(elements)
            pass
        elif choice == '3':
            # Ukončení smyčky v případě volby "Konec"
            break
        else:
            # Výpis chybové zprávy v případě neplatné volby
            print("Neplatná volba. Zvolte číslo od 1 do 3.")
