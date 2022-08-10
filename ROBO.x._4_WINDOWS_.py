import os
from getch import getch #Для установки этой библиотеки: pip install py-getch
import random


dlina_k = int(input("\nНет ограничений на длину карты,\
но рекомендую <= 33\n\ndlina: "))

visota_k = int(input("\nНет ограничений на высоту карты,\
но рекомендую <= 33\n\nvisota: "))

r_r_k = dlina_k * visota_k

roboX = int(input(f"\nИгрок должен находиться в пределах карты(<={r_r_k})\
    Введите координау местонохождения 'R': "))


#_________________________________________Генерация координат целей(цветков)


flowers = list(set([(random.randint(0,r_r_k)) for fl in range(0,dlina_k)]))   #_Координаты цветов из сучайной последовательности (0, end map point)
                                                                              #_метод list(set(список)) удаляет дубликаты (также меняет изначальный порядок данных в списке)



flowers_vost = [] #___Список оживших цветов

#_______________________________________________________Цикл с ОТРИСОВКОЙ

while True:

    for i in range(0,r_r_k):
        if i % dlina_k ==0:        #_Тут  print переходит на новую строку после определенного
            print("")              #_колличество символов равному dlina_k
        
        if roboX == i:
            print("🚿",end="")
        elif i in flowers:
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

    print("\n\n\n\
    !!! Работает только с английской раскладкой !!!\n\n\
        'w' - ВВЕРХ\n\
            'a' - ЛЕВО\n\
                'd' - ПРАВО\n\
                    's' - ВНИЗ\n\n\
        'e' - нажми для Полива цветка\n\n\
        Нажми 'X' если вдруг, решишься остановить эту прекрасную игру...")   


    #_______________________________________________Ввод без нажатия ENTER

    joystick = getch()
    if joystick == b"a":
        roboX -=1
        if roboX < 0:
            roboX +=dlina_k #не выпускает за пределы карты
        
    elif joystick == b"d":
        roboX +=1
        if roboX == r_r_k:
            roboX -=(dlina_k) #не выпускает за пределы карты

    elif joystick == b"w":
        roboX -=dlina_k
        if roboX < 0:
            roboX =roboX+(r_r_k) #не выпускает за пределы карты
        
    elif joystick == b"s":
        roboX +=dlina_k
        if roboX >= r_r_k:
            roboX =roboX-(r_r_k) #не выпускает за пределы карты
        
    #________________________________Вносит цветок в список уже политых
    elif joystick == b"e":       
        if roboX in flowers:
            flowers_vost.append(roboX)

    #_________________________________Условия окончания игры

    if set(flowers) == set(flowers_vost):   #Условие Успешного прохождения.

        print("\n\n\n\n\n\n\n\n\n\n\
    Ты большой молодец! Все увядающие цветы снова полны жизни и воды!)\
        \n")
        break
    elif joystick == b"x":   #_______PRESS_TO_EXITE
        break
    
    

    #_____________________________________________________________________
    
    os.system('cls')