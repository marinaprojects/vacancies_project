class Vacancy:
    def __init__(self, title, url, salary_from, company_name, description='No description provided'):
        self.salary = None
        self.title = title
        self.link = url
        self.salary_from = salary_from
        self.company_name = company_name
        self.description = description


    def __repr__(self):
        return f"Vacancy(title={self.title}, salary={self.salary_from})"

    @classmethod
    def cast_to_object_list(cls, hh_vacancies):
        vacancies = []
        for vac_data in hh_vacancies:
            title = vac_data.get('name', '')
            url = vac_data.get('alternate_url', '')
            salary_from = vac_data.get('salary_from', 0)
            company_name = vac_data.get('employer', {}).get('name', '')
            description = vac_data.get('description', '')
            instance = cls(title, url, salary_from, company_name, description)
            vacancies.append(instance)
        return vacancies

    def __lt__(self, other):
        if self.salary < other.salary:
            return True
        else:
            return False


    def __str__(self):
        return (f"Title: {self.title}\nURL: {self.link}\nSalary: {self.salary_from}\nCompany:"
                f" {self.company_name}\nDescription: {self.description}\n")
