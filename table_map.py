import PySimpleGUI as sg
from datetime import datetime
import db

def render_table():
	records = db.intersect_records(datetime.now(), datetime.now(), db.get_records(datetime.now().year))
	all_tables = db.get_tables()
	reserved_tables: list[int] = []
	table = []
	for r in records:
		reserved_tables.extend(r.tables)
		r.tables.sort()
		table.append([
			", ".join(map(lambda x: str(x), r.tables)),
			"Foglalt",
			r.name,
			r.end.strftime("%X"),
		])
	for t in all_tables:
		if t.id not in reserved_tables:
			table.append([
				str(t.id),
				"Szabad",
				"-",
				"-"
			])
	table.sort(key=lambda x: int(x[0].split(",")[0]))
	return table

def run():
	layout = [
		[sg.Text("Asztaltérkép", font=("Arial", 16, "bold")), 
			sg.Text("", expand_x=True), 
			sg.Input("", key="-CLOCK-", readonly=True, size=(8, None), font=("Arial", 16, "bold"))],
		[sg.Table(
			values = render_table(),
			headings = ["Asztal(ok)", "Állapot", "Foglaló", "Foglalás vége"],
			key = "-TABLE-",
			font = ('Arial', 12),
			expand_x = True,
			expand_y = True,
			auto_size_columns = True,
			vertical_scroll_only = True,
			row_height = 18,
		)]
	]

	window = sg.Window('Asztaltérkép', layout, resizable=True, size=(600, 350))
	window.finalize()
	window.set_min_size((500, 300))

	while True:
		event, values = window.read(timeout=1000, timeout_key="-TIMEOUT-")
		print(event, values)

		match event:
			case sg.WIN_CLOSED | "-EXIT-": break

		now = datetime.now().strftime("%X")
		window["-CLOCK-"].update(now)
		if now.endswith(":00"):
			window["-TABLE-"].update(render_table())
		

	window.close()

if __name__ == "__main__":
	run()