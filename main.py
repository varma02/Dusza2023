import PySimpleGUI as sg
import new_record, list_records, del_records, stats

layout = [
	[sg.Button("Foglalás rögzítése", key="-NEW-", expand_x=True, font=("Arial", 14)), ],
	[sg.Button("Foglalás törlése", key="-DEL-", expand_x=True, font=("Arial", 14)), ],
	[sg.Button("Foglalások listája", key="-LIST-", expand_x=True, font=("Arial", 14)), ],
	[sg.Button("Statisztika", key="-STAT-", expand_x=True, font=("Arial", 14)), ],
	[sg.Button("Kilépés", key="-EXIT-", expand_x=True, font=("Arial", 14)), ],
]

window = sg.Window('Foglalás - MENÜ', layout, resizable=False, size=(200, 210))

while True:
	event, values = window.read()
	print(event, values)

	match event:
		case "-NEW-": new_record.run()
		case "-DEL-": del_records.run()
		case "-LIST-": list_records.run()
		case "-STAT-": stats.run()
		case sg.WIN_CLOSED | "-EXIT-": break

window.close()
