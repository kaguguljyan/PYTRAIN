a_text = "/home/kseniya/PYTRAIN/W04/text.txt"  # путь к файлу, из которого читаем
b_file = "/home/kseniya/PYTRAIN/W04/file.txt"  # путь к файлу, в который записываем

try:  # для обработки ошибок
    with open(a_text, "r") as a:  # открываем и читаем из первого файла
        c = a.read()  # возвращаем строку

    with open(b_file, "w") as b:  # открываем и записываем во второй файл
        b.write(c)  # записываем строку

    print("Данные успешно записаны в файл!")

except FileNotFoundError:  # ошибка, файл не найден
    print("Ошибка: файл не найден!")

except Exception as e:  # ошибка
    print(f"Произошла ошибка: {e}")

finally:
    print("Проверка завершена")
