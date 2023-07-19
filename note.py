import json
import datetime
import os

NOTES_FILE = "notes.json"


def load_notes():
    if not os.path.exists(NOTES_FILE):
        return []
    with open(NOTES_FILE, "r") as file:
        return json.load(file)


def save_notes(notes):
    with open(NOTES_FILE, "w") as file:
        json.dump(notes, file, indent=4)


def create_note():
    title = input("Введите заголовок заметки: ")
    body = input("Введите тело заметки: ")
    created_at = datetime.datetime.now().isoformat()
    return {
        "id": len(notes) + 1,
        "title": title,
        "body": body,
        "created_at": created_at,
        "last_modified": created_at
    }


def add_note():
    new_note = create_note()
    notes.append(new_note)
    save_notes(notes)
    print("Заметка успешно сохранена.")


def list_notes():
    if not notes:
        print("Список заметок пуст.")
        return
    print("Список заметок:")
    for note in notes:
        print(f"{note['id']}. {note['title']} ({note['created_at']})")


def main():
    global notes
    notes = load_notes()

    while True:
        print("\nВведите команду:")
        print("add - добавить новую заметку")
        print("list - посмотреть список заметок")
        print("edit - редактировать заметку")
        print("delete - удалить заметку")
        print("filter - фильтровать заметки по дате")
        print("exit - выход")

        command = input().lower()

        if command == "add":
            add_note()
        elif command == "list":
            list_notes()
        elif command == "exit":
            print("Выход из программы.")
            break
        else:
            print("Некорректная команда. Попробуйте снова.")


if __name__ == "__main__":
    main()
