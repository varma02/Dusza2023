import PySimpleGUI as sg
import new_record, list_records, del_records, stats, table_map

layout = [
	[sg.Button("Foglalás rögzítése", key="-NEW-", expand_y=True, expand_x=True, font=("Arial", 14)), ],
	[sg.Button("Foglalás törlése", key="-DEL-", expand_y=True, expand_x=True, font=("Arial", 14)), ],
	[sg.Button("Foglalások listája", key="-LIST-", expand_y=True, expand_x=True, font=("Arial", 14)), ],
	[sg.Button("Asztaltérkép", key="-TABLEMAP-", expand_y=True, expand_x=True, font=("Arial", 14)), ],
	[sg.Button("Statisztika", key="-STAT-", expand_y=True, expand_x=True, font=("Arial", 14)), ],
	[sg.Button("Kilépés", key="-EXIT-", expand_y=True, expand_x=True, font=("Arial", 14)), ],
]

window = sg.Window('Foglalás - MENÜ', layout, resizable=True, size=(200, 270))
window.finalize()
window.set_min_size((200, 270))

while True:
	event, values = window.read()
	print(event, values)

	match event:
		case "-NEW-": new_record.run()
		case "-DEL-": del_records.run()
		case "-LIST-": list_records.run()
		case "-TABLEMAP-": table_map.run()
		case "-STAT-": stats.run()
		case sg.WIN_CLOSED | "-EXIT-": break

window.close()
