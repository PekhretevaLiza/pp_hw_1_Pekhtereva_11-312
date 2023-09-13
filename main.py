"""
Поигаем в игру Угадай число
"""
print("Введите число от 1 до 100")

from random import randint
numberX = randint(1, 100)

Try = 1
while True:
    number = int(input())
    if number == numberX:
        print("Ура! Ты угадал с",Try,"попытки!")
        break
    elif number < numberX:
        print("Слишком мало")
    else:
        print("Слишком много")
    Try += 1


