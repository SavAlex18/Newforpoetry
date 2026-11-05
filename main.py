from src.import_csv_xlsx import get_transactions_csv, get_transactions_xlsx
from src.utils import get_operations
from src.processing import filter_by_state, sort_by_date
from src.get_operations import process_bank_search
from src.widget import mask_account_card, get_date

statuses = ("EXECUTED", "CANCELED", "PENDING")
category_list = ['Открытие вклада', 'Перевод организации', 'Перевод с карты на карту', 'Перевод со счета на счет']

json_file_path = r"data\operations.json"
xlsx_file_path = r"data\transactions_excel.xlsx"
csv_file_path = r"data\transactions.csv"

list_json_operations = []
list_xlsx_operations = []
list_csv_operations = []


def main():
    global origin_list
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")
    print()
    user_choose_import = input()
    if user_choose_import not in ["1", "2", "3"]:
        print(""
              "сделан неправильный выбор, выход.\nПопробуйте позже!")
        return
    if user_choose_import == "1":
        list_json_operations = get_operations(json_file_path)
        # json нало преобразовать к тому же виду, как csv и excel
        origin_list = []
        for item in list_json_operations:
            op = item.get("operationAmount", {})
            cur = op.get("currency", {})
            origin_list.append({
                "id": item.get("id", None),
                "state": item.get("state", None),
                # "date": item.get("date",None),
                "date": str(item.get("date", None))[:19] + "Z",
                "amount": op.get("amount", None),
                "currency_name": cur.get("name", None),
                "currency_code": cur.get("code", None),
                "description": item.get("description", None),
                "from": item.get("from", None),
                "to": item.get("to", None),
            })
        print("Для обработки выбран JSON-файл")
    elif user_choose_import == "2":
        origin_list = get_transactions_csv(csv_file_path)
        print("Для обработки выбран CSV-файл")
    elif user_choose_import == "3":
        origin_list = get_transactions_xlsx(xlsx_file_path)
        print("Для обработки выбран XLSX-файл")

    # Дальнейшая пошаговая обработка
    # Select by stat key
    print(f"Введите статус, по которому необходимо выполнить фильтрацию. "
          f"\nДоступные для фильтровки статусы: {', '.join(statuses)} ")
    choose_status = input()
    while choose_status.upper() not in statuses:
        print(f"Статус операции {choose_status} недоступен")
        print(f"Введите статус, по которому необходимо выполнить фильтрацию. "
              f"\nДоступные для фильтровки статусы: {', '.join(statuses)} ")
        choose_status = input()
    print(f"Операции отфильтрованы по статусу {choose_status}")
    choose_status = choose_status.upper()
    filtered_list = filter_by_state(origin_list, choose_status)

    # Sort option
    operation_date_sort = input("Отсортировать операции по дате? Да/Нет ")
    while operation_date_sort.upper() not in ('ДА', 'НЕТ'):
        operation_date_sort = input("Отсортировать операции по дате? Да/Нет ")

    if operation_date_sort.upper() == "ДА":
        sort_direction = input("Отсортировать по возрастанию или по убыванию?\n(по возрастанию/по убыванию)")
        while sort_direction.upper() not in ('ПО ВОЗРАСТАНИЮ', 'ПО УБЫВАНИЮ'):
            sort_direction = input("Отсортировать по возрастанию или по убыванию? ")
        sign_sort_asc = False if sort_direction.upper() == 'ПО ВОЗРАСТАНИЮ' else True
        sorted_list = sort_by_date(filtered_list,  order_by=sign_sort_asc)
    else:
        sorted_list = filtered_list

    # Currency filter
    only_rub_operation = input("Выводить только рублевые транзакции? Да/Нет ")
    while only_rub_operation.upper() not in ('ДА', 'НЕТ'):
        only_rub_operation = input("Выводить только рублевые транзакции? Да/Нет ")

    if only_rub_operation.upper() == "ДА":
        currency_list = [item for item in sorted_list if item.get("currency_code", "") == "RUB"]
    else:
        currency_list = sorted_list

    # Filter by word in description
    need_filter_word = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет ")
    while need_filter_word.upper() not in ('ДА', 'НЕТ'):
        need_filter_word = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет ")

    if need_filter_word.upper() == 'ДА':
        filter_word = input("Введите слово для фильтрации транзакций")
    else:
        filter_word = ""

    if len(filter_word) > 0 :
        filter_word_list = process_bank_search(currency_list, filter_word)
    else:
        filter_word_list = currency_list

    operation_found = len(filter_word_list)
    if operation_found > 0:
        for item in filter_word_list:
            print(f'{get_date(item.get("date"))} {item.get("description")} \n{mask_account_card(item.get("from"))}'
                  f'-> {mask_account_card(item.get("to"))} \nСумма: {item.get("amount")} {item.get("currency_code")}')
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")

    return


if __name__ == '__main__':
    main()
