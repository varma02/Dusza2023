import PySimpleGUI as sg
import new_record, list_records

layout = [
	[sg.Button("Foglalás rögzítése", key="-NEW-", expand_x=True, font=("Arial", 14)), ],
	[sg.Button("Foglalások listája", key="-LIST-", expand_x=True, font=("Arial", 14)), ],
	[sg.Button("Statisztika", key="-STAT-", expand_x=True, font=("Arial", 14)), ],
	[sg.Button("Kilépés", key="-EXIT-", expand_x=True, font=("Arial", 14)), ],
]

window = sg.Window('Foglalás - MENÜ', layout, resizable=False, size=(200, 170))

while True:
	event, values = window.read()
	print(event, values)

	match event:
		case sg.WIN_CLOSED | "-EXIT-": break
		case "-NEW-": new_record.run()
		case "-LIST-": list_records.run()

window.close()
