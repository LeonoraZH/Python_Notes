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


def edit_note():
    note_id = int(
        input("Введите ID заметки, которую хотите отредактировать: "))
    note_to_edit = find_note_by_id(note_id)
    if note_to_edit:
        print(f"Редактирование заметки ID {note_id}:")
        title = input("Введите новый заголовок заметки: ")
        body = input("Введите новое тело заметки: ")
        note_to_edit["title"] = title
        note_to_edit["body"] = body
        note_to_edit["last_modified"] = datetime.datetime.now().isoformat()
        save_notes(notes)
        print("Заметка успешно отредактирована.")
    else:
        print(f"Заметка с ID {note_id} не найдена.")


def find_note_by_id(note_id):
    for note in notes:
        if note["id"] == note_id:
            return note
    return None


def delete_note():
    note_id = int(input("Введите ID заметки, которую хотите удалить: "))
    note_to_delete = find_note_by_id(note_id)
    if note_to_delete:
        notes.remove(note_to_delete)
        save_notes(notes)
        print("Заметка успешно удалена.")
    else:
        print(f"Заметка с ID {note_id} не найдена.")


def filter_notes_by_date():
    date_str = input(
        "Введите дату для фильтрации заметок (в формате ГГГГ-ММ-ДД): ")
    try:
        filter_date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        print("Некорректный формат даты. Введите дату в формате ГГГГ-ММ-ДД.")
        return

    filtered_notes = [
        note for note in notes if note["created_at"].startswith(date_str)]
    if not filtered_notes:
        print(f"Заметок, созданных {date_str}, не найдено.")
        return

    print(f"Список заметок, созданных {date_str}:")
    for note in filtered_notes:
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
        elif command == "edit":
            edit_note()
        elif command == "delete":
            delete_note()
        elif command == "filter":
            filter_notes_by_date()
        elif command == "exit":
            print("Выход из программы.")
            break
        else:
            print("Некорректная команда. Попробуйте снова.")


if __name__ == "__main__":
    main()
