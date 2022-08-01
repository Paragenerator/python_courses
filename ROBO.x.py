from os import system
from getch import getche, getch #Для установки этой библиотеки: pip install getch
import random


dlina_k = int(input("\nНет ограничений на длину карты,\
но рекомендую <= 33\n\ndlina: "))

visota_k = int(input("\nНет ограничений на высоту карты,\
но рекомендую <= 33\n\nvisota: "))

r_r_k = dlina_k * visota_k

roboX = int(input(f"\nИгрок должен находиться в пределах карты(<={r_r_k})\
    Введите координау местонохождения 'R': "))


#_________________________________________Генерация координат целей(цветков)


flowers = []
flowers2 = []
for i in range(0,dlina_k):
    flowers.append(random.randint(0,r_r_k))
    if flowers[i] not in flowers2:
        flowers2.append(flowers[i])

flowers_vost = [] #___Список оживших цветов

#_______________________________________________________Цикл с ОТРИСОВКОЙ

while True:

    for i in range(0,r_r_k):
        if i % dlina_k ==0:
            print("")
        
        if roboX == i:
            print("🚿",end="")
        elif i in flowers2:
            if i in flowers_vost:
                print("🌹",end="")
            else:
                print("🥀",end="")
        else:
            print(".",end=" ")
    #__________________________________Сообщает о последнем политом цветке

    if roboX in flowers_vost and roboX == flowers_vost[-1]:
        print("Ура! Цветок",flowers_vost[-1],"ожил!")
    #___________________________________________________

    print("\n\n\n\n\n\n\
    !!! Работает только с английской раскладкой !!!\n\n\
        'w' - ВВЕРХ\n\
            'a' - ЛЕВО\n\
                'd' - ПРАВО\n\
                    's' - ВНИЗ\n\n\
        'e' - нажми для Полива цветка\n\n\
        Нажми 'X' если вдруг, решишься остановить эту прекрасную игру...")   


    #_______________________________________________Ввод без нажатия ENTER

    joystick = getch()
    if joystick == "a":
        roboX -=1
        if roboX < 0:
            roboX +=dlina_k
        else:
            pass
    elif joystick == "d":
        roboX +=1
        if roboX == r_r_k:
            roboX -=(dlina_k)

    elif joystick == "w":
        roboX -=dlina_k
        if roboX < 0:
            roboX =roboX+(r_r_k)
        
        else:
            pass
    elif joystick == "s":
        roboX +=dlina_k
        if roboX >= r_r_k:
            roboX =roboX-(r_r_k)
        else:
            pass
    #________________________________Вносит цветок в список уже политых
    elif joystick == "e":       
        if roboX in flowers2:
            flowers_vost.append(roboX)

    #_________________________________Условия окончания игры

    if set(flowers2) == set(flowers_vost):   #Условие Успешного прохождения.

        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\
    Ты большой молодец! Все увядающие цветы снова полны жизни и воды!)\
        \n")
        break
    elif joystick == "x":   #_______PRESS_TO_EXITE
        break
    
    

    #_____________________________________________________________________
    
    system("clear")