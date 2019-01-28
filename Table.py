class table:
	"""Generate and save tables to text files."""
	def __init__(self):
		self.columns = []
		self.rows = []
		self.widths = []

	def setColumns(self, *columns):
		"""
		Set table columns. Multiple columns can be added at once. Column names must be strings.
		"""
		self.columns = []
		for column in columns:
			if type(column) != str:
				raise TypeError("Column names must be strings.")

			if column in self.columns:
				raise TableError("Column already exists: "+str(format))
			else:
				self.columns.append(column)

	def addRow(self, *items):
		"""
		Add row to table.
		"""
		if len(self.columns) == 0:
			raise TableError("Cannot add rows to a table with no columns.")

		self.rows.append(items)

	def save(self, file, **kwargs):
		"""
		Writes the table to file.

		Args;
			<file>		-	File to write table to.
			[fileMode]	-	Whether to append, overwrite or create a file. Defaults to x.
				x	-	Create. Throws an error if file already exists,
				a	-	Append. Creates a file if it doesn't exist,
				w	-	Write. Overwrites the file, or creates it if it doesn't already exist.
			[tableType]	-	The formatting used for the table. Defaults to ASCII.
				ASCII	- Simple text.
				Reddit	- A table using Reddit's markdown.
			[alignment]	-	Reddit mode only. List of "L", "R", and/or "C", used to specify the column alignment.
		"""
		fileMode = kwargs.get("fileMode", "x")
		tableType = kwargs.get("tableType", "ASCII")
		alignment = kwargs.get("alignment", None)

		outputFile = open(file, fileMode)
		
		###Calculate column widths
		#Find initial column widths
		for column in self.columns:
			width = findLargestMultiple(len(column)+1, 4)
			self.widths.append(width)

		if tableType.lower() == "ASCII".lower():
			#Find item widths
			for row in self.rows:
				for item in range(len(row)):
					if len(row[item])+1 > self.widths[item]:
						self.widths[item] = findLargestMultiple(len(row[item]), 4)

			#Draw table
			line = "-"*(sum(self.widths)+len(self.columns)+5)+"\n"
			tableString = "" + line
			for column in range(len(self.columns)):
				spaceCount = self.widths[column]
				spaceCount-= len(self.columns[column])
				tableString += "| " + self.columns[column] + " "*spaceCount
			tableString+= "|\n"
			tableString+= line

			for row in self.rows:
				for item in range(len(row)):
					spaceCount = self.widths[item] - len(row[item])
					tableString += "| " + str(row[item]) + " "*spaceCount
				if len(row) < len(self.columns):
					for item in range(len(row), len(self.columns)):
						tableString += "| " + " "*self.widths[item]

				tableString+= "|\n"

		elif tableType.lower() == "Reddit".lower():
			#Create tablestring. Spaces are irrelevant because Reddit does that for us.
			tableString = "|"
			header1 = header2 = ""
			if alignment == None:
				alignment = [":--|" for x in range(len(self.columns))]

			for i in range(len(self.columns)):
				header1+= ("**"+self.columns[i]+"**|")
				header2+=alignment[i]
			tableString+= header1 +"\n" + header2 + "\n"
			for row in self.rows:
				tableString+="|"
				for item in row:
					tableString+= (item+"|")
				tableString+="\n"


		outputFile.write(tableString)

	def sort(self, column, ascending=False):
		"""
		Sort a column.

		Args;
			ascending	-	If true, will sort ascending instead of descending
		"""
		if column not in self.columns:
				raise TableError("No such column: "+str(column))

		column = self.columns.index(column)
		self.rows = sorted(self.rows, key=lambda item: item[column], reverse=ascending)

class TableError(ValueError):
	pass

def findLargestMultiple(num, multiple):
	var = num % multiple
	num+= multiple-var
	return num