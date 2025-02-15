NOTES_FILE = "notes.txt"

"""Братцы, это простой код создания заметок. Конечно, лучшие программы на Python мы будем писать на курсе Python)"""

import os  # Добавим os для проверки существования файла


def show_notes():
    """Выводит все заметки с нумерацией"""
    if not os.path.exists(NOTES_FILE):
        print("\nФайл с заметками отсутствует. Добавьте первую заметку.")
        return

    with open(NOTES_FILE, "r", encoding="utf-8") as file:
        notes = file.readlines()
        if notes:
            print("\nВаши заметки:")
            for idx, note in enumerate(notes, 1):  # Добавили нумерацию заметок
                print(f"{idx}. {note.strip()}")
        else:
            print("\nЗаметок пока нет.")


def add_note():
    """Добавляет новую заметку"""
    note = input("Введите заметку: ").strip()
    if note:
        with open(NOTES_FILE, "a", encoding="utf-8") as file:
            file.write(note + "\n")
        print("Заметка сохранена!")
    else:
        print("Нельзя сохранить пустую заметку.")

def main():
    """Основное меню"""
    while True:
        print("\n1. Показать заметки")
        print("2. Добавить заметку")
        print("3. Выйти")
        choice = input("Выберите действие: ").strip()

        if choice == "1":
            show_notes()
        elif choice == "2":
            add_note()
        elif choice == "3":
            print("Выход.")
            break
        else:
            print("Ошибка: выберите правильный номер.")

if __name__ == "__main__":
    main()
