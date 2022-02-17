tickets = int(input("Какое количество билетов вы хотите приобрести: "))
price = 0
i = 1
while i <= tickets:
    age = int(input(f"Укажите возраст {i} посетителя: "))
    if age <= 0:
        print("Возраст посетителя не может быть меньше 0, давайте попробуем еще раз")
        continue
    elif 0 < age < 18:
        price += 0
    elif 18 <= age < 25:
        price += 990
    elif 25 <= age:
        price += 1390
    i = i + 1
print("Общая стоимость билетов: ", price)
if tickets > 3:
    price = int(price * 0.9)
    print("Сумма к оплате с учетом скидки: ", price)
else:
    print("Сумма к оплате : ", price)
