#!/usr/bin/env python3
import os


from moduls import comment
from moduls import recen
from moduls import graph
from moduls import out
from moduls import delete_comments

def main():

    graph.leha() # это важно

    print("Доступные функции:")
    print("1 - Поиск файлов с комментариями")
    print("2 - Проверка режима рецензирования")
    print("3 - Вывести все примечания")
    print("4 - Удалить все примечания")

    choice = input("Введите номер действия: ").strip()

    if choice not in ("1", "2", "3", "4"):
        print("Некорректный выбор. Введите 1 или 2 или 3.")
        return

    path = input("Укажите путь к файлу или папке: ").strip().strip('"')

    if choice == "1":
        print("🔍 Поиск файлов с комментариями...")
        comment.fcomments(path)
    elif choice == "2":
        print("🔍 Поиск файлов с комментариями...")
        recen.recenzirovanie(path)
    elif choice == "3":
        print("🔍 Поиск файлов с комментариями...")
        out.comments_out(path)
    elif choice == "4":
        print("🧹 Удаление всех комментариев...")
        delete_comments.remove_comments(path)

    else:
        print("❌ Неверный выбор. Введите 1, 2, 3, 4 или 0 для выхода.")



if __name__ == "__main__":
    main()