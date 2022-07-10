#online shop order


# 1. free delivery ? (yes/no - True/False)
#       - vip ?
#       - cost >= 500 ?






# 2. order completion ? (yes/no - True/False)
#     1  - select food       
#     2  - confirm order
#     3  - enter client info
#     4  - delivery info
#     5  - payment
#     6  - delivery (physycal)
#     7  - client satisfied

# SELECT FOOD_____________________________________________________________________________________________________________________

menu_price = {"pizza":100,'cola':25,'burger':50,'water':10,}                #Словарь "продукт:цена"
print("\nPRODUCT:price",menu_price)


select = input('Enter name selected food: ')                                 # Переменная- ключ(продукт) для словаря menu_price
client_spends = menu_price[select] * int(input("How many?:(only int) "))     # Общая цена за продукты клиента

#CONFIRM ORDER____________________________________________________________________________________________________________________

print('Price for selected products:\n', client_spends,'lei\n')
last_confirm = input('Do you want to add  another purchase?! type "yes/no": ')                     # Подверждение завершение списка заказа

while last_confirm == "yes":
    print("\nPRODUCT:price",menu_price)                                                            # Цикл while на случай доп покупок
    client_spends = client_spends + \
        (menu_price[input('Enter name selected food: ')] * int(input("How many?:(only int) ")))    # Продукт * количество

    print("Price for all products:\n",client_spends,'lei\n')                                                # (Хорошо бы тут создать список всех продуктов при выводе)
    last_confirm = input('Do you want to add  another purchase?! type "yes/no": ')
    if last_confirm == 'no':
        break

#ENTER CLIENT INFO________________________________________________________________________________________________________________

if last_confirm == "no":
    name = input("Nice! Now we need your first and last name for delivery servise\n(example John Smith: ")         # Имя покупателя
print('Nice to meet you ',name)

#DELIVERY INFO____________________________________________________________________________________________________________________

VIP_list = list()                                                                          # Лист с вип клиентами
free_deliv_4expenses = 400                                                                 # Минимальный чек для получения бесплатной доставки
delivery_cost = 40                                                                         # Стаоимость доставки
free_delivery = (name in VIP_list) or (free_deliv_4expenses <= client_spends)              # Условие получения беспл. доставки

need_delivery = input('Do you need delivery service ? (yes/no): ')                         # Надобность в доставке                       

#ниже - условия и АДРЕС доставки
if need_delivery == 'no':                                                                                                   
    print("Ok, let's proceed to payment.")                                  

elif need_delivery == "yes" and free_delivery == True:
    print("Congrats! Delivery for you is free!")                                           
    adress = input("Adress for delivery: ")
else:
    print("Delivery will cost: ",delivery_cost)
    adress = input("Adress for delivery: ")

#PAYMENT and delivery (physycal)_____________________________________________________________________________________________________

if need_delivery == "yes" and free_delivery == False:                                       
    print("\nTotal price(with delivery) =",delivery_cost+client_spends)                                      # Общая цена + оплата доставки
elif need_delivery == "no" or free_delivery == True:
    print("\nTotal price(only products) =",client_spends)                                                    # Общая цена без оплаты доставки

print("\nСhoose payment method, CASH or CARD ?")
pay_method = int(input("CASH - 0\nCARD - 1\ntype 0 or 1: "))                                # Выбор метода оплаты
if need_delivery == "no" and pay_method == 0:
    print('Super! Your purchases are waiting for you "here".')                              # В случае самовывоза
elif need_delivery == "yes" and pay_method == 1:                                      # Тут должна быть оплата картой
    print("Мы преходим на страницу оплаты\n\
        где все данные для оплаты были предоставлены")
    print("Peter Parker will be within 30 minutes at the address:", adress)           # Названное время доставки
elif need_delivery == "yes" and pay_method == 0:
    print("Peter Parker will be within 30 minutes at the address:", adress)           # Названное время доставки

#delivery (end)______________________________________________________________________________________________________________________
if need_delivery == "yes":
    input("we hope you spend this time in the most pleasant expectation, right?:")

    for i in range(30):
        print("after 30 minuts...")
    print("\nНа Peter'a Parker'a напали злодеи, ваши продукты очень сильно пострадали...\n\
        процедура 'лечения' будет долгой и мучительной для нашего повара,\n\
            но он обязательно приготовит ваш заказ еще раз!\n\
                Всё будет хорошо, oчень скоро вы встретистесь со своей едой!")
    ocenka = input("(После получения доставки)\n Оцениете пожалуйста работу нашего ресторана\n\
        от 1 до 13: ")