from utils import create_database, save_employer_data_to_database, save_vacancy_data_to_database, \
    save_currency_data_to_database
from config import config
from HeadHunterAPI import HeadHunterAPI


def main():
    hh_api = HeadHunterAPI('банк')
    employer_data = hh_api.get_formatted_employers()
    vacancy_data = hh_api.get_formatted_vacancies()
    currency_data = HeadHunterAPI.get_currency_rate()
    params = config()
    create_database('hh_vacancies', params)
    save_employer_data_to_database(employer_data, 'hh_vacancies', params)
    save_vacancy_data_to_database(vacancy_data, 'hh_vacancies', params)
    save_currency_data_to_database(currency_data, 'hh_vacancies', params)


if __name__ == '__main__':
    main()
