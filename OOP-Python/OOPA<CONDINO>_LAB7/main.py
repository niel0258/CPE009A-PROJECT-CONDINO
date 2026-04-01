from FileReaderWriter import FileReaderWriter
from CSVFileReaderWriter import CSVFileReaderWriter
from JSONFileReaderWriter import JSONFileReaderWriter
from TextFileReadWriter import TextFileReadWriter

#Default Case
df = FileReaderWriter()
df.read()
df.write()

#Test the polymorphed methods
c = CSVFileReaderWriter()
c.read("sample.csv")
c.write(filepath="sample2.csv", data=["Hello", "World"])

j = JSONFileReaderWriter()
j.read("sample.json")
j.write(data=['foo', {'bar': ('baz', None, 1.0, 2)}],filepath="sample2.json")

t = TextFileReadWriter()
t.read("sample.txt")
t.write("sample2.txt",["Niel\n","Vincent\n","Condino\n"])