import PySimpleGUI as sg

menu_layout = [
	[sg.Button("Foglalás rögzítése", key="-REC-", expand_x=True), ],
	[sg.Button("Foglalás törlése", key="-DEL-", expand_x=True), ],
	[sg.Button("Statisztika", key="-STAT-", expand_x=True), ],
	[sg.Button("Kilépés", key="-EXIT-", expand_x=True), ],
]

window = sg.Window('Foglalás - MENÜ', menu_layout, resizable=False, size=(200, 140))

while True:
	event, values = window.read()
	print(event, values)

	match event:
		case sg.WIN_CLOSED | "-EXIT-": break

window.close()
