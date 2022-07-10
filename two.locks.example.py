pin_door_1 = "1234"
pin_door_2 = "4321"

pin_dveri_1 = input("Введите пароль дверь-1: ") #pin1 str
zamok_1_otkrit = pin_door_1 == pin_dveri_1      #bool 

pin_dveri_2 = input("Введите пароль дверь-1: ") #pin1 str
zamok_2_otkrit = pin_door_2 == pin_dveri_2      #bool


if zamok_1_otkrit and zamok_2_otkrit:
    print("Аладин в здании!")
else:
    print("Один из паролей или оба, неверны!\n\
        Try again!")
# Если условие "if" неверно, то сработает "else"