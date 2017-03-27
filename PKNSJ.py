# Metody wytwarzania oprogramowania w duzych organizacjach
# WSTE w Szczecinie, Krzysztof Chwalisz

def procent(ilosc, wszystkich):
    return ((ilosc*1.0)/wszystkich )*100

from random import randint

liczba_gier_pkn = liczba_gier_pknsj = 0
wygrane_gracza_pkn = wygrane_gracza_pknsj = 0
wygrane_komputera_pkn = wygrane_komputera_pknsj = 0
pknsj = ("Papier", "Kamien", "Nozyce", "Spock", "Jaszczurka")
koniec = False

while koniec == False:
    print "  Witaj w grze. Wybierz: 1 lub 2 lub 3 lub 4\n 1  GRA Papier-Kamien-Nozyce"
    print " 2  GRA Papier-Kamien-Nozyce-Spock-Jaszczurka\n 3  Wyniki gier - statystyki"
    print " 4  KONIEC - wyjscie z programu"
    wybor_menu = raw_input("Twoj wybor ?: ")

    if wybor_menu == "1": #Papier-Kamien-Nozyce

        print " Wybrales gre Papier-Kamien-Nozyce\nZaczynasz Ty."
        isok = False
        while isok == False:

            figura_gracza = raw_input("Podaj swoj wybor wpisujac caly wyraz z wielkiej litery bez polskich znakow:\nPapier lub Kamien lub Nozyce : ")
            figura_komputera = pknsj[randint(0, 2)]
            if figura_gracza == figura_komputera:
                print "komputer rowniez wylosowal : " +figura_komputera +". Wynik tej gry - remis\n"
                liczba_gier_pkn += 1
                isok = True
            elif figura_gracza == "Papier":
                if figura_komputera == "Kamien":
                    print "Komputer wylosowal : " + figura_komputera + "\nWygrales - papier jest silniejszy od kamienia, poniewaz go owija\n"
                    wygrane_gracza_pkn +=1
                else:
                    print "Komputer wylosowal : " + figura_komputera + "\nPrzegrales - nozyce sa silniejsze od papieru, poniewaz go tna\n"
                    wygrane_komputera_pkn +=1
                liczba_gier_pkn += 1
                isok = True
            elif figura_gracza == "Kamien":
                if figura_komputera == "Papier":
                    print "Komputer wylosowal : " + figura_komputera + "\nPrzegrales - papier jest silniejszy od kamienia, poniewaz go owija\n"
                    wygrane_komputera_pkn +=1
                else:
                    print "Komputer wylosowal : " + figura_komputera + "\nWygrales - kamien jest silniejszy od nozyc, poniewaz je tepi\n"
                    wygrane_gracza_pkn += 1
                liczba_gier_pkn += 1
                isok = True
            elif figura_gracza == "Nozyce":
                if figura_komputera == "Papier":
                    print "Komputer wylosowal : " + figura_komputera + "\nWygrales - nozyce sa silniejsze od papieru, poniewaz go tna\n"
                    wygrane_gracza_pkn += 1
                else:
                    print "Komputer wylosowal : " + figura_komputera + "\nPrzegrales - kamien jest silniejszy od nozyc, poniewaz je tepi\n"
                    wygrane_komputera_pkn += 1
                liczba_gier_pkn += 1
                isok = True
            else:
                print("\nBlednie wpisales swoj wybor. Sprobuj jeszcze raz")

    elif wybor_menu == "2": #Papier-Kamien-Nozyce-Spock-Jaszczurka
        print " Wybrales gre Papier-Kamien-Nozyce-Spock-Jaszczurka\nZaczynasz Ty."
        isok = False
        while isok == False:

            figura_gracza = raw_input("""Podaj swoj wybor wpisujac caly wyraz z wielkiej litery bez polskich znakow
            Papier lub Kamien lub Nozyce lub Spock lub Jaszczurka: """)
            figura_komputera = pknsj[randint(0, 4)]
            if figura_gracza == figura_komputera:
                print "komputer rowniez wylosowal : " + figura_komputera + ". Wynik tej gry - remis\n"
                liczba_gier_pknsj += 1
                isok = True

            elif figura_gracza == "Papier":
                if figura_komputera == "Kamien":
                    print "Komputer wylosowal : " + figura_komputera + "\nWygrales - papier jest silniejszy od kamienia, poniewaz go owija\n"
                    wygrane_gracza_pknsj += 1
                elif figura_komputera == "Spock":
                    print "Komputer wylosowal : " + figura_komputera + "\nWygrales - poniewaz papier obala Spocka\n"
                    wygrane_gracza_pknsj += 1
                elif figura_komputera == "Nozyce":
                    print "Komputer wylosowal : " + figura_komputera + "\nPrzegrales - poniewaz nozyce tna papier\n"
                    wygrane_komputera_pknsj += 1
                else:
                    print "Komputer wylosowal : " + figura_komputera + "\nPrzegrales - poniewaz jaszczurka zjada papier\n"
                    wygrane_komputera_pknsj += 1
                liczba_gier_pknsj += 1
                isok = True

            elif figura_gracza == "Kamien":
                if figura_komputera == "Papier":
                    print "Komputer wylosowal : " + figura_komputera + "\nPrzegrales - papier jest silniejszy od kamienia, poniewaz go owija\n"
                    wygrane_komputera_pknsj += 1
                elif figura_komputera == "Spock":
                    print "Komputer wylosowal : " + figura_komputera + "\nPrzegrales - poniewaz Spock dezintegruje kamien\n"
                    wygrane_komputera_pknsj += 1
                elif figura_komputera == "Nozyce":
                    print "Komputer wylosowal : " + figura_komputera + "\nWygrales - poniewaz kamien tepi nozyce\n"
                    wygrane_gracza_pknsj += 1
                else:
                    print "Komputer wylosowal : " + figura_komputera + "\nWygrales - poniewaz kamien zgniata jaszczurke\n"
                    wygrane_gracza_pknsj += 1
                liczba_gier_pkn += 1
                isok = True

            elif figura_gracza == "Nozyce":
                if figura_komputera == "Papier":
                    print "Komputer wylosowal : " + figura_komputera + "\nWygrales - nozyce sa silniejsze od papieru, poniewaz go tna\n"
                    wygrane_gracza_pknsj += 1
                elif figura_komputera == "Spock":
                    print "Komputer wylosowal : " + figura_komputera + "\nPrzegrales - poniewaz Spock niszczy nozyce\n"
                    wygrane_komputera_pknsj += 1
                elif figura_komputera == "Kamien":
                    print "Komputer wylosowal : " + figura_komputera + "\nPrzegrales - poniewaz kamien tepi nozyce\n"
                    wygrane_komputera_pknsj += 1
                else:
                    print "Komputer wylosowal : " + figura_komputera + "\nWygrales - poniewaz nozyce dekapituja jaszczurke\n"
                    wygrane_gracza_pknsj += 1
                liczba_gier_pknsj += 1
                isok = True

            elif figura_gracza == "Spock":
                if figura_komputera == "Papier":
                    print "Komputer wylosowal : " + figura_komputera + "\nPrzegrales - papier obala Spocka\n"
                    wygrane_komputera_pknsj += 1
                elif figura_komputera == "Nozyce":
                    print "Komputer wylosowal : " + figura_komputera + "\nWygrales - poniewaz Spock niszczy nozyce\n"
                    wygrane_gracza_pknsj += 1
                elif figura_komputera == "Kamien":
                    print "Komputer wylosowal : " + figura_komputera + "\nWygrales - poniewaz Spock dezintegruje kamien\n"
                    wygrane_gracza_pknsj += 1
                else:
                    print "Komputer wylosowal : " + figura_komputera + "\nPrzegrales - poniewaz jaszczurka otruwa Spocka\n"
                    wygrane_komputera_pknsj += 1
                liczba_gier_pknsj += 1
                isok = True

            elif figura_gracza == "Jaszczurka":
                if figura_komputera == "Papier":
                    print "Komputer wylosowal : " + figura_komputera + "\nWygrales - jaszczurka zjada papier\n"
                    wygrane_gracza_pknsj += 1
                elif figura_komputera == "Nozyce":
                    print "Komputer wylosowal : " + figura_komputera + "\nPrzegrales - poniewaz nozyce dekapituja jaszczurke\n"
                    wygrane_komputera_pknsj += 1
                elif figura_komputera == "Kamien":
                    print "Komputer wylosowal : " + figura_komputera + "\nPrzegrales - poniewaz kamien zgniata jaszczurke\n"
                    wygrane_komputera_pknsj += 1
                else:
                    print "Komputer wylosowal : " + figura_komputera + "\nWygrales - poniewaz jaszczurka otruwa Spocka\n"
                    wy1grane_gracza_pknsj += 1
                liczba_gier_pknsj += 1
                isok = True

            else:
                print("\nBlednie wpisales swoj wybor. Sprobuj wpisac jeszcze raz")

    elif wybor_menu == "3": #Statystyka
        if liczba_gier_pkn > 0:
            print "\n\tWyniki rozgrywek Papier-Kamien-Nozyce:"
            print " Liczba gier : " + str(liczba_gier_pkn)
            print "Gracz wygral z komputerem: " + str(wygrane_gracza_pkn) + " razy co stanowi %.2f " %procent(wygrane_gracza_pkn, liczba_gier_pkn) + "% wszystkich gier PKN"
            print "Komputer wygral z graczem: " + str(wygrane_komputera_pkn)+ " razy co stanowi %.2f " %procent(wygrane_komputera_pkn, liczba_gier_pkn) + "% wszystkich gier PKN"
            print "Zremisowano z komputerem razy "  +str(liczba_gier_pkn-wygrane_gracza_pkn-wygrane_komputera_pkn) + " co stanowi %.2f " %procent((liczba_gier_pkn-wygrane_gracza_pkn-wygrane_komputera_pkn), liczba_gier_pkn) + "% wszystkich gier PKN\n"
        else:
            print "\nNie grales jeszcze w gre Papier-Kamien-Nozyce"
        if liczba_gier_pknsj > 0:
            print "\n\tWyniki rozgrywek Papier-Kamien-Nozyce-Spock-Jaszczurka:"
            print " Liczba gier : " + str(liczba_gier_pknsj)
            print "Gracz wygral z komputerem: " + str(wygrane_gracza_pknsj) + " razy co stanowi %.2f " %procent(wygrane_gracza_pknsj, liczba_gier_pknsj) + "% wszystkich gier PKNSJ"
            print "Komputer wygral z graczem: " + str(wygrane_komputera_pknsj)+ " razy co stanowi %.2f " %procent(wygrane_komputera_pknsj, liczba_gier_pknsj) + "% wszystkich gier PKNSJ"
            print "Zremisowano z komputerem razy "  +str(liczba_gier_pknsj-wygrane_gracza_pknsj-wygrane_komputera_pknsj) + " co stanowi %.2f " %procent((liczba_gier_pknsj-wygrane_gracza_pknsj-wygrane_komputera_pknsj), liczba_gier_pknsj) + "% wszystkich gier PKNSJ\n"
        else:
            print "Nie grales jeszcze w gre Papier-Kamien-Nozyce-Spock-Jaszczurka\n"

    elif wybor_menu == "4": #Koniec
        koniec = True
        print "Zakonczyles program - do zobaczenia"
    else:
        print "\n_ Wprowadzono niepoprawna wartosc. Mozliwe do wyboru jest: 1 lub 2 lub 3 lub 4 _\n"
