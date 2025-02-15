NOTES_FILE = "notes.txt"


import os  


def show_notes():
    """Выводит все заметки с нумерацией"""
    if not os.path.exists(NOTES_FILE) or os.stat(NOTES_FILE).st_size == 0:
        print("\nФайл с заметками пуст. Добавьте первую заметку.")
        return

    with open(NOTES_FILE, "r", encoding="utf-8") as file:
        notes = file.readlines()

    print("\nВаши заметки:")
    for idx, note in enumerate(notes, 1):  
        print(f"{idx}. {note.strip()}")


def add_note():
    """Добавляет новую заметку"""
    note = input("Введите заметку: ").strip()
    if note:
        with open(NOTES_FILE, "a", encoding="utf-8") as file:
            file.write(note + "\n")
        print("✅ Заметка сохранена!")
    else:
        print("⚠ Нельзя сохранить пустую заметку.")


def delete_note():
    """Удаляет заметку по номеру"""
    show_notes()
    if not os.path.exists(NOTES_FILE) or os.stat(NOTES_FILE).st_size == 0:
        print("Файл пуст, удалять нечего.")
        return

    try:
        note_number = int(input("\nВведите номер заметки для удаления: ")) - 1
        with open(NOTES_FILE, "r", encoding="utf-8") as file:
            notes = file.readlines()

        if 0 <= note_number < len(notes):
            del notes[note_number]
            with open(NOTES_FILE, "w", encoding="utf-8") as file:
                file.writelines(notes)
            print("✅ Заметка удалена.")
        else:
            print("⚠ Ошибка: неверный номер заметки.")
    except ValueError:
        print("⚠ Ошибка: введите число.")


def clear_notes():
    """Полностью очищает файл заметок"""
    confirmation = input("Вы уверены, что хотите удалить все заметки? (да/нет): ").strip().lower()
    if confirmation == "да":
        open(NOTES_FILE, "w").close()  # Очищаем файл
        print("✅ Все заметки удалены.")
    else:
        print("Операция отменена.")


def main():
    """Основное меню"""
    while True:
        print("\n===== Меню =====")
        print("1. Показать заметки")
        print("2. Добавить заметку")
        print("3. Удалить заметку")  
        print("4. Очистить все заметки")  # Новый пункт меню
        print("5. Выйти")
        print("================")

        choice = input("Выберите действие: ").strip()

        if choice == "1":
            show_notes()
        elif choice == "2":
            add_note()
        elif choice == "3":
            delete_note()
        elif choice == "4":
            clear_notes()
        elif choice == "5":
            print("🚀 Выход.")
            break
        else:
            print("⚠ Ошибка: выберите правильный номер.")


if __name__ == "__main__":
    main()
