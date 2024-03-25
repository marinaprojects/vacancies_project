import json

from src.filesaver import JSONSaver
from src.vacancy import Vacancy


def user_interaction(api):
    keyword = input("Введите ключевое слово для поиска вакансий: ")
    vacancies_data = api.get_vacancies(keyword)
    vacancies_list = [Vacancy(vacancy['name'], vacancy['alternate_url'], vacancy['salary'],
                      vacancy.get('description', 'No description provided'))
                      for vacancy in vacancies_data['items']]
    json_saver = JSONSaver("../data/vacancies.json")
    while True:
        print("1. Отобразить вакансии")
        print("2. Добавить вакансию в файл")
        print("3. Удалить вакансию из файла")
        print("4. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            print_vacancies(vacancies_list)
        elif choice == "2":
            if not vacancies_list:
                print("Список вакансий пуст.")
                continue
            vacancy_index = int(input(f"Введите индекс вакансии для добавления (от 0 до {len(vacancies_list)-1}): "))
            if 0 <= vacancy_index < len(vacancies_list):
                json_saver.add_vacancy(vacancies_list[vacancy_index])
                print("Вакансия добавлена в файл.")
            else:
                print("Неверный индекс. Пожалуйста, выберите индекс из диапазона.")
        elif choice == "3":
            if not json_saver.vacancies:
                print("Список вакансий пуст.")
                continue
            print("Список вакансий:")
            print_vacancies(json_saver.vacancies)
            vacancy_index = int(
                input(f"Введите индекс вакансии для удаления (от 0 до {len(json_saver.vacancies) - 1}): "))
            if 0 <= vacancy_index < len(json_saver.vacancies):
                del json_saver.vacancies[vacancy_index]
                json_saver._save_vacancies_to_file()  # Сохранение изменений в файл
                print("Вакансия удалена из файла.")
            else:
                print("Неверный индекс. Пожалуйста, выберите индекс из диапазона.")
        elif choice == "4":
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите действие из списка.")


def print_vacancies(vacancies_list):
    for i, vacancy in enumerate(vacancies_list):
        print(f"Index: {i}")
        print(vacancy)


def filter_vacancies(vacancies_list, filter_words):
    pass


def get_vacancies_by_salary(vacancies_list, salary_range):
    pass


def sort_vacancies(vacancies_list):
    pass


def get_top_vacancies(vacancies_list, top_n):
    pass


