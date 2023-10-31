import main

def create_html_table(elements, groups, prvek):
    html_table = "<table border='1'>\n<thead><tr>"
    for i in range (1,19):
        html_table += f"<th>{i}.</th>"
    html_table += "</tr></thead><tbody>"
    for i in range (0, 140):
        print(i)
        if ((i > 0 and i < 17) or (i > 19 and i < 30) or (i > 37 and i < 48) or i > 124):
            html_table += "<td></td>"
        else:
            if (i == 0 or i == 18 or i == 36 or i == 54 or i == 90 or i == 122):
                html_table += "<tr>"
            if (prvek >= 57 and prvek <= 70):
                prvek += 1
            else:
                element = elements[prvek]
                html_table += f"<td>{element['Symbol']} + {i} + {prvek}</td>"
                prvek += 1
            if (i == 17 or i == 35 or i == 53 or i == 71 or i == 121):
                html_table += "</tr>"
    #for element in elements:
    #    html_table += f"<tr><td>{element['Symbol']}</td><td>{element['Element']}</td><td>{element['NumberofProtons']}</td><td>{element['Type']}</td><td>{element['Period']}</td><td>{element['AtomicMass']}</td></tr>"

    html_table += "</tbody></table>"
    return html_table

def vytvor_html():
    prvek = 0
    html_table = create_html_table(main.elements, main.groups, prvek)

    with open('periodic_table.html', 'w') as file:
        file.write(html_table)
    print("Periodická tabulka byla uložena do souboru 'periodic_table.html'.")