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
			dateEndD = 31
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



def _createWindow(insideRecordsNUM, outsideRecordsNUM, 
		  uncategorizedRecordsNUM, insideRecordsImFullfilled, 
		  outsideRecordsImFullfilled, insideRecordsWait, 
		  completedInsideWait, outsideRecordsWait,
		  completedOutsideWait, uncategorizedRecordsWait, 
		  resignedInsideReservations, resignedOutsideReservations,
		  uncategorizedRecords):
	layout = [
		[sg.Text("Külső")],
		[sg.Text("  Foglalási igények száma: "), sg.Text(outsideRecordsNUM)],
		[sg.Text("  Azonnal teljesített foglalások: "), sg.Text(outsideRecordsImFullfilled)],
		[sg.Text("  Várólistás foglalások száma: "), sg.Text(outsideRecordsWait)],
		[sg.Text("    Ebből teljesített: "), sg.Text(completedOutsideWait)],
		[sg.Text("  Lemondott foglalások száma: "), sg.Text(resignedOutsideReservations)],
		[sg.Text("")],
		[sg.Text("Belső")],
		[sg.Text("  Foglalási igények száma: "), sg.Text(insideRecordsNUM)],
		[sg.Text("  Azonnal teljesített foglalások: "), sg.Text(insideRecordsImFullfilled)],
		[sg.Text("  Várólistás foglalások száma: "), sg.Text(insideRecordsWait)],
		[sg.Text("    Ebből teljesített: "), sg.Text(completedInsideWait)],
		[sg.Text("  Lemondott foglalások száma: "), sg.Text(resignedInsideReservations)],
		[sg.Text("")],
		[sg.Text("Nem kategorizált")],
		[sg.Text("	Foglalások száma: ", sg.Text(uncategorizedRecordsNUM))],
		[sg.Text("	Várólistás foglalások száma: ", sg.Text(uncategorizedRecordsWait))],
		[sg.Text("	Sikertelen foglalások: ", sg.Text(len(uncategorizedRecords)))]
	]
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

	print("Benti recordok száma: ", insideRecordsNUM) #1
	print("Kinti recordok száma: ", outsideRecordsNUM) #1
	print("Nem kategorizált recordok száma: ", uncategorizedRecordsNUM) #1

	insideRecordsImFullfilled = insideRecordsNUM - _categorized[3]
	for record in insideRecords:
		if record.type == "L": insideRecordsImFullfilled -= 1
	print("\nEgyből teljesített benti recordok száma: ", insideRecordsImFullfilled) #2
	outsideRecordsImFullfilled = outsideRecordsNUM - _categorized[4]
	for record in outsideRecords:
		if record.type == "L": outsideRecordsImFullfilled -= 1
	print("Egyből teljesített benti recordok száma: ", outsideRecordsImFullfilled) #2

	insideRecordsWait = 0
	for record in insideRecords:
		if record.tables[0] == -1: insideRecordsWait += 1
	print("\nBenti várólistás recordok száma: ", insideRecordsWait) #3
	print("Mégis teljesített benti várólistás recordok száma: ", _categorized[3]) #3.2
	outsideRecordsWait = 0
	for record in outsideRecords:
		if record.tables[0] == -1: outsideRecordsWait += 1
	print("Kinti várólistás recordok száma: ", outsideRecordsWait) #3
	print("Mégis teljesített kinti várólistás recordok száma: ", _categorized[4]) #3.2
	uncategorizedRecordsWait = 0
	for record in uncategorizedRecords:
		if record.tables[0] == -1: uncategorizedRecordsWait += 1
	print("Nem kategorizált várólistás recordok száma: ", uncategorizedRecordsWait) #3

	resignedInsideReservations = 0
	for i in insideRecords:
		if i.type[0] == "L":
			resignedInsideReservations += 1
	print("\nLemondott benti foglalások: ", resignedInsideReservations) #4
	resignedOutsideReservations = 0
	for i in outsideRecords:
		if i.type[0] == "L":
			resignedOutsideReservations += 1
	print("Lemondott kinti foglalások: ", resignedOutsideReservations) #4
	
	print("\nSikertelen foglalások: ", len(uncategorizedRecords)) #5

	_createWindow(insideRecordsNUM, outsideRecordsNUM, 
		  uncategorizedRecordsNUM, insideRecordsImFullfilled, 
		  outsideRecordsImFullfilled, insideRecordsWait, 
		  _categorized[3], outsideRecordsWait,
		  _categorized[4], uncategorizedRecordsWait, 
		  resignedInsideReservations, resignedOutsideReservations,
		  uncategorizedRecords)

run()