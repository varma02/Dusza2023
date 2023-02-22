import PySimpleGUI as sg

def save_reservation(name, phone, date, table):
    # Itt lehetne az asztalfoglalásokat fájlba menteni vagy adatbázisban tárolni
    # Ebben a példában csak kiírjuk őket a konzolra
    print(f"{name}, {phone}, {date}, {table} asztalt foglalt")

layout = [
    [sg.Text("Név"), sg.Input(key="-NAME-")],
    [sg.Text("Telefonszám"), sg.Input(key="-PHONE-")],
    [sg.Text("Dátum (YYYY-MM-DD)"), sg.Input(key="-DATE-")],
    [sg.Text("Asztal száma"), sg.Input(key="-TABLE-")],
    [sg.Button("Foglalás"), sg.Button("Mégse")]
]

window = sg.Window("Asztalfoglalás").Layout(layout)

while True:
    event, values = window.Read()
    if event == sg.WIN_CLOSED or event == "Mégse":
        break
    elif event == "Foglalás":
        name = values["-NAME-"]
        phone = values["-PHONE-"]
        date = values["-DATE-"]
        table = values["-TABLE-"]
        save_reservation(name, phone, date, table)
        sg.Popup("Foglalás megerősítve", auto_close=True)

window.Close()