import os

print(os.getcwd())
# Output: /home/pozdniakov/Desktop/all_my_project/Learning-Python

# change directory
os.chdir('/home/pozdniakov/Desktop/all_my_project/Learning-Python/File_Operation/')
print(os.getcwd())
# Output: /home/pozdniakov/Desktop/all_my_project/Learning-Python/Functions
# change directory
os.chdir('/home/pozdniakov/Desktop/all_my_project/Learning-Python/')
print(os.getcwd())
# Output: /home/pozdniakov/Desktop/all_my_project/Learning-Python/Functions


# change directory
os.chdir('/home/pozdniakov/Desktop/all_my_project/Learning-Python/Functions/')
print(os.getcwd())
# list all sub-directories
print(os.listdir('/home/pozdniakov/Desktop/all_my_project/Learning-Python/Functions/'))
# Output: ['Anonymous_Function(Lambda).py', 'Recursion_Function.py', 'Functions.py', 'Variable_Scope.py']


# Making a new Directory
os.mkdir('Test')
os.listdir()


# Renaming a directory or a file
os.rename('Test', 'New_test')
os.listdir()


# Removing directory or file
# Remove file
# os.remove('test.py')
# Remove directory
os.rmdir('New_test')


# Чтобы удалить непустой каталог, мы можем использовать rmtree()метод внутри shutilмодуль.
# import shutil

# delete "mydir" directory and all of its contents
# shutil.rmtree("mydir")