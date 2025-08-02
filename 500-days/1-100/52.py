import csv
# StringIO lets us treat a string like a file (needed because csv expects a file-like object).
from io import StringIO
data = "a,b\n1,2\n3,4"
# csv.DictReader reads each row as a dictionary using the first row as keys.
reader = csv.DictReader(StringIO(data))
print(next(reader)['b'])
