def month_to_season(month):
    if 1 <= month <= 12:
        if month in [1, 2, 12]:
            return "Зима"
        elif month in [3, 4, 5]:
            return "Весна"
        elif month in [6, 7, 8]:
            return "Лето"
        else:
            return "Осень"
    else:
        return "Некорректный номер месяца"

result = month_to_season(9)

print(f"Сезон: {result}")
