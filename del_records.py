import PySimpleGUI as sg
from datetime import datetime
import db

def run():
	reca = db.get_records(datetime.now().year, filter_canceled=False, filter_today=False)
	rndr = []
	for Item in reca: 
		dct = Item.__dict__
		print(dct)
		dt = dct["start"]
		rndr.append([
			sg.Text(dct["name"], font=("Arial", 14)),
			sg.Text(" "),
			sg.Text(f"{dt.strftime('%m. %d. %H:%M')}", font=("Arial", 11)),
			sg.Text("", expand_x=True),
			sg.Button("Törlés", button_color=('white', "red"), key="-SAVE-", font=("Arial", 12)),
        ])
      

	window = sg.Window('Foglalás - Törlés', [
		[sg.Column(
            layout=rndr,
            scrollable=True,
	        vertical_scroll_only=True,
            expand_x=True,
            expand_y=True
        ),]
	], resizable=False, size=(600, 200))
	
	window.finalize()

	while True:
		event, values = window.read()
		print(event, values)

		match event:
			case sg.WIN_CLOSED | "-EXIT-": break
				
					

	window.close()

if __name__ == "__main__":
	run()