import PySimpleGUI as sg

layout = [
    [sg.Text("Név"), sg.Input(key="-NAME-")],
    [sg.Text("Telefonszám"), sg.Input(key="-PHONE-", enable_events=True, size=(20, 1))],
    [sg.Input(key="-DATE-"), sg.CalendarButton("Dátum kiválasztása", target="-DATE-", key="-CALENDAR-", enable_events=True)],
    [sg.Text("Időpont"), sg.Input(key="-TIME-", enable_events=True, size=(20, 1))],
    [sg.Text("Asztal száma"), sg.Input(key="-TABLE-")],
    [sg.Button("Foglalás", key="-SUBMIT-")]
]

phone_num_chars = ["+", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

window = sg.Window("Asztalfoglalás").Layout(layout)

while True:
    event, values = window.Read()
    if event == sg.WIN_CLOSED:
        break
    elif event == "-SUBMIT-":
        print("submit")
    elif event == "-CALENDAR-":
        print("calendar")
        window.Element("-DATE-").Update(value=values["-CALENDAR-"].strftime("%Y-%m-%d"))
    elif event == "-PHONE-":
        filtered_phone = "".join([char for char in values["-PHONE-"] if char in phone_num_chars])
        window.Element("-PHONE-").Update(value=filtered_phone)
        print("phone")
        
window.Close()
