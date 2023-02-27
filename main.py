import PySimpleGUI as sg

menu_layout = [
	[sg.Button("Foglalás rögzítése", expand_x=True), ],
	[sg.Button("Foglalás törlése", expand_x=True), ],
	[sg.Button("Statisztika", expand_x=True), ],
	[sg.Button("Kilépés", expand_x=True), ],
]

window = sg.Window('Foglalás Rögzítése', menu_layout, resizable=True, finalize=True)
window.set_min_size((200, 140))

while True:
	event, values = window.read()
	print(event, values)
	if event == sg.WIN_CLOSED:
		break

window.close()
