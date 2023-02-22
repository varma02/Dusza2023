import PySimpleGUI as sg
sg.theme('DarkBlue14')   # Add a little color to your windows
# All the stuff inside your window. This is the PSG magic code compactor...
layout = [  [sg.Text('Some text on Row 1')],
						[sg.Text('Enter something on Row 2'), sg.InputText()],
						[sg.OK(), sg.Cancel()]]

# Create the Window
window = sg.Window('Window Title', layout, no_titlebar=True, )
# Event Loop to process "events"
while True:             
	event, values = window.read()
	print(event, values)

	if event in (sg.WIN_CLOSED, 'Cancel'):
		break
	

window.close()