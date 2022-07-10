#App that:
# IN: time in seconds
# OUT: time in HMS


# INPUT
 #const
seconds_in_minuts = 60     # 1) количество Секунд в минуте
minuts_in_hour = 60     # 2) количество Минут в часах
hours_in_day = 24     # 3) количество Часов в день

    #seconds
seconds = int(input("Введите количество секунд: "))
s = seconds % seconds_in_minuts # Видимый Остаток секунд
    #minuts
minuts = seconds // seconds_in_minuts
m = minuts % minuts_in_hour  # Видимый остаток минут
    #hours
hour = minuts // minuts_in_hour
h = hour % hours_in_day  # Видимый остаток часов
    #days
days = hour // hours_in_day # Видимое оличество дней

#OUTPUT
print('Time in D_HMS\n',days,'дней:',h,'часов:',m,'минут:',s,'секунд')