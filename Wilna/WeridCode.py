DaysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def GetDate(production_date, shelf_life):
    year, month, day = map(int, production_date.split('-'))
    
    day += shelf_life
    
    while day > DaysInMonth[month - 1]:
        day -= DaysInMonth[month - 1]
        month += 1
        if month > 12:
            month = 1
            year += 1
    
    use_by_date = f"{year:04d}-{month:02d}-{day:02d}"
    return use_by_date

production_date = "2024-12-30"
shelf_life = 7
use_by_date = GetDate(production_date, shelf_life)
print(f"Use-by date: {use_by_date}")