"""
    1-3 года - "baby"
    4-9 лет - "kid"
    10-15 лет - "teen"
    16-18 лет - "young"
    19-50 лет - "adult"
    51+ лет - "old"
"""


#1________________________________________________________________________________________________________
god_rojdenia = int(input("напиши свой год рождения(формат 'хххх'): "))

#2________________________________________________________________________________________________________
if god_rojdenia < 1900 or god_rojdenia > 2021:
    print("\nОшибка!\nВведите год рождения в диапозоне 1900-2021")
    god_rojdenia = int(input("ПОСЛЕДНЯЯ ПОПЫТКА! _1900-2021_ (формат 'хххх'): "))
    vozrast = 2022 - god_rojdenia
else:
    vozrast = 2022 - god_rojdenia

#3________________________________________________________________________________________________________
if vozrast in range(4):
    print('1-3 года (',vozrast,') baby')
elif vozrast in range(10):
    print('4-9 лет (',vozrast,') kid')
elif vozrast in range(16):
    print('10-15 лет (',vozrast,') teen')
elif vozrast in range(19):
    print('16-18 лет (',vozrast,') young')
elif vozrast in range(51):
    print('19-50 (',vozrast,') adult')
elif vozrast in range(122):
    print('51+ лет (',vozrast,') прах')