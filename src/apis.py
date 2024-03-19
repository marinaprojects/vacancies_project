from abc import ABC, abstractmethod
import json
import requests


class BaseAPI(ABC):
    @abstractmethod
    def get_vacancies(self, keyword):
        pass


class HHAPI(BaseAPI):
    def __init__(self):
        self.vacancies = None
        self.filename = None

    def get_vacancies(self, keyword):
        params = {
            'per page': 100,
            'area': 113,
            'only_with_salary': True,
            'page': 20,
            'text': keyword
        }
        url = 'https://api.hh.ru/vacancies'
        response = requests.get(url, params=params)
        return response.json()

    def add_vacancy(self, vacancy):
        self.vacancies.append(vars(vacancy))
        with open(self.filename, 'w') as file:
            json.dump(self.vacancies, file)

    def delete_vacancy(self, vacancy):
        self.vacancies = [v for v in self.vacancies if v != vars(vacancy)]
        with open(self.filename, 'w') as file:
            json.dump(self.vacancies, file)

    def get_vacancies_by_criteria(self, criteria):
        pass
