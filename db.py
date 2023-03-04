from datetime import datetime
import glob

DATA_DIR = "./data/"

class Record():
	def __init__(self, name:str, type:str, start:datetime, end:datetime, chairs:int, tables:list[int]):
		self.name = name
		self.type = type
		self.start = start
		self.end = end
		self.chairs = chairs
		self.tables = tables

class Table():
	def __init__(self, id:int, chairs:int, type:str):
		self.id = id
		self.chairs = chairs
		self.type = type


def _read_db(year:int) -> list[Record]:
	path = f"{DATA_DIR}/foglalasok/{year}.txt"
	records: list[Record] = []
	with open(path, "r", encoding="utf-8") as f:
		for line in f.readlines():
			line = line.split(";")
			if len(line) < 6: continue

			records.append(Record(
				name = line[0],
				type = line[1],
				start = datetime.strptime(f"{year}-{line[2]}", "%Y-%m-%d %H:%M"),
				end = datetime.strptime(f"{year}-{line[2][:5]} {line[3]}", "%Y-%m-%d %H:%M"),
				chairs = int(line[4]),
				tables = [int(x) for x in line[5:]]
			))
	return records

def append_db(record:Record) -> None:
	""" Appends a record at the end of the database.
	`record`: A db.Record object
	"""
	path = f"{DATA_DIR}/foglalasok/{record.start.year}.txt"
	if glob.glob(path):
		with open(path, "a", encoding="utf-8") as f:
			f.write(f"\n{record.name};{record.type};{record.start.strftime('%m-%d %H:%M')};{record.end.strftime('%H:%M')};{record.chairs};{';'.join(map(lambda x: str(x.id),record.tables))}")
	else:
		with open(path, "w", encoding="utf-8") as f:
			f.write(f"{record.name};{record.type};{record.start.strftime('%m-%d %H:%M')};{record.end.strftime('%H:%M')};{record.chairs};{';'.join(map(lambda x: str(x.id),record.tables))}")


def get_tables() -> list[Table]:
	""" Returns a list of all tables. """
	tables: list[Table] = []
	with open(f"{DATA_DIR}/asztalok.txt", "r", encoding="utf-8") as f:
		for line in f.readlines():
			line = line.strip().split(";")
			tables.append(Table(
				id = int(line[0]),
				chairs = int(line[1]),
				type = line[2],
			))
	return tables

def get_records(year:int=None, filter_canceled=False, filter_today=False):
	""" By default it returns a list of non canceled records from the current year.
	`year`: the year to get records from
	`filter_canceled`: if true, only returns records that were canceled
	`filter_today`: if true, only returns records that have the current date as start time
	"""
	records = _read_db(year if year else datetime.now().year)
	if filter_today: 
		records = list(filter(lambda x: x.start.date() == datetime.now().date(), records))

	canceled = list(filter(lambda x: x.type == "L", records))

	if filter_canceled:
		return canceled
	else:
		not_canceled_records: list[Record] = []
		for r in records:
			for c in canceled:
				if (c.name == r.name and c.start == r.start):
					break
			else:
				not_canceled_records.append(r)
		return not_canceled_records


def get_years() -> list[int]:
	""" Returns a list of all years that are in the database.
	"""
	return list(map(lambda x: int(x[:-4]), glob.glob("*.txt", root_dir=f"{DATA_DIR}/foglalasok/", recursive=False)))

def intersect_records(start:datetime, end:datetime, records:list[Record]):
	intersecting_records:list[Record] = []
	for r in records:
		if max(r.start, start) <= min(r.end, end):
			intersecting_records.append(r)
	return intersecting_records

def reserve_table(name:str, start:datetime, end:datetime, chairs:int, type:str = None) -> list[Table] | bool:
	""" Returns a list of tables to be reserved. Or if there are not enough of tables, it returns an empty list and if the person alredy reserved in this interval, it returns false.
	"""
	records = get_records(start.year)
	intersecting_records = intersect_records(start, end, records)

	for r in intersecting_records:
		if r.name == name:
			return False

	reserved_tables = [t for r in intersecting_records for t in r.tables]
	
	if type:
		tables = [x for x in get_tables() if x.type == type and x.id not in reserved_tables]
	else:
		tables = [x for x in get_tables() if x.id not in reserved_tables]
	tables.sort(key=lambda x: x.chairs)
	print(tables)
	print(reserved_tables)
	print(intersecting_records)

	for t in tables:
		if t.chairs >= chairs:
			return [t,]

	reserving = []
	table_seats = 0
	while len(tables) > 0:
		table = tables.pop(0)
		chairs -= table_seats + table.chairs - 2 if table_seats > 2 and table.chairs > 2 else table_seats + table.chairs
		reserving.append(table)

		if chairs <= 0: return reserving
	
	return []
