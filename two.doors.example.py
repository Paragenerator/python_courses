pin_door_1 = "1234"
pin_door_2 = "4321"

pin_dveri_1 = input("Введите пароль дверь-1: ") #pin1 str
zamok_1_otkrit = pin_door_1 == pin_dveri_1

if zamok_1_otkrit:
    print("Открыто!")

    pin_dveri_2 = input("Введите пароль-2: ") #pin2 str
    zamok_2_otkrit = pin_door_2 == pin_dveri_2

    if zamok_2_otkrit:
        print("Чувствуй себя как дома!")
    else:
        print("Неверно!Пароль-2, есть еще 2 попытки") #отправить юзера ввести пароль-2 еще два раза
        if zamok_2_otkrit:
            print("Чувствуй себя как дома!")
        else:
            print("Сезам не открылся!") # На случай неверного пароль-2
else:
    print("Неверно! Введи пароль-1 заново!")  # На случай неверного пароль-1
    