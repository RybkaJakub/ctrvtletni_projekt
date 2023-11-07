def select_action():
    print("------------------------------------------------")
    print("Vyber si možnost!")
    print("------------------------------------------------")
    print("1. Skupina")
    print("2. Perioda")
    print("3. Konec")
    print("------------------------------------------------")
    return input("Vyberte akci (1-3): ")


def get_input(text):
    return input(text)


def groupmarkdown(elements):
    input_ = get_input("Zadej číslo skupiny: ")
    markdownFile = f"# Skupina prvku - {input_}\n"
    if (int(input_) > 18):
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
    with open('group.md', 'w', encoding='utf-8') as file:
        file.write(markdownFile)
    print("Byl vytvořen soubor group.md!")


def periodmarkdown(elements):
    input_ = get_input("Zadej číslo periody: ")
    markdownFile = f"# Perioda prvku - {input_}\n"
    if (int(input_) > 7):
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
    with open('period.md', 'w', encoding='utf-8') as file:
        file.write(markdownFile)
    print("Byl vytvořen soubor period.md!")

def vytvoreni_markdown(elements, groups):
    while True:
        choice = select_action()

        if choice == '1':
            groupmarkdown(elements)
            pass
        elif choice == '2':
            periodmarkdown(elements)
            pass
        elif choice == '3':
            break
        else:
            print("Neplatná volba. Zvolte číslo od 1 do 3.")
