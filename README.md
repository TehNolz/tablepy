# TablePy

(I couldn't think of a better name)

A module to generate text-based tables and save them to a text file.

## Usage

### Creation

Create a table object;

```python
example = table()
```

### Columns

Table columns can be set at any time, even if there's already rows present.

Set its columns;

```python
example.setColumns("1", "2", "3", "4")
```

### Rows

Table rows can be added at any time. If a row contains more items than there are columns, the extra items will not show up when saving the table.

Add rows;

```python
example.addRow("a", "b", "c", "d")
example.addRow("green", "blue", "yellow", "red")
```

### Sort

Sort the table by the specified column, either ascending or descending. Default is descending.

```python
example.sort("1")
#or
example.sort("1", ascending=False)
```

Ascending;

```python
example.sort("1", ascending=True)
```

### Saving

Once you finish adding columns and rows to the table, you can save it to file.

Save table to "example.txt". Will create a file if it doesn't exist, otherwise returns an error.

```python
example.save("example.txt")
#or;
example.save("example.txt", fileMode="x")
```

Append table to "example.txt";

```python
example.save("example.txt", fileMode="a")
```

Save table to "example.txt", and overwrite it if it already exists;

```python
example.save("example.txt", fileMode="w")
```