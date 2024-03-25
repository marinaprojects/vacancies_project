import json
from abc import abstractmethod, ABC


class BaseSaver(ABC):
    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy_index):
        pass

    @abstractmethod
    def get_vacancies_by_criteria(self, criteria):
        pass


class JSONSaver(BaseSaver):
    def __init__(self, filename):
        self.filename = filename
        self.vacancies = []

    def add_vacancy(self, vacancy):
        self.vacancies.append(vars(vacancy))
        self._save_vacancies_to_file()
        file_path = f"data/{self.filename}"
        with open(file_path, 'w') as file:
            json.dump(self.vacancies, file)


    def delete_vacancy(self, vacancy_index):
        if 0 <= vacancy_index < len(self.vacancies):
            del self.vacancies[vacancy_index]
            self._save_vacancies_to_file()

    def get_vacancies_by_criteria(self, criteria):
        pass


    def _save_vacancies_to_file(self):
        file_path = f"data/{self.filename}"
        with open(file_path, 'w') as file:
            json.dump(self.vacancies, file)


class CSVSaver(BaseSaver, ABC):
    pass


class TXTSaver(BaseSaver, ABC):
    pass


class XLSSaver(BaseSaver, ABC):
    pass
