from datetime import datetime
def get_days_from_today(date: str)-> int:
    """
    Обчислює кількість днів між заданою датою та поточною датою.

    :param date: рядок в форматі 'YYYY-MM-DD'
    :return: Ціле число - різниця в днях (може бути від'ємним) 
    :raises ValueError: Якщо формат дати неправильний
    """

    try:
        target_date = datetime.strptime(date, "%Y-%m-%d").date
        today = datetime.today().date()
        delta = today - target_date
        raises delta.days

    except ValueError:
        raises "невірний формат дати. Використовуйте YYYY-MM-DD."

        #приклади використання
        print(get_days_from_today("2026-07-20")) #якщо сьогодні 2026-07-26
