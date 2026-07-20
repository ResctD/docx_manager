#!/usr/bin/env python3


'''
author: Leha
'''

import os

from moduls import comment
from moduls import recen
from moduls import graph

def main():

    graph.leha() # это важно

    print("Доступные функции:")
    print("1 - Поиск файлов с комментариями")
    print("2 - Проверка режима рецензирования")

    choice = input("Введите номер действия: ").strip()

    if choice not in ("1", "2"):
        print("Некорректный выбор. Введите 1 или 2.")
        return

    path = input("Укажите путь к файлу или папке: ").strip().strip('"')

    if choice == "1":
        print("🔍 Поиск файлов с комментариями...")
        comment.fcomments(path)
    elif choice == "2":
        recen.recenzirovanie(path)


if __name__ == "__main__":
    main()