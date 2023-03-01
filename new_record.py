import PySimpleGUI as sg
from datetime import datetime

def _validate_input(values) -> bool:
	if values["-NAME-"].strip() == "":
		sg.PopupOK("Írj be létező nevet!", title="Hiba", no_titlebar=True, grab_anywhere=True, keep_on_top=True, font=("Arial", 14, "bold"))
		return False

	try: 
		date = datetime.strptime(values["-DATE-"], "%Y/%m/%d").date()
		start_datetime = datetime.combine(date, datetime.strptime(f'{values["-START-H-"]}:{values["-START-M-"]}', "%H:%M").time())
		end_datetime = datetime.combine(date, datetime.strptime(f'{values["-END-H-"]}:{values["-END-M-"]}', "%H:%M").time())
		if start_datetime < datetime.now():
			sg.PopupOK("Az időpont nem lehet a múltban!", title="Hiba", no_titlebar=True, grab_anywhere=True, keep_on_top=True, font=("Arial", 14, "bold"))
			return False
		if start_datetime > end_datetime:
			sg.PopupOK("A kezdő időpont nem lehet a végső előtt!", title="Hiba", no_titlebar=True, grab_anywhere=True, keep_on_top=True, font=("Arial", 14, "bold"))
			return False
	except ValueError:
		sg.PopupOK("Létező időpontot adj meg!", title="Hiba", no_titlebar=True, grab_anywhere=True, keep_on_top=True, font=("Arial", 14, "bold"))
		return False

	try: 
		if int(values["-CHAIR-"]) <= 0:
			raise ValueError()
	except ValueError:
		sg.PopupOK("A székek száma csak pozitív egész lehet!", title="Hiba", no_titlebar=True, grab_anywhere=True, keep_on_top=True, font=("Arial", 14, "bold"))
		return False
	
	return True


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
			sg.Combo(list(range(6, 23)), datetime.now().hour+1, key="-START-H-", expand_x=True, font=("Arial", 14)),
			sg.Text(":", font=("Arial", 14, "bold")), 
			sg.Combo(list(range(0, 60)), 0, key="-START-M-", expand_x=True, font=("Arial", 14)),
		],[
			sg.Text("Végső időpont: ", font=("Arial", 14)), 
			sg.Combo(list(range(6, 23)), datetime.now().hour+2, key="-END-H-", expand_x=True, font=("Arial", 14)),
			sg.Text(":", font=("Arial", 14, "bold")), 
			sg.Combo(list(range(0, 60)), 0, key="-END-M-", expand_x=True, font=("Arial", 14)),
		],[
			sg.Text("Székek száma: ", font=("Arial", 14)), 
			sg.Input(key="-CHAIR-", default_text=2, expand_x=True, font=("Arial", 14))
		],[
			sg.Radio("Beltéri", "-radioG1-", key="-IN-", default=True, font=("Arial", 14)),
			sg.Radio("Kültéri", "-radioG1-", key="-OUT-", font=("Arial", 14)),
			sg.Text("", expand_x=True),
			sg.Button("Mégse", key="-EXIT-", font=("Arial", 14)),
			sg.Button("Mentés", key="-SAVE-", font=("Arial", 14)),
		],
	], resizable=False, size=(600, 200))
	
	window.finalize()
	window["-DATE-"].update(datetime.now().strftime("%Y/%m/%d"))

	while True:
		event, values = window.read()
		print(event, values)

		match event:
			case sg.WIN_CLOSED | "-EXIT-": break
			case "-SAVE-":
				_validate_input(values)
				raise Exception("TODO: IMPLEMENT RECORD SAVING")
					

	window.close()
