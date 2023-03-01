import PySimpleGUI as sg
from datetime import datetime
import db

# def prn(num):
# 	n = str(num)

# 	if len(n) == 1:
# 		return f'0{n}'
# 	else:
# 		return f'{n}'

# def all():
# 	foglalasok = db.readRealFoglalasok()
# 	frender = []
# 	for Item in foglalasok:
# 		frender.append(
# 			[
# 				f'{ Item["nev"] }',
# 				f'{ prn(Item["kezdet"]["honap"]) }.{prn(Item["kezdet"]["nap"])}.   {prn(Item["kezdet"]["ora"])}:{prn(Item["kezdet"]["perc"])} - {prn(Item["befejezes"]["ora"])}:{prn(Item["befejezes"]["perc"])}',
# 				f'{Item["szekek"]}',
# 				f'{ ", ".join(str(e) for e in Item["asztalok"]) }'
# 			]
# 		)
# 	return frender

# def notall():
# 	now = datetime.datetime.now()
# 	foglalasok = db.readRealFoglalasok()
# 	frender = []
# 	for Item in foglalasok:
# 		if Item["kezdet"]["honap"] == now.month and Item["kezdet"]["nap"] == now.day:
# 			frender.append(
# 				[
# 					f'{ Item["nev"] }',
# 					f'{ prn(Item["kezdet"]["honap"]) }.{prn(Item["kezdet"]["nap"])}.   {prn(Item["kezdet"]["ora"])}:{prn(Item["kezdet"]["perc"])} - {prn(Item["befejezes"]["ora"])}:{prn(Item["befejezes"]["perc"])}',
# 					f'{Item["szekek"]}',
# 					f'{ ", ".join(str(e) for e in Item["asztalok"]) }',
# 				]
# 			)
# 	return frender

def render_table(today=False, year=None) -> list | None:
	try:
		return [[
			x.name, x.start.strftime("%Y/%m/%d  %H:%M") + " - " + x.end.strftime("%H:%M"), x.chairs, ", ".join(map(lambda x: str(x), x.tables))
		] for x in db.get_records(year if year else datetime.now().year, filter_today=today)]
	except Exception as e:
		print(e.with_traceback(e.__traceback__))
		return None

def run():
	
	layout = [
		[
			sg.Text("Asztalfoglalási napló", font=('Arial', 18), expand_x=True),
			sg.InputCombo(db.get_years(), datetime.now().year, enable_events=True, key="-FILTER-YEAR-", font=('Arial', 12)),
			sg.Checkbox("Csak maiak", key="-FILTER-TODAY-", enable_events=True, font=('Arial', 12))
		],[
			sg.Table(
				values = render_table(),
				headings = ["Név","Dátum","Székek","Asztalok"],
				key = "-TABLE-",
				font = ('Arial', 12),
				expand_x = True,
				expand_y = True,
				auto_size_columns = True,
				vertical_scroll_only = True,
				row_height = 14,
			)
		]
	]

	window = sg.Window('Foglalás - Lista', layout=layout, resizable=(False, True), size=(600, 300))
	window.finalize()
	window.set_min_size((500, 150))

	while True:
		event, values = window.read()
		print(event, values)

		match event:
			case sg.WIN_CLOSED | "-EXIT-": break
			case "-FILTER-TODAY-" | "-FILTER-YEAR-": 
				window["-TABLE-"].update(values = render_table(values["-FILTER-TODAY-"], values["-FILTER-YEAR-"]))

	window.close()

if __name__ == "__main__":
	run()