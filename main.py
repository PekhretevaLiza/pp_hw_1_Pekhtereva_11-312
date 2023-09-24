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
        if numberX - number <=10:
            print("Mало, но ты близок к отгадке!")
        else:
            print("Слишком мало")
    else:
        if number - numberX <=10:
            print("Много, но ты близок к отгадке!")
        else:
            print("Слишком много")
    Try += 1