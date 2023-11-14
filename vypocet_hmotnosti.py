def select_action():
    # Výpis nabídky akcí pro uživatele
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
    # Funkce pro získání uživatelského vstupu s daným textem
    return input(text)

def groupmass(elements):
    # Funkce pro výpočet průměrné atomové hmotnosti ve skupině prvků
    input_ = get_input("Zadej číslo skupiny: ")
    mass = 0
    count = 0
    if (int(input_) > 18):
        # Ošetření neplatné volby skupiny
        print("Neplatná možnost!")
        return
    for row in elements:
        if row['Group'] == input_:
            mass += float(row['AtomicMass'])
            count += 1
    print("------------------------------------------------")
    print(f"Průměrná atomová hmotnost je {round(mass / count, 2)}")

def periodmass(elements):
    # Funkce pro výpočet průměrné atomové hmotnosti v periodě prvků
    input_ = get_input("Zadej číslo skupiny: ")
    mass = 0
    count = 0
    if (int(input_) > 7):
        # Ošetření neplatné volby periody
        print("Neplatná možnost!")
        return
    for row in elements:
        if row['Period'] == input_:
            mass += float(row['AtomicMass'])
            count += 1
    print("------------------------------------------------")
    print(f"Průměrná atomová hmotnost je {round(mass / count, 2)}")

def prumerna_hmotnost(elements):
    # Nekonečná smyčka pro opakovaný výběr akcí, dokud uživatel nezvolí "Konec"
    while True:
        # Volání funkce pro výběr akce a uložení výběru do proměnné
        choice = select_action()

        # Větvení podle volby uživatele
        if choice == '1':
            groupmass(elements)
            # 'pass' je zde záměrně, aby bylo jasné, že se zatím v těle podmínky nic dalšího neděje
            pass
        elif choice == '2':
            periodmass(elements)
            pass
        elif choice == '3':
            # Ukončení smyčky v případě volby "Konec"
            break
        else:
            # Výpis chybové zprávy v případě neplatné volby
            print("Neplatná volba. Zvolte číslo od 1 do 3.")
