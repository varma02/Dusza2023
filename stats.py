"""
import PySimpleGUI as sg
from datetime import date, datetime
import db

def run():
	while True:
		try:
        
			#dateStartH = int(input("Kezdő hónap: "))
			#dateStartD = int(input("Kezdő nap: "))
			#dateEndH = int(input("Végző hónap: "))
			#dateEndD = int(input("Végző nap: "))
            
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
	
	for i in recordsInRange:
		print(i.tables)
	print()	

	pairs = []
	for record in recordsInRange:
		if record.tables[0] == -1:
			for checkRecord in recordsInRange:
				if checkRecord != record and (record.name == checkRecord.name and record.start == checkRecord.start):
					pairs.append([record, checkRecord])


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
	
	#_createWindow()

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

run()
"""

import PySimpleGUI as sg
from datetime import date, datetime
import db


def _dateInput():
	while True:
		try:
        
			#dateStartH = int(input("Kezdő hónap: "))
			#dateStartD = int(input("Kezdő nap: "))
			#dateEndH = int(input("Végző hónap: "))
			#dateEndD = int(input("Végző nap: "))
            
			dateStartH = 1
			dateStartD = 1
			dateEndH = 12
			dateEndD = 12
			if date(datetime.now().year, dateStartH, dateStartD) > date(datetime.now().year, dateEndH, dateEndD):
				raise ValueError
			else:
				global dateStart
				global dateEnd
				dateStart = date(datetime.now().year, dateStartH, dateStartD)
				dateEnd = date(datetime.now().year, dateEndH, dateEndD)
				break
		except ValueError:
			print("Helytelen dátumok!")
			continue

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

def run():
	_dateInput()
	recordsInRange = _recordsQuery(dateStart, dateEnd)
	pairs = _makePairs(recordsInRange)
	_categorized = _categorize(recordsInRange, pairs)
	insideRecords = _categorized[0]
	outsideRecords = _categorized[1]
	uncategorizedRecords = _categorized[2]
	insideRecordsNUM = len(insideRecords) - _categorized[3]
	outsideRecordsNUM = len(outsideRecords) - _categorized[4]
	uncategorizedRecordsNUM = len(uncategorizedRecords)

	print("Benti recordok száma: ", insideRecordsNUM)
	print("Kinti recordok száma: ", outsideRecordsNUM)
	print("Nem kategorizált recordok száma: ", uncategorizedRecordsNUM)

	print("Egyből teljesített benti recordok száma: ", )
	"""
	for i in categories[0]:
		print(i.tables, i.type)
	print()
	for i in categories[1]:
		print(i.tables, i.type)
	print()
	for i in categories[2]:
		print(i.tables, i.type, i.name)
	print()
	"""
run()