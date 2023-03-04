import PySimpleGUI as sg
from datetime import date, datetime
import db

def run():
	while True:
		try:
			"""
			dateStartH = int(input("Kezdő hónap: "))
			dateStartD = int(input("Kezdő nap: "))
			dateEndH = int(input("Végző hónap: "))
			dateEndD = int(input("Végző nap: "))
			"""
			dateStartH = 1
			dateStartD = 1
			dateEndH = 12
			dateEndD = 12
			if date(datetime.now().year, dateStartH, dateStartD) > date(datetime.now().year, dateEndH, dateEndD):
				raise ValueError
			else:
				dateStart = date(datetime.now().year, dateStartH, dateStartD)
				dateEnd = date(datetime.now().year, dateEndH, dateEndD)
			break
		except ValueError:
			print("Helytelen dátumok!")
			continue
	
	recordsInRange = []
	for record in db.get_records(): 
		if dateStart <= date(record.start.year, record.start.month, record.start.day) <= dateEnd:
			recordsInRange.append(record)
	for record in db.get_records(filter_canceled=True):
		if dateStart <= date(record.start.year, record.start.month, record.start.day) <= dateEnd:
			recordsInRange.append(record)
	
	#for i in recordsInRange:
	#    print(type(i.tables))

	pairs = []
	for record in recordsInRange:
		if record.tables[0] == -1:
			for checkRecord in recordsInRange:
				if checkRecord != record and (record.name == checkRecord.name and record.start == checkRecord.start):
					pairs.append([record, checkRecord])
	
	#for i in pairs:
	#    print(i[0].start, i[0].tables, "   ", i[1].start, i[1].tables)


	# Change 2023.txt for optimization!
	outsideRecords = []
	insideRecords = []
	for records in pairs:
		for table in db.get_tables():
			if records[1].tables[0] == table.id and table.type == "K": 
				outsideRecords.append(records[0])
				outsideRecords.append(records[1])
			elif records[1].tables[0] == table.id and table.type == "B":
				insideRecords.append(records[0])
				insideRecords.append(records[1])
	
	for record in recordsInRange:
		for table in db.get_tables():
			if record.tables[0] == table.id and table.type == "K" and record not in outsideRecords:
				outsideRecords.append(record)
			elif record.tables[0] == table.id and table.type == "B" and record not in insideRecords:
				insideRecords.append(record)

	for i in recordsInRange:
		print(i.tables)
	print()
	for i in outsideRecords:
		print(i.tables)
	print()
	for i in insideRecords:
		print(i.tables)
	
	_createWindow()



	"""
	records = {"In": {"cancelled" : [], "not_cancelled" : []},
			  "Out": {"cancelled" : [], "not_cancelled" : []}}

	for i in db.get_records():
		print(f"{i.tables} Correct")
	for i in db.get_records(filter_canceled=True):
		print(f"{i.tables} Cancelled")

	for not_cancelled_records in db.get_records():
		if dateEnd >= date(not_cancelled_records.start.year, not_cancelled_records.start.month, not_cancelled_records.start.day) >= dateStart:
			for tables in db.get_tables():
				if tables.id == not_cancelled_records.tables[0]:
					if tables.type == "B": records["In"]["not_cancelled"].append(not_cancelled_records)
					else: records["Out"]["not_cancelled"].append(not_cancelled_records)

	for cancelled_records in db.get_records(filter_canceled=True):
		if dateEnd >= date(cancelled_records.start.year, cancelled_records.start.month, cancelled_records.start.day) >= dateStart:
			for tables in db.get_tables():
				if tables.id == cancelled_records.tables[0]:
					if tables.type == "B": records["In"]["cancelled"].append(cancelled_records)
					else: records["Out"]["cancelled"].append(cancelled_records)
	

	reservationNum = (len(records["In"]["cancelled"]) * 2 + 
					  len(records["In"]["not_cancelled"]) + 
					  len(records["Out"]["cancelled"]) * 2 + 
					  len(records["Out"]["not_cancelled"]))
	_minus = 0
	for record in records["In"]["not_cancelled"]:
		if checkDuplication(record, records["In"]["not_cancelled"]): _minus += 1
	for record in records["Out"]["not_cancelled"]:
		if checkDuplication(record, records["Out"]["not_cancelled"]): _minus += 1
	
	reservationNum -= _minus
	print(reservationNum)


	
	#print(reservationNum) #Összes foglalási igény

def checkDuplication(recordCheck, records):
	_count = 0
	for record in records:
		if recordCheck.name == record.name:
			if recordCheck.start == record.start:
				_count += 1
	if _count > 1: return True
	else: return False """

def _createWindow():
	layout = [
		[sg.Text("Külső")],
		[sg.Text("  Foglalási igények száma: "), sg.Text("PLACEHOLDER")],
		[sg.Text("  Azonnal teljesített foglalások: "), sg.Text("PLACEHOLDER")],
		[sg.Text("  Várólistás foglalások száma: "), sg.Text("PLACEHOLDER")],
		[sg.Text("    Ebből teljesített: "), sg.Text("PLACEHOLDER")],
		[sg.Text("  Lemondott foglalások száma: "), sg.Text("PLACEHOLDER")],
		[sg.Text("  Nem teljesített foglalások száma: "), sg.Text("PLACEHOLDER")],
		[sg.Text("")],
		[sg.Text("Belső")],
		[sg.Text("  Foglalási igények száma: "), sg.Text("PLACEHOLDER")],
		[sg.Text("  Azonnal teljesített foglalások: "), sg.Text("PLACEHOLDER")],
		[sg.Text("  Várólistás foglalások száma: "), sg.Text("PLACEHOLDER")],
		[sg.Text("    Ebből teljesített: "), sg.Text("PLACEHOLDER")],
		[sg.Text("  Lemondott foglalások száma: "), sg.Text("PLACEHOLDER")],
		[sg.Text("  Nem teljesített foglalások száma: "), sg.Text("PLACEHOLDER")]]
	window = sg.Window("Statistics", layout)

	while True:
		event, values = window.read()
		match event:
			case sg.WIN_CLOSED | "-EXIT-": break