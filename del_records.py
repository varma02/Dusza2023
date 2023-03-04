import PySimpleGUI as sg
from datetime import datetime
import db

def generate_layout(year, query:str = None):
	layout = []
	records = db.get_records(year, filter_canceled=False, filter_today=False)
	for index, item in enumerate(records): 
		if (not query) or (item.name.lower().strip().find(query.lower().strip()) != -1):
			layout.append([
				sg.Text(item.name, font=("Arial", 11, "bold")),
				sg.Text(f"{item.start.strftime('%Y/%m/%d %H:%M')} - {item.end.strftime('%H:%M')}", expand_x=True, font=("Arial", 11)),
				sg.Button("Lemondás", button_color=('white', "red"), key=f"-DEL-{index}-", font=("Arial", 12)),
			])

	return [
		[
			sg.Text("Foglalás lemondása", font=('Arial', 18), expand_x=True),
			sg.Input(query, key="-QUERY-", enable_events=True, size=(15, None)),
			sg.InputCombo(db.get_years(), year, key="-YEAR-", enable_events=True),
			sg.Button("Keresés", key="-SEARCH-"),
		],[sg.Column(
			layout=layout,
			scrollable=True,
			vertical_scroll_only=True,
			expand_x=True,
			expand_y=True,
			key="-LIST-",
		),]
	]


def create_window(year, query):
	window = sg.Window(
		title = 'Foglalás - Lemondás', 
		layout = generate_layout(year, query), 
		resizable = True, 
		size = (600, 300))
	window.finalize()
	window.set_min_size((470, 150))
	return window



def run():    
	query = ""
	year = datetime.now().year
	window = create_window(year, query)

	while True:
		event, values = window.read()
		print(event, values)

		match event:
			case "-SEARCH-":
				window.close()
				window = create_window(year, query)
			case "-QUERY-": query = values["-QUERY-"]
			case "-YEAR-": year = values["-YEAR-"]
			case sg.WIN_CLOSED | "-EXIT-": break

		if event.startswith("-DEL-"):
			raise Exception("TODO: Implement record deletion")

	window.close()

if __name__ == "__main__":
	run()