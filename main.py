FILE_NAME = "notes.txt"

"""Братцы, это простой код создания заметок. Конечно лучшие программы на Пайтоне, мы будем писать на курсе Пайтона)"""


def show_notes():
    """Выводит все заметки"""
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            notes = file.readlines()
            if notes:
                print("\nВаши заметки:")
                for note in notes:
                    print(f"- {note.strip()}")
            else:
                print("\nЗаметок пока нет.")
    except FileNotFoundError:
        print("\nФайл с заметками отсутствует. Добавьте первую заметку.")

def add_note():
    """Добавляет новую заметку"""
    note = input("Введите заметку: ").strip()
    if note:
        with open(FILE_NAME, "a", encoding="utf-8") as file:
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
