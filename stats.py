import PySimpleGUI as sg
from datetime import date, datetime
import db

dateStart = None
dateEnd = None

def _popup_ok(text:str):
	return sg.PopupOK(text, title="Hiba", no_titlebar=True, grab_anywhere=True, 
	keep_on_top=True, font=("Arial", 14, "bold"))

def _dateInput():
	window = sg.Window("Statisztika - Dátumok", [
		[sg.CalendarButton("Válassz kezdő dátumot", target="-DATE1-", font=("Arial", 14), format="%Y/%m/%d"), 
		sg.Input(key="-DATE1-", expand_x=True, font=("Arial", 14), enable_events=True)],
		[sg.CalendarButton("Válassz záró dátumot", target="-DATE2-", font=("Arial", 14), format="%Y/%m/%d"), 
		sg.Input(key="-DATE2-", expand_x=True, font=("Arial", 14), enable_events=True)],
		[sg.Button("Generálás", key="-SAVE-", font=("Arial", 14))]
	])

	global dateStart
	global dateEnd
	while True:
		event, values = window.read()
		match event:
			case sg.WIN_CLOSED | "-EXIT-": break
			case "-SAVE-": 
				if values['-DATE1-'] == "" or values['-DATE2-'] == "": 
					_popup_ok("Hibás dátum.")
				else:
					try:
						dateStart = datetime.strptime(values["-DATE1-"], "%Y/%m/%d").date()
						dateEnd = datetime.strptime(values["-DATE2-"], "%Y/%m/%d").date()
					except ValueError:
						_popup_ok("Létező dátumot adj meg!")
						continue
					if dateStart > dateEnd:
						_popup_ok("A kezdő dátum nem lehet kisebb, mint a befejező dátum!")
					else: break
	window.close()
	

def _recordsQuery(dateStart, dateEnd):
	_recordsInRange = []
	for record in db.get_records(): 
		if dateStart <= date(record.start.year, record.start.month, record.start.day) <= dateEnd:
			_recordsInRange.append(record)
	for record in db.get_records(filter_canceled=True):
		if dateStart <= date(record.start.year, record.start.month, record.start.day) <= dateEnd:
			_recordsInRange.append(record)
	return _recordsInRange

def _makePairs(_recordsInRange):
	_pairs = []
	for record in _recordsInRange:
		if record.tables[0] == -1:
			for checkRecord in _recordsInRange:
				if checkRecord != record and (record.name == checkRecord.name and record.start == checkRecord.start):
					_pairs.append([record, checkRecord])
	return _pairs

def _categorize(_recordsInRange, _pairs):
	_insideRecords = []
	_outsideRecords = []
	_uncategorizedRecords = []
	_insideRecordsNum = 0
	_outsideRecordsNum = 0
	for records in _pairs:
		for table in db.get_tables():
			if records[1].tables[0] == table.id and table.type == "K": 
				_outsideRecords.append(records[0])
				_outsideRecords.append(records[1])
				_outsideRecordsNum += 1
			elif records[1].tables[0] == table.id and table.type == "B":
				_insideRecords.append(records[0])
				_insideRecords.append(records[1])
				_insideRecordsNum += 1
	
	for record in _recordsInRange:
		for table in db.get_tables():
			if record.tables[0] == table.id and table.type == "K" and record not in _outsideRecords:
				_outsideRecords.append(record)
			elif record.tables[0] == table.id and table.type == "B" and record not in _insideRecords:
				_insideRecords.append(record)
			elif (record.tables[0] == -1 or record.tables[0] == -2) and record not in _uncategorizedRecords and record not in (i[0] for i in _pairs):
				_uncategorizedRecords.append(record)
	return [_insideRecords, _outsideRecords, _uncategorizedRecords, _insideRecordsNum, _outsideRecordsNum]



