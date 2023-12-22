while True:
   try:
       fraction = input("Дробь: ")
       x, y = map(int, fraction.split('/'))

       if x > y or y == 0:
           raise ValueError

       percent = (x / y) * 100

       if percent <= 1:
           print("E")
       elif percent >= 99:
           print("F")
       else:
           print(f"{round(percent)}%")

       break

   except ValueError:
       print("Некорректный ввод. Пожалуйста, введите дробь в правильном формате.")

   except ZeroDivisionError:
       print("Некорректный ввод. Знаменатель не может быть нулем.")
