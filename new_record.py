import PySimpleGUI as sg
from datetime import datetime

import utils

def run():

	window = sg.Window('Foglalás - Rögzítés', [
		[
			sg.Text("Vendég neve: ", font=("Arial", 14)), 
			sg.Input(key="-NAME-", expand_x=True, font=("Arial", 14))
		],[
			sg.CalendarButton("Válassz dátumot", target="-DATE-", font=("Arial", 14), format="%Y/%m/%d"), 
			sg.Input(key="-DATE-", expand_x=True, font=("Arial", 14), enable_events=True)
		],[
			sg.Text("Kezdő időpont: ", font=("Arial", 14)), 
			sg.Combo(list(range(6, 23)), 6, key="-START-H-", expand_x=True),
			sg.Text(":", font=("Arial", 14, "bold")), 
			sg.Combo(list(range(0, 60)), 0, key="-START-M-", expand_x=True),
		],[
			sg.Text("Végső időpont: ", font=("Arial", 14)), 
			sg.Input(key="-END-", expand_x=True, font=("Arial", 14))
		],[
			sg.Text("Székek száma: ", font=("Arial", 14)), 
			sg.Input(key="-CHAIR-", expand_x=True, font=("Arial", 14))
		],[
			sg.Radio("Beltéri", "-radioG1-", key="-IN-", default=True, font=("Arial", 14)),
			sg.Radio("Kültéri", "-radioG1-", key="-OUT-", font=("Arial", 14)),
			sg.Text("", expand_x=True),
			sg.Button("Mégse", key="-EXIT-", font=("Arial", 14)),
			sg.Button("Mentés", key="-SAVE-", font=("Arial", 14)),
		],
	], resizable=False, size=(600, 200))
	
	while True:
		event, values = window.read()
		print(event, values)

		match event:
			case sg.WIN_CLOSED | "-EXIT-": break
			case "-SAVE-":
				# --- ERROR CHECKING ---
				if values["-NAME-"].strip() == "":
					sg.PopupOK("Írj be létező nevet!", title="Hiba", no_titlebar=True, grab_anywhere=True, keep_on_top=True, font=("Arial", 14, "bold"))
					continue
				
				try: datetime.strptime(values["-DATE-"], "%Y/%m/%d")
				except ValueError:
					sg.PopupOK("Írj be létező dátumot!", title="Hiba", no_titlebar=True, grab_anywhere=True, keep_on_top=True, font=("Arial", 14, "bold"))
					continue

	window.close()
