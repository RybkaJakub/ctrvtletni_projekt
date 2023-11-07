def select_action():
    print("------------------------------------------------")
    print("Vyber si možnost!")
    print("------------------------------------------------")
    print("1. Skupina")
    print("2. Perioda")
    print("3. Konec")
    print("------------------------------------------------")
    return input("Vyberte akci (1-5): ")

def get_input(text):
    return input(text)

def groupmass(elements):
    input_ = get_input("Zadej číslo skupiny: ")
    mass = 0
    count = 0
    if (int(input_) > 18):
        print("Neplatná možnost!")
        return
    for row in elements:
        if row['Group'] == input_:
            mass += float(row['AtomicMass'])
            count += 1
    print("------------------------------------------------")
    print(f"Průměrná atomová hmotnost je {round(mass / count, 2)}")

def periodmass(elements):
    input_ = get_input("Zadej číslo skupiny: ")
    mass = 0
    count = 0
    if (int(input_) > 7):
        print("Neplatná možnost!")
        return
    for row in elements:
        if row['Period'] == input_:
            mass += float(row['AtomicMass'])
            count += 1
    print("------------------------------------------------")
    print(f"Průměrná atomová hmotnost je {round(mass / count, 2)}")

def prumerna_hmotnost(elements, groups):
    while True:
        choice = select_action()

        if choice == '1':
            groupmass(elements)
            pass
        elif choice == '2':
            periodmass(elements)
            pass
        elif choice == '3':
            break
        else:
            print("Neplatná volba. Zvolte číslo od 1 do 3.")