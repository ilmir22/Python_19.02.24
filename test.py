
#Добавьте доп функционал данному приложени

print("Добро пожаловать в наш сервис по заказу бургеров, пожалуйста выберите начинку для вашего бургера из списка: ")

toppings = ["томаты", "сыр", "огурцы", "салат", "котлета", "бекон", "соус", "кетчуп"]

for i in range(len(toppings)):
    print(f"{i+1}: {toppings[i]}")
user_burger = []
while True:
    print("Введите любое число не из списка топпингов чтобы завершить заказ")
    user_choice = int(input("Введите номер позиции, который вы хотите"
                        "добавить: "))
    if user_choice not in range(1,9): 
        print("Вы завершили заказ!")
        break
    else:
        user_burger.append(toppings[user_choice-1])


print(f"В ваш бургер будут добавлены следующие ингридиенты:  {", ".join(user_burger)}")

#Добавление котлет
print ("Какие котлеты вы хотите? ")
cotlets = ["Куриные", "Говяжьи", "Свинина"]
for i in range(len(cotlets)):
    print(f"{i+1}: {cotlets[i]}")
user_cotleta = []
while True:
    print("Введите любое число не из списка топпингов чтобы завершить заказ")
    user_choice2 = int(input("Введите номер позиции, который вы хотите"
                        "добавить"))
    if user_choice2 not in range(1,3): 
        print("Вы завершили заказ!")
        break
    else:
        user_cotleta.append(cotlets[user_choice2-1])
print(f"Вы добавили котлету: {''.join(user_cotleta)}")

#Добавление булок
print ("Какие булки вы хотите? ")
bulki = ["Ржаные", "обычные", "кунжутные"]
for i in range(len(bulki)):
    print(f"{i+1}: {bulki[i]}")
user_bulka = []
while True:
    print("Введите любое число не из списка топпингов чтобы завершить заказ")
    user_choice3 = int(input("Введите номер позиции, который вы хотите"
                        "добавить"))
    if user_choice3 not in range(1,3): 
        print("Вы завершили заказ!")
        break
    else:
        user_bulka.append(bulki[user_choice3-1])
print(f"Вы добавили булку: {''.join(user_bulka)}")
#Добаление салфеток
salfetki1= (input("Нужны ли вам салфетки? Ответьте Да или Нет: ")) 

if salfetki1 == "Да":
    print ("Вы добавили салфетки")
else:
    print ("Вы не добавили салфетки")

print("Вы успешно сделали заказ")
print(f"Ваши ингридиенты - {",".join(user_burger)}\n"
      f"Котлета: - {"". join(user_cotleta)}\n"
      f"Булка: - {"". join(user_bulka)}\n"
      f"Салфетки: - {"". join(salfetki1)}\n")
