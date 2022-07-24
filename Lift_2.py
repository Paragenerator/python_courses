from os import system
import time
system("clear")
# Состояние лифта
napr_up     = -1
napr_stop   = False
napr_down   = 1


krisha = True
etaji_zdania = 9
parkovka = True

etaj_lifta = 9
lift_otkrit = False
lift_napravl = napr_stop


print("Этаж лифта:",etaj_lifta)

cel_na_etaje = int(input("\n\nНа каком этаже ждет человек:"))
cel_v_lifte = False
#__________________________________________________________________Napravlenie lifta



#___________________________________________________________________________________



# ОТрисовка
#           krisha
if krisha:
    print(" --|=====|-- ")
    print("-K-|_____|---")
    
else:
    print("   _-----_   ")

    #________ЦИКЛ_________etji___________________
while etaj_lifta >= cel_na_etaje:


    if etaj_lifta > cel_na_etaje:
        lift_napravl = napr_down
    elif etaj_lifta < cel_na_etaje:
        lift_napravl = napr_up
    elif etaj_lifta == cel_na_etaje:
        lift_napravl = napr_stop
    else:
        pass


    time.sleep(0.5)
    system("clear")

    if krisha:
        print(" --|=====|-- ")
        print("-K-|_____|---")
    
    else:
        print("   _-----_   ")


    for etaj in range(9,0,-1):

        if etaj == etaj_lifta : #______Vverh i niz lifta
            l_otrisovka = "|‾‾‾|"
        elif etaj == etaj_lifta-1:
            l_otrisovka = "|___|"
        else:
            l_otrisovka = "     "
        print(f"---|{l_otrisovka}|---")  #__Telo zdania
        #___________________________________________________________________________________
        if lift_napravl == napr_stop and etaj_lifta == cel_na_etaje:               # Otkrit ili net lift
            lift_otkrit = True
        else:
            lift_otkrit = False
        #___________________________________________________________________________________
        if etaj == etaj_lifta and etaj == cel_na_etaje and lift_otkrit:     #cel v lifte
            cel_v_lifte = True
        #___________________________________________________________________________________
        if etaj == cel_na_etaje and not cel_v_lifte:
            cel = "cel"
        else:
            cel = "   "
        #___________________________________________________________________________________

        

        if etaj == etaj_lifta and not cel_v_lifte: #_______Centr lifta
            lift = "| - |"
        
        elif etaj == etaj_lifta and etaj_lifta == cel_na_etaje and cel_v_lifte:
            lift = "|cel|"
        #___________________________________________________________________________________Ukazateli
        elif etaj == (etaj_lifta+1) and lift_otkrit:
            lift = " <o> "
        elif etaj == (etaj_lifta+1) and not lift_otkrit and lift_napravl == napr_stop:
            lift = "  X  "
        elif etaj == (etaj_lifta+1) and not lift_otkrit and lift_napravl == napr_up:
            lift = "  ^  "
        elif etaj == (etaj_lifta+1) and not lift_otkrit and lift_napravl == napr_down:
            lift = "  v  "

        else:
            lift = "     "


        print(f'{etaj:^3}|{lift}|{cel}')


    #_________________parkovka_________________________
    if parkovka:
        print("---|-----|---")
        print("-P-|     |---")
        print("___|-----|___")
    elif parkovka is False:
        print("___|-----|___")

    etaj_lifta -=1    

