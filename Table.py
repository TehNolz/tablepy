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
		elif len(items) > len(self.columns):
			raise TableError("Too many items in row.")

		self.rows.append(items)

	def generate(self, file, **kwargs):
		"""
		Writes the table to file.

		Args;
			<file>		-	File to write table to.
			[fileMode]	-	Whether to append, overwrite or create a file.
		"""
		padding = kwargs.get("padding", 1)
		fileMode = kwargs.get("fileMode", "x")
		outputFile = open(file, fileMode)
		
		###Calculate column widths
		#Find initial column widths
		for column in self.columns:
			width = findLargestMultiple(len(column)+padding+1, 4)
			self.widths.append(width)

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
			tableString+= "|\n"

		outputFile.write(tableString)

class TableError(ValueError):
	pass

def findLargestMultiple(num, multiple):
	var = num % multiple
	num+= multiple-var
	return num

#Example
tableTest = table()
tableTest.setColumns("1", "2", "3", "455555555555555555555")
tableTest.addRow("a", "b", "c", "d")
tableTest.generate("test.txt", fileMode="w")