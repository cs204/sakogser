months = {
    "январь": "01",
    "февраль": "02",
    "март": "03",
    "апрель": "04",
    "май": "05",
    "июнь": "06",
    "июль": "07",
    "август": "08",
    "сентябрь": "09",
    "октябрь": "10",
    "ноябрь": "11",
    "декабрь": "12"
}

while True:
    try:
        date = input("Дата: ")
        parts = date.split(".")
        if len(parts) == 3:
            year = parts[2]
            month = parts[1]
            day = parts[0]
        else:
            parts = date.split()
            if len(parts) == 3:
                year = parts[2]
                month = months.get(parts[1].lower())
                day = parts[0]
            else:
                raise ValueError
        formatted_date = f"{year}-{month}-{day}"
        print(formatted_date)
        break
    except (ValueError, KeyError):
        print("")
