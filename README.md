from datetime import datetime

def get_days_from_today(date):
    try:
        # Перетворення рядка у форматі 'YYYY-MM-DD' на об'єкт datetime
        given_date = datetime.strptime(date, "%Y-%m-%d").date()
        
        # Отримання поточної дати
        current_date = datetime.today().date()
        
        # Розрахунок різниці
        delta = current_date - given_date
        
        return delta.days
    except ValueError:
        return "Помилка: введіть дату у форматі 'РРРР-ММ-ДД'"

# Приклад використання
print(get_days_from_today("2026-07-09")) 