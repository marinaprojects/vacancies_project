import json

from src.filesaver import JSONSaver
from src.vacancy import Vacancy


def user_interaction(api):
    keyword = input("Введите ключевое слово для поиска вакансий: ")
    vacancies_data = api.get_vacancies(keyword)
    vacancies_list = [Vacancy(vacancy['name'], vacancy['alternate_url'], vacancy['salary'], vacancy.get('description', 'No description provided'))
                      for vacancy in vacancies_data['items']]
    while True:
        print("1. Отобразить вакансии")
        print("2. Добавить вакансию в файл")
        print("3. Удалить вакансию из файла")
        print("4. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            print_vacancies(vacancies_list)
        elif choice == "2":
            json_saver = JSONSaver("../data/vacancies.json")
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
            json_saver = JSONSaver("../data/vacancies.json")
            # Add logic for deleting vacancies
        elif choice == "4":
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите действие из списка.")



def print_vacancies(vacancies_list):
    pass

def filter_vacancies(vacancies_list, filter_words):
    pass


def get_vacancies_by_salary(vacancies_list, salary_range):
    pass


def sort_vacancies(vacancies_list):
    pass


def get_top_vacancies(vacancies_list, top_n):
    pass

