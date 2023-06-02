import os

path = r"C:\Users\Admin\AppData\Local\Фото"

i = 1

for file_name in os.listdir(path):
    # Имя файла и его формат
    base_name, ext = os.path.splitext(file_name)

    # Нужны файлы определенного формата
    if ext.lower() not in ['.jpg', '.jpeg']:
        continue

    # Полный путь к текущему файлу
    abs_file_name = os.path.join(path, file_name)

    # Полный путь к текущему файлу с новым названием
    new_abs_file_name = os.path.join(path, str(i) + ext)

    os.rename(abs_file_name, new_abs_file_name)

    i += 1
