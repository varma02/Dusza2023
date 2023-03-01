import PySimpleGUI as sg
from old import db
import datetime

def prn(num):
	n = str(num)

	if len(n) == 1:
		return f'0{n}'
	else:
		return f'{n}'

def all():
	foglalasok = db.readRealFoglalasok()
	frender = []
	for Item in foglalasok:
		frender.append(
			[
				f'{ Item["nev"] }',
				f'{ prn(Item["kezdet"]["honap"]) }.{prn(Item["kezdet"]["nap"])}.   {prn(Item["kezdet"]["ora"])}:{prn(Item["kezdet"]["perc"])} - {prn(Item["befejezes"]["ora"])}:{prn(Item["befejezes"]["perc"])}',
				f'{Item["szekek"]}',
				f'{ ", ".join(str(e) for e in Item["asztalok"]) }'
			]
		)
	return frender

def notall():
	now = datetime.datetime.now()
	foglalasok = db.readRealFoglalasok()
	frender = []
	for Item in foglalasok:
		if Item["kezdet"]["honap"] == now.month and Item["kezdet"]["nap"] == now.day:
			frender.append(
				[
					f'{ Item["nev"] }',
					f'{ prn(Item["kezdet"]["honap"]) }.{prn(Item["kezdet"]["nap"])}.   {prn(Item["kezdet"]["ora"])}:{prn(Item["kezdet"]["perc"])} - {prn(Item["befejezes"]["ora"])}:{prn(Item["befejezes"]["perc"])}',
					f'{Item["szekek"]}',
					f'{ ", ".join(str(e) for e in Item["asztalok"]) }'
				]
			)
	return frender

def run():
	layout = [
		[
			sg.Text("Asztalfoglalási napló", font=('Arial', 18), expand_x=True),
			sg.Input("Keresés", size=(20, None), font=('Arial', 12)),
			sg.Checkbox("Csak maiak", font=('Arial', 12))
		],
		[
			sg.Table(values=all(),
				headings=[
					"Név",
					"Dátum",
					"Székek",
					"Asztalok"
				],
				font=('Arial', 12),
				expand_x=True,
				expand_y=True,
				auto_size_columns=True,
				vertical_scroll_only=True,
				row_height=14,
			)
			# sg.Column(
			#     layout=frender,
			#     scrollable=True,
			#     size=(800, 1),
			#     expand_y=True,
			#     vertical_scroll_only=True
			# )
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

	# window.close()

if __name__ == "__main__":
	run()