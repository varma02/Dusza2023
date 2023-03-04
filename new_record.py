import PySimpleGUI as sg
from datetime import datetime
import db

def _popup_ok(text:str):
	return sg.PopupOK(text, title="Hiba", no_titlebar=True, grab_anywhere=True, keep_on_top=True, font=("Arial", 14, "bold"))

def _validate_input(values) -> bool:
	if values["-NAME-"].strip() == "":
		_popup_ok("Írj be létező nevet!")
		return False

	try: 
		date = datetime.strptime(values["-DATE-"], "%Y/%m/%d").date()
		start_datetime = datetime.combine(date, datetime.strptime(f'{values["-START-H-"]}:{values["-START-M-"]}', "%H:%M").time())
		end_datetime = datetime.combine(date, datetime.strptime(f'{values["-END-H-"]}:{values["-END-M-"]}', "%H:%M").time())
		if start_datetime < datetime.now():
			_popup_ok("Az időpont nem lehet a múltban!")
			return False
		if start_datetime > end_datetime:
			_popup_ok("A kezdő időpont nem lehet a végső előtt!")
			return False
	except ValueError:
		_popup_ok("Létező időpontot adj meg!")
		return False

	try: 
		if int(values["-CHAIR-"]) <= 0:
			raise ValueError()
	except ValueError:
		_popup_ok("A székek száma csak pozitív egész lehet!")
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
				if _validate_input(values):
					start = datetime.strptime(f"{values['-DATE-']} {values['-START-H-']}:{values['-START-M-']}", "%Y/%m/%d %H:%M")
					end = datetime.strptime(f"{values['-DATE-']} {values['-END-H-']}:{values['-END-M-']}", "%Y/%m/%d %H:%M")
					tables = db.reserve_table(
						name = values["-NAME-"],
						start = start,
						end = end,
						chairs = int(values["-CHAIR-"]),
						type = "B" if values["-IN-"] else "K",
					)

					if tables == []:
						waitlist = sg.PopupYesNo("\tNincs elég hely!\nSzeretnél várólistára kerülni?", title="Hiba", no_titlebar=True, grab_anywhere=True, keep_on_top=True, font=("Arial", 14, "bold"))
						if waitlist == "Yes":
							tables = [db.Table(-1, 0, "NA"), ]
						else:
							tables = [db.Table(-2, 0, "NA"), ]
					elif tables == False:
						_popup_ok("Nem foglalhatsz kétszer ugyan arra az időpontra!")
						continue

					db.append_db(db.Record(
						name = values["-NAME-"],
						start = start,
						end = end,
						chairs = int(values["-CHAIR-"]),
						type = "F",
						tables = tables,
					), year=start.year)

					_popup_ok("Foglalás mentve")
					break
					

	window.close()


if __name__ == "__main__":
	run()