import PySimpleGUI as sg
from old import db

def prn(num):
    n = str(num)

    if len(n) == 1:
        return f'0{n}'
    else:
        return f'{n}'

def run():

    foglalasok = db.readRealFoglalasok()
    frender = []
    for Item in foglalasok:
        frender.append(
            [
                f'{ Item["nev"] }',
                f'{ prn(Item["kezdet"]["honap"]) }.{prn(Item["kezdet"]["nap"])}.   {prn(Item["kezdet"]["ora"])}:{prn(Item["kezdet"]["perc"])} - {prn(Item["befejezes"]["ora"])}:{prn(Item["befejezes"]["perc"])}',
                f'{Item["szekek"]}',
                f'{ ", ".join(str(e) for e in Item["asztalok"]) }'
            ]
        )
	
    layout = [
	    [
            sg.Text("Asztalfoglalási napló", font=('Arial', 18)),
        ],
        [
            sg.Table(
                values=frender,
                headings=[
                    "Foglaló neve",
                    "Dátum -tól-ig",
                    "Székek száma",
                    "Lefoglalt asztalok"
                ],
                expand_x=True,
                expand_y=True,
                auto_size_columns=True,
                vertical_scroll_only=True
            )
            # sg.Column(
            #     layout=frender,
            #     scrollable=True,
            #     size=(800, 1),
            #     expand_y=True,
            #     vertical_scroll_only=True
            # )
        ]
        
    ]

    window = sg.Window('Foglalás - Rögzítés', layout=layout, resizable=False, size=(600, 200))
	
    while True:
        event, values = window.read()
        print(event, values)

        match event:
            case sg.WIN_CLOSED | "-EXIT-": break

    # window.close()
run()