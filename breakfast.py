menu = {
   "кофе": 20.00,
   "чай": 10.00,
   "булочка": 5.00,
   "салат": 30.40,
   "пирожное": 45.50
}

total_cost = 0.00

while True:
    try:
        dish = input("Блюдо: ").lower()
        if dish in menu:
           total_cost += menu[dish]
    except EOFError:
        break

print(f"Сумма: {total_cost:.2f}")