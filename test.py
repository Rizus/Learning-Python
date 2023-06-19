import os
import re


def rename_file(file_path):
    # Получаем базовое имя файла
    file_name = os.path.basename(file_path)

    # Удаляем все лишние символы из имени файла
    new_file_name = re.sub(r'[^\w\s.-]', '', file_name)

    # Получаем путь к директории файла
    directory = os.path.dirname(file_path)

    # Формируем новый путь для переименованного файла
    new_file_path = os.path.join(directory, new_file_name)

    try:
        # Переименовываем файл
        os.rename(file_path, new_file_path)
        print(f"Файл успешно переименован в {new_file_name}")
    except OSError as e:
        print(f"Ошибка при переименовании файла: {e}")


# Получаем текущий путь, где находится запущенный файл
file_path = os.getcwd()
rename_file(file_path)


# Формируем полный путь к файлу
file_name = "название_файла.txt"
file_path = os.path.join(current_path, file_name)

# Вызываем функцию для переименования файла
rename_file(file_path)