def _createWindow(insideRecordsNUM, outsideRecordsNUM, 
		  uncategorizedRecordsNUM, insideRecordsImFullfilled, 
		  outsideRecordsImFullfilled, insideRecordsWait, 
		  completedInsideWait, outsideRecordsWait,
		  completedOutsideWait, uncategorizedRecordsWait, 
		  resignedInsideReservations, resignedOutsideReservations,
		  uncategorizedRecords):
	layout = [
		[sg.Text("Külső", font=("Arial", 14, "bold"))],
		[sg.Text("  Foglalási igények száma: "), sg.Text(outsideRecordsNUM)],
		[sg.Text("  Azonnal teljesített foglalások: "), sg.Text(outsideRecordsImFullfilled)],
		[sg.Text("  Várólistás foglalások száma: "), sg.Text(outsideRecordsWait)],
		[sg.Text("    Ebből teljesített: "), sg.Text(completedOutsideWait)],
		[sg.Text("  Lemondott foglalások száma: "), sg.Text(resignedOutsideReservations)],
		[sg.Text("")],
		[sg.Text("Belső", font=("Arial", 14, "bold"))],
		[sg.Text("  Foglalási igények száma: "), sg.Text(insideRecordsNUM)],
		[sg.Text("  Azonnal teljesített foglalások: "), sg.Text(insideRecordsImFullfilled)],
		[sg.Text("  Várólistás foglalások száma: "), sg.Text(insideRecordsWait)],
		[sg.Text("    Ebből teljesített: "), sg.Text(completedInsideWait)],
		[sg.Text("  Lemondott foglalások száma: "), sg.Text(resignedInsideReservations)],
		[sg.Text("")],
		[sg.Text("Nem kategorizált", font=("Arial", 14, "bold"))],
		[sg.Text("	Foglalások száma: "), sg.Text(uncategorizedRecordsNUM)],
		[sg.Text("	Várólistás foglalások száma: "), sg.Text(uncategorizedRecordsWait)],
		[sg.Text("	Sikertelen foglalások: "), sg.Text(len(uncategorizedRecords))]
	]
	window = sg.Window("Statistics", layout)

	while True:
		event, values = window.read()
		match event:
			case sg.WIN_CLOSED | "-EXIT-": break
	window.close()

def run():
	_dateInput()
	if not (dateStart or dateEnd):
		return

	recordsInRange = _recordsQuery(dateStart, dateEnd)
	pairs = _makePairs(recordsInRange)
	_categorized = _categorize(recordsInRange, pairs)
	insideRecords = _categorized[0]
	outsideRecords = _categorized[1]
	uncategorizedRecords = _categorized[2]
	insideRecordsNUM = len(insideRecords) - _categorized[3]
	outsideRecordsNUM = len(outsideRecords) - _categorized[4]
	uncategorizedRecordsNUM = len(uncategorizedRecords)

	#2
	insideRecordsImFullfilled = insideRecordsNUM - _categorized[3]
	for record in insideRecords:
		if record.type == "L": insideRecordsImFullfilled -= 1

	outsideRecordsImFullfilled = outsideRecordsNUM - _categorized[4]
	for record in outsideRecords:
		if record.type == "L": outsideRecordsImFullfilled -= 1

	#3
	insideRecordsWait = 0
	for record in insideRecords:
		if record.tables[0] == -1: insideRecordsWait += 1

	outsideRecordsWait = 0
	for record in outsideRecords:
		if record.tables[0] == -1: outsideRecordsWait += 1

	uncategorizedRecordsWait = 0
	for record in uncategorizedRecords:
		if record.tables[0] == -1: uncategorizedRecordsWait += 1

	#4
	resignedInsideReservations = 0
	for record in insideRecords:
		if record.type[0] == "L":
			resignedInsideReservations += 1

	resignedOutsideReservations = 0
	for record in outsideRecords:
		if record.type[0] == "L":
			resignedOutsideReservations += 1

	_createWindow(insideRecordsNUM, outsideRecordsNUM, 
		  uncategorizedRecordsNUM, insideRecordsImFullfilled, 
		  outsideRecordsImFullfilled, insideRecordsWait, 
		  _categorized[3], outsideRecordsWait,
		  _categorized[4], uncategorizedRecordsWait, 
		  resignedInsideReservations, resignedOutsideReservations,
		  uncategorizedRecords)

if __name__ == "__main__":
	run()