import main

def create_html_table(elements, groups):
    html_table = "<table border='1'>"
    html_table += "<tr><th>Značka</th><th>Latinský název</th><th>Anglický název</th><th>Protonové číslo</th><th>Skupina</th><th>Perioda</th><th>Relativní atomová hmotnost</th></tr>"

    for element in elements:
        group_name = groups[element['skupina']]
        html_table += f"<tr><td>{element['značka']}</td><td>{element['latinský název']}</td><td>{element['anglický název']}</td><td>{element['protonové číslo']}</td><td>{group_name}</td><td>{element['perioda']}</td><td>{element['relativní atomová hmotnost']}</td></tr>"

    html_table += "</table>"
    return html_table

def vytvor_html():
    html_table = create_html_table(main.elements, main.groups)

    with open('periodic_table.html', 'w') as file:
        file.write(html_table)
    print("Periodická tabulka byla uložena do souboru 'periodic_table.html'.")