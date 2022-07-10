ser_price = 100

client_cash = int(input("\n Сколько налички?: "))


if client_cash >= ser_price:
    print("\n Оплата наличными прошла успешно!")

else:
    print("\n Оплата наличкой провалилась.")
    client_card = int(input("\n Сколько денег на карте?: "))
    
    if client_card >= ser_price:
        print("\n Ура, грошей на карте достаточно!")
    
    else:
        print("\n Оплата картой не прошла :С")
        client_crypto = int(input("\n Может в собакеКоинах достаточно ?!: "))
        coef_sobakeCoin = 0.067
        sobakeCoin_to_USD = client_crypto * coef_sobakeCoin       # Конвертация крипты в обычную валюту
        print("В долларах это будет:",sobakeCoin_to_USD)

        if sobakeCoin_to_USD >= ser_price:
            print("\n Фух, не последний бомж)")

        else:
            print("\n Ну, вернись после зарплаты...")