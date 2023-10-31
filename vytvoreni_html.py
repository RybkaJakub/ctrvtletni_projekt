import main


def add_to_table(id, symbol, element):
    return (f"<td id='{id}'>"
            f"<p id='Symbol'> {symbol} </p>"
            f"<p id='Element'> {element} </p>"
            "</td>")


def create_html_table(elements, radek, prvek):
    html_table = "<link rel=""stylesheet"" href=""./css/style.css>"
    html_table2 = "<table id=""second""><tbody>"
    html_table += "<body><div id=""tables""><table id=""main"">\n<thead><tr>"
    for i in range(1, 19):
        if (i == 1):
            html_table += "<th></th>"
            html_table += f"<th>{i}.</th>"
        elif (i == 3):
            html_table += f"<th>{i}.</th>"
            html_table += "<th id='Empty'></th>"
        else:
            html_table += f"<th>{i}.</th>"
    html_table += "</tr></thead><tbody>"
    for i in range(0, 161):
        # print(i)
        # print(prvek)
        if (i == 1 or i == 2 or (i > 3 and i < 18) or i == 21 or (i > 22 and i < 32) or i == 40 or (i > 41 and i < 51)):
            html_table += "<td></td>"
        elif (i == 3 or i == 22 or i == 41 or i == 60 or i == 79 or i == 112 or i == 131):
            html_table += "<td id='Empty'></td>"
            radek += 1
        else:
            if (i == 0 or i == 19 or i == 38 or i == 57 or i == 76 or i == 95 or i == 128):
                html_table += f"<tr><td id='Radek'>{radek}.</td>"
            if ((prvek >= 57 and prvek <= 70) or (prvek >= 89 and prvek <= 102)):
                element = elements[prvek]
                type = element['Type'].split()
                if (prvek == 57 or prvek == 89):
                    html_table2 += "<tr>"
                if type:
                    # html_table += f"<td id='{type[0]}'>{element['Symbol']} \n {element['Element']}</td>"
                    html_table2 += add_to_table(type[0], element['Symbol'], f"{element['Element']}")
                else:
                    # html_table += f"<td id='None'>{element['Symbol']} \n {element['Element']}</td>"
                    html_table2 += add_to_table("None", element['Symbol'], f"{element['Element']}")
                if (prvek == 70 or prvek == 102):
                    html_table2 += "</tr>"
                prvek += 1
            else:
                element = elements[prvek]
                if (i == 0):
                    # html_table += f"<td id='Helium'>{element['Symbol']} \n {element['Element']}</td>"
                    html_table += add_to_table("Helium", element['Symbol'], f"{element['Element']}")
                else:
                    type = element['Type'].split()
                    if (type and prvek < 112):
                        # html_table += f"<td id='{type[0]}'>{element['Symbol']} \n {element['Element']}</td>"
                        html_table += add_to_table(type[0], element['Symbol'], f"{element['Element']}")
                    else:
                        # html_table += f"<td id='None'>{element['Symbol']} \n {element['Element']}</td>"
                        html_table += add_to_table("None", element['Symbol'], f"{element['Element']}")
                prvek += 1
            if (i == 18 or i == 37 or i == 56 or i == 75 or i == 94 or i == 127):
                html_table += "</tr>"
    # for element in elements:
    #    html_table += f"<tr><td>{element['Symbol']}</td><td>{element['Element']}</td><td>{element['NumberofProtons']}</td><td>{element['Type']}</td><td>{element['Period']}</td><td>{element['AtomicMass']}</td></tr>"

    html_table += "</tbody></table>"
    html_table2 += "</tbody></table></div></body>"
    html_table += html_table2
    return html_table


def vytvor_html():
    prvek = 0
    radek = 1
    html_table = create_html_table(main.elements, radek, prvek)

    with open('periodic_table.html', 'w') as file:
        file.write(html_table)
    print("Periodická tabulka byla uložena do souboru 'periodic_table.html'.")
