from datetime import datetime

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
	path = f"./data/foglalasok/{year}.txt"
	records: list[Record] = []
	with open(path, "r", encoding="utf-8") as f:
		for line in f.readlines():
			line = line.split(";")
			records.append(Record(
				name = line[0],
				type = line[1],
				start = datetime.strptime(f"{year}-{line[2]}", "%Y-%m-%d %H:%M"),
				end = datetime.strptime(f"{year}-{line[2][:5]} {line[3]}", "%Y-%m-%d %H:%M"),
				chairs = int(line[4]),
				tables = [int(x) for x in line[5:]]
			))
	return records

def _append_db(*records:Record, year:int):
	path = f"./data/foglalasok/{year}.txt"
	open(path, "w", encoding="utf-8").close()
	with open(path, "a", encoding="utf-8") as f:
		for r in records:
			f.write(f"\n{r.name};{r.type};{r.start.strftime('%Y-%m-%d %H:%M')};{r.end.strftime('%H:%M')};{r.chairs};{';'.join(map(lambda x: str(x),r.tables))}")


def get_tables() -> list[Table]:
	""" Returns a list of all tables. """
	tables: list[Table] = []
	with open("./data/asztalok.txt", "r", encoding="utf-8") as f:
		for line in f.readlines():
			line = line.split(";")
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


def add_records(*records:Record):
	raise Exception("TODO: IMPLEMENT NEW RECORD")