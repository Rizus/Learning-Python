"""
r - Open a file for reading. (default)
w - Open a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
x - Open a file for exclusive creation. If the file already exists, the operation fails.
a - Open a file for appending at the end of the file without truncating it. Creates a new file if it does not exist.
t - Open in text mode. (default)
b - Open in binary mode.
+ - Open a file for updating (reading and writing)

file1 = open("test.txt")      # equivalent to 'r' or 'rt'
file1 = open("test.txt",'w')  # write in text mode
file1 = open("img.bmp",'r+b') # read and write in binary mode

"""

# Reading Files
# open a file
file1 = open('../Learning-Python/File_Operation/test.txt')

# read the file
read_content = file1.read()
print(read_content)
# close the file
file1.close()
# Output: This is a test file.
# Output: Hello from the test file.

# Обработка исключений в файлах
try:
    file21 = open('../Learning-Python/File_Operation/test.txt')
    read_content = file21.read()
    print(read_content)
finally:
    # close the file
    file21.close()


# Использование with...open Синтаксис
with open('..//Learning-Python/File_Operation/test.txt') as file2:
    read_content = file2.read()
    print(read_content)

# Запись в файлы в Python
# Есть две вещи, которые нам нужно помнить при записи в файл.
# 1 - Если мы попытаемся открыть несуществующий файл, будет создан новый файл.
# 2 - Если файл уже существует, его содержимое стирается, а в файл добавляется новое содержимое.

with open('../Learning-Python/File_Operation/test2.txt', 'w') as my_test_file:
    # write contents to the test2.txt file
    my_test_file.write("Добро пожаловать в АД!\n")
    my_test_file.write("АД уже давно наступил!")
with open('../Learning-Python/File_Operation/test2.txt') as my_test_file:
    read_content = my_test_file.read()
    print(read_content)

"""

close()             - Closes an opened file. It has no effect if the file is already closed.
detach()            - Separates the underlying binary buffer from the TextIOBase and returns it.
fileno()            - Returns an integer number (file descriptor) of the file.
flush()             - Flushes the write buffer of the file stream.
isatty()            - Returns True if the file stream is interactive.
read(n)             - Reads at most n characters from the file. Reads till end of file if it is negative or None.
readable()          - Returns True if the file stream can be read from.
readline(n=-1)              - Reads and returns one line from the file. Reads in at most n bytes if specified.
readlines(n=-1)             - Reads and returns a list of lines from the file. Reads in at most n bytes/characters if specified.
seek(offset,from=SEEK_SET)  - Changes the file position to offset bytes, in reference to from (start, current, end).
seekable()                  - Returns True if the file stream supports random access.
tell()                      - Returns an integer that represents the current position of the file's object.
truncate(size=None)         - Resizes the file stream to size bytes. If size is not specified, resizes to current location.
writable()                  - Returns True if the file stream can be written to.
write(s)                    - Writes the string s to the file and returns the number of characters written.
writelines(lines)           - Writes a list of lines to the file.

"""


# from pathlib import Path

# entries = Path('../Learning-Python/')
# for entry in entries.iterdir():
#     print(entry.name)
