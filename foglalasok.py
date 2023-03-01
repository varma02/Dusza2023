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
			sg.Text("Asztalfoglalási napló", font=('Arial', 18)),
		],
		[
			sg.Table(
				values=frender,
				headings=[
					"Név",
					"Dátum",
					"Székek",
					"Asztalok"
				],
				# expand_x=True,
				expand_y=True,
				# auto_size_columns=True,
				vertical_scroll_only=True
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

	window = sg.Window('Foglalás - Rögzítés', layout=layout, resizable=False, size=(600, 200))
	
	while True:
		event, values = window.read()
		print(event, values)

		match event:
			case sg.WIN_CLOSED | "-EXIT-": break

	# window.close()

if __name__ == "__main__":
	run